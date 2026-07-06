# Tournament packages

This repo is a monorepo holding **three independent Python packages** for running tournament brackets. Each is its own PyPI package with its own `setup.py`, version, and tests — merging them into one repo did **not** merge them into one package. Installing one does not install or depend on the others.

| Package | PyPI | Source |
|---|---|---|
| `double_elimination` | [pypi.org/project/double_elimination](https://pypi.org/project/double_elimination/) | [packages/double_elimination](packages/double_elimination) |
| `single_elimination` | [pypi.org/project/single_elimination](https://pypi.org/project/single_elimination/) | [packages/single_elimination](packages/single_elimination) |
| `round_robin_tournament` | [pypi.org/project/round_robin_tournament](https://pypi.org/project/round_robin_tournament/) | [packages/round_robin_tournament](packages/round_robin_tournament) |

Install whichever one you need, same as always:

```bash
pip install double_elimination
pip install single_elimination
pip install round_robin_tournament
```

These previously lived in three separate repos (`smwa/double_elimination`, `smwa/single_elimination`, `smwa/round_robin_tournament`); they were consolidated here for easier maintenance, with full commit history preserved. Each package's own README (linked above) has its usage details.
