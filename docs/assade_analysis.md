# httpie/cli — ASS-ADE Static Analysis

> Automated static analysis of the `httpie/cli` module using [ASS-ADE](https://atomadic.tech) (Autonomous Sovereign System: Atomadic Development Environment). No LLM was used in the recon phase — pure static analysis in < 2 seconds.

## Findings

### Recon (full repo)

| Metric | Value |
|--------|-------|
| Source files | 135 Python |
| Circular imports | 2 detected |
| Doc coverage | 17% (189 / 1107 public callables) |
| Untested modules | 66 |
| Test ratio | 0.43 (429 test functions / 35 test files) |
| Tier violations | 3 files spanning multiple responsibility layers |

### httpie/cli module breakdown

The `httpie/cli` directory contains 1,708 lines across 5 files:

| File | Lines | Tier classification |
|------|-------|---------------------|
| `definition.py` | 956 | Mixed (constants + arg groups + spec) |
| `argtypes.py` | 275 | at-layer functions |
| `options.py` | 249 | mo-layer composites |
| `constants.py` | 134 | qk-layer constants |
| `dicts.py` | 94 | at-layer functions |

`definition.py` at 956 lines is the primary concern — it conflates constant declarations, argument group definitions, and top-level spec composition, which are three distinct responsibility layers.

### Rebuild (httpie/cli only)

Running ASS-ADE rebuild on just the `httpie/cli` directory produced a tier-partitioned reference:

| Phase | Result |
|-------|--------|
| Ingest | 15 files, 153 symbols, 153 gaps |
| Gap-fill proposals | 101 |
| Enrichment | 101 bodies, 108 edges |
| Cycle check | **Acyclic** (all cycles resolved) |
| Purity | 84 violating edges removed |
| Audit | 101/101 clean (100.0%) |

Tier partition:

| Tier | Components |
|------|-----------|
| `a0_qk_constants` (pure constants, no deps) | 11 |
| `a1_at_functions` (pure functions, simple deps) | 68 |
| `a2_mo_composites` (composite structures) | 22 |

## Proposed improvements

1. **Split `definition.py`** — Extract constants to `constants.py`, move argument group builders to `groups.py`, keep only the top-level `ParserSpec` composition in `definition.py`. Target: < 300 lines each.

2. **Resolve circular imports** — Two import cycles detected (`client.py → context.py → output/utils.py` and a self-referential import in `output/formatters/xml.py`). Introduce an interface layer or lazy import to break the cycle.

3. **Docstring coverage** — 17% of 1,107 public callables are documented. Prioritize `httpie/cli/argtypes.py` and `httpie/cli/options.py` which have the highest external call surface.

## Tool

[ASS-ADE](https://atomadic.tech) — `pip install ass-ade-rebuild` — runs locally, no LLM required for recon. Full recon took 1.5 seconds on this repo.
