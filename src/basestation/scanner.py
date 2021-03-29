import argparse
import logging
import sys
from bleak import BleakScanner
from .device import BasestationDevice
from .const import NAME_SUFFIX

_logger = logging.getLogger(__name__)


class BasestationScanner:
    async def discover():
        devices = []
        for d in await BleakScanner.discover():
            if d.name.startswith(NAME_SUFFIX):
                # TODO: should probably also check for existence of service
                devices.append(BasestationDevice(d.address))

        return devices
