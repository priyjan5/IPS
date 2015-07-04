from scapy.all import *
from scapy.utils import rdpcap



pkts=rdpcap("./icmp2.pcap") 
samp = pkts[4]

print samp[Ether].src
print samp[Ether].dst
print samp[IP].src
print samp[IP].dst
samp[IP].ttl = 5
sendp(samp)

