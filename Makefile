.PHONY: validate audit diversity quality-gate test test-all build-index eval-retrieval post-compile check lint format clean

validate:
	python scripts/validate.py

audit:
	python scripts/audit.py

diversity:
	python scripts/diversity_metrics.py

quality-gate:
	python scripts/quality_gate.py

test:
	pytest tests/ -v --ignore=tests/test_index.py

test-all:
	pytest tests/ -v

build-index:
	python scripts/build_index.py

eval-retrieval:
	python scripts/eval_retrieval.py

post-compile: build-index validate audit diversity eval-retrieval
	@echo "Post-compile pipeline complete."

check: validate quality-gate audit diversity test
	@echo "All checks passed."

lint:
	ruff check . && ruff format --check .

format:
	ruff format .

clean:
	rm -rf data/index/openem.lance data/index/manifest.json
	rm -rf .pytest_cache __pycache__
	find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
