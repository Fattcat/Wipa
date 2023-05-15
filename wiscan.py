import wifi

import time

while True:

    # získa zoznam sietí WiFi

    networks = wifi.scan()

    # otvorí textový súbor SCAN.txt

    with open("SCAN.txt", "w") as file:

        # pre každú sieť vypíše informácie a zapíše ich do súboru

        for network in networks:

            ssid = network.ssid

            encryption = network.encryption

            signal = network.signal

            mac_address = network.address

            print(f"SSID: {ssid}, Encryption: {encryption}, Signal Strength: {signal}, MAC Address: {mac_address}")

            file.write(f"SSID: {ssid}, Encryption: {encryption}, Signal Strength: {signal}, MAC Address: {mac_address}\n")

    # počká 6 sekúnd pred ďalším skenovaním

    time.sleep(6)

