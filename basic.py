from scapy.all import sniff

def pkt_callback(packet):
    packet.show()

sniff(prn= pkt_callback, count= 3)