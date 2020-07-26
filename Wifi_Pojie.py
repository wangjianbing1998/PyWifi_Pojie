import time

import pywifi
from pywifi import const


def testwifi(ssid, password):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    print('网卡名称', ifaces.name())

    ifaces.scan()
    print('可连接网络： ', '\n'.join([r.ssid for r in ifaces.scan_results()]))
    ifaces.disconnect()

    print('正在连接', ssid)
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password  # wifi密钥 如果无密码，则应该设置此项CIPHER_TYPE_NONE

    ifaces.remove_all_network_profiles()
    tmp_profile = ifaces.add_network_profile(profile)

    ifaces.connect(tmp_profile)
    time.sleep(1)

    if ifaces.status() == const.IFACE_CONNECTED:
        print(ifaces.network_profiles()[0].ssid)
        return True
    else:
        return False


def main():
    ssid = 'data_server'

    test_wifi_file(ssid,'wordlist.TXT')
    # test_one_wifi(ssid)


def test_one_wifi(ssid):
    while True:
        if testwifi(ssid, 'hustjhlbigdata907'): #修改这里的密码即可
            print(f'wifi {ssid} 连接成功')
            break
        else:
            print(f'wifi {ssid} 连接失败 ...')
        time.sleep(2)


def test_wifi_file(ssid, path):
    with open(path, 'r') as files:
        print("start ...")

        f = files.readline()[:-1]
        print('[-]正在尝试:', f)
        bool = testwifi(ssid, f)
        if bool:
            print('[+]wifi连接成功!')
            print("密码为：", f)
        else:
            print("[-]wifi连接失败！")


if __name__ == "__main__":
    main()
