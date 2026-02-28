.PHONY: validate audit diversity quality-gate test test-all build-index eval-retrieval post-compile check lint format clean check-freshness generate-fhir validate-fhir scan-repos

PYTHON ?= python3

validate:
	$(PYTHON) scripts/validate.py

audit:
	$(PYTHON) scripts/audit.py

diversity:
	$(PYTHON) scripts/diversity_metrics.py

quality-gate:
	$(PYTHON) scripts/quality_gate.py

test:
	pytest tests/ -v --ignore=tests/test_index.py

test-all:
	pytest tests/ -v

build-index:
	$(PYTHON) scripts/build_index.py

eval-retrieval:
	$(PYTHON) scripts/eval_retrieval.py

check-freshness:
	$(PYTHON) scripts/check_index_freshness.py

post-compile: build-index validate audit diversity eval-retrieval check-freshness
	@echo "Post-compile pipeline complete."

check: validate quality-gate audit diversity test
	@echo "All checks passed."

lint:
	ruff check . && ruff format --check .

format:
	ruff format .

generate-fhir:
	$(PYTHON) scripts/generate_fhir.py --all

validate-fhir:
	$(PYTHON) scripts/generate_fhir.py --all --validate

scan-repos:
	$(PYTHON) scripts/scan_repos.py

clean:
	rm -rf data/index/openem.lance data/index/manifest.json
	rm -rf fhir/bundles/*.json
	rm -rf .pytest_cache __pycache__
	find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
