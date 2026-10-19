# Tests

`tests/offline.txt` lists the suites that run without any server (request building, parsing, errors, helpers, timers).
CI runs them on every push:

```bash
uv sync --group tests
uv run pytest $(cat tests/offline.txt) --import-mode=importlib
```

The other suites are integration tests: they need a running StitchDB stack (`stitchdb start` from the StitchDB CLI)
and the `STITCHDB_TEST_URL` / `STITCHDB_TEST_KEY` variables pointing at it.
