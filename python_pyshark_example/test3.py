import scapy
from scapy.all import *
from scapy.utils import PcapReader
packets=rdpcap("./抖音.pcapng")
for data in packets:
  # if 'UDP' in data:
    s = repr(data)
    print(s)
    # print(data['Ether'].dst)
    # print(data['UDP'].sport)
    # break