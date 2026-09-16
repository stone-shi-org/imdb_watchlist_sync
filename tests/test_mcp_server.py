import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from mcp.client.session import ClientSession
from mcp.shared.memory import create_connected_server_and_client_session

from mcp_server import INSTRUCTIONS, mcp


def test_instructions_content():
    assert INSTRUCTIONS is not None
    assert len(INSTRUCTIONS.strip()) > 0
    # Usage guidance & recommended tool order
    assert "get_stats" in INSTRUCTIONS
    assert "list_watchlist" in INSTRUCTIONS
    assert "search_watchlist" in INSTRUCTIONS
    # Caveats
    assert "scrape" in INSTRUCTIONS.lower()
    assert "background" in INSTRUCTIONS.lower()


def test_initialization_options_instructions():
    init_opts = mcp._mcp_server.create_initialization_options()
    assert init_opts.instructions == INSTRUCTIONS


def test_initialize_handshake_returns_instructions():
    async def run_handshake():
        async with create_connected_server_and_client_session(mcp._mcp_server) as client:
            result = await client.initialize()
            assert result.instructions == INSTRUCTIONS

    asyncio.run(run_handshake())
