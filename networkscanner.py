import scapy.all as scapy
import optparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    print("IP address\t\tMAC address\n-------------------------------------------------------")
    for element in answered_list:
        print(f"{element[1].psrc}\t\t{element[1].hwsrc}")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Target IP/IP range")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify an IP address, use --help for more info")
    return options

scan(get_arguments().ip)
