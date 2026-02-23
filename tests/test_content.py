"""Content quality checks over all real condition files.

Parametrized over all_condition_files. Each condition must meet minimum
content quality standards: word count, section depth, pitfall count,
no hedge language, and specific time_to_harm phrasing.
"""

import re
from pathlib import Path

import pytest
import yaml


# ---- Hedge phrases banned from condition files ----

HEDGE_PHRASES = [
    "it is important to note",
    "it is important to note that",
    "may want to consider",
    "you may want to consider",
    "one might consider",
    "it should be noted",
    "it is worth noting",
    "it is crucial to note",
    "it is essential to note",
    "please note that",
]

# Vague time_to_harm patterns (these should NOT appear as the complete value)
VAGUE_TIME_PATTERNS = [
    r"^time[-\s]sensitive$",
    r"^urgent$",
    r"^emergent$",
    r"^immediately$",
    r"^varies$",
    r"^n/?a$",
]


# ---- Helpers ----

def parse_file(path: Path):
    """Return (frontmatter_dict, body_text) for a condition file."""
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not match:
        return None, text
    fm = yaml.safe_load(match.group(1))
    body = match.group(2)
    return fm, body


def count_words(text: str) -> int:
    """Count words in text (strips markdown syntax)."""
    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Remove markdown links
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    return len(text.split())


def get_sections(body: str) -> dict[str, str]:
    """Extract {section_name: section_body} from markdown body."""
    sections = {}
    current = None
    lines = []
    for line in body.split("\n"):
        if line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(lines).strip()
            current = line[3:].strip()
            lines = []
        else:
            lines.append(line)
    if current is not None:
        sections[current] = "\n".join(lines).strip()
    return sections


def count_bullet_items(text: str) -> int:
    """Count list items (lines starting with -, *, or a number followed by period/dot)."""
    count = 0
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            count += 1
        elif re.match(r"^\d+\.", stripped):
            count += 1
    return count


# ---- Tests ----

class TestWordCounts:
    def test_total_word_count_at_least_500(self, all_condition_files):
        path = all_condition_files
        _, body = parse_file(path)
        wc = count_words(body)
        assert wc >= 500, (
            f"{path.name}: Only {wc} words total (minimum 500 required)"
        )


class TestSectionWordCounts:
    def _check_section_words(self, path, section_name, min_words=30):
        _, body = parse_file(path)
        sections = get_sections(body)
        if section_name not in sections:
            pytest.skip(f"{path.name}: Section '{section_name}' not found")
        wc = count_words(sections[section_name])
        assert wc >= min_words, (
            f"{path.name}: Section '{section_name}' has only {wc} words (minimum {min_words})"
        )

    def test_recognition_section_min_30_words(self, all_condition_files):
        self._check_section_words(all_condition_files, "Recognition", 30)

    def test_critical_actions_section_min_30_words(self, all_condition_files):
        self._check_section_words(all_condition_files, "Critical Actions", 30)

    def test_pitfalls_section_min_30_words(self, all_condition_files):
        self._check_section_words(all_condition_files, "Pitfalls", 30)


class TestPitfallsCount:
    def test_pitfalls_has_at_least_3_items(self, all_condition_files):
        path = all_condition_files
        _, body = parse_file(path)
        sections = get_sections(body)
        if "Pitfalls" not in sections:
            pytest.skip(f"{path.name}: No Pitfalls section")
        pitfall_text = sections["Pitfalls"]
        item_count = count_bullet_items(pitfall_text)
        assert item_count >= 3, (
            f"{path.name}: Pitfalls has only {item_count} bullet items (minimum 3 required)"
        )


class TestNoHedgePhrases:
    @pytest.mark.parametrize("phrase", HEDGE_PHRASES)
    def test_no_hedge_phrase(self, all_condition_files, phrase):
        path = all_condition_files
        _, body = parse_file(path)
        lower_body = body.lower()
        assert phrase.lower() not in lower_body, (
            f"{path.name}: Contains hedge phrase '{phrase}' — remove it"
        )


class TestTimeToHarmSpecificity:
    def test_time_to_harm_not_vague(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "time_to_harm" not in fm:
            pytest.skip(f"{path.name}: No frontmatter or time_to_harm")

        tth = fm["time_to_harm"]

        if isinstance(tth, dict):
            # Structured form: at least one value must be non-empty
            values = [v for v in tth.values() if v]
            assert len(values) >= 1, (
                f"{path.name}: time_to_harm dict has no non-empty values"
            )
            # Check each value for vagueness
            for v in values:
                _assert_tth_specific(path.name, str(v))
        elif isinstance(tth, str):
            _assert_tth_specific(path.name, tth)
        # else: invalid type caught by test_schema


def _assert_tth_specific(filename: str, value: str):
    """Assert that a time_to_harm string is not vague."""
    cleaned = value.strip().lower()
    for pat in VAGUE_TIME_PATTERNS:
        if re.match(pat, cleaned, re.IGNORECASE):
            pytest.fail(
                f"{filename}: time_to_harm '{value}' is too vague (matches pattern '{pat}'). "
                "Use specific values like '< 6 hours' or '< 90 minutes'."
            )


class TestH2SectionMinWords:
    """Every H2 section present in the file must have >= 30 words."""

    def test_all_sections_have_min_words(self, all_condition_files):
        path = all_condition_files
        _, body = parse_file(path)
        sections = get_sections(body)
        failures = []
        for section_name, section_text in sections.items():
            wc = count_words(section_text)
            if wc < 30:
                failures.append(f"'{section_name}': {wc} words")
        assert not failures, (
            f"{path.name}: Sections with < 30 words: {', '.join(failures)}"
        )
