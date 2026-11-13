# IP Connectivity (part 2)

## ipconn-101  (Question 13.58)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e3248dda841c39c5.png]
Router-Y#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
ia - IS-IS inter area, * - candidate default, U - per-user static route
o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
+ - replicated route, % - next hop override, p - overrides from PfR
Gateway of last resort is not set
10.0.0.0/8 is variably subnetted
B       10.0.0.0/8 [1/0] via 10.224.1.2
B       10.27.150.224/27 [20/0] via 10.224.1.3, 1w6d
S       10.128.0.0/9 [1/0] via 10.224.1.3
B       10.224.0.0/11 [20/0] via 10.224.1.5, 5d18h
B       10.224.0.0/15 [20/0] via 10.224.1.4, 5d18h
C       10.223.0.0/24 is directly connected, GigabitEthernet0/1
C       10.224.0.0/24 is directly connected, GigabitEthernet0/0
B       10.226.34.0/24 [20/0] via 10.224.1.5, 5d18h
PC A is communicating with another device at IP address 10.225.34.225. Through which router does router Y route the traffic?
- A. router A
- B. router B
- C. router C
- D. router D
ANSWER: C

## ipconn-102  (Question 13.63)
Which Windows command is used instead of the route print command to display the contents of the IP routing table?
- A. netstat-n
- B. ipconfig
- C. ifconfig
- D. netstat-r
ANSWER: D

## ipconn-103  (Question 13.89)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/1b5b9010ec3380b2.png]
An engineer just installed network 10.120.10.0/24. Which configuration must be applied to the R14 router to add the new network to its OSPF routing table?
- A. router ospf 100 network 10.120.10.0 0.0.0.255 area 0
- B. router ospf 100 area 0 network 10.120.10.0 0.0.0.255
- C. router ospf 120 network 10.120.10.0 255.255.255.0 area 0 ip route 10.120.10.0 255.255.255.0 fa0/1
- D. router ospf 100 network 10.120.10.0 255.255.255.0 area 0
ANSWER: A

## ipconn-104  (Question 14.4)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b95cd60e48870ec3.png]
Router R1 receives static routing updates from routers A, B, C. and D. The network engineer wants R1 to advertise static routes in OSPF area 1. Which summary address must be advertised in OSPF?
- A. 10.1.40.0/25
- B. 10.1.40.0/24
- C. 10.1.41.0/25
- D. 10.1.40.0/23
ANSWER: D

## ipconn-105  (Question 14.13)
Refer to the exhibit.
R_1# show ip route
.....
D	192.168.20.0/26 [90/24513456] via 10.10.10.1
R	192.168.20.0/24 [120/5] via 10.10.10.2
0	192.168.0.0/19 [110/219414] via 10.10.10.13
B	192.168.0.0/16 is variably subnetted, 4 subnets,4 masks
D	192.168.20.0/27 [90/4123710] via 10.10.10.12
D	192.168.20.0/25 [90/14464211] via 10.10.10.11
S*	0.0.0.0/0 [1/0] via 10.10.10.14
Packets are flowing from 192.168.10.1 to the destination at IP address 192.168.20.75. Which next hop will the router select for the packet?
- A. 10.10.10.1
- B. 10.10.10.11
- C. 10.10.10.12
- D. 10.10.10.14
ANSWER: B

## ipconn-106  (Question 14.32)
Which interface is used to send traffic to the destination network?
O 10.18.75.113/27 [110/6906] via G0/6
O 10.18.75.113/27 [110/23018] via G0/3
R 10.18.75.113/27 [120/16] via G0/16
R 10.18.75.113/27 [120/14] via G0/23
- A. G0/6
- B. G0/3
- C. G0/16
- D. G0/23
ANSWER: A

## ipconn-107  (Question 14.38)
Which interface is used to send traffic to the destination network?
D 10.47.114.119/29 [90/6451] via F0/2
D 10.47.114.119/29 [90/52201] via F0/20
R 10.47.114.119/29 [120/9] via F0/12
R 10.47.114.119/29 [120/10] via F0/10
- A. F0/2
- B. F0/20
- C. F0/12
- D. F0/10
ANSWER: A

## ipconn-108  (Question 14.48)
Refer to the exhibit.
R1# Gateway of last resort is 10.56.0.1 to network 0.0.0.0 S* 0.0.0.0/0 [1/0] via R1#
Gateway of last resort is 10.56.0.1 to network 0.0.0.0
S*   0.0.0.0/0 [1/0] via 10.56.0.1
10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C      10.56.0.0/16 is directly connected, Null0
C      10.56.0.0/26 is directly connected, Vlan58
C      10.56.0.0/17 is directly connected, Vlan59
C      10.56.0.0/24 is directly connected, Vlan60
When router R1 receives a packet with destination IP address 10.56.0.62, through which interface does it route the packet?
- A. Vlan59
- B. Vlan60
- C. Null0
- D. Vlan58
ANSWER: D

## ipconn-109  (Question 14.49)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/280475aa67926127.png]
A network engineer is verifying the settings on a new OSPF network. All OSPF configurations use the default values unless otherwise indicated. Which router does the engineer expect will be elected as the DR when all devices boot up simultaneously?
- A. R1
- B. R2
- C. R3
- D. R4
ANSWER: D

## ipconn-110  (Question 14.77)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/fb44249fa39bf3f2.png]
Router-Y#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
ia - IS-IS inter area, * - candidate default, U - per-user static route
o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
+ - replicated route, % - next hop override, p - overrides from PfR
Gateway of last resort is not set
10.0.0.0/8 is variably subnetted
S   10.0.0.0/8 [1/0] via 10.224.4.2
B   10.127.151.192/27 [20/0] via 10.224.4.3, 1w6d
S   10.128.0.0/9 [1/0] via 10.224.4.3
B   10.224.0.0/11 [20/0] via 10.224.4.5, 5d18h
B   10.224.0.0/15 [20/0] via 10.224.4.4, 5d18h
C   10.223.4.0/24 is directly connected, GigabitEthernet0/1
C   10.224.4.0/24 is directly connected, GigabitEthernet0/0
B   10.226.34.0/24 [20/0] via 10.224.4.5, 5d18h
PC A is communicating with another device at IP address 10.227.151.255.Through which router does router Y route the traffic?
- A. router A
- B. router B
- C. router C
- D. router D
ANSWER: D

## ipconn-111  (Question 14.78)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/bd37ea6738371d90.png]
What is preventing host A from reaching the internet?
- A. LAN and WAN network segments are different.
- B. IP address assignment is incorrect.
- C. The default gateway should be the first usable IP address.
- D. The domain name server is unreachable.
ANSWER: D

## ipconn-112  (Question 14.104)
Refer to the exhibit.
Refer to the exhibit.
R1#show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
ia - IS-IS inter area, * - candidate default, U - per-user static route
o - ODR, P - periodic downloaded static route
Gateway of last resort is 192.168.30.10 to network 0.0.0.0
192.168.30.0/29 is subnetted, 2 subnets
C  	  192.168.30.0 is directly connected, FastEthernet0/0
C 	  192.168.30.8 is directly connected, Serial0/0.1
192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
O IA 	  192.168.10.32/28 [110/193] via 192.168.30.10, 00:18:49, Serial0/0.1
O IA 	  192.168.10.0/27 [110/192] via 192.168.30.10, 00:18:49, Serial0/0.1
192.168.20.0/30 is subnetted, 1 subnets
O IA 	  192.168.20.0 [110/128] via 192.168.30.10, 00:18:49, Serial0/0.1
192.168.50.0/32 is subnetted, 1 subnets
C 	  192.168.50.1 is directly connected, Loopback0
O*IA 0.0.0.0/0 [110/84] via 192.168.30.10, 00:10:36, Serial0/0.1
What is the metric for the route to the 192.168.10.33 host?
- A. 84
- B. 110
- C. 192
- D. 193
ANSWER: D

## ipconn-113  (Question 14.1)
A network administrator wants the syslog server to filter incoming messages into different files based on their importance. Which filtering criteria must be used?
- A. message body
- B. process ID
- C. level
- D. facility
ANSWER: C

## ipconn-114  (Question 14.27)
What are two capabilities provided by VRRP within a LAN network? (Choose two)
- A. load sharing
- B. bandwidth optimization
- C. dynamic routing updates
- D. redundancy
- E. granular QoS
ANSWER: A, D

## ipconn-115  (Question 14.44)
Which type of protocol is VRRP?
- A. uses dynamic IP address assignment
- B. uses a destination IP address 224.0.0.102 for router-to-router communication
- C. uses Cisco-proprietary First Hop Redundancy Protocol
- D. allows two or more routers to act as a default gateway
ANSWER: D

## ipconn-116  (Question 15.8)
Refer to the exhibit.
100.0.0.0/8 is variably subnetted, 4 subnets, 4 masks
R    100.0.0.0/8 [120/2] via 192.168.3.1, 00:00:13, Ethernet0/3
S    100.100.0.0/16 [1/0] via 192.168.4.1
D    100.100.100.0/24 [90/435200] via 192.168.2.1, 00:00:13, Ethernet0/2
O    100.100.100.100/32 [110/21] via 192.168.1.1, 00:05:57, Ethernet0/1
How will the device handle a packet destined to IP address 100.100.100.100?
- A. It will always prefer the static route over dynamic routes and choose the route S 100.100.0.0/16 [1/0] via 192.168.4.1
- B. It will choose the route with the lowest metric R 100.0.0.0/8 [120/2] via 192.168.3.1, 00:00:13, Ethernet0/3
- C. It will choose the route with the highest metric D 100.100.100.0/24 [90/435200] via 192.168.2.1, 00:00:13, Ethernet0/2
- D. It will choose the route with the longest match O 100.100.100.100/32 [110/21] via 192.168.1.1, 00:05:57, Ethernet0/1
ANSWER: D

## ipconn-117  (Question 15.10)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/dfa90d58a4309fa5.png]
Which configuration parameter is preventing host С from reaching the internet?
- A. IP address assignment
- B. default gateway
- C. IP network mask
- D. automatic DNS
ANSWER: B

## ipconn-118  (Question 15.38)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e7eb29be80debff7.png]
With a reference bandwidth of 100 Gb on all routers, which path does router Y use to get to network 192.168.1.0/24?
- A. router C > D > A > F
- B. router E > B > F
- C. router E > F
- D. router C > D > A > B > F
ANSWER: D

## ipconn-119  (Question 15.44)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/01a577a8d4415953.png]
Inter-VLAN routing is configured on SW1. Client A is running Linux as an OS in VLAN 10 with a default gateway IP 10.0.0.1 but cannot ping client B in VLAN 20 running Windows. What action must be taken to verify that client A has the correct IP settings?
- A. Run the ifconfig command on client A to confirm that its IP and subnet mask fall within 255.254.0.0.
- B. Run the ipconfig command on client A and ensure that the IP address is within the host range of 10.0.0.1 – 10.0.255.254.
- C. Run the ipconfig command on client A to confirm that the correct 10.0.0.1 default gateway is used.
- D. Run the ifconfig command on client A to confirm that the subnet mask is set to 255.255.128.0
ANSWER: A

## ipconn-120  (Question 15.48)
Refer to the exhibit.
C:\Users\ADMIN>ipconfig
Windows IP Configuration
Ethernet adapter Ethernet:
<...>
Physical Address . . . . . . . . . . . : 04-42-1A-EE-AA-5E
DHCP Enabled . . . . . . . . . . . . . : Yes
Autoconfiguration Enabled. . . . . . . : Yes
Link-local IPv6 Address. . . . . . . . :
fe80::8a79:bcde:34dc:c11e35%(Preferred)
Ipv4 Address . . . . . . . . . . . . . : 192.168.3.20(Preferred)
Subnet Mask. . . . . . . . . . . . . . : 255.255.255.0
Lease Obtained . . . . . . . . . . . . : Thursday, 16 March 2023
6:25:01 AM
Lease Expires. . . . . . . . . . . . . : Sunday, 26 March 2023
4:17:26 PM
Default Gateway. . . . . . . . . . . . : 192.168.3.1
DHCP Server. . . . . . . . . . . . . . : 192.168.3.1
DHCPv6 IAID. . . . . . . . . . . . . . : 201605658
DHCPv6 Client DUID . . . . . . . . . . : 00-01-00-01-2A-3F-45-34-03-
13-23-EE-AD-5E
DNS Servers. . . . . . . . . . . . . . : 10.10.1.254
NetBIOS over Tcpip . . . . . . . . . . : Enabled
The user has connectivity to devices on network 192.168.3.0/24 but cannot reach users on the network 10.10.1.0/24. What is the first step to verify connectivity?
- A. Is the internet reachable?
- B. Is the default gateway reachable?
- C. Is the DNS server reachable?
ANSWER: B

## ipconn-121  (Question 15.83)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ecc18bcdbb4252b5.png]
Configurations for the switch and PCs are complete. Which configuration must be applied so that VLANs 2 and 3 communicate back and forth?
- A. interface GigabitEthernet0/0 ip address 10.10.2.10 255.255.252.0
- B. interface GigabitEthernet0/0.3 encapsulation dot1Q 10 ip address 10.10.2.10 255.255.255.252
- C. interface GigabitEthernet0/0.10 encapsulation dot1Q 3 ip address 10.10.2.10 255.255.254.0
- D. interface GigabitEthernet0/0.3 encapsulation dot1Q 3 native ip address 10.10.2.10 255.255.252.0
ANSWER: C

## ipconn-122  (Question 15.84)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/42cc1f90b415817d.png]
Wireless LAN adapter Wi-Fi:
Connection-specific DNS Suffix  . :
Description . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
Physical Address. . . . . . . . . : AC-63-DA-AC-B4-AD
DHCP Enabled. . . . . . . . . . . : No
Autoconfiguration Enabled . . . . : Yes
IPv6 Address. . . . . . . . . . . : ::70D6:5432:6D8A:90B2(Preferred)
Temporary IPv6 Address. . . . . . : ::dc3f:a66c:f996:bdb9(Preferred)
Link-local IPv6 Address . . . . . : fe80::7096:5693:6d8a:90ba%8(Preferred)
IPv4 Address. . . . . . . . . . . : 172.16.1.8(Preferred)
Subnet Mask . . . . . . . . . . . : 255.255.255.240
Default Gateway . . . . . . . . . : 172.16.1.1
DHCPv6 IAID . . . . . . . . . . . : 116155351
DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-BE-0A-47-3C-15-AB-80-12-F6
DNS Servers . . . . . . . . . . . : 172.16.1.3
172.16.1.4
NetBIOS over Tcpip. . . . . . . . : Enabled
During initial configuration testing, the Windows workstation PC1 cannot connect with the 172.16.2.0/24 network. Which set of actions corrects the configuration?
- A. Change the IP address to 172.16.1.9 and change the DNS server to 172.16.1.12 only.
- B. Change the IP address to 172.16.1.6 and change the DNS servers to 172.16.1.12 and 172.16.1.13.
- C. Change the IP address to 172.16.1.9 and change the default gateway to 172.16.1.7.
- D. Change the IP address to 172.16.1.6 and change the subnet mask to 255.255.255.248.
ANSWER: D

## ipconn-123  (Question 15.86)
Refer to the exhibit.
AA#show ip route
10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
C    10.0.0.0/30 is directly connected, GigabitEthernet0/0
L    10.0.0.1/32 is directly connected, GigabitEthernet0/0
C    10.10.0.0/30 is directly connected, GigabitEthernet0/1
L    10.10.0.1/32 is directly connected, GigabitEthernet0/1
O    10.20.0.0/30 [110/2] via 10.0.0.2, 00:00:40, GigabitEthernet0/0
O    10.30.0.0/30 [110/2] via 10.0.0.2, 00:00:40, GigabitEthernet0/0
172.16.0.0/24 is subnetted, 1 subnets
S    172.16.10.0 [1/0] via 10.0.0.2
192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C    192.168.10.0/24 is directly connected, GigabitEthernet0/2
L    192.168.10.1/32 is directly connected, GigabitEthernet0/2
S    192.168.20.0/24 [1/0] via 192.168.10.2
What is the administrative distance for the advertised prefix that includes the host IP address 10.30.0.1?
- A. 10.0.0.2
- B. 110
- C. 30
- D. 2
ANSWER: B

## ipconn-124  (Question 15.91)
Refer to the exhibit.
R1#show ip route
Gateway of last resort is 10.0.0.2 to network 0.0.0.0
10.0.0.0/8 is variably subnetted, 10 subnets, 3 masks
C 10.0.0.0/24 is directly connected, FastEthernet0/0
L 10.0.0.1/32 is directly connected, FastEthernet0/0
C 10.0.1.0/24 is directly connected, FastEthernet0/1
L 10.0.1.1/32 is directly connected, FastEthernet0/1
C 10.0.2.0/24 is directly connected, FastEthernet1/0
L 10.0.2.1/32 is directly connected, FastEthernet1/0
C 10.0.3.0/24 is directly connected, FastEthernet1/1
L 10.0.3.1/32 is directly connected, GigabitEthernet1/l
O 10.0.4.0/29 [110/2] via 10.0.4.2 00:00:03, GigabitEthernet1/1
S 10.1.0.0/16 [1/0] via 10.0.3.2
S 10.1.3.0/24 [1/0] via 10.0.3.2
S* 0.0.0.0/0 [1/0] via 10.0.0.2
How does router R1 forward packets destined to 10.0.4.10?
- A. via 10.0.4.2
- B. via FastEthernet1/1
- C. via FastEthernet0/1
- D. via 10.0.0.2
ANSWER: D

## ipconn-125  (Question 15.96)
R1 has learned route 10.10.10.0/24 via numerous routing protocols. Which route is installed?
- A. route with the lowest cost
- B. route with the next hop that has the highest IP
- C. route with the shortest prefix length
- D. route with the lowest administrative distance
ANSWER: D

## ipconn-126  (Question 15.98)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/605af093b7016397.png]
Which settings must be verified on workstation 1 to establish IP connectivity to server 1 using the server’s fully qualified domain name?
Option A IP address: 10.0.63.80 Subnet mask: 255.255.255.224 Default gateway: 10.0.71.0 DHCP server: 10.0.63.8
Option B IP address: 10.0.71.16 Subnet mask: 255.255.255.224 Default gateway: 10.0.71.1 DNS server: 10.0.63.5
Option C IP address: 10.0.63.80 Subnet mask: 255.255.255.0 Default gateway: 10.0.71.1 DNS server: 10.0.63.5
Option D IP address: 10.0.71.16 Subnet mask: 255.255.255.0 Default gateway: 10.0.71.0 DHCP server: 10.0.63.8
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B

## ipconn-127  (Question 15.99)
Refer to the exhibit. Which path is used by the router for Internet traffic?
[IMAGE: D:\CCNA_ontap\web\img/c3d6e84d72603cec.png]
R1#show ip route
Gateway of last resort is 10.10.11.2 to network 0.0.0.0
209.165.200.0/27 is subnetted, 1 subnets
B	209.165.200.224 [20/0] via 10.10.12.2, 00:10:34
10.0.0.0/8 is variably subnetted, 4 subnets, 3 masks
C		10.10.10.0/28 is directly connected, GigabitEthernet0/0
C		10.10.11.0/30 is directly connected, FastEthernet2/0
C		10.10.13.0/30 [110/2] via 10.10.10.1, 00:03:34, GigabitEthernet0/0
C		10.10.12.0/30 is directly connected, GigabitEthernet0/1
S*	0.0.0.0/0 [1/0] via 10.10.11.2
Switch1#show ip route
Gateway of last resort is not set
10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C		10.10.10.0/28 is directly connected, FastEthernet0/1
C		10.10.13.0/24 is directly connected, VLAN20
- A. 209.165.200.0/27
- B. 10.10.10.0/28
- C. 0.0.0.0/0
- D. 10.10.13.0/24
ANSWER: C

## ipconn-128  (Question 15.101)
Refer to the exhibit. To which device does Router1 send packets that are destined to host 10.10.13.165?
[IMAGE: D:\CCNA_ontap\web\img/dec1cce6b418ff48.png]
Router1#show ip route
Gateway of last resort is 10.10.11.2 to network 0.0.0.0
209.165.200.0/27 is subnetted, 1 subnets
B     209.165.200.224 [20/0] via 10.10.12.2,03:32:14
209.165.201.0/27 is subnetted, 1 subnets
B     209.165.201.0 [20/0] via 10.10.12.2,02:26:53
209.165.202.0/27 is subnetted, 1 subnets
B     209.165.202.128 [20/0] via 10.10.12.2,02:46:03
10.0.0.0/8 is variably subneted, 10 subnets, 4 masks
O     10.10.13.0/25 [110/2] via 10.10.10.1,00:00:04, GigabitEthernet0/0
O     10.10.13.128/28 [110/2] via 10.10.10.5,00:00:12, GigabitEthernet0/1
O     10.10.13.144/28 [110/2] via 10.10.10.9,00:01:57, GigabitEthernet0/2
O     10.10.13.160/29 [110/2] via 10.10.10.5,00:00:12, GigabitEthernet0/1
O     10.10.13.208/29 [110/2] via 10.10.10.13,00:01:57, GigabitEthernet0/3
S*  0.0.0.0/0 [1/0] via 10.10.11.2
- A. Router2
- B. Router3
- C. Router4
- D. Router5
ANSWER: B

## ipconn-129  (Question 15.102)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e77785dbfbefb71a.jpeg]
Router R1 is running three different routing protocols. Which route characteristic is used by the router to forward the packet that it receives for destination IP 172.16.32.1?
- A. longest prefix
- B. metric
- C. cost
- D. administrative distance
ANSWER: A

## ipconn-130  (Question 15.107)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/05db370ffdf8b988.png]
A packet is being sent across router R1 to host 172.16.3.14. To which destination does the router send the packet?
- A. 207.165.200.246 via Serial0/1/0
- B. 207.165.200.254 via Serial0/0/0
- C. 207.165.200.254 via Serial0/0/1
- D. 207.165.200.250 via Serial0/0/0
ANSWER: C

## ipconn-131  (Question 15.115)
Refer to the exhibit.
R1# show ip route | begin gateway
Gateway of last resort is not set
172.16.0.0/16 is variably subnetted, 3 subnets, 2 masks
C       172.16.1.0/24 is directly connected, FastEthernet0/0
L       172.16.1.3/32 is directly connected, FastEthernet0/0
EX      172.16.2.0/24 [170/2] via 207.165.200.250, 00:00:25, Serial0/0/0
O       192.168.1.0/24 [110/84437] via 207.165.200.254, 00:00:17, Serial0/0/1
D       192.168.2.0/24 [90/184437] via 207.165.200.254, 00:00:15, Serial0/0/1
E1      192.168.3.0/24 [110/1851437] via 207.165.200.254, 00:00:19, Serial0/0/1
207.165.200.0/24 is variably subnetted, 4 subnets, 2 masks
C       207.165.200.248/30 is directly connected, Serial0/0/0
L       207.165.200.249/32 is directly connected, Serial0/0/0
C       207.165.200.252/30 is directly connected, Serial0/0/1
L       207.165.200.253/32 is directly connected, Serial0/0/1
Which prefix did router R1 learn from internal EIGRP?
- A. 192.168.1.0/24
- B. 192.168.3.0/24
- C. 192.168.2.0/24
- D. 172.16.1.0/24
ANSWER: C

## ipconn-132  (Question 15.121)
Refer to the exhibit.
Router#show ip route
Gateway of last resort is 172.17.0.2 to network 0.0.0.0
S* 0.0.0.0/0 [1/0] via 172.17.0.2
10.0.0.0/8 is variably subnetted, 412 subnets, 10 masks
O E2 10.0.0.0/16 [110/10] via 10.2.24.1, 7w0d, Vlan82
O 10.2.17.0/24 [110/6] via 10.2.24.1, 6w4d, vlan82
O 10.2.17.0/24 [110/6] via 10.2.24.1, 6w4d, vlan82
O 10.2.23.0/24 [110/6] via 10.2.24.1, 7w0d, vlan82
--output suppressed--
C 10.173.5.0/24 is directly connected, vlan283
L 10.173.5.2/32 is directly connected, vlan283
What is the value of the administrative distance for the default gateway?
- A. 110
- B. 0
- C. 1
- D. 10
ANSWER: C

## ipconn-133  (Question 16.11)
Which technology allows for logical Layer 3 separation on physical network equipment?
- A. Virtual Switch System
- B. Virtual Route Forwarding
- C. IPsec Transport Mode
- D. Time Division Multiplexer
ANSWER: B

## ipconn-134  (Question 16.25)
Refer to the exhibit.
R3#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP, D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area,
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2,
E1 - OSPF external type 1, E2 - OSPF external type 2, i - IS-IS,
su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS
inter area, * - candidate default, I - per-user static route, o - ODR,
P - periodic download static route, H - NHRP, I - LISP,
a - application route, + - replicated route, % - next hop override,
p - overrides from PfR
Gateway of last resort is not set
10.0.0.0/8 is variably subnetted, 8 subnets, 4 masks
C    10.10.10.16/28 is directly connected, FastEthernet 0/0
L    10.10.10.17/32 is directly connected, FastEthernet 0/0
C    10.10.10.8/29 is directly connected, FastEthernet 0/1
L    10.10.10.9/32 is directly connected, FastEthernet 0/1
C    10.10.10.4/30 is directly connected, FastEthernet 0/2
L    10.10.10.5/32 is directly connected, FastEthernet 0/2
C    10.10.10.0/30 is directly connected, Serial 0/0
L    10.10.10.1/32 is directly connected, Serial 0/0
Which interface does a packet take to reach the destination address of 10.10.10.14?
- A. Serial 0/0
- B. FastEthernet 0/1
- C. FastEthernet 0/0
- D. FastEthernet 0/2
ANSWER: B

## ipconn-135  (Question 16.39)
Refer to the exhibit.
R4#show ip route
Gateway of last resort is not set
10.0.0.0/8 is variably subnetted, 14 subnets, 2 masks
O    10.0.12.0/24 [100/2] via 10.0.24.2, 00:02:27, GigabitEthernet0/1
D    10.0.13.0/24 [90/3072] via 10.0.34.3, 00:00:19, GigabitEthernet0/0
C    10.0.24.0/24 is directly connected, GigabitEthernet0/1
L    10.0.24.4/32 is directly connected, GigabitEthernet0/1
C    10.0.34.0/24 is directly connected, GigabitEthernet0/0
L    10.0.34.4/32 is directly connected, GigabitEthernet0/0
C    10.0.45.0/24 is directly connected, GigabitEthernet0/2
L    10.0.45.4/32 is directly connected, GigabitEthernet0/2
R    10.2.0.0/24 [120/1] via 10.0.45.5, 00:00:08, GigabitEthernet0/2
O    10.255.1.1/32 [100/3] via 10.0.34.3, 00:02:27, GigabitEthernet0/0
[100/3] via 10.0.24.2, 00:02:27, GigabitEthernet0/1
D    10.255.2.2/32 [90/130816] via 10.0.24.2, 00:01:46, GigabitEthernet0/1
O    10.255.3.3/32 [100/2] via 10.0.34.3, 00:02:27, GigabitEthernet0/0
C    10.255.4.4/32 is directly connected, Loopback0
R    10.255.5.5/32 [120/1] via 10.0.45.5, 00:00:08, GigabitEthernet0/2
Of the routes learned with dynamic routing protocols, which has the least preferred metric?
- A. Local
- B. EIGRP
- C. OSPF
- D. RIP
ANSWER: D

## ipconn-136  (Question 16.40)
Refer to the exhibit.
R1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP,
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area,
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2,
E1 - OSPF external type 1, E2 - OSPF external type 2, i - IS-IS,
su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2,
ia - IS-IS inter area, * - candidate default, I - per-user static route,
o - ODR, P - periodic downloaded static route, H - NHRP, I - LISP, a -
application route, + - replicated route, % - next hop override,
p - overrides from PFR
Gateway of last resort is not set
10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
C       10.10.10.0/24 is directly connected, GigabitEthernet0/0
L       10.10.10.1/32 is directly connected, GigabitEthernet0/0
C       10.10.20.0/24 is directly connected, GigabitEthernet1/0
L       10.10.20.1/32 is directly connected, GigabitEthernet1/0
C       10.10.30.0/24 is directly connected, GigabitEthernet2/0
L       10.10.30.1/32 is directly connected, GigabitEthernet2/0
192.168.18.0/24 is variably subnetted, 3 subnets, 3 masks
D       192.168.18.0/24 [90/3072] via 10.10.10.10, 00:13:10, GigabitEthernet0/0
R       192.168.18.0/27 [120/1] via 10.10.20.10, 00:09:15, GigabitEthernet1/0
O       192.168.18.0/28 [110/2] via 10.10.30.10, 00:12:56, GigabitEthernet2/0
Which interface does a packet take to reach the host address of 192.168.18.16?
- A. GigabitEthernet1/0
- B. GigabitEthernet0/0
- C. GigabitEthernet2/0
- D. Null0
ANSWER: A

## ipconn-137  (Question 16.41)
Refer to the exhibit.
Prefix               Interface   Next-hop
152.168.32.0/22      f0/0        10.10.1.2
152.168.32.0/24      f1/0        10.10.2.2
152.168.32.0/26      f2/0        10.10.3.2
152.168.32.0/23      f3/0        10.10.4.2
Which next hop is used to route packets to the application server at 152.168.32.85?
- A. 10.10.1.2
- B. 10.10.2.2
- C. 10.10.3.2
- D. 10.10.4.2
ANSWER: B

## ipconn-138  (Question 16.42)
Refer to the exhibit.
R1#show ip route static
10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
S    10.20.1.0/26 [1/0] via 172.16.1.4
S    10.20.1.0/24 [1/0] via 172.16.1.2
S    10.20.1.32/27 [1/0] via 172.16.1.3
192.168.2.0/24 is variably subnetted, 3 subnets, 3 masks
S    192.168.2.0/24 [1/0] via 172.16.1.4
S    192.168.2.64/27 [1/0] via 172.16.1.2
S    192.168.2.80/29 [1/0] via 172.16.1.3
[IMAGE: D:\CCNA_ontap\web\img/d0d33c21e7a58ddd.png]
What is the correct next hop for router R1 to reach IP addresses 192.168.2.86 and 10.20.1.50?
- A. 172.16.1.4
- B. 172.16.1.1
- C. 172.16.1.2
- D. 172.16.1.3
ANSWER: C

## ipconn-139  (Question 16.43)
A default route must be configured to use the IP address of 192.168.1.1 until a WAN circuit is installed. The WAN circuit will use a dynamic routing protocol with an Administrative Distance of 20. Which configuration must be applied to allow the dynamic route to take precedence when it is in place?
- A. ip route 0.0.0.0 0.0.0.0 192.168.1.1
- B. ip route 0.0.0.0 0.0.0.0 192.168.1.1 25
- C. ip route 0.0.0.0 0.0.0.0 192.168.1.1 track 1
- D. ip route 0.0.0.0 0.0.0.0 192.168.1.1 20
ANSWER: B

## ipconn-140  (Question 16.49)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/efc8488964f7d08f.png]
The loopback IP of R3 has been learned via the two interfaces on R1. R1 is configured with a reference bandwidth of 10 Gbps. Based on the metric calculations, which next hop IP would be used for outgoing routing?
- A. 10.12.0.5
- B. 10.12.0.2
- C. 10.12.0.1
- D. 10.12.0.6
ANSWER: D

## ipconn-141  (Question 16.52)
Refer to the exhibit.
R1#show ip route
S  192.168.64.0/18 [1/0] via 10.1.1.1
O  192.168.64.0/18 [110/236855] via 10.1.1.2
O  192.168.64.0/18 [110/229840] via 10.1.1.3
S  192.168.64.0/19 [1/0] via Null0
How will router R1 handle packets destined to 192.168.64.22?
- A. It will use the static route to 10.1.1.1.
- B. It will use the route with the highest AD and highest destination IP.
- C. It will route the packets to 10.1.1.2.
- D. It will drop the packets.
ANSWER: D

## ipconn-142  (Question 16.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5d6208ff75529395.png]
OSPF neighbors routers A, B, C, and D are sending a route for 10.227.150.160/27. When the current route for 10.227.150.160/27 becomes unavailable, which cost will router Y use to route traffic to 10.227.150.160/27?
- A. Cost 20
- B. Cost 30
- C. Cost 40
- D. Cost 50
ANSWER: B

## ipconn-143  (Question 16.55)
Refer to the exhibit.
AA#show ip route
10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
C    10.0.0.0/30 is directly connected, GigabitEthernet0/0
L    10.0.0.1/32 is directly connected, GigabitEthernet0/0
C    10.10.0.0/30 is directly connected, GigabitEthernet0/1
L    10.10.0.1/32 is directly connected, GigabitEthernet0/1
O    10.20.0.0/30 [110/2] via 10.0.0.2, 00:00:40, GigabitEthernet0/0
O    10.30.0.0/30 [110/2] via 10.0.0.2, 00:00:40, GigabitEthernet0/0
172.16.0.0/24 is subnetted, 1 subnets
S    172.16.10.0 [1/0] via 10.0.0.2
192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C    192.168.10.0/24 is directly connected, GigabitEthernet0/2
L    192.168.10.1/32 is directly connected, GigabitEthernet0/2
S    192.168.20.0/24 [1/0] via 192.168.10.2
What is the administrative distance for the advertised prefix that includes the host IP address 192.168.20.1?
- A. 0
- B. 192.168.10.2
- C. 24
- D. 1
ANSWER: D

## ipconn-144  (Question 16.58)
Refer to the exhibit.
10.0.0.0/8 is variably subnetted, 15 subnets, 2 masks
O    10.0.12.0/24 [110/2] via 10.0.14.1, 00:17:46, GigabitEthernet0/2
C    10.0.14.0/24 is directly connected, GigabitEthernet0/2
L    10.0.14.4/32 is directly connected, GigabitEthernet0/2
O    10.0.23.0/24 [110/2] via 10.0.34.3, 00:17:46, GigabitEthernet0/0
C    10.0.34.0/24 is directly connected, GigabitEthernet0/0
L    10.0.34.4/32 is directly connected, GigabitEthernet0/0
C    10.0.45.0/24 is directly connected, GigabitEthernet0/1
L    10.0.45.4/32 is directly connected, GigabitEthernet0/1
O    10.0.254.1/32 [110/2] via 10.0.14.1, 00:17:46, GigabitEthernet0/2
R    10.255.2.4/24 [90/1] via 10.0.45.5, 00:00:13, GigabitEthernet0/1
O    10.255.1.1/32 [110/2] via 10.0.14.1, 00:17:46, GigabitEthernet0/0
O    10.255.2.2/32 [110/3] via 10.0.34.3, 00:17:46, GigabitEthernet0/0
[110/3] via 10.0.14.1, 00:17:46, GigabitEthernet0/2
O    10.255.3.3/32 [110/2] via 10.0.34.3, 00:17:46, GigabitEthernet0/0
C    10.255.3.4/32 is directly connected, Loopback0
R    10.255.5.5/32 [90/1] via 10.0.45.5, 00:00:13, GigabitEthernet0/1
Which routes are configured with their default administrative distances?
- A. EIGRP
- B. OSPF
- C. RIP
- D. Local
ANSWER: B

## ipconn-145  (Question 16.67)
[IMAGE: D:\CCNA_ontap\web\img/5ebfb6eb993c781b.png]
Refer to the exhibit.
A packet is being sent across router R1 to host 172.16.0.14. To which destination does the router send the packet?
- A. 209.165.200.246 via Serial0/1/0
- B. 209.165.200.254 via Serial0/0/0
- C. 209.165.200.254 via Serial0/0/1
- D. 209.165.200.250 via Serial0/0/0
ANSWER: A

## ipconn-146  (Question 16.77)
Refer to the exhibit.
ip route 172.0.0.0 255.0.0.0 10.12.13.14
ip route 172.16.0.0 255.255.0.0 10.56.22.23
ip route 122.16.153.0 255.255.255.0 10.35.47.17
ip route 172.16.153.153 255.255.255.255 10.65.34.19
ip route 0.0.0.0 0.0.0.0 10.17.44.36
The static routes were implemented on the border router. What is the next hop IP address for a ping sent to 172.16.153.154 from the border router?
[IMAGE: D:\CCNA_ontap\web\img/ed470ef5f5e636f4.png]
- A. 10.35.47.17
- B. 10.65.34.19
- C. 10.12.13.14
- D. 10.56.22.23
ANSWER: D
