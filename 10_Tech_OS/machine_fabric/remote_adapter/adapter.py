#!/usr/bin/env python3
"""A'Space Sovereign DC Remote Adapter.

Provides a transport-agnostic user-owned private remote adapter for Sovereign DC.
- Authenticated private transport adapter boundary
- Proxies traffic to local gateway preserving operation_id/receipt semantics
- Unauthorized-client DENY
- Local gateway remains healthy on transport failure
- No public listener by default
"""

import argparse
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse, StreamingResponse
from starlette.routing import Route
from starlette.requests import Request
import httpx
import logging
import asyncio
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

# Global config
CONFIG = {
    "gateway_url": "http://127.0.0.1:8055",
    "token": None
}

HOP_BY_HOP = {
    "connection", "keep-alive", "proxy-authenticate",
    "proxy-authorization", "te", "trailers",
    "transfer-encoding", "upgrade"
}

client: httpx.AsyncClient = None

@asynccontextmanager
async def lifespan(app: Starlette):
    global client
    client = httpx.AsyncClient()
    yield
    await client.aclose()


async def check_auth(request: Request) -> bool:
    if not CONFIG["token"]:
        return True
    auth_header = request.headers.get("Authorization")
    expected = f"Bearer {CONFIG['token']}"
    return auth_header == expected

async def health(request: Request):
    try:
        resp = await client.post(f"{CONFIG['gateway_url']}/mcp", timeout=3)
        gw_up = True
    except Exception:
        gw_up = False

    return JSONResponse({
        "schema": "aspace.dc.remote-adapter.health.v1",
        "adapter": "ONLINE",
        "gateway": "ONLINE" if gw_up else "UNAVAILABLE",
    })

def filter_headers(headers: httpx.Headers) -> dict:
    return {k: v for k, v in headers.items() if k.lower() not in HOP_BY_HOP}

async def proxy(request: Request):
    if not await check_auth(request):
        return JSONResponse({"state": "DENIED", "error": "UNAUTHORIZED"}, status_code=401)

    url = f"{CONFIG['gateway_url']}{request.url.path}"
    if request.url.query:
        url += f"?{request.url.query}"

    headers = dict(request.headers)
    headers.pop("host", None)

    filtered_request_headers = {k: v for k, v in headers.items() if k.lower() not in HOP_BY_HOP}

    req = client.build_request(
        method=request.method,
        url=url,
        headers=filtered_request_headers,
        content=request.stream()
    )

    try:
        resp = await client.send(req, stream=True)
        return StreamingResponse(
            resp.aiter_raw(),
            status_code=resp.status_code,
            headers=filter_headers(resp.headers),
            background=resp.aclose
        )
    except Exception as e:
        return JSONResponse({"state": "FAILED", "error": "BAD_GATEWAY", "detail": str(e)}, status_code=502)

app = Starlette(
    debug=True,
    routes=[
        Route("/health", health, methods=["GET"]),
        Route("/{path:path}", proxy, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
    ],
    lifespan=lifespan
)

def main():
    parser = argparse.ArgumentParser(description="A'Space Sovereign DC Remote Adapter")
    parser.add_argument("--gateway-url", required=True, help="Local Gateway URL to proxy to")
    parser.add_argument("--token", required=True, help="Bearer token for authentication")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host (default 127.0.0.1 for private boundary)")
    parser.add_argument("--port", type=int, default=8056, help="Bind port")
    args = parser.parse_args()

    CONFIG["gateway_url"] = args.gateway_url.rstrip("/")
    CONFIG["token"] = args.token

    uvicorn.run(app, host=args.host, port=args.port, log_level="info")

if __name__ == "__main__":
    main()
