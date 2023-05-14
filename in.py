import os

import re

def wifi_connect(ssid, password):

    output = os.popen("iwlist wlan0 scan").read()

    networks = re.findall('ESSID:"(.*)"\n', output)

    if ssid not in networks:

        print(f"Error: {ssid} not found in available networks")

        return False

    os.system(f"iwconfig wlan0 essid {ssid} key s:{password}")

    os.system("dhclient wlan0")

    return True

