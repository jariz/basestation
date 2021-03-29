import pytest
from asyncio import sleep

from basestation.scanner import BasestationScanner

"""
It should be kinda obvious, but just FYI, these tests need to be run near actual hardware for them to succeed.

TODO: would love to split this up into multiple tests, but that causes the event loop to get closed or something.
I don't know (aka, don't wanna know) too much about asyncio.
"""


@pytest.mark.asyncio
async def test_pwr():
    devices = await BasestationScanner.discover()
    assert len(devices) > 0
    dev = devices[0]

    try:
        await dev.connect()

        await dev.identify()

        print(
            "\n\nYou should now check if your device flashes 😂. we can't read this state to confirm it is.\n\n"
        )

        await sleep(5)

        await dev.turn_on()
        assert await dev.is_turned_on() is True

        await dev.turn_off()
        assert await dev.is_turned_on() is False
    finally:
        await dev.disconnect()
