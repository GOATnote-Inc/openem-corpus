# Review Evidence

Review a condition file's evidence base and citations.

## Usage
```
/review-evidence [file path or condition name]
```

## Team
1. **evidence-reviewer** (Sonnet): Check every clinical claim against its cited source. Verify PubMed IDs, guideline URLs, and license compatibility.

2. **clinical-validator** (Opus): Independent clinical review. Challenge any claim that seems clinically suspect regardless of what the evidence reviewer found.

## Output
A report listing:
- Total claims checked
- Claims verified
- Issues found (UNSUPPORTED, OUTDATED, INACCURATE, LICENSE_RISK)
- Recommended fixes
