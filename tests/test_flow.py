import pytest
from time import sleep

from basestation.scanner import BasestationScanner

"""
It should be kinda obvious, but just FYI, these tests need to be ran near actual hardware for them to succeed.
"""

dev = None


def test_scan():
    global dev
    devices = BasestationScanner.discover()
    assert len(devices) > 0
    dev = devices[0]


def test_connect():
    dev.connect()


def test_identify():
    dev.identify()
    print(
        "\n\nYou should now check if your device flashes 😂. we can't read this state to confirm it is.\n\n"
    )

    sleep(5)


def test_turn_on():
    dev.turn_on()
    assert dev.is_turned_on() is True


def test_turn_off():
    dev.turn_off()
    assert dev.is_turned_on() is False


def test_disconnect():
    dev.disconnect()
