"""Tools extracted from small_cluster_isomers/all_minima_data_analysis.ipynb.

Query the Minima Hopping database of 43606 DFT (BigDFT) minima of 58 neutral and charged
Na, Mg, Al, Al12Si, Si and Ge clusters ("Principles of isomer stability in small clusters",
Fisicaro, Schaefer, Finkler, Goedecker, Mater. Adv. 2023, doi:10.1039/D2MA01088G).
Stored values are returned unchanged; nothing is recomputed.
"""
import csv
import json
import os
import tarfile
import tempfile
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Annotated

import numpy
from fastmcp import FastMCP

REFERENCE = "https://archive.materialscloud.org/records/j7hwv-81q79 (all_minima_data_analysis.ipynb)"
DATA_DIR_ENV = "SMALL_CLUSTER_ISOMERS_DATA_DIR"
NAMES_FILE = "all_minima_names.npy"
DATA_FILE = "all_minima_data.npy"
TAR_FILE = "all_minima_xyz_structures.tar.gz"
ORDER_NOTE = ("stored order (energy above the global minimum, Fingerprint-distance-GM[0], ascending); "
              "rank 0 = global minimum")

minima_database_mcp = FastMCP(name="minima_database")

# Per-minimum property keys and units, as documented in notebook cell 9.
# VEA is stored per minimum like every other key (cell 9's cluster-level path is wrong; cell 11 shows it).
UNITS = {
    "KS-Final-energy": "Ha (final Kohn-Sham DFT energy of the optimized minimum)",
    "KS-energy-contributions": "Ha (BigDFT energy terms Ekin, EXC, Epot, Enl, Eion, EvXC, EH)",
    "Coordination": "(average coordination [-], average distance from the coordinated atoms [Angstrom])",
    "Fingerprint-distance-GM": "(energy with respect to the global minimum [Ha], fingerprint distance from the global minimum)",
    "Eccentricity": "(eccentricity e = 1 - min(w_i)/mean(w_i) [-], [w1, w2, w3] eigenvalues of the moment of inertia tensor)",
    "Soft-spheres-cavity": "(surface, volume, surface/volume ratio) of a soft-spheres cavity, mesh discretization 0.4",
    "Fermi-level": "Ha",
    "Homo-Lumo-gap": "eV",
    "Homo-Lumo": "[HOMO, LUMO] Ha",
    "Dipole": "Debye",
    "Adiabatic-Ionization-energy": "eV",
    "Vertical-Ionization-energy": "eV",
    "Vertical-Electron-Affinity": "eV (per minimum)",
    "Chemical-Hardness": "eV, CH = (VIE - VEA) * 0.5",
    "Eigenvalue-degeneracy": "list of KS eigenvalue multiplicities (degenerate if difference < 1e-4 Ha)",
    "Pointgroup": "point group from get_pymatgen_pointgroup(filename, tol=0.0009)",
    "Magic-numbers-distance": "- (old data not used in the main manuscript)",
    "Shape-factor": "- (shape factor S, Eq. 3 of the paper, from the moment of inertia eigenvalues)",
}
DOC_KEYS = list(UNITS)

# CSV components of tuple/list-valued keys, named after the cell 9 comments.
COMPONENTS = {
    "Coordination": ["average_coordination", "average_distance_Angstrom"],
    "Fingerprint-distance-GM": ["energy_above_GM_Ha", "fingerprint_distance"],
    "Eccentricity": ["e", "w1", "w2", "w3"],
    "Soft-spheres-cavity": ["surface", "volume", "surface_volume_ratio"],
    "Homo-Lumo": ["HOMO_Ha", "LUMO_Ha"],
}
JSON_CELL_KEYS = {"KS-energy-contributions", "Eigenvalue-degeneracy"}
CHARGES = {"m1": -1, "": 0, "p1": 1, "p2": 2, "p3": 3}  # cell 4 legend


def _data_path(filename: str) -> Path:
    root = os.environ.get(DATA_DIR_ENV)
    if not root:
        raise RuntimeError(f"Set {DATA_DIR_ENV} to the directory holding {NAMES_FILE}, {DATA_FILE} and {TAR_FILE} "
                           f"from https://archive.materialscloud.org/records/j7hwv-81q79 (see fetch_minima_data.py).")
    path = Path(root).expanduser().resolve() / filename
    if not path.is_file():
        raise FileNotFoundError(f"{path} not found; {DATA_DIR_ENV} must point to the files of "
                                f"https://archive.materialscloud.org/records/j7hwv-81q79 (see fetch_minima_data.py).")
    return path


@lru_cache(maxsize=4)
def _load_dicts(names_path: str, data_path: str) -> tuple[dict, dict]:
    all_minima = numpy.load(names_path, allow_pickle=True).item()  # cell 3
    all_minima_data = numpy.load(data_path, encoding="latin1", allow_pickle=True).item()  # cell 7
    return all_minima, all_minima_data


def _database() -> tuple[dict, dict]:
    return _load_dicts(str(_data_path(NAMES_FILE)), str(_data_path(DATA_FILE)))


def _cluster_of(system: str, all_minima: dict) -> str:
    hits = [c for c in all_minima if system in all_minima[c]]
    if len(hits) != 1:
        valid = [s for c in all_minima for s in all_minima[c]]
        raise ValueError(f"Unknown system {system!r}; valid systems: {valid}")
    return hits[0]


def _select(system: str, name: str | None, rank: int | None) -> tuple[str, list, str, int, dict]:
    all_minima, all_minima_data = _database()
    cluster = _cluster_of(system, all_minima)
    names = list(all_minima[cluster][system])
    if name is not None and rank is not None:
        raise ValueError("Give either name or rank, not both.")
    if name is not None:
        if name not in names:
            raise ValueError(f"{name!r} is not a stored minimum of {system} (names come from {NAMES_FILE}; "
                             f"e.g. {names[0]!r}).")
        rank = names.index(name)
    else:
        rank = 0 if rank is None else rank
        if not 0 <= rank < len(names):
            raise ValueError(f"rank must be in [0, {len(names) - 1}] for {system}.")
        name = names[rank]
    return cluster, names, name, rank, all_minima_data[cluster][system][name]


def _to_json(v):
    if isinstance(v, dict):
        return {k: _to_json(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_to_json(x) for x in v]
    if isinstance(v, numpy.ndarray):
        return v.tolist()
    if isinstance(v, numpy.generic):
        return v.item()
    return v


def _cells(key: str, value) -> list:
    value = _to_json(value)
    if key in COMPONENTS:
        flat = [value[0], *value[1]] if key == "Eccentricity" else list(value)
        if len(flat) != len(COMPONENTS[key]):
            raise ValueError(f"{key} has {len(flat)} components, expected {COMPONENTS[key]}.")
        return flat
    return [json.dumps(value)] if key in JSON_CELL_KEYS else [value]


@minima_database_mcp.tool()
def minima_database_list_systems(
    cluster: Annotated[str | None, "Cluster family to list (e.g. 'Al13', 'Al12Si', 'Si20'); None lists all 17"] = None,
) -> dict:
    """List cluster families, their charge-state systems and the number of stored minima.
    Optional cluster family -> per-system counts, global-minimum names and available property keys."""
    all_minima, all_minima_data = _database()
    if cluster is not None and cluster not in all_minima:
        raise ValueError(f"Unknown cluster {cluster!r}; valid clusters: {list(all_minima)}")
    out = []
    for c in [cluster] if cluster else all_minima:
        systems = []
        for s, names in all_minima[c].items():  # cell 5 iteration
            present = set.intersection(*(set(r) for r in all_minima_data[c][s].values()))
            suffix = s[len(c):]
            systems.append({
                "system": s, "charge_label": suffix or "neutral", "charge": CHARGES.get(suffix),
                "n_minima": len(names), "global_minimum_name": names[0],
                "available_property_keys": [k for k in DOC_KEYS if k in present],
                "missing_property_keys": [k for k in DOC_KEYS if k not in present]})
        out.append({"cluster": c, "systems": systems, "n_minima_total": sum(x["n_minima"] for x in systems)})
    n_sys = sum(len(c["systems"]) for c in out)
    total = sum(c["n_minima_total"] for c in out)
    return {"message": f"{n_sys} systems, {total} minima", "reference": REFERENCE, "artifacts": [],
            "clusters": out, "n_systems": n_sys, "grand_total": total, "ordering": ORDER_NOTE}


@minima_database_mcp.tool()
def minima_database_get_isomer_properties(
    system: Annotated[str, "System label with charge state, e.g. 'Al13m1', 'Al12Si', 'Si10p1'"],
    name: Annotated[str | None, "Stored minimum name, e.g. 'min0001.xyz'; give this or rank"] = None,
    rank: Annotated[int | None, "0-based index in stored order (0 = global minimum); default 0 if name is not given"] = None,
) -> dict:
    """Return every stored structural and electronic property of one isomer, with units.
    System + minimum name or rank -> property dict, units and keys missing for this record."""
    cluster, names, name, rank, rec = _select(system, name, rank)
    return {"message": f"{system} {name} (rank {rank} of {len(names)})", "reference": REFERENCE, "artifacts": [],
            "cluster": cluster, "system": system, "name": name, "rank": rank, "n_minima": len(names),
            "properties": _to_json(dict(rec)), "units": {k: UNITS.get(k, "not documented") for k in rec},
            "missing_keys": [k for k in DOC_KEYS if k not in rec], "ordering": ORDER_NOTE}


@minima_database_mcp.tool()
def minima_database_export_property_table(
    system: Annotated[str, "System label with charge state, e.g. 'Al13m1'"],
    keys: Annotated[list[str] | None, "Property keys to include (cell 9 names, e.g. 'KS-Final-energy'); None = all"] = None,
    max_rank: Annotated[int | None, "Include only ranks 0..max_rank (inclusive); None = all minima"] = None,
    output_dir: Annotated[str | None, "Base output directory; a fresh subdirectory is created (default: temp dir)"] = None,
) -> dict:
    """Export a per-isomer property table of one system in stored (energy-ranked) order.
    System + optional keys/max_rank -> CSV with rank, name and flattened property columns."""
    all_minima, all_minima_data = _database()
    cluster = _cluster_of(system, all_minima)
    names = list(all_minima[cluster][system])
    recs = all_minima_data[cluster][system]
    if keys is not None:
        bad = [k for k in keys if k not in UNITS]
        if bad or not keys:
            raise ValueError(f"Unknown keys {bad}; valid keys: {DOC_KEYS}")
    wanted = [k for k in DOC_KEYS if keys is None or k in keys]
    if max_rank is not None:
        if max_rank < 0:
            raise ValueError("max_rank must be >= 0.")
        names = names[:max_rank + 1]
    present = [k for k in wanted if any(k in recs[n] for n in names)]
    header = ["rank", "name"]
    for k in present:
        header += [f"{k}:{c}" for c in COMPONENTS[k]] if k in COMPONENTS else [k]
    partial = Counter()
    base = Path(output_dir).expanduser() if output_dir else Path(tempfile.gettempdir())
    base.mkdir(parents=True, exist_ok=True)
    out_dir = Path(tempfile.mkdtemp(prefix=f"{system}_table_", dir=base)).resolve()
    csv_path = out_dir / f"{system}_properties.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for i, n in enumerate(names):
            row = [i, n]
            for k in present:
                if k in recs[n]:
                    row += _cells(k, recs[n][k])
                else:  # left empty, never filled
                    partial[k] += 1
                    row += [""] * len(COMPONENTS.get(k, [k]))
            w.writerow(row)
    return {"message": f"Wrote {len(names)} rows x {len(header)} columns for {system}", "reference": REFERENCE,
            "artifacts": [{"description": f"{system} per-isomer property table (stored order)", "path": str(csv_path)}],
            "cluster": cluster, "system": system, "n_rows": len(names), "columns": header,
            "units": {k: UNITS[k] for k in present}, "missing_keys": [k for k in wanted if k not in present],
            "records_missing_key": dict(partial), "ordering": ORDER_NOTE}


@minima_database_mcp.tool()
def minima_database_extract_isomer_xyz(
    system: Annotated[str, "System label with charge state, e.g. 'Al13m1', 'Si10p1'"],
    name: Annotated[str | None, "Stored minimum name, e.g. 'min0001.xyz'; give this or rank"] = None,
    rank: Annotated[int | None, "0-based index in stored order (0 = global minimum); default 0 if name is not given"] = None,
    output_dir: Annotated[str | None, "Base output directory; a fresh subdirectory is created (default: temp dir)"] = None,
) -> dict:
    """Extract the stored BigDFT xyz file of one isomer verbatim from the structures archive.
    System + minimum name or rank -> .xyz file plus parsed header, units and atoms (no unit conversion)."""
    cluster, _, name, rank, _ = _select(system, name, rank)
    member = f"all_minima_xyz_structures/{cluster}/{system}/{name}"
    raw = None
    with tarfile.open(_data_path(TAR_FILE), "r:gz") as tar:
        for m in tar:  # read only the named member; never extractall
            if m.name == member:
                if not m.isfile():
                    raise ValueError(f"{member} is not a regular file in {TAR_FILE}.")
                raw = tar.extractfile(m).read()
                break
    if raw is None:
        raise FileNotFoundError(f"{member} not found in {TAR_FILE}.")
    lines = raw.decode().splitlines()
    head = lines[0].split()
    n_atoms = int(head[0])
    if len(head) < 4 or head[3] != "(Ha)" or len(lines) < 2 + n_atoms:
        raise ValueError(f"Unexpected BigDFT xyz header in {member}: {lines[0]!r}")
    atoms = []
    for line in lines[2:2 + n_atoms]:
        t = line.split()
        atoms.append({"element": t[0], "x": float(t[1]), "y": float(t[2]), "z": float(t[3]), "extra_fields": t[4:]})
    base = Path(output_dir).expanduser() if output_dir else Path(tempfile.gettempdir())
    base.mkdir(parents=True, exist_ok=True)
    out_dir = Path(tempfile.mkdtemp(prefix=f"{system}_xyz_", dir=base)).resolve()
    xyz_path = out_dir / f"{system}_{name}"
    xyz_path.write_bytes(raw)
    return {"message": f"Extracted {member} ({n_atoms} atoms, units {head[1]})", "reference": REFERENCE,
            "artifacts": [{"description": f"verbatim BigDFT xyz of {system} {name} (includes forces block)",
                           "path": str(xyz_path)}],
            "cluster": cluster, "system": system, "name": name, "rank": rank, "tar_member": member,
            "header_line": lines[0], "boundary_line": lines[1], "n_atoms": n_atoms, "units": head[1],
            "units_note": "angstroemd0 = Angstrom, atomicd0 = Bohr; coordinates are as stored",
            "header_energy_Ha": float(head[2]), "element_counts": dict(Counter(a["element"] for a in atoms)),
            "atoms": atoms}
