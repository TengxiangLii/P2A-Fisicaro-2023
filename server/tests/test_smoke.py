"""Smoke test against a local copy of the archive data.

Run: SMALL_CLUSTER_ISOMERS_DATA_DIR=/path/to/data python -m pytest server/tests  (needs pytest, pytest-asyncio)
"""
import os

import pytest

if not os.environ.get("SMALL_CLUSTER_ISOMERS_DATA_DIR"):
    pytest.skip("set SMALL_CLUSTER_ISOMERS_DATA_DIR to a verified data copy", allow_module_level=True)

from fastmcp import Client  # noqa: E402

from small_cluster_isomers.server import mcp  # noqa: E402


@pytest.mark.asyncio
async def test_database_and_al13m1_global_minimum(tmp_path):
    async with Client(mcp) as c:
        r = (await c.call_tool("minima_database_list_systems", {})).data
        assert (r["n_systems"], r["grand_total"]) == (58, 43606)
        gm = (await c.call_tool("minima_database_get_isomer_properties", {"system": "Al13m1"})).data
        assert gm["name"] == "min0001.xyz" and gm["properties"]["Pointgroup"] == "Ih"
        assert gm["properties"]["KS-Final-energy"] == -26.672682316180612
        xyz = (await c.call_tool("minima_database_extract_isomer_xyz",
                                 {"system": "Si10p1", "output_dir": str(tmp_path)})).data
        assert xyz["units"] == "atomicd0" and xyz["n_atoms"] == 10
