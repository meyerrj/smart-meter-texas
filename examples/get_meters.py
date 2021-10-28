"""Example to show how to fetch all meters associated with a user's account."""

import asyncio
import logging
import os
import sys

import socket
from socket import AF_INET, AF_INET6
import aiohttp
from aiohttp import CookieJar, TraceConfig, TCPConnector, BaseConnector, HttpVersion11

from smart_meter_texas import Account, Client, ClientSSLContext

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

username = os.environ["SMTUSER"]
password = os.environ["SMTPW"]


async def on_request_end(session, trace_config_ctx, params):
    print("Ending %s request for %s. I sent: %s" % (params.method, params.url, params.headers))
    print('Sent headers: %s' % params.response.request_info.headers)

async def main():

    trace_config = TraceConfig()
    #trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_end.append(on_request_end)
    trace_config.on_request_exception.append(on_request_end)

    client_ssl_ctx = ClientSSLContext()
    ssl_context = await client_ssl_ctx.get_ssl_context()

    async with aiohttp.ClientSession(cookie_jar = CookieJar(), trace_configs=[trace_config], version=HttpVersion11) as websession:
        account = Account(username, password)
        client = Client(websession, account, ssl_context)
        await client.authenticate()
        meters = await account.fetch_meters(client)

        for i, meter in enumerate(meters, 1):
            print(f"Meter {i}:")
            print(f"  Meter:\t{meter.meter}")
            print(f"  ESIID:\t{meter.esiid}")
            print(f"  Address:\t{meter.address}\n")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
