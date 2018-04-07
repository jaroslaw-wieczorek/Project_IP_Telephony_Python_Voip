from scapy.all import RTP, UDP, Ether, IP
from scapy.fields import *

r = RTP()

u = UDP()

ip = IP()

e = Ether()



p = e / ip / u / r


p.show()

print(p.command())