# Network Traffic Analyzer 🛡️  

📌 **A Python-based tool for capturing and analyzing network traffic to understand security insights.**  

## 🔍 Overview  
This project helps you capture, filter, and analyze network traffic using Python (`scapy`, `pyshark`). It provides insights into different protocols, identifies potential security threats, and serves as a great hands-on learning experience.  

## ⚡ Features  
✔️ Capture live network packets  
✔️ Filter traffic based on protocol (TCP, UDP, DNS, HTTP)  
✔️ Detect potential security risks (brute-force attempts, large data transfers)  
✔️ Generate reports with key findings  

## 🚀 Installation  
Ensure you have Python installed (3.8+). Then, install dependencies:  
```bash
pip install scapy pyshark
```
##  🛠️ Usage
Run the packet sniffer:
```bash
python basic.py
```
## 📊 Sample Output
```nginx
IP Packet: 192.168.1.10 -> 8.8.8.8 | Protocol: UDP
DNS Request: google.com
Potential brute-force attack detected from 192.168.1.5
```
## 📖 Learning Outcomes
✅ Understand networking fundamentals (OSI model, protocols, packets)
✅ Gain hands-on experience with network monitoring
✅ Learn how attackers exploit network vulnerabilities

##🤝 Contributing
Feel free to fork this repo and submit PRs for improvements!

## 📄 License
This project is licensed under the MIT License.
