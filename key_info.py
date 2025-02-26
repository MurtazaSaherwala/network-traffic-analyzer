from scapy.all import sniff, IP, TCP, UDP

def process_pkt(packet):
    if packet.haslayer(IP):
        protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"
        print(f"Packet :{packet[IP].src} -> {packet[IP].dst} | Protocol:{protocol}")

sniff(prn=process_pkt,count=10)