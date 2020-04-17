import binascii
import socket

MAC = '1a-2b-3c-4d-5e-6f'
PORT = 9

#格式化 mac 地址
def formatMac(mac):
    if(len(mac) != 12):
        if(len(mac) == 17):
            if(mac.count(":") == 5 or mac.count("-") == 5):
                sep = mac[2]
                mac = mac.replace(sep, "")
    return mac

#创建唤醒包
def createMagicPacket(mac):
    data = 'FF' * 6 + str(mac) * 16
    send_data = binascii.unhexlify(data)
    # print(send_data)
    return send_data

#发送魔术唤醒包
def sendMagicPacket(data):
    #广播地址
    broadcastAddress = '255.255.255.255'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(data, (broadcastAddress, PORT))

def main():
    mac = formatMac(MAC)
    data = createMagicPacket(mac)
    sendMagicPacket(data)
    print("已开机")

if __name__ == '__main__':
    main()