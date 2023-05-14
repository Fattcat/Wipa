import subprocess

# create WISCAN folder if it does not exist

subprocess.run(["mkdir", "-p", "WISCAN"])

# run command to scan all WiFi networks

result = subprocess.run(["termux-wifi-scaninfo"], stdout=subprocess.PIPE)

# decode the output and split into lines

output = result.stdout.decode().split("\n")

# open scan.txt file in write mode

with open("WISCAN/scan.txt", "w") as f:

    for line in output:

        # check if the line contains details of a WiFi network

        if "SSID" in line:

            ssid = line.split(": ")[1].strip()

        elif "BSSID" in line:

            bssid = line.split(": ")[1].strip()

        elif "Capabilities" in line:

            cap = line.split(": ")[1].strip()

            # check if the network is secured

            if "WEP" in cap:

                security = "WEP"

            elif "WPA" in cap:

                security = "WPA"

            else:

                security = "Open"

        elif "Signal level" in line:

            signal = line.split(": ")[1].strip()

            # write the details to the file

            f.write(f"SSID: {ssid}\nBSSID: {bssid}\nSecurity: {security}\nSignal: {signal}\n\n")
