# P2A-Fisicaro-2023

A Claude Code plugin made with [Paper2Agent](https://github.com/jmiao24/Paper2Agent) from the paper
**"Principles of isomer stability in small clusters"**, by G. Fisicaro, B. Schaefer, J. A. Finkler and S. Goedecker, *Mater. Adv.* 2023, 4, 1746 ([doi:10.1039/D2MA01088G](https://doi.org/10.1039/D2MA01088G)).
It combines the paper's isomer database with a reviewed reading skill for the paper itself.

| Component | What it gives the agent |
|---|---|
| MCP server `small_cluster_isomers` | Four tools over the 43,606 DFT (BigDFT) minima of 58 neutral and charged Na, Mg, Al, Al<sub>12</sub>Si, Si and Ge clusters found by Minima Hopping ([Materials Cloud Archive record](https://archive.materialscloud.org/records/j7hwv-81q79)) |
| Skill `fisicaro2023-isomer-stability-paper` | The full paper and ESI text, 20 figures, 12 ESI figure images and Tables 1–2 as CSV, with a navigation index |

## Install

You need Claude Code and [`uv`](https://docs.astral.sh/uv/). `uv` fetches Python 3.12 and the dependencies itself.

```
/plugin marketplace add TengxiangLii/P2A-Fisicaro-2023
/plugin install fisicaro2023@p2a-fisicaro-2023
/reload-plugins
```

On first use, `uv` builds the server from this repository at tag `v0.1.0`. The first tool call then downloads the archive data (about 73 MB) into `~/.cache/small_cluster_isomers` (or `$XDG_CACHE_HOME/small_cluster_isomers`) and checks it against the record's md5 checksums. That call takes about 20 s; later calls read the cache.

To use a copy of the data you already have, set `SMALL_CLUSTER_ISOMERS_DATA_DIR` to the folder holding `all_minima_names.npy`, `all_minima_data.npy` and `all_minima_xyz_structures.tar.gz`. The server then reads that folder and never downloads into it.

## Tools

The tools return stored values unchanged; nothing is recomputed.

| Tool | Use it to |
|---|---|
| `minima_database_list_systems` | List cluster families and charge states, with isomer counts, the global-minimum name and the stored property keys |
| `minima_database_get_isomer_properties` | Get every stored property of one isomer, with units. Pick it by `name` (e.g. `min0001.xyz`) or by `rank` (0 = global minimum) |
| `minima_database_export_property_table` | Write a CSV of a system's isomers in stored order, optionally limited to certain keys or to the first N ranks |
| `minima_database_extract_isomer_xyz` | Copy an isomer's BigDFT xyz file out of the archive byte for byte, with the parsed header and atoms |

System labels are `<cluster><charge>`: `m1` means −1, no suffix means neutral, and `p1`/`p2`/`p3` mean +1/+2/+3. Examples are `Al13m1`, `Na8` and `Si15p3`.

Example prompts:

- "Which Al13 charge state has an icosahedral global minimum, and what are its HOMO–LUMO gap and hardness?"
- "Export the 20 lowest isomers of Mg14 with their KS energies and shape factors, then explain the trend using the paper."
- "Extract the Si10+ global minimum structure and tell me what units it is in."

## Data caveats

- **Ordering:** ranks follow the stored order, which rises in energy above the global minimum. In 22 systems this order is not strictly sorted by KS energy, and the tools never re-sort.
- **Names:** use isomer names exactly as stored. Si systems use 9-digit names, and several Mg systems have gaps in their numbering.
- **Al12Si:** these systems store only 11 of the 18 property keys. The missing ones are reported, not filled in.
- **xyz units:** each file keeps its own units, `angstroemd0` (Å) or `atomicd0` (Bohr). Coordinates are returned as stored, without conversion.

## Manual use (without the plugin)

```bash
uv tool run --python 3.12 --from "git+https://github.com/TengxiangLii/P2A-Fisicaro-2023.git@v0.1.0#subdirectory=server" small-cluster-isomers-mcp
# fetch the data ahead of time (optional):
uv tool run --python 3.12 --from "git+https://github.com/TengxiangLii/P2A-Fisicaro-2023.git@v0.1.0#subdirectory=server" small-cluster-isomers-fetch ~/data/small_cluster_isomers
```

Any MCP client that can launch a stdio server can run the first command.

## Validation

Validation covered these 4 tools, not the paper's analyses.

- **Upstream reference:** the archive's own notebook was run as the reference, with its counts and stored outputs reproduced.
- **Tests:** 48 tests by an agent separate from the one that wrote the tools compare the outputs with direct reads of the archive files.
- **stdio acceptance:** 18 real calls over stdio pass in a fresh environment, after a relocated install, and in this packaged layout.
- **Zero-config start:** a cold-cache run of the plugin's launch command passed, with the download verified byte-identical against the archive.
- **Platform:** only macOS arm64 with CPython 3.12.9 was tested.

The paper skill was reviewed page by page against the PDFs and passes Paper2Skill's strict verification. One limitation: the number listings inside ESI Figs S3–S8 are images, not searchable text.

## Repository layout

```text
.claude-plugin/marketplace.json        marketplace "p2a-fisicaro-2023"
plugins/fisicaro2023/
  .claude-plugin/plugin.json
  .mcp.json                            launches the server with uv
  skills/fisicaro2023-isomer-stability-paper/
server/
  pyproject.toml                       package small-cluster-isomers-mcp
  small_cluster_isomers/               server.py, minima_database.py, fetch_minima_data.py
  tests/test_smoke.py
```

## Citation and licenses

When you use the data or the paper content, cite the paper (doi:10.1039/D2MA01088G) and the data record (doi:[10.24435/materialscloud:46-nr](https://doi.org/10.24435/materialscloud:46-nr)).

The code is MIT-licensed ([LICENSE](LICENSE)). The paper content and the data are CC BY 4.0, © the authors; see [NOTICE.md](NOTICE.md).
