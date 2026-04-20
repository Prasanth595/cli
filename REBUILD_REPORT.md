# Rebuild Report

**Rebuild tag**: `20260419_025004`
**Issued**: 2026-04-19T09:50:05.998797+00:00
**Issuer**: ass_ade.engine.schema_rebuilder
**Schema**: ASSADE-SPEC-003

## Source

| Field | Value |
|-------|-------|
| Input path | `C:\httpie-assade-demo\httpie\cli` |
| Plan digest | `7c2a02e77c1ea061` |
| Control root | `` |

## Output

| Field | Value |
|-------|-------|
| Components written | 101 |
| Output folder | `C:\httpie-cli-rebuilt` |

## Tier breakdown

| Tier | Count |
|------|-------|
| `a0_qk_constants` | 11 |
| `a1_at_functions` | 68 |
| `a2_mo_composites` | 22 |
| **Total** | **101** |

## Public invariants

| Invariant | Observed | Limit | Pass |
|-----------|---------|-------|------|
| D_max (depth) | ? | 23 | YES |
| epsilon_KL (dup fraction) | 0.00e+00 | 0.00e+00 | YES |
| tau_trust | 1820/1823 | ≥1820/1823 | YES |
| G_18 parity | ? mod 324 | — | — |

## Audit summary

- **Structural conformant**: YES
- **Pass rate**: 100.0%
- **Total findings**: 0
- **Valid components**: 101 / 101

## Certificate

- **Version**: ASSADE-SPEC-CERT-1
- **SHA-256**: `33585e1fd45121ac34cdbd081b4479a55d4fa58ef5e219b144a85ee77725952b`

Verify:

```bash
python -c "import json,hashlib; c=json.load(open('CERTIFICATE.json')); h=c.pop('certificate_sha256'); b=json.dumps(c,sort_keys=True).encode(); print('VERIFIED' if hashlib.sha256(b).hexdigest()==h else 'TAMPERED')"
```
