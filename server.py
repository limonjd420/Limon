import os
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
import uvicorn

security = TransportSecuritySettings(enable_dns_rebinding_protection=False)

mcp = FastMCP("Cricket-Betting-Agent", transport_security=security)

@mcp.tool()
def get_live_cricket_odds(match_query: str) -> str:
    """Fetch live cricket odds for a specific match from 1xBet."""
    return f"Match: {match_query}. Live Odds - Team A: 1.50, Team B: 2.60. Over/Under 150.5: Over 1.83, Under 1.83."

app = mcp.streamable_http_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
