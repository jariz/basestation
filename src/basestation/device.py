from .const import (
    PWR_CHARACTERISTIC,
    IDENTIFY_CHARACTERISTIC,
    PWR_ON,
    PWR_STANDBY,
    SERVICE,
)
from bluepy.btle import Peripheral, ADDR_TYPE_RANDOM


class BasestationDevice:
    def __init__(self, mac):
        self.mac = mac

    def connect(self):
        self.client = Peripheral()
        self.client.connect(self.mac, ADDR_TYPE_RANDOM)
        self.service = self.client.getServiceByUUID(SERVICE)

    def disconnect(self):
        self.client.disconnect()

    def is_turned_on(self):
        char = self.service.getCharacteristics(PWR_CHARACTERISTIC)[0]
        pwr = char.read()
        return pwr != PWR_STANDBY

    def turn_on(self):
        char = self.service.getCharacteristics(PWR_CHARACTERISTIC)[0]
        return char.write(PWR_ON, True)

    def turn_off(self):
        char = self.service.getCharacteristics(PWR_CHARACTERISTIC)[0]
        return char.write(PWR_STANDBY, True)

    def identify(self):
        char = self.service.getCharacteristics(IDENTIFY_CHARACTERISTIC)[0]
        return char.write(
            # any byte will do really, which is why it's not in consts.py
            b"\x01"
        )
