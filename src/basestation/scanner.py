import argparse
import logging
import sys
from bluepy.btle import Scanner

from .device import BasestationDevice
from .const import NAME_SUFFIX

_logger = logging.getLogger(__name__)


class BasestationScanner:
    def discover():
        devices = []
        scanner = Scanner()
        for d in scanner.scan():
            name = d.getValueText(9)

            if name is not None and name.startswith(NAME_SUFFIX):
                # TODO: should probably also check for existence of service
                devices.append(BasestationDevice(d.addr))

        return devices
