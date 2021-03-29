from .const import PWR_CHARACTERISTIC, IDENTIFY_CHARACTERISTIC, PWR_ON, PWR_STANDBY
from bleak import BleakClient


class BasestationDevice:
    def __init__(self, mac):
        self.mac = mac
        self.client = None

    async def connect(self):
        self.client = BleakClient(self.mac)
        await self.client.connect()

    async def disconnect(self):
        await self.client.disconnect()

    async def is_turned_on(self):
        pwr = await self.client.read_gatt_char(PWR_CHARACTERISTIC)
        return pwr[0] is not PWR_STANDBY[0]

    async def turn_on(self):
        return await self.client.write_gatt_char(PWR_CHARACTERISTIC, PWR_ON)

    async def turn_off(self):
        return await self.client.write_gatt_char(PWR_CHARACTERISTIC, PWR_STANDBY)

    async def identify(self):
        return await self.client.write_gatt_char(
            IDENTIFY_CHARACTERISTIC,
            # any byte will do really, which is why it's not in consts.py
            bytearray([0x01]),
        )
