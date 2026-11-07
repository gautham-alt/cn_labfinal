import socket
import struct

# Convert MAC address into readable format
def get_mac_address(address):
    return ':'.join('%02x' % b for b in address)

# Create raw socket
s = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.htons(3)
)

print("Packet Capturing Started...")
print("Press CTRL+C to stop\n")

try:
    while True:

        # Receive packet
        packet, addr = s.recvfrom(65535)

        # Ethernet Header (14 bytes)
        eth_header = packet[:14]

        dest_mac, src_mac, protocol = struct.unpack(
            '!6s6sH', eth_header
        )

        print("\n--------------------------------")
        print("Ethernet Header")
        print("Source MAC      :", get_mac_address(src_mac))
        print("Destination MAC :", get_mac_address(dest_mac))

        # IPv4 Protocol
        if protocol == 0x0800:

            ip_header = packet[14:34]

            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            version_ihl = iph[0]
            ihl = (version_ihl & 15) * 4

            ttl = iph[5]
            proto = iph[6]

            src_ip = socket.inet_ntoa(iph[8])
            dest_ip = socket.inet_ntoa(iph[9])

            print("\nIPv4 Header")
            print("Source IP      :", src_ip)
            print("Destination IP :", dest_ip)
            print("TTL            :", ttl)

            # TCP
            if proto == 6:
                tcp_header = packet[14 + ihl:14 + ihl + 4]
                src_port, dest_port = struct.unpack(
                    '!HH', tcp_header
                )

                print("Transport      : TCP")
                print("Source Port    :", src_port)
                print("Destination Port:", dest_port)

            # UDP
            elif proto == 17:
                udp_header = packet[14 + ihl:14 + ihl + 4]
                src_port, dest_port = struct.unpack(
                    '!HH', udp_header
                )

                print("Transport      : UDP")
                print("Source Port    :", src_port)
                print("Destination Port:", dest_port)

            # ICMP
            elif proto == 1:
                print("Transport      : ICMP")

            else:
                print("Transport      : Other")

        # IPv6
        elif protocol == 0x86DD:
            print("Network Protocol: IPv6")

        # ARP
        elif protocol == 0x0806:
            print("Network Protocol: ARP")

        else:
            print("Network Protocol: Other")

except KeyboardInterrupt:
    print("\nPacket Capturing Stopped.")

finally:
    s.close()
