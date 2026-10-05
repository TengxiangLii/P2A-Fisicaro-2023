"""MCP server for the small-cluster isomer database (Materials Cloud Archive j7hwv-81q79).

Data location: SMALL_CLUSTER_ISOMERS_DATA_DIR if set (used as is, never downloaded into);
otherwise a user cache dir, filled with md5-verified downloads on the first tool call.
"""
import asyncio
import contextlib
import os
import sys
from pathlib import Path

from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware

from small_cluster_isomers import fetch_minima_data
from small_cluster_isomers.minima_database import DATA_DIR_ENV, minima_database_mcp


def _default_data_dir() -> Path:
    base = os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache"
    return Path(base) / "small_cluster_isomers"


class EnsureData(Middleware):
    """Download the archive files into the default cache dir before the first tool call that needs them."""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.lock = asyncio.Lock()

    def _missing(self) -> bool:
        return any(not (self.data_dir / n).is_file() for n in fetch_minima_data.MD5)

    async def on_call_tool(self, context, call_next):
        if self._missing():
            async with self.lock:
                if self._missing():
                    with contextlib.redirect_stdout(sys.stderr):  # keep stdout for the MCP protocol
                        code = await asyncio.to_thread(fetch_minima_data.main, [str(self.data_dir)])
                    if code != 0:
                        raise RuntimeError(f"Downloading the archive data into {self.data_dir} failed md5 checks; "
                                           f"retry, or set {DATA_DIR_ENV} to a verified copy.")
        return await call_next(context)


mcp = FastMCP(name="small_cluster_isomers")
mcp.mount(minima_database_mcp)

if not os.environ.get(DATA_DIR_ENV):
    _dir = _default_data_dir()
    os.environ[DATA_DIR_ENV] = str(_dir)
    mcp.add_middleware(EnsureData(_dir))


def main() -> None:
    mcp.run(show_banner=False)


if __name__ == "__main__":
    main()
