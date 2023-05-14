import os

import time

import pywifi

from pywifi import const

def wifi_scan(duration):

    # Create a Wi-Fi object

    wifi = pywifi.PyWiFi()

    # Get the first interface (should be the only one)

    iface = wifi.interfaces()[0]

    # Turn on Wi-Fi radio

    iface.radio_on()

    # Begin the scan

    iface.scan()

    # Wait for the scan to complete

    time.sleep(duration)

    # Get scan results

    results = iface.scan_results()

    # Save results to file

    if not os.path.exists("WISCAN"):

        os.mkdir("WISCAN")

    with open("WISCAN/scan.txt", "w") as f:

        for r in results:

            f.write("SSID: {}\n".format(r.ssid))

            f.write("BSSID: {}\n".format(r.bssid))

            f.write("Signal Strength: {} dBm\n".format(r.signal))

            f.write("Security: {}\n".format(r.akm[0]))

            f.write("Vulnerability: {}\n\n".format(r.akm[-1]))

    # Turn off Wi-Fi radio

    iface.radio_off()

# Get scan duration input from user

duration = int(input("Enter scan duration in seconds: "))

# Run the scan and save results to file

wifi_scan(duration)

print("Scan completed! Results saved to WISCAN/scan.txt")
