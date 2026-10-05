"""Download the small-cluster-isomers database files (Materials Cloud Archive j7hwv-81q79).

Usage: python fetch_minima_data.py TARGET_DIR [--verify-only]
Then set SMALL_CLUSTER_ISOMERS_DATA_DIR=TARGET_DIR for the minima_database tools.
"""
import argparse
import hashlib
import sys
import urllib.request
from pathlib import Path

URL = "https://archive.materialscloud.org/api/records/j7hwv-81q79/files/{}/content"
MD5 = {  # from the archive record
    "all_minima_names.npy": "d971ad96e6f40c2840b061aa65464e97",
    "all_minima_data.npy": "5de9f0897b2c9dd152857e8219096d83",
    "all_minima_xyz_structures.tar.gz": "d8e75cc8c91d8143fc2ed89259a9741e",
}


def md5(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("target_dir")
    p.add_argument("--verify-only", action="store_true", help="only check md5s of files already in target_dir")
    args = p.parse_args(argv)
    target = Path(args.target_dir).expanduser()
    if not args.verify_only:
        target.mkdir(parents=True, exist_ok=True)
    ok = True
    for name, expected in MD5.items():
        path = target / name
        if not args.verify_only and not (path.is_file() and md5(path) == expected):
            print(f"downloading {name}", file=sys.stderr)
            part = path.with_name(name + ".part")
            urllib.request.urlretrieve(URL.format(name), part)
            if md5(part) != expected:  # keep a corrupt download out of the data dir
                print(f"BAD {name} download md5={md5(part)} expected={expected} (kept as {part})")
                ok = False
                continue
            part.replace(path)
        got = md5(path) if path.is_file() else "missing"
        good = got == expected
        ok &= good
        print(f"{'OK ' if good else 'BAD'} {name} md5={got} expected={expected}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
