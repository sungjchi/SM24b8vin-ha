FULL_NAME = "Eight 24-Bit Analog Inputs"
LINK = "https://sequentmicrosystems.com/products/eight-24-bit-analog-inputs-daq-8-layer-stackable-hat-for-raspberry-pi"

import SM24b8vin
API = SM24b8vin.SM24b8vin
DOMAIN = "SM24b8vin"
NAME_PREFIX = "sm24b8vin"
SM_MAP = {
    "sensor": {
        "voltage": {
            "chan_no": 8,
            "uom": "V",
            "com": {
                "get": "get_u_in",
            },
        },
    },
    "select": {
        "range": {
            "chan_no": 8,
            "com": {
                "get": "get_gain",
                "set": "set_gain",
            },
            "option_map": {
                "±24V": 0,
                "±12V": 1,
                "±6V": 2,
                "±3V": 3,
                "±1.5V": 4,
                "±0.75V": 5,
                "±0.37V": 6,
                "±0.18V": 7,
            }
        },
    },
}
