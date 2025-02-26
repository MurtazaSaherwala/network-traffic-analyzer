from scapy.all import sniff, DNS
 
 
def dns_callback(packet):
    if packet.haslayer(DNS):
        print(f"DNS Request: {packet[DNS].qd.qname.decode()}")


sniff(filter="udp port 53", prn=dns_callback, count=5)