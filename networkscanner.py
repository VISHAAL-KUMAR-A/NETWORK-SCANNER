import scapy
import optparse

def scan(ip):
  arp_request=scapy.ARP()
