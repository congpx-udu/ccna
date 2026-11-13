# IP Connectivity (part 1)

## ipconn-1  (Question 6.9)
What is the benefit of using FHRP (First Hop Redundancy Protocol)?
- A. balancing traffic across multiple gateways in proportion to their loads
- B. reduced management overhead on network routers
- C. reduced ARP traffic on the network
- D. higher degree of availability
ANSWER: D

## ipconn-2  (Question 7.5)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b0c723805ba033aa.jpeg]
When PC-A sends traffic to PC-B, which network component is in charge of receiving the packet from PC-A verifying the IP addresses, and forwarding the packet to PC-B?
- A. Layer 2 switch
- B. firewall
- C. Load balancer
- D. Router
ANSWER: D

## ipconn-3  (Question 7.6)
Refer to the exhibit.
Router1#show ip route
Gateway of last resort is not set
209.165.200.0/27 is subnetted, 1 subnets
B	   209.165.200.224 [20/0] via 10.10.12.2, 00:08:34
10.0.0.0/8 is variably subnetted, 4 subnets, 3 masks
C	   10.10.10.0/28 is directly connected, GigabitEthernet0/0
C	   10.10.11.0/30 is directly connected, FastEthernet2/0
O	   10.10.13.0/24 [110/2] via 10.10.10.1, 00:09:25, GigabitEthernet0/0
C	   10.10.12.0/30 is directly connected, GigabitEthernet0/1
Which action is taken by the router when a packet is sourced from 10.10.10.2 and destined for 10.10.10.16?
- A. It discards the packets
- B. It uses a route that is similar to the destination address
- C. It floods packets to all learned next hops
- D. It queues the packets waiting for the route to be learned
ANSWER: A

## ipconn-4  (Question 7.12)
What is the purpose of using First Hop Redundancy Protocol in a specific subnet?
- A. forwards multicast hello messages between routers
- B. sends the default route to the hosts on a network
- C. filter traffic based on destination IP addressing
- D. ensures a loop-free physical topology
ANSWER: A

## ipconn-5  (Question 7.21)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f24a5f94e366ee51.jpeg]
Which two commands, when configured on router R1, fulfill these requirements? (Choose two)
– Packets toward the entire network 2001:db8:23::/64 must be forwarded through router R2. 
– Packets toward host 2001:db8:23::14 preferably must be forwarded through R3.
- A. ipv6 route 2001:db8:23::/128 fd00:12::2
- B. ipv6 route 2001:db8:23::14/128 fd00:13::3
- C. ipv6 route 2001:db8:23::14/64 fd00:12::2
- D. ipv6 route 2001:db8:23::14/64 fd00:12::2 200
- E. ipv6 route 2001:db8:23::/64 fd00:12::2
ANSWER: B, E

## ipconn-6  (Question 7.26)
Refer to the exhibit.
R1#show ip route
--output omitted--
Gateway of last resort is 192.168.14.4 to network 0.0.0.0
C     172.16.1.128/25 is directly connected, GigabitEthernet1/1/0
C     192.168.12.0/24 is directly connected, FastEthernet0/0
C     192.168.13.0/24 is directly connected, FastEthernet0/1
C     192.168.14.0/24 is directly connected, FastEthernet1/0
C     172.16.16.1 is directly connected, Loopback1
192.168.10.0/24 is variably subnetted, 3 subnets, 3 masks
O     192.168.10.0/24 [110/2] via 192.168.14.4, 00:03:01, FastEthernet1/0
O     192.168.10.32/27 [110/11] via 192.168.13.3, 00:00:11, FastEthernet0/1
O     192.168.0.0/16 [110/2] via 192.168.15.5, 00:05:11, FastEthernet1/1
D     192.168.10.1/32 [90/52778] via 192.168.12.2, 00:05:11, FastEthernet0/0
O*E2  0.0.0.0/0 [110/1] via 192.168.14.4, 00:05:11, FastEthernet1/0
If R1 receives a packet destined to 172.16.1.1, to which IP address does it send the packet?
- A. 192.168.12.2
- B. 192.168.13.3
- C. 192.168.14.4
- D. 192.168.15.5
ANSWER: C

## ipconn-7  (Question 7.36)
Refer to the exhibit.
[TABLE]
R2#show ip route
C 192.168.1.0/26 is directly connected, FastEthernet0/1
[/TABLE]
Which two prefixes are included in this routing table entry? (Choose two)
- A. 192.168.1.17
- B. 192.168.1.61
- C. 192.168.1.64
- D. 192.168.1.127
- E. 192.168.1.254
ANSWER: A, B

## ipconn-8  (Question 7.52)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5b0bece01f11f153.jpeg]
R3#show ip ospf neighbor
Neighbor ID  Pri   State          Dead Time  Address        Interface
1.1.1.1        1   2WAY/DROTHER   00:00:35   172.16.10.1    GigabitEthernet0/0
2.2.2.2        1   2WAY/DROTHER   00:00:35   172.16.10.2    GigabitEthernet0/0
4.4.4.4        1   FULL/BDR       00:00:35   172.16.10.4    GigabitEthernet0/0
5.5.5.5        1   FULL/DR        00:00:35   172.16.10.5    GigabitEthernet0/0
R5 is the current DR on the network, and R4 is the BDR. Their interfaces are flapping, so a network engineer wants the OSPF network to elect a different DR and BDR. Which set of configurations must the engineer implement?
[TABLE]
Option A
R4(config)#interface gi0/0
R4(config-if)#ip ospf priority 20
R5(config)#interface gi0/0
R5(config-if)#ip ospf priority 10 | Option B
R2(config)#interface gi0/0
R2(config-if)#ip ospf priority 259
R3(config)#interface gi0/0
R3(config-if)#ip ospf priority 256
---
Option C
R3(config)#interface gi0/0
R3(config-if)#ip ospf priority 255
R2(config)#interface gi0/0
R2(config-if)#ip ospf priority 240 | Option D
R5(config)#interface gi0/0
R5(config-if)#ip ospf priority 120
R4(config)#interface gi0/0
R4(config-if)#ip ospf priority 110
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: C

## ipconn-9  (Question 7.53)
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
C       192.168.30.0 is directly connected, FastEthernet0/0
C       192.168.30.8 is directly connected, Serial0/0.1
192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
O IA    192.168.10.32/28 [110/193] via 192.168.30.10, 00:11:34, Serial0/0.1
O IA    192.168.10.0/27 [110/192] via 192.168.30.10, 00:11:34, Serial0/0.1
192.168.20.0/30 is subnetted, 1 subnets
O IA    192.168.20.0 [110/128] via 192.168.30.10, 00:11:34, Serial0/0.1
192.168.50.0/32 is subnetted, 1 subnets
C       192.168.50.1 is directly connected, Loopback0
O*IA 0.0.0.0/0 [110/84] via 192.168.30.10, 00:11:21, Serial0/0.1
What is the metric of the route to the 192.168.10.33/28 subnet?
- A. 84
- B. 110
- C. 128
- D. 192
- E. 193
ANSWER: E

## ipconn-10  (Question 8.8)
What are two benefits of FHRPs? (Choose two)
- A. They prevent loops in the Layer 2 network.
- B. They allow encrypted traffic.
- C. They are able to bundle multiple ports to increase bandwidth
- D. They enable automatic failover of the default gateway.
- E. They allow multiple devices to serve as a single virtual gateway for clients in the network
ANSWER: D, E

## ipconn-11  (Question 8.19)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/15fc7892c1fd36e9.jpeg]
A network engineer is in the process of establishing IP connectivity between two sites. Routers R1 and R2 are partially configured with IP addressing. Both routers have the ability to access devices on their respective LANs. Which command set configures the IP connectivity between devices located on both LANs in each site?
- A. R1
ip route 0.0.0.0 0.0.0.0 209.165.200.225
R2
ip route 0.0.0.0 0.0.0.0 209.165.200.226
- B. R1
ip route 0.0.0.0 0.0.0.0 209.165.200.226
R2
ip route 0.0.0.0 0.0.0.0 209.165.200.225
- C. R1
ip route 192.168.1.0 255.255.255.0 GigabitEthernet0/0
R2
ip route 10.1.1.1 255.255.255.0 GigabitEthernet0/0
- D. R1
ip route 192.168.1.1 255.255.255.0 GigabitEthernet0/1
R2
ip route 10.1.1.1 255.255.255.0 GigabitEthernet0/1
ANSWER: B

## ipconn-12  (Question 8.26)
What is a function of a Layer 3 switch?
- A. move frames between endpoints limited to IP addresses
- B. transmit broadcast traffic when operating in Layer 3 mode exclusively
- C. forward Ethernet frames between VLANs using only MAC addresses
- D. flood broadcast traffic within a VLAN
ANSWER: A

## ipconn-13  (Question 8.39)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d5f3441b0abf5404.jpeg]
Which command must be issued to enable a floating static default route on router A?
- A. ip route 0.0.0.0 0.0.0.0 192.168.2.1 10
- B. ip route 0.0.0.0 0.0.0.0 192.168.1.2
- C. ip route 0.0.0.0 0.0.0.0 192.168.1.2 10
- D. ip default-gateway 192.168.2.1
ANSWER: C

## ipconn-14  (Question 8.40)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d330b01fa1efe7a5.jpeg]
Router R1 currently is configured to use R3 as the primary route to the Internet, and the route uses the default administrative distance settings. A network engineer must configure R1 so that it uses R2 as a backup, but only if R3 goes down. Which command must the engineer configure on R1 so that it correctly uses R2 as a backup route, without changing the administrative distance configuration on the link to R3?
- A. ip route 0.0.0.0 0.0.0.0 g0/1 6
- B. ip route 0.0.0.0 0.0.0.0 g0/1 1
- C. ip route 0.0.0.0 0.0.0.0 209.165.201.5 10
- D. ip route 0.0.0.0 0.0.0.0 209.165.200.226 1
ANSWER: A

## ipconn-15  (Question 8.41)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/455eaf0a9f7eebf6.jpeg]
An engineer is updating the R1 configuration to connect a new server to the management network. The PCs on the management network must be blocked from pinging the default gateway of the new server. Which command must be configured on R1 to complete the task?
- A. R1(config)#ip route 172.16.2.0 255.255.255.0 192.168.1.15
- B. R1(config)#ip route 172.16.2.2 255.255.255.255 gi0/0
- C. R1(config)#ip route 172.16.2.0 255.255.255.0 192.168.1.5
- D. R1(config)#ip route 172.16.2.2 255.255.255.248 gi0/1
ANSWER: B

## ipconn-16  (Question 8.45)
Refer to the exhibit.
Which configuration allows routers R14 and R86 to form an OSPFv2 adjacency while acting as a central point for exchanging OSPF information between routers?
[TABLE]
Option A
R14# 
interface FastEthernet0/0 
ip address 10.73.65.65 255.255.255.252 
ip ospf network broadcast 
ip ospf priority 0 
ip mtu 1400
router ospf 10 
router-id 10.10.1.14 
network 10.10.1.14 0.0.0.0 area 0 
network 10.73.65.64 0.0.0.3 area 0
R86#
interface Loopback0
ip address 10.10.1.86 255.255.255.255
interface FastEthernet0/0 
ip address 10.73.65.66 255.255.255.252 
ip ospf network broadcast 
ip mtu 1500
router ospf 10 
router-id 10.10.1.86 
network 10.10.1.86 0.0.0.0 area 0 
network 10.73.65.64 0.0.0.3 area 0 | Option B
R14#
interface FastEthernet0/0 
ip address 10.73.65.65 255.255.255.252 
ip ospf network broadcast 
ip ospf priority 255
ip mtu 1500
router ospf 10
router-id 10.10.1.14
network 10.10.1.14 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0
R86#
interface FastEthernet0/0
ip address 10.73.65.66 255.255.255.252 
ip ospf network broadcast 
ip mtu 1500
router ospf 10
router-id 10.10.1.86
network 10.10.1.86 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0
---
Option C
R14#
interface Loopback0 
ip ospf 10 area 0
interface FastEthernet0/0
ip address 10.73.65.65 255.255.255.252
ip ospf network broadcast
ip ospf 10 area 0
ip mtu 1500
router ospf 10
ip ospf priority 255
router-id 10.10.1.14
R86#
interface Loopback0
ip ospf 10 area 0
interface FastEthernet0/0
ip address 10.73.65.66 255.255.255.252
ip ospf network broadcast
ip ospf 10 area 0
ip mtu 1500
router ospf 10 
router-id 10.10.1.86 | Option D
R14#
interface FastEthernet0/0
ip address 10.73.65.65 255.255.255.252
ip ospf network broadcast
ip ospf priority 255
ip mtu 1500
router ospf 10 
router-id 10.10.1.14 
network 10.10.1.14 0.0.0.0 area 0 
network 10.73.65.64 0.0.0.3 area 0
R86#
interface FastEthernet0/0 
ip address 10.73.65.66 255.255.255.252 
ip ospf network broadcast 
ip mtu 1400
router ospf 10 
router-id 10.10.1.86
network 10.10.1.86 0.0.0.0 area 0 
network 10.73.65.64 0.0.0.3 area 0
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B

## ipconn-17  (Question 8.48)
A network engineer must configure two new subnets using the address block 10.70.128.0/19 to meet these requirements:
* The first subnet must support 24 hosts.
* The second subnet must support 472 hosts
* Both subnets must use the longest subnet mask possible from the address block
Which two configurations must be used to configure the new subnets and meet a requirement to use the first available address in each subnet for the router interfaces? (Choose two)
- A. interface vlan 4722
ip address 10.70.133.17 255.255.255.192
- B. interface vlan 3002
ip address 10.70.147.17 255.255.255.224
- C. interface vlan 1148
ip address 10.70.148.1 255.255.254.0
- D. interface vlan 1234
ip address 10.70.159.1 255.255.254.0
- E. interface vlan 155
ip address 10.70.155.65 255.255.255.224
ANSWER: C, E

## ipconn-18  (Question 8.50)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3fb338377947522d.jpeg]
Traffic sourced from the loopback0 interface is trying to connect via ssh to the host at 10.0.1.15. What is the next hop to the destination address?
- A. 192.168.0.7
- B. 192.168.0.4
- C. 192.168.0.40
- D. 192.168.3.5
ANSWER: A

## ipconn-19  (Question 8.52)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/cfc7348dcd52127c.jpeg]
Which action must be taken to ensure that router A is elected as the DR for OSPF area 0?
- A. Configure the OSPF priority on router A with the lowest value between the three routers
- B. Configure the router A interfaces with the highest OSPF priority value within the area.
- C. Configure router A with a fixed OSPF router ID.
- D. Configure router B and router C as OSPF neighbors of router A.
ANSWER: B

## ipconn-20  (Question 8.64)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f11cbe6d1164d83f.jpeg]
An IP subnet must be configured on each router that provides enough addresses for the number of assigned hosts and anticipates no more than 10% growth for new hosts. Which configuration script must be used?
[TABLE]
Option A
R7#
configure terminal 
interface Fa1/0
ip address 10.1.56.1 255.255.240.0 
no shutdown
R8#
configure terminal 
interface Fa0/0
ip address 10.9.32.1 255.255.224.0 
no shutdown
R9#
configure terminal 
interface Fa1/1
ip address 10.23.96.1 255.255.192.0 
no shutdown | Option B
R7#
configure terminal 
interface Fa1/0
ip address 10.1.56.1 255.255.248.0 
no shutdown
R8#
configure terminal 
interface Fa0/0
ip address 10.9.32.1 255.255.254.0 
no shutdown
R9#
configure terminal 
interface Fa1/1
ip address 10.23.96.1 255.255.248.0 
no shutdown
---
Option C
R7#
configure terminal 
interface Fa1/0
ip address 10.1.56.1 255.255.252.0 
no shutdown
R8#
configure terminal 
interface Fa0/0
ip address 10.9.32.1 255.255.255.0 
no shutdown
R9#
configure terminal 
interface Fa1/1
ip address 10.23.96.1 255.255.240.0 
no shutdown | Option D
R7#
configure terminal 
interface Fa1/0
ip address 10.1.56.1 255.255.192.0 
no shutdown
R8#
configure terminal 
interface Fa0/0
ip address 10.9.32.1 255.255.224.0 
no shutdown
R9#
configure terminal 
interface Fa1/1
ip address 10.23.96.1 255.255.128.0 
no shutdown
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: C

## ipconn-21  (Question 8.65)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9b80b7999062b4ad.jpeg]
Which network prefix was learned via EIGRP?
- A. 172.16.0.0/16
- B. 207.165.200.0/24
- C. 192.168.2.0/24
- D. 192.168.1.0/24
ANSWER: C

## ipconn-22  (Question 8.68)
Refer to the exhibit.
[TABLE]
R1#show run
!
router ospf 1
auto-cost reference-bandwidth 100000
!
interface GigabitEthernet0/0
bandwidth 10000000
!
interface GigabitEthernet0/1
bandwidth 100000000
!
interface GigabitEthernet0/2
ip ospf cost 100
!
interface GigabitEthernet0/3
ip ospf cost 1000
[/TABLE]
Router R1 resides in OSPF Area 0. After updating the R1 configuration to influence the paths that it will use to direct traffic, an engineer verified that each of the four Gigabit interfaces has the same route to 10.10.0.0/16. Which interface will R1 choose to send traffic to reach the route?
- A. GigabitEthernet0/0
- B. GigabitEthernet0/1
- C. GigabitEthernet0/2
- D. GigabitEthernet0/3
ANSWER: B

## ipconn-23  (Question 8.75)
OSPF must be configured between routers R1 and R2. Which OSPF configuration must be applied to router R1 to avoid a DR/BDR election?
- A. router ospf 1
network 192.168.1.1 0.0.0.0 area 0
interface e1/1
ip address 192.160.1.1 255.255.255.252
ip ospf network broadcast
- B. router ospf 1
network 192.168.1.1 0.0.0.0 area 0
interface e1/1
ip address 192.168.1.1 255.255.255.252
ip ospf cost 0
- C. router ospf 1
network 192.168.1.1 0.0.0.0 area 0
hello interval 15
interface e1/1
ip address 192.168.1.1 255.255.255.252
- D. router ospf 1
network 192.168.1.1 0.0.0.0 area 0
interface e1/1
ip address 192.168.1.1 255.55.255.252
ip ospf network point-to-point
ANSWER: D

## ipconn-24  (Question 8.78)
Refer to the exhibit.
[TABLE]
EIGRP 10.10.10.0/24[90/1441] via F0/10
EIGRP 10.10.10.0/24[90/144] via F0/11
EIGRP 10.10.10.0/24[90/1441] via F0/12
OSPF 10.10.10.0/24[110/20] via F0/13
OSPF 10.10.10.0/24[110/30] via F0/14
[/TABLE]
Packets received by the router from BGP enter via a serial interface at 209.165.201.10. Each route is present within the routing table. Which interface is used to forward traffic with a destination IP of 10.10.10.24?
- A. F0/10
- B. F0/11
- C. F0/12
- D. F0/13
ANSWER: B

## ipconn-25  (Question 9.4)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/04bbf4f596f6bced.jpeg]
Which two configurations must the engineer apply on this network so that R1 becomes the DR? (Choose two)
- A. R1(config)#interface fastethernet0/0
R1(config-if)#ip ospf priority 200
- B. R1(config)#router ospf 1
R1(config-router)#router-id 192.168.100.1
- C. R3(config)#interface fastethernet0/0
R3(config-if)#ip ospf priority 0
- D. R1(config)#interface fastethernet0/0
R1(config-if)#ip ospf priority 0
- E. R3(config)#interface fastethernet0/0
R3(config-if)#ip ospf priority 200
ANSWER: A, C

## ipconn-26  (Question 9.5)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/15a893bb3ecc3c34.jpeg]
The router has been configured with a supernet to accommodate the requirement for 380 users on a subnet. The requirement already considers 30% future growth. Which configuration verifies the IP subnet on router R4?
- A. Subnet: 10.7.54.0
Subnet mask: 255.255.254.0
Broadcast address: 10.7.54.255
Usable IP address range: 10.7.54.1 – 10.7.55.254
- B. Subnet: 10.7.54.0
Subnet mask: 255.255.254.0
Broadcast address: 10.7.55.255
Usable IP address range: 10.7.54.1 – 10.7.55.254
- C. Subnet: 10.7.54.0
Subnet mask: 255.255.128.0
Broadcast address: 10.7.55.255
Usable IP address range: 10.7.54.1 – 10.7.55.254
- D. Subnet: 10.7.54.0
Subnet mask: 255.255.255.0
Broadcast address: 10.7.54.255
Usable IP address range: 10.7.54.1 – 10.7.55.254
ANSWER: B

## ipconn-27  (Question 9.11)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/58a3f7a8bc8f6f74.jpeg]
Which route must be configured on R1 so that OSPF routing is used when OSPF is up. But the server is still reachable when OSPF goes down?
- A. ip route 10.1.1.10 255.255.255.255 172.16.2.2 100
- B. ip route 10.1.1.0 255.255.255.0 gi0/1 125
- C. ip route 10.1.1.0 255.255.255.0 172.16.2.2 100
- D. ip route 10.1.1.10 255.255.255.255 gi0/0 125
ANSWER: D

## ipconn-28  (Question 9.14)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6a1ff273265c9d00.jpeg]
Which command configures OSPF on the point-to-point link between routers R1 and R2?
- A. network 10.0.0.0 0.0.0.255 area 0
- B. neighbor 10.1.2.0 cost 180
- C. ip ospf priority 100
- D. router-id 10.0.0.15
ANSWER: A

## ipconn-29  (Question 9.21)
Refer to the exhibit.
A#show ip ospf neighbor
Neighbor ID  Pri   State       Dead Time   Address       Interface
172.1.1.1    1     EXCHANGE/-  00:00:36    172.16.32.1   Serial0.1
An engineer assumes a configuration task from a peer. Router A must establish an OSPF neighbor relationship with neighbor 172.1.1.1. The output displays the status of the adjacency after 2 hours. What is the next step in the configuration process for the routers to establish an adjacency?
- A. Set the router B OSPF ID to the same value as its IP address
- B. Set the router B OSPF ID to a nonhost address
- C. Configure a point-to-point link between router A and router B
- D. Configure router A to use the same MTU size as router B
ANSWER: D

## ipconn-30  (Question 9.22)
Refer to the exhibit.
CPE#show ip route
192.168.1.0/24 is variably subnetted, 3 subnets, 3 masks
B    192.168.1.0/24 [20/1] via 192.168.12.2, 00:00:06
R    192.168.1.128/25 [120/5] via 192.168.13.3, 00:02:22, Ethernet0/1
O    192.168.1.192/26 [110/11] via 192.168.14.4, 00:02:22, Ethernet0/2
D    192.168.1.224/27 [90/1024640] via 192.168.15.5, 00:01:33, Ethernet0/3
All traffic enters the CPE router from interface Serial0/3 with an IP address of 192.168.50.1. Web traffic from the WAN is destined for a LAN network where servers are load-balanced. An IP packet with a destination address of the HTTP virtual IP of 192.168.1.250 must be forwarded. Which routing table entry does the router use?
- A. 192.168.1.0/24 via 192.168.12.2
- B. 192.168.1.128/25 via 192.168.13.3
- C. 192.168.1.192/26 via 192.168.14.4
- D. 192.168.1.224/27 via 192.168.15.5
ANSWER: D

## ipconn-31  (Question 9.27)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9b22465db2b33447.png]
A static route must be configured on R14 to forward traffic for the 172.21.34.0/25 network that resides on R86. Which command must be used to fulfill the request?
- A. ip route 172.21.34.0 255.255.255.192 10.73.65.65
- B. ip route 172.21.34.0 255.255.255.0 10.73.65.65
- C. ip route 172.21.34.0 255.255.128.0 10.73.65.64
- D. ip route 172.21.34.0 255.255.255.128 10.73.65.66
ANSWER: D

## ipconn-32  (Question 9.29)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5b588f7319736056.jpeg]
A company is configuring a failover plan and must implement the default routes in such a way that a floating static route will assume traffic forwarding when the primary link goes down. Which primary route configuration must be used?
- A. ip route 0.0.0.0 0.0.0.0 192.168.0.2 GigabitEthernet1/0
- B. ip route 0.0.0.0 0.0.0.0 192.168.0.2 tracked
- C. ip route 0.0.0.0 0.0.0.0 192.168.0.2 floating
- D. ip route 0.0.0.0 0.0.0.0 192.168.0.2
ANSWER: D

## ipconn-33  (Question 9.33)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/543f07905951a119.jpeg]
Routers R1 and R3 have the default configuration. The router R2 priority is set to 99. Which commands on R3 configure it as the DR in the 10.0.4.0/24 network?
- A. R3(config)#interface Gig0/1
R3(config-if)#ip ospf priority 100
- B. R3(config)#interface Gig0/0
R3(config-if)#ip ospf priority 100
- C. R3(config)#interface Gig0/0
R3(config-if)#ip ospf priority 1
- D. R3(config)#interface Gig0/1
R3(config-if)#ip ospf priority 0
ANSWER: A

## ipconn-34  (Question 9.35)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6140c492a00c45c5.jpeg]
Router1#show ip route
Gateway of last resort is 10.10.11.2 to network 0.0.0.0
209.165.200.0/27 is subnetted, 1 subnets
B     209.165.200.224 [20/0] via 10.10.12.2,03:32:14
209.165.201.0/27 is subnetted, 1 subnets
B     209.165.201.0 [20/0] via 10.10.12.2,02:26:53
209.165.202.0/27 is subnetted, 1 subnets
B     209.165.202.128 [20/0] via 10.10.12.2,02:46:03
10.0.0.0/8 is variably subnetted, 10 subnets, 4 masks
O     10.10.13.0/25 [110/2] via 10.10.10.1,00:00:04, GigabitEthernet0/0
O     10.10.13.128/28 [110/2] via 10.10.10.5,00:00:12, GigabitEthernet0/1
O     10.10.13.144/28 [110/2] via 10.10.10.9,00:01:57, GigabitEthernet0/2
O     10.10.13.160/29 [110/2] via 10.10.10.5,00:00:12, GigabitEthernet0/1
O     10.10.13.208/29 [110/2] via 10.10.10.13,00:01:57, GigabitEthernet0/3
S*  0.0.0.0/0 [1/0] via 10.10.11.2
Which next-hop IP address does Router1 use for packets destined to host 10.10.13.158?
- A. 10.10.10.5
- B. 10.10.11.2
- C. 10.10.12.2
- D. 10.10.10.9
ANSWER: D

## ipconn-35  (Question 9.37)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d6b9bed1a2c41b6c.jpeg]
Web traffic is coming in from the WAN interface. Which route takes precedence when the router is processing traffic destined for the LAN network at 10.0.10.0/24?
- A. via next-hop 10.0.1.5
- B. via next-hop 10.0.1.4
- C. via next-hop 10.0.1.50
- D. via next-hop 10.0.1.100
ANSWER: A

## ipconn-36  (Question 9.51)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7b1a7d293374432e.jpeg]
R1 learns all routes via OSPF. Which command configures a backup static route on R1 to reach the 192.168.20.0/24 network via R3?
- A. R1(config)#ip route 192.168.20.0 255.255.255.0 192.168.30.2 111
- B. R1(config)#ip route 192.168.20.0 255.255.255.0 192.168.30.2 90
- C. R1(config)#ip route 192.168.20.0 255.255.0.0 192.168.30.2
- D. R1(config)#ip route 192.168.20.0 255.255.255.0 192.168.30.2
ANSWER: A

## ipconn-37  (Question 9.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/acbb6f5fc3d3e6f6.jpeg]
The primary route across Gi0/0 is configured on both routers. A secondary route must be configured to establish connectivity between the workstation networks. Which command set must be configured to complete this task?
- A. R1
ip route 172.16.2.0 255.255.255.240 172.16.0.2 113
R2
ip route 172.16.1.0 255.255.255.0 172.16.0.1 114
- B. R1
ip route 172.16.2.0 255.255.255.240 172.16.0.5 89
R2
ip route 172.16.1.0 255.255.255.0 172.16.0.6 89
- C. R1
ip route 172.16.2.0 255.255.255.248 172.16.0.5 110
R2
ip route 172.16.1.0 255.255.255.0 172.16.0.6 110
- D. R1
ip route 172.16.2.0 255.255.255.224 172.16.0.6 111
R2
ip route 172.16.1.0 255.255.255.0 172.16.0.5 112
ANSWER: D

## ipconn-38  (Question 9.79)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3d50de34f811fa76.jpeg]
R1 has taken the DROTHER role in the OSPF DR/BDR election process. Which configuration must an engineer implement so that R1 is elected as the DR?
- A. R1(config)#interface FastEthernet0/0
R1(config-if)#ip ospf priority 1
R1#clear ip ospf process
- B. R1(config)#interface FastEthernet0/0
R1(config-if)#ip ospf priority 200
R1#clear ip ospf process
- C. R3(config)#interface FastEthernet0/1
R3(config-if)#ip ospf priority 200
R3#clear ip ospf process
- D. R2(config)#interface FastEthernet0/2
R2(config-if)#ip ospf priority 1
R2#clear ip ospf process
ANSWER: B

## ipconn-39  (Question 9.87)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3b604fb4f9701cb7.jpeg]
An OSPF neighbor relationship must be configured using these guidelines:
– R1 is only permitted to establish a neighbor with R2.
– R1 will never participate in DR elections.
– R1 will use a router-id of 10.1.1.1.
Which configuration must be used?
[IMAGE: D:\CCNA_ontap\web\img/61ea63e0e4efdfa3.jpeg]
[IMAGE: D:\CCNA_ontap\web\img/50903110b0db7d5b.jpeg]
[IMAGE: D:\CCNA_ontap\web\img/940c8fb9eadb5660.jpeg]
[IMAGE: D:\CCNA_ontap\web\img/7c3c330649421938.jpeg]
[TABLE]
Option A | Option B
---
Option C | Option D
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B

## ipconn-40  (Question 9.89)
A user configured OSPF and advertised the Gigabit Ethernet interface in OSPF. By default, to which type of OSPF network does this interface belong?
- A. point-to-multipoint
- B. point-to-point
- C. nonbroadcast
- D. broadcast
ANSWER: D

## ipconn-41  (Question 9.92)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/2d3649cdca22c974.jpeg]
Router R1 must be configured to reach the 10.0.3.0 network from the 10.0.1.0/24 segment. Which command must be used to configure the route?
- A. route add 10.0.3.0 0.255.255.255 10.0.4.2
- B. route add 10.0.3.0 mask 255.255.255.0 10.0.4.3
- C. ip route 10.0.3.0 0.255.255.255 10.0.4.2
- D. ip route 10.0.3.0 255.255.255.0 10.0.4.3
ANSWER: D

## ipconn-42  (Question 9.98)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/37aeead49420f53a.jpeg]
Routers R1 and R2 have been configured with their respective LAN interfaces. The two circuits are operational and reachable across WAN. Which command set establishes failover redundancy if the primary circuit goes down?
- A. R1(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.6 2
R2(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.5 2
- B. R1(config)#ip route 10.10.13.10 255.255.255.255 10.10.10.6
R2(config)#ip route 192.166.0.100 255.255.255.255 10.10.10.5
- C. R1(config)#ip route 10.10.13.10 255.255.255.255 10.10.10.2
R2(config)#ip route 192.168.0.100 255.255.255.255 10.10.10.1
- D. R1(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.6
R2(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.5
ANSWER: A

## ipconn-43  (Question 9.104)
Refer to the exhibit.
R1#show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
ia - IS-IS inter area, * - candidate default, U - per-user static route
o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
+ - replicated route, % - next hop override
Gateway of last resort is 10.56.0.1 to network 0.0.0.0
S*	0.0.0.0/0 [1/0] via 10.56.0.1
10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C	  10.56.0.0/17 is directly connected, Vlan56
L	  10.56.0.19/32 is directly connected, Vlan56
C	  10.56.128.0/18 is directly connected, Vlan57
L	  10.56.128.19/32 is directly connected, Vlan57
When router R1 is sending traffic to IP address 10.56.192.1, which interface or next hop address does it use to route the packet?
- A. 0.0.0.0/0
- B. Vlan57
- C. 10.56.0.1
- D. 10.56.128.19
ANSWER: C

## ipconn-44  (Question 9.107)
What is the effect when loopback interfaces and the configured router ID are absent during the OSPF Process configuration?
- A. The router ID 0.0.0.0 is selected and placed in the OSPF process.
- B. No router ID is set, and the OSPF protocol does not run.
- C. The highest up/up physical interface IP address is selected as the router ID.
- D. The lowest IP address is incremented by 1 and selected as the router ID.
ANSWER: C

## ipconn-45  (Question 10.1)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ffa7327a95c78f6c.jpeg]
An engineer is asked to configure router R1 so that it forms an OSPF single-area neighbor relationship with R2. Which command sequence must be implemented to configure the router?
- A. router ospf 10
network 10.0.0.0 0.0.0.3 area 0
network 10.0.2.0 0.0.0.255 area 0
- B. router ospf 10
network 10.0.0.0 0.0.0.3 area 0
network 10.0.1.0 0.0.0.255 area 0
- C. router ospf 10
network 10.0.0.0 0.0.0.3 area 0
network 10.0.2.0 255.255.255.0 area 0
- D. router ospf 10
network 10.0.0.0 0.0.0.252 area 0
network 10.0.1.0 0.0.0.255 area 0
ANSWER: B

## ipconn-46  (Question 10.4)
What is the MAC address used with VRRP as a virtual address?
- A. 00-00-0C-07-AD-89
- B. 00-00-5E-00-01-0a
- C. 00-07-C0-70-AB-01
- D. 00-C6-41-93-90-91
ANSWER: B

## ipconn-47  (Question 10.6)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b95adc732713c71b.jpeg]
All routers in the network are configured. R2 must be the DR. After the engineer connected the devices, R1 was elected as the DR. Which command sequence must be configure on R2 to be elected as the DR in the network?
- A. R2(config)#interface gi0/0
R2(config-if)#ip ospf priority 1
- B. R2(config)#interface gi0/0
R2(config-if)#ip ospf priority 100
- C. R2(config)#router ospf 1
R2(config-router)#router-id 10.100.100.100
- D. R2(config)#router ospf 1
R2(config-router)#router-id 192.168.2.7
ANSWER: B

## ipconn-48  (Question 10.11)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5f46be83bbff6b86.jpeg]
What is the next hop for traffic entering R1 with a destination of 10.1.2.126?
- A. 10.165.20.126
- B. 10.165.20.146
- C. 10.165.20.166
- D. 10.165.20.226
ANSWER: C

## ipconn-49  (Question 10.12)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b466f3dd44847a30.jpeg]
A network engineer must configure R1 so that it sends all packets destined to the 10.0.0.0/24 network to R3, and all packets destined to PC1 to R2. Which configuration must the engineer implement?
- A. R1(config)#ip route 10.0.0.0 255.255.0.0 172.16.0.2
R1(config)#ip route 10.0.0.5 255.255.255.255 192.168.0.2
- B. R1(config)#ip route 10.0.0.0 255.255.255.0 172.16.0.2
R1(config)#ip route 10.0.0.5 255.255.255.255 192.168.0.2
- C. R1(config)#ip route 10.0.0.0 255.255.0.0 192.168.0.2
R1(config)#ip route 10.0.0.0 255.255.255.0 172.16.0.2
- D. R1(config)#ip route 10.0.0.0 255.255.255.0 192.168.0.2
R1(config)#ip route 10.0.0.5 255.255.255.255 172.16.0.2
ANSWER: D

## ipconn-50  (Question 10.16)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/1fec4afa85a5e1dc.jpeg]
An engineer must configure router R2 so it is elected as the DR on the WAN subnet. Which command sequence must be configured?
- A. interface gigabitethernet0/0
ip address 10.0.1.1 255.255.255.224
ip ospf priority 98
- B. interface gigabitethernet0/0
ip address 10.0.1.1 255.255.255.0
ip ospf priority 255
- C. interface gigabitethernet0/0
ip address 10.0.0.34 255.255.255.248
ip ospf priority 0
- D. interface gigabitethernet0/0
ip address 10.0.0.34 255.255.255.224
ip ospf priority 100
ANSWER: D

## ipconn-51  (Question 10.17)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/da93b314fd075c17.jpeg]
R1 has just received a packet from host A that is destined to host B. Which route in the routing table is used by R1 to reach host B?
- A. 10.10.13.0/25[1/0] via 10.10.10.2
- B. 10.10.13.0/25[110/2] via 10.10.10.6
- C. 10.10.13.0/25[110/2] via 10.10.10.2
- D. 10.10.13.0/25[108/0] via 10.10.10.10
ANSWER: D

## ipconn-52  (Question 10.29)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/64b434b218f0b5d2.jpeg]
Router R1 is added to the network and configured with the 10.0.0.64/26 and 10.0.20.0/24 subnets. However, traffic destined for the LAN on R3 is not accessible. Which command when executed on R1 defines a static route to reach the R3 LAN?
- A. ip route 10.0.15.0 255.255.255.0 10.0.20.1
- B. ip route 10.0.15.0 255.255.255.192 10.0.20.1
- C. ip route 10.0.0.64 255.255.255.192 10.0.20.3
- D. ip route 10.0.15.0 255.255.255.0 10.0.20.3
ANSWER: D

## ipconn-53  (Question 10.39)
Refer to the exhibit.
Router1#show ip route
Gateway of last resort is 10.10.11.2 to network 0.0.0 0
209.165.200.0/27 is subnetted, 1 subnets
B     209.165.200.224 [20/0] via 10 10.12.2,03:22:14
209.165.201.0/27 is subnetted, 1 subnets
B     209.165.201.0 [20/0] via 10.10.12.2, 02:26:33
209.165.202.0/27 is subnetted, 1 subnets
B     209.165.202.128 [20/0] via 10.10.12.2,02:26:03
10.0.0.0/8 is variably subnetted, 8 subnets, 4 masks
C     10.10.10.0/28 is directly connected, GigabitEthernet0/0
C     10.10.11.0/30 is directly connected, FastEthernet2/0
C     10.10.12.0/30 is directly connected, GigabitEthernet0/1
O     10.10.13.0/25 [110/2] via 10.10.10.1, 00:00:04, GigabitEthernet0/0
O     10.10.13.128/28 [110/2] via 10.10.10.1, 00:00:04, GigabitEthernet0/0
O     10.10.13.144/28 [110/2] via 10.10.10.1, 00:00:04, GigabitEthernet0/0
O     10.10.13.160/29 [110/2] via 10.10.10.1, 00:00:04, GigabitEthernet0/0
O     10.10.13.208/29 [110/2] via 10.10.10.1, 00:00:04, GigabitEthernet0/0
S* 0.0.0 0/0 [1/0] via 10.10.11.2
What is the subnet mask of the route to the 10.10.13.160 prefix?
- A. 255.255.255.240
- B. 255.255.255.128
- C. 255.255.248.0
- D. 255.255.255.248
ANSWER: D

## ipconn-54  (Question 10.44)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d0656be0fd5586ae.jpeg]
A network engineer must configure router R1 with a host route to the server. Which command must the engineer configure?
- A. R1(config)#ip route 10.10.10.10 255.255.255.255 192.168.0.2
- B. R1(config)#ip route 10.10.10.0 255.255.255.0 192.168.0.2
- C. R1(config)#ip route 0.0.0.0 0.0.0.0 192.168.0.2
- D. R1(config)#ip route 192.168.0.2 255.255.255.255 10.10.10.10
ANSWER: A

## ipconn-55  (Question 10.63)
Refer to the exhibit.
Current Neighbor Relationship
Neighbor ID   Pri   State	Dead Time    Address	  Interface
192.168.1.1   1    FULL/DR	00:00:33     192.168.1.1  GigabitEthernet0/0
Desired Neighbor Relationship
Neighbor ID   Pri   State	Dead Time    Address	  Interface
192.168.1.1   0    FULL/ -	00:00:31     192.168.1.1  GigabitEthernet0/0
How must OSPF be configured on the GigabitEthernet0/0 interface of the neighbor device to achieve the desired neighbor relationship?
- A. Router(config)#interface GigabitEthernet 0/0
Router(config-if)#ip ospf cost 5
- B. Router(config)#interface GigabitEthernet 0/0
Router(config-if)#ip ospf 1 area 2
- C. Router(config)#interface GigabitEthernet 0/0
Router(config-if)#ip ospf network point-to-point
- D. Router(config)#interface GigabitEthernet 0/0
Router(config-if)#ip ospf priority 1
ANSWER: C

## ipconn-56  (Question 10.74)
Refer to the exhibit.
Gateway of last resort is not set
10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C      10.1.1.0/30 is directly connected, GigabitEthernet0/0
L      10.1.1.2/32 is directly connected, GigabitEthernet0/0
S   192.168.0.0/20 [1/0] via 10.1.1.1
192.168.1.0/30 is subnetted, 1 subnets
S      192.168.1.0/30 [1/0] via 10.1.1.1
192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
S      192.168.2.0/28 [1/0] via 10.1.1.1
S      192.168.2.0/29 [1/0] via 10.1.1.1
An engineer is checking the routing table in the main router to identify the path to a server on the network. Which route does the router use to reach the server at 192.168.2.2?
- A. S 192.168.2.0/28 [1/0] via 10.1.1.1
- B. S 192.168.1.0/30 [1/0] via 10.1.1.1
- C. S 192.168.0.0/20 [1/0] via 10.1.1.1
- D. S 192.168.2.0/29 [1/0] via 10.1.1.1
ANSWER: D

## ipconn-57  (Question 10.76)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c5d5d23ec7c5b4a1.jpeg]
After applying this configuration to router R1, a network engineer is verifying the implementation. If all links are operating normally, and the engineer sends a series of packets from PC1 to PC3, how are the packets routed?
- A. They are routed to 172.16.20.2.
- B. They are distributed sent round robin to interfaces S0/0/0 and S0/0/1.
- C. They are routed to 192.168.100.2.
- D. They are routed to 10.0.0.2.
ANSWER: A

## ipconn-58  (Question 10.85)
Refer to the exhibit.
Gateway of last resort is 172.16.2.2 to network 0.0.0.0
10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C     10.10.8.0/28 is directly connected, GigabitEthernet0/0/2
C     10.10.10.0/24 is directly connected, GigabitEthernet0/0/0
L     10.10.10.3/32 is directly connected, GigabitEthernet0/0/0
172.16.0.0/16 is variably subnetted, 3 subnets, 2 masks
S     172.16.1.33/32 is directly connected, GigabitEthernet0/0/1
C     172.16.2.0/23 is directly connected, GigabitEthernet0/0/1
L     172.16.2.1/32 is directly connected, GigabitEthernet0/0/1
S* 0.0.0.0/0 [1/0] via 172.16.2.2
A packet sourced from 10.10.10.1 is destined for 10.10.8.14. What is the subnet mask of the destination route?
- A. 255.255.254.0
- B. 255.255.255.240
- C. 255.255.255.248
- D. 255.255.255.252
ANSWER: B

## ipconn-59  (Question 10.91)
Refer to the exhibit. With which metric does router R1 learn the route to host 172.16.0.202?
R1#show ip route | begin gateway
Gateway of last resort is 209.165.200.246 to network 0.0.0.0
S* 0.0.0.0/0 [1/0] via 209.165.200.246, Serial0/1/0
is directly connected, Serial0/1/0
172.16.0.0/16 is variably subnetted, 3 subnets, 3 masks
S   172.16.0.0/24 [1/0] via 207.165.200.250, Serial0/0/0
O   172.16.0.128/25 [110/32445] via 207.165.200.254, 00:00:33, Serial0/0/1
D   172.16.0.192/29 [90/3184439] via 207.165.200.254, 00:00:33, Serial0/0/1
207.165.200.0/24 is variably subnetted, 4 subnets, 2 masks
C   207.165.200.248/30 is directly connected, Serial0/0/0
L   207.165.200.249/32 is directly connected, Serial0/0/0
C   207.165.200.252/30 is directly connected, Serial0/0/1
L   207.165.200.253/32 is directly connected, Serial0/0/1
- A. 0
- B. 110
- C. 32445
- D. 3184439
ANSWER: C

## ipconn-60  (Question 10.93)
Refer to the exhibit.
Gateway of last resort is 0.0.0.0 to network 0.0.0.0
10.0.0.0/8 is variably subnetted, 6 subnets, 5 masks
S       10.0.0.0/8 is directly connected, GigabitEthernet0/0
C       10.1.1.0/24 is directly connected, GigabitEthernet0/0
L       10.1.1.1/32 is directly connected, GigabitEthernet0/0
S       10.10.0.0/22 is directly connected, GigabitEthernet0/0
S       10.10.10.0/28 is directly connected, GigabitEthernet0/0
S       10.10.10.1/32 is directly connected, GigabitEthernet0/0
S*  0.0.0.0/0 is directly connected, GigabitEthernet0/0
Which IP route command created the best path for a packet destined for 10.10.10.3?
- A. ip route 10.0.0.0 255.0.0.0 g0/0
- B. ip route 10.10.10.1 255.255.255.255 g0/0
- C. ip route 10.10.10.0 255.255.255.240 g0/0
- D. ip route 10.10.0.0 255.255.252.0 g0/0
ANSWER: C

## ipconn-61  (Question 11.16)
Refer to the exhibit.
Entry #
1     192.168.10.0 255.255.254.0
2     192.168.10.0 255.255.255.192
3     192.168.10.0 255.255.0.0
4     192.168.10.0 255.255.224.0
Which entry is the longest prefix match for host IP address 192.168.10.5?
- A. 1
- B. 2
- C. 3
- D. 4
ANSWER: B

## ipconn-62  (Question 11.18)
Refer to the exhibit.
router# show ip route
...
D  172.18.32.0/26 [90/25789217] via 10.1.1.1
R  172.18.32.0/24 [120/4] via 10.1.1.2
O  172.18.32.0/19 [110/229840] via 10.1.1.3
C  172.18.32.32/32 is directly connected, Loopback0
C  172.18.32.36/30 directly connected, GigabitEthernet0/0
L  172.18.32.37/32 is directly connected, GigabitEthernet0/0
A packet sourced from 172.18.33.2 is destined for 172.18.32.38. Where does the router forward the packet?
- A. GigabitEthernet0/0
- B. Loopback0
- C. 10.1.1.1
- D. 10.1.1.3
ANSWER: A

## ipconn-63  (Question 11.48)
Refer to the exhibit.
EIGRP: 192.168.12.0/24
RIP: 192.168.12.0/27
OSPF: 192.168.12.0/28
How does the router manage traffic to 192.168.12.16?
- A. It selects the RIP route because it has the longest prefix inclusive of the destination address.
- B. It load-balances traffic between all three routes.
- C. It chooses the OSPF route because it has the longest prefix inclusive of the destination address.
- D. It chooses the EIGRP route because it has the lowest administrative distance.
ANSWER: A

## ipconn-64  (Question 11.57)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/021085528d6b44e9.png]
A network administrator configures the CPE to provide internet access to the company headquarters. Traffic must be load-balanced via ISP1 and ISP2 to ensure redundancy. Which two command sets must be configured on the CPE router? (Choose two)
- A. ip route 0.0.0.0 0.0.0.0 198.51.100.1
ip route 0.0.0.0 0.0.0.0 203.0.113.1 2
- B. ip route 0.0.0.0 128.0.0.0 198.51.100.1
ip route 128.0.0.0 128.0.0.0 203.0.113.1
ip route 0.0.0.0 0.0.0.0 198.51.100.1
ip route 0.0.0.0 0.0.0.0 203.0.113.1
- C. ip route 0.0.0.0 128.0.0.0 198.51.100.1
ip route 128.0.0.0 128.0.0.0 203.0.113.1
- D. ip route 0.0.0.0 0.0.0.0 198.51.100.1 255
ip route 0.0.0.0 0.0.0.0 203.0.113.1 255
ip route 128.0.0.0 128.0.0.0 203.0.113.1
- E. ip route 0.0.0.0 0.0.0.0 198.51.100.1
ip route 0.0.0.0 0.0.0.0 203.0.113.1
ANSWER: B, E

## ipconn-65  (Question 11.70)
A packet from a company’s branch office is destined to host 172.31.0.1 at headquarters. The sending router has three possible matches in its routing table for the packet: prefixes 172.31.0.0/16, 172.31.0.0/24, and 172.31.0.0/25. How does the router handle the packet?
- A. It sends the traffic via the default gateway 0.0.0.0/0.
- B. It sends the traffic via prefix 172.31.0.0/16.
- C. It sends the traffic via prefix 172.31.0.0/25.
- D. It sends the traffic via prefix 172.31.0.0/24.
ANSWER: C

## ipconn-66  (Question 11.77)
Refer to the exhibit.
Gateway of last resort is 172.16.2.2 to network 0.0.0.0
10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C     10.10.10.0/24 is directly connected, GigabitEthernet0/0/0
L     10.10.10.3/32 is directly connected, GigabitEthernet0/0/0
172.16.0.0/16 is variably subnetted, 3 subnets, 2 masks
S     172.16.1.33/32 is directly connected, GigabitEthernet0/0/1
C     172.16.2.0/23 is directly connected, GigabitEthernet0/0/1
L     172.16.2.1/32 is directly connected, GigabitEthernet0/0/1
S* 0.0.0.0/0 [1/0] via 172.16.2.2
A packet sourced from 10.10.10.1 is destined for 172.16.3.254. What is the subnet mask of the destination route?
- A. 0.0.0.0
- B. 255.255.254.0
- C. 255.255.255.0
- D. 255.255.255.255
ANSWER: B

## ipconn-67  (Question 11.9)
What is the purpose of configuring different levels of syslog for different devices on the network?
- A. to rate-limit messages for different severity levels from each device
- B. to set the severity of syslog messages from each device
- C. to identify the source from which each syslog message originated
- D. to control the number of syslog messages from different devices that are stored locally
ANSWER: B

## ipconn-68  (Question 11.17)
Which two features introduced in SNMPv2 provide the ability to retrieve large amounts of data in one request? (Choose two)
- A. Get
- B. GetNext
- C. Set
- D. GetBulk
- E. Inform
ANSWER: D, E

## ipconn-69  (Question 11.23)
Which type of address is shared by routers in a HSRP implementation and used by hosts on the subnet as their default gateway address?
- A. multicast address
- B. loopback IP address
- C. virtual IP address
- D. broadcast address
ANSWER: C

## ipconn-70  (Question 11.42)
Refer to the exhibit. What is the next step to complete the implementation for the partial NAT configuration shown?
- A. Reconfigure the static NAT entries that overlap the NAT pool
- B. Configure the NAT outside interface
- C. Modify the access list for the internal network on e0/1
- D. Apply the ACL to the pool configuration
ANSWER: B

## ipconn-71  (Question 11.56)
When deploying a new network that includes both Cisco and third-party network devices, which redundancy protocol avoids the interruption of network traffic if the default gateway router fails?
- A. FHRP
- B. VRRP
- C. HSRP
- D. GLBP
ANSWER: B

## ipconn-72  (Question 12.12)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7bce5d5785b6f9e9.png]
Router R14 is in the process of being configured. Which configuration must be used to establish a host route to PC 10?
- A. ip route 10.80.65.10 255.255.255.254 10.80.65.1
- B. ip route 10.73.65.66 0.0.0.255 10.80.65.10
- C. ip route 10.80.65.10 255.255.255.255 10.73.65.66
- D. ip route 10.73.65.65 255.0.0.0 10.80.65.10
ANSWER: C

## ipconn-73  (Question 12.13)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/379b790dbccc8b90.jpeg]
A static route must be configured on R86 to forward traffic for the 172.16.34.0/29 network, which resides on R14. Which command must be used to fulfill the request?
- A. ip route 172.16.34.0 255.255.255.248 10.73.65.65
- B. ip route 172.16.34.0 255.255.255.224 10.73.65.66
- C. ip route 10.73.65.65 255.255.255.248 172.16.34.0
- D. ip route 172.16.34.0 0.0.0.7 10.73.65.64
ANSWER: A

## ipconn-74  (Question 12.16)
Refer to the exhibit.
Which two values does router R1 use to identify valid routes for the R3 loopback address 1.1.1.3/32? (Choose two)
- A. lowest cost to reach the next hop
- B. lowest administrative distance
- C. lowest metric
- D. highest metric
- E. highest administrative distance
ANSWER: B, C

## ipconn-75  (Question 12.18)
Refer to the exhibit.
User traffic originating within site B is failing to reach an application hosted on IP address 192.168.0.10, which is located within site A. What is determined by the routing table?
- A. The traffic to 192.168.0.10 requires a static route to be configured in router1
- B. The lack of a default route prevents delivery of the traffic
- C. The default gateway for site B is configured incorrectly.
- D. The traffic is blocked by an implicit deny in an ACL on router2.
ANSWER: B

## ipconn-76  (Question 12.26)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/40277c81c11ade13.png]
The router R1 is in the process of being configured. Routers R2 and R3 are configured correctly for the new environment. Which two commands must be configured on R1 for PC1 to communicate to all PCs on the 10.10.10.0/24 network? (Choose two)
- A. ip route 10.10.10.8 255.255.255.248 g0/1
- B. ip route 10.10.10.10 255.255.255.255 g0/1
- C. ip route 10.10.10.0 255.255.255.248 192.168.2.2
- D. ip route 10.10.10.0 255.255.255.0 192.168.2.3
- E. ip route 10.10.10.10 255.255.255.255 192.168.2.2
ANSWER: D, E

## ipconn-77  (Question 12.30)
Refer to the exhibit.
What is the next-hop IP address for R2 so that PC2 reaches the application server via EIGRP?
- A. 10.10.10.5
- B. 192.168.20.1
- C. 10.10.10.6
- D. 192.168.30.1
ANSWER: C

## ipconn-78  (Question 12.43)
A network engineer must migrate a router loopback interface to the IPv6 address space. If the current IPv4 address of the interface is 10.54.73.1/32, and the engineer configures IPv6 address 0:0:0:0:0:ffff:a36:4901, which prefix length must be used?
- A. /64
- B. /96
- C. /124
- D. /128
ANSWER: D

## ipconn-79  (Question 12.47)
Refer to the exhibit.
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
ia - IS-IS inter area, * - candidate default, U - per-user static route
o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
+ - replicated route, % - next hop override, p - overrides from PfR
Gateway of last resort is 0.0.0.0 to network 0.0.0.0
S*	0.0.0.0/0 is directly connected, Null0
10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
C	10.0.12.0/24 is directly connected, GigabitEthernet0/1
L	10.0.12.1/32 is directly connected, GigabitEthernet0/1
C	10.0.13.0/24 is directly connected, GigabitEthernet0/2
L	10.0.13.1/32 is directly connected, GigabitEthernet0/2
C	10.0.14.0/24 is directly connected, GigabitEthernet0/3
L	10.0.14.1/32 is directly connected, GigabitEthernet0/3
D	192.168.0.0/16 [90/130816] via 10.0.13.3, 00:10:09, GigabitEthernet0/2
O	192.168.0.0/23 [110/2] via 10.0.14.4, 00:00:46, GigabitEthernet0/3
S	192.168.0.0/24 [100/0] via 10.0.12.2
Which interface is chosen to forward traffic to the host at 192.168.0.55?
- A. GigabitEthernet0/1
- B. Null0
- C. GigabitEthernet0/3
- D. GigabitEthernet0/2
ANSWER: A

## ipconn-80  (Question 12.49)
A Cisco engineer notices that two OSPF neighbors are connected using a crossover Ethernet cable. The neighbors are taking too long to become fully adjacent. Which command must be issued under the interface configuration on each router to reduce the time required for the adjacency to reach the FULL state?
- A. ip ospf priority 0
- B. ip ospf network broadcast
- C. ip ospf dead-interval 40
- D. ip ospf network point-to-point
ANSWER: D

## ipconn-81  (Question 12.53)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ec49b4982ded46d7.png]
Each router must be configured with the last usable IP address in the subnet. Which configuration fulfills this requirement?
- A. Option A R7# interface FastEthernet1/0 ip address 10.88.31.126 255.255.255.192 R8# interface FastEthernet0/0 ip address 10.19.63.95 255.255.255.192 R9# interface FastEthernet1/1 ip address 10.23.98.159 255.255.255.248
- B. Option B R7# interface FastEthernet1/0 ip address 10.88.31.126 255.255.255.240 R8# interface FastEthernet0/0 ip address 10.19.63.94 255.255.255.192 R9# interface FastEthernet1/1 ip address 10.23.98.158 255.255.255.248
- C. Option C R7# interface FastEthernet1/0 ip address 10.88.31.127 255.255.255.192 R8# interface FastEthernet0/0 ip address 10.19.63.95 255.255.255.240 R9# interface FastEthernet1/1 ip address 10.23.98.159 255.255.255.224
- D. Option D R7# interface FastEthernet1/0 ip address 10.88.31.127 255.255.255.240 R8# interface FastEthernet0/0 ip address 10.19.63.95 255.255.255.192 R9# interface FastEthernet1/1 ip address 10.23.98.159 255.255.255.248
ANSWER: B

## ipconn-82  (Question 12.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d2cec875c8e2abbf.png]
A network engineer is updating the configuration on router R1 to connect a new branch office to the company network. R2 has been configured correctly. Which command must the engineer configure so that devices at the new site communicate with the main office?
- A. ip route 172.25.25.1 255.255.255.255 g0/2
- B. ip route 172.25.25.0 255.255.255.0 192.168.2.1
- C. ip route 172.25.25.1 255.255.255.255 g0/1
- D. ip route 172.25.25.0 255.255.255.0 192.168.2.2
ANSWER: D

## ipconn-83  (Question 12.56)
Refer to the exhibit.
Gateway of last resort is 172.16.2.2 to network 0.0.0.0
10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
10.10.100.0/26 is directly connected, GigabitEthernet0/0/6
C      10.10.10.0/24 is directly connected, GigabitEthernet0/0/0
L      10.10.10.3/32 is directly connected, GigabitEthernet0/0/0
172.16.0.0/16 is variably subnetted, 3 subnets, 2 masks
S      172.16.1.33/32 is directly connected, GigabitEthernet0/0/1
C      172.16.2.0/23 is directly connected, GigabitEthernet0/0/1
L      172.16.2.1/32 is directly connected, GigabitEthernet0/0/1
S*  0.0.0.0/0 [1/0] via 172.16.2.2
A packet sourced from 10.10.10.32 is destined for the Internet. What is the administrative distance for the destination route?
- A. 0
- B. 1
- C. 2
- D. 32
ANSWER: B

## ipconn-84  (Question 12.60)
Refer to the exhibit.
Refer to the exhibit.
R1# show ip route
Codes: C — connected, S — static, I — IGRP, R - RIP, M - mobile, B — BGP
D — EIGRP, EX - EIGRP external, O — OSPF, IA — OSPF inter area
N1 — OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 — OSPF external type 2, E — EGP
i — IS-IS, L1 - IS-IS level-1, L2 — IS-IS level-2, * — candidate default
U - per-user static route, o — ODR
Gateway of last resort is not set
C   172.16.0.0/16 is directly connected, Loopback0
172.16.0/16 is variably subnetted, 4 subnets, 2 masks
O	  172.16.1.3/3 [110/100] via 192.168.7.40, 00:39:08, Serial0
C	  172.16.1.0/24 is directly connected, Serial0
O	  172.16.1.184/29 [110/5] via 192.168.7.35, 00:39:08, Serial0
O	  172.16.3.0/24 [110/10] via 192.168.7.4, 00:39:08, GigabitEthernet 0/0
D	  172.16.1.0/28 [90/10] via 192.168.7.7, 00:39:08, GigabitEthernet 0/0
Load-balanced traffic is coming in from the WAN destined to a host at 172.16.1.190. Which next-hop is used by the router to forward the request?
- A. 192.168.7.4
- B. 192.168.7.7
- C. 192.168.7.35
- D. 192.168.7.40
ANSWER: C

## ipconn-85  (Question 12.61)
Refer to the exhibit.
R1#show ip ospf interface g0/0/0
GigabitEthernet0/0/0 is up, line protocol is up
Internet address is 192.168.1.2/24, Area 0
Process ID 1, Router ID 192.168.1.2, Network Type POINT-TO-POINT, Cost: 1
Transmit Delay is 1 sec, State POINT-TO-POINT,
Timer intervals configured, Hello 15, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:08
Index 1/1, flood queue length 0
Next 0x0(0) /0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Suppress hello for 0 neighbor(s)
R2#show ip ospf interface g0/0/0
GigabitEthernet0/0/0 is up, line protocol is up
Internet address is 192.168.1.1/24, Area 0
Process ID 1, Router ID 10.1.1.1, Network Type POINT-TO-POINT, Cost: 1
Transmit Delay is 1 sec, State POINT-TO-POINT,
Timer intervals configured, Hello 15, Dead 45, Wait 15, Retransmit 5
Hello due in 00:00:11
Index 1/1, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Suppress hello for 0 neighbor(s)
The network engineer is configuring router R2 as a replacement router on the network. After the initial configuration is applied it is determined that R2 failed to show R1 as a neighbor. Which configuration must be applied to R2 to complete the OSPF configuration and enable it to establish the neighbor relationship with R1?
- A. Option A R2(config)#interface g0/0/0 R2(config-if)#ip ospf hello-interval 10
- B. Option B R2(config)#router ospf 1 R2(config-router)#router-id 192.168.1.2
- C. Option C R2(config)#router ospf 1 R2(config-router)#network 192.168.1.0 255.255.255.0 area 2
- D. Option D R2(config)#interface g0/0/0 R2(config-if)#ip ospf dead-interval 40
ANSWER: D

## ipconn-86  (Question 12.70)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/469829a900b6b989.png]
Routers R1 and R2 are configured with RIP as the dynamic routing protocol. A network engineer must configure R1 with floating static route to serve as a backup route to network 192.168.23.0. Which command must the engineer configure on R1?
- A. ip route 192.168.23.0 255.255.255.255 192.168.13.3 121
- B. ip route 192.168.23.0 255.255.255.0 192.168.13.3 100
- C. ip route 192.168.23.0 255.255.255.0 192.168.13.3
- D. ip route 192.168.23.0 255.255.255.0 192.168.13.3 121
ANSWER: D

## ipconn-87  (Question 12.78)
A router received three destination prefixes: 10.0.0.0/8, 10.0.0.0/16, and 10.0.0.0/24. When the show ip route command is executed, which output does it return?
- A. Gateway of last resort is 172.16.1.1 to network 0.0.0.0 O E2 10.0.0.0/24[110/5] via 192.168.3.1, 0:01:00, Ethernet2
- B. Gateway of last resort is 172.16.1.1 to network 0.0.0.0 O E2 10.0.0.0/16[110/5] via 192.168.2.1, 0:01:00, Ethernet1 O E2 10.0.0.0/24[110/5] via 192.168.3.1, 0:01:00, Ethernet2
- C. Gateway of last resort is 172.16.1.1 to network 0.0.0.0 O E2 10.0.0.0/8 [110/5] via 192.168.1.1, 0:01:00, Ethernet0
- D. Gateway of last resort is 172.16.1.1 to network 0.0.0.0 O E2 10.0.0.0/8 [110/5] via 192.168.1.1, 0:01:00, Ethernet0 O E2 10.0.0.0/16[110/5] via 192.168.2.1, 0:01:00, Ethernet1 O E2 10.0.0.0/24[110/5] via 192.168.3.1, 0:01:00, Ethernet2
ANSWER: D

## ipconn-88  (Question 12.87)
Refer to the exhibit.
R1
interface GigabitEthernet0/1
ip address 192.168.12.1 255.255.255.128
no shutdown
router ospf 1
network 192.168.12.1 0.0.0.0 area 1
R2
interface GigabitEthernet0/1
ip address 192.168.12.2 255.255.255.128
no shutdown
A network engineer started to configure two directly-connected routers as shown. Which command sequence must the engineer configure on R2 so that the two routers become OSPF neighbors?
- A. interface GigabitEthernet0/1 ip ospf 1 area 0
- B. interface GigabitEthernet0/1 ip ospf 1 area 1
- C. router ospf 1 network 192.168.12.0 0.0.0.127 area 0
- D. router ospf 1 network 192.168.12.1 0.0.0.0 area 1
ANSWER: B

## ipconn-89  (Question 12.88)
Refer to the exhibit.
R1# show ip route
Codes: C - connected, S - static, I - IGRP, R - rip, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, * - candidate
default
U - per-user static route, o - ODR
Gateway of last resort is not set
C    10.0.0.0/8 is directly connected, Loopback0
10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O	10.0.1.3/32 [110/100] via 10.0.1.100, 00:39:08, Serial0
C	10.0.1.0/24 is directly connected, Serial0
O	10.0.1.5/32 [110/5] via 10.0.1.50, 00:39:08, Gigabit Ethernet 0/0
D	10.0.1.4/32 [110/10] via 10.0.1.4, 00:39:08, Gigabit Ethernet 0/0
What does route 10.0.1.3/32 represent in the routing table?
- A. all hosts in the 10.0.1.0 subnet
- B. the source 10.0.1.100
- C. a single destination address
- D. the 10.0.0.0 network
ANSWER: C

## ipconn-90  (Question 12.94)
A router has two static routes to the same destination network under the same OSPF process. How does the router forward packets to the destination if the next-hop devices are different?
- A. The router chooses the next hop with the lowest IP address.
- B. The router load-balances traffic over all routes to the destination.
- C. The router chooses the next hop with the lowest MAC address.
- D. The router chooses the route with the oldest age.
ANSWER: B

## ipconn-91  (Question 12.97)
A network engineer is upgrading a small data center to host several new applications, including server backups that are expected to account for up to 90% of the bandwidth during peak times. The data center connects to the MPLS network provider via a primary circuit and a secondary circuit. How does the engineer inexpensively update the data center to avoid saturation of the primary circuit by traffic associated with the backups?
- A. Place the backup servers in a dedicated VLAN.
- B. Configure a dedicated circuit for the backup traffic.
- C. Assign traffic from the backup servers to a dedicated switch.
- D. Advertise a more specific route for the backup traffic via the secondary circuit.
ANSWER: D

## ipconn-92  (Question 12.98)
Refer to the exhibit.
R1#show ip ospf interface g0/0/0
GigabitEthernet0/0/0 is up, line protocol is up
Internet address is 192.168.1.2/24, Area 0
Process ID 1, Router ID 192.168.1.2, Network Type POINT-TO-POINT, Cost: 1
Transmit Delay is 1 sec, State POINT-TO-POINT,
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:08
Index 1/1, flood queue length 0
Next 0x0(0) /0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Suppress hello for 0 neighbor(s)
R2#show ip ospf interface g0/0/0
GigabitEthernet0/0/0 is up, line protocol is up
Internet address is 192.168.1.1/24, Area 0
Process ID 1, Router ID 10.1.1.1, Network Type POINT-TO-POINT, Cost: 1
Transmit Delay is 1 sec, State POINT-TO-POINT,
Timer intervals configured, Hello 15, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:11
Index 1/1, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Suppress hello for 0 neighbor(s)
The network engineer is configuring router R2 as a replacement router on the network. After the initial configuration is applied it is determined that R2 failed to show R1 as a neighbor. Which configuration must be applied to R2 to complete the OSPF configuration and enable it to establish the neighbor relationship with R1?
- A. Option A R2(config)#interface g0/0/0 R2(config-if)#ip ospf hello-interval 10
- B. Option B R2(config)#router ospf 1 R2(config-router)#router-id 192.168.1.1
- C. Option C R2(config)#router ospf 1 R2(config-router)#network 192.168.1.0 255.255.255.0 area 2
- D. Option D R2(config)#interface g0/0/0 R2(config-if)#ip ospf dead-interval 45
ANSWER: A

## ipconn-93  (Question 13.30)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/53a98a8efd57be3e.jpeg]
All interfaces are configured with duplex auto and ip ospf network broadcast. Which configuration allows routers R14 and R86 to form an OSPFv2 adjacency and act as a central point for exchanging OSPF information between routers?
[TABLE]
Option A
R14#
interface FastEthernet0/0
ip address 10.73.65.65 255.255.255.252
ip ospf priority 0
ip mtu 1500
router ospf 10
router-id 10.10.1.14
network 10.10.1.14 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0
R86#
interface FastEthernet0/0
ip address 10.73.65.66 255.255.255.252
ip mtu 1500
router ospf 10
router-id 10.10.1.86
network 10.10.1.86 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0 | Option B
R14#
interface Loopback0
ip ospf 10 area 0
interface FastEthernet0/0
ip address 10.73.65.65 255.255.255.252
ip ospf priority 255
ip ospf 10 area 0
ip mtu 1500
router ospf 10
router-id 10.10.1.14
R86#
interface Loopback0
ip ospf 10 area 0
interface FastEthernet0/0
ip address 10.73.65.66 255.255.255.252
ip ospf 10 area 0
ip mtu 1500
router ospf 10
router-id 10.10.1.86
---
Option C
R14#
interface FastEthernet0/0
ip address 10.73.65.65 255.255.255.252
ip ospf priority 255
ip mtu 1500
router ospf 10
router-id 10.10.1.14
network 10.10.1.14 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0
R86#
interface FastEthernet0/0
ip address 10.73.65.66 255.255.255.252
ip mtu 1400
router ospf 10
router-id 10.10.1.86
network 10.10.1.86 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0 | Option D
R14#
interface Loopback0
ip ospf 10 area 0
interface FastEthernet0/0
ip address 10.73.65.65 255.255.255.252
ip ospf 10 area 0
ip mtu 1500
router ospf 10
router-id 10.10.1.14
network 10.10.1.14 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0
R86#
interface FastEthernet0/0
ip address 10.73.65.66 255.255.255.252
ip mtu 1400
router ospf 10
router-id 10.10.1.86
network 10.10.1.86 0.0.0.0 area 0
network 10.73.65.64 0.0.0.3 area 0
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B

## ipconn-94  (Question 13.32)
An engineer must configure a core router with a floating static default route to the backup router at 10.200.0.2. Which command meets the requirements?
- A. ip route 0.0.0.0 0.0.0.0 10.200.0.2 floating
- B. ip route 0.0.0.0 0.0.0.0 10.200.0.2
- C. ip route 0.0.0.0 0.0.0.0 10.200.0.2 10
- D. ip route 0.0.0.0 0.0.0.0 10.200.0.2 1
ANSWER: C

## ipconn-95  (Question 13.33)
Which interface is used to send traffic to the destination network?
D 10.87.161.30/27 [90/10331] via G0/17
D 10.87.161.30/27 [90/44594] via G0/8
O 10.87.161.30/27 [110/7820] via G0/24
O 10.87 161.30/27 [110/7879] via G0/1
- A. G0/1
- B. G0/8
- C. G0/24
- D. G0/17
ANSWER: D

## ipconn-96  (Question 13.34)
Refer to the exhibit.
R1# show ip route
Codes: C - connected, S — static, I — IGRP, R — RIP, M — mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, XA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2, E — EGP
i - IS-IS, LI - IS-IS level-1, L2 — IS-IS level-2, * — candidate default
U - per-user static route, o - ODR
Gateway of last resort is not set
C   172.16.0.0/16 is directly connected, Loopback0
172.16.0.0/16 is variably subnetted, 4 subnets, 2 masks
O      172.16.1.3/32 [110/100] via 10.0.1.100, 00:39:08, Serial0
O      172.16.1.9/32 [110/5] via 172.16.1.50, 00:43:01, Gigabit Ethernet 0/0
D      172.16.1.4/30 [90/7445] via 172.16.9.5, 00:39:08, Gigabit Ethernet 0/0
[90/7445] via 172.16.4.4, 00:39:08, Gigabit Ethernet 0/4
How does router R1 handle traffic to the 172.16.1.4/30 subnet?
- A. It sends all traffic over the path via 172.16.4.4
- B. It sends all traffic over the path via 10.0.1 100
- C. It sends all traffic over the path via 172.16.9.5 using 172.16.4.4 as a backup
- D. It load-balances traffic over 172.16.9.5 and 172.16.4.4
ANSWER: D

## ipconn-97  (Question 13.44)
Which interface is used to send traffic to the destination network?
D 10.214.247.237/28 [90/2170] via G0/12
D 10.214.247.237/28 [90/46985] via G0/19
O 10.214.247.237/28 [110/665] via G0/9
O 10.214.247.237/28 [110/3399] via G0/1
- A. G0/12
- B. G0/1
- C. G0/9
- D. G0/19
ANSWER: A

## ipconn-98  (Question 13.45)
Which interface is used to send traffic to the destination network?
O 10.139.120.253/29 [110/9443] via G0/20
O 10.139.120.253/29 [110/29560] via G0/16
R 10.139.120.253/29 [120/12] via G0/11
R 10.139120 253/29 [120/6] via G0/9
- A. G0/11
- B. G0/20
- C. G0/9
- D. G0/16
ANSWER: B

## ipconn-99  (Question 13.51)
Refer to the exhibit.
router# show ip route
...
D       172.16.32.0/26 [90/25789217] via 10.0.0.1
R       172.16.32.0/24 [120/4] via 10.0.0.2
O       172.16.32.0/19 [110/229840] via 10.0.0.3
C       172.16.32.32/32 is directly connected, Loopback0
C       172.16.32.4/30 is directly connected, GigabitEthernet0/0
A packet sourced from 172.16.32.254 is destined for 172.16.32.8. What is the subnet mask of the preferred destination route?
- A. 255.255.224.0
- B. 255.255.255.0
- C. 255.255.255.192
- D. 255.255.255.252
ANSWER: C

## ipconn-100  (Question 13.57)
Refer to the exhibit.
0ldR#show ip ospf interface
GigabitEthernet0/0/0 is up, line protocol is up
Internet address is 192.168.1.2/24, Area 0
Process ID 1, Router ID 192.168.1.1, Network Type BROADCAST, Cost: 1 Transmit Delay is 1 sec, State DROTHER, Priority 1
Designated Router (ID) 192.168.1.1, Interface address 192.168.1.1
Backup Designated Router (ID) 192.168.1.1, Interface address 192.168.1.1
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:01
Index 1/1, flood queue length 0
Neighbor Count is 1, Adjacent neighbor count is 2
R2#show ip ospf interface
GigabitEthernet0/0/0 is up, line protocol is up
Internet address is 192.168.1.1/24, Area 0
Process ID 1, Router ID 192.168.1.1, Network Type BROADCAST, Cost: 1
Transmit Delay is 1 sec, State DROTHER, Priority 1
Designated Router (ID) 192.168.1.1, Interface address 192.168.1.2
Backup Designated Router (ID) 192.168.1.1, Interface address 192.168.1.2
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:02
Index 2/2, flood queue length 0
Neighbor Count is 1, Adjacent neighbor count is 2
Router OldR is replacing another router on the network with the intention of having OldR and R2 exchange routes. After the engineer applied the initial OSPF configuration, the routes were still missing on both devices. Which command sequence must be issued before the clear IP ospf process command is entered to enable the neighbor relationship?
- A. OldR(config)#router ospf 1 OldR(config-router)#no router-id 192.168.1.1
- B. OldR(config)#interface g0/0/0 OldR(config-if)#ip ospf dead-interval 15
- C. OldR(config)#interface g0/0/0 OldR(config-if)#ip ospf hello-interval 15
- D. OldR(config)#router ospf 1 OldR(config-router)# network 192.168.1.0 255.255.255.0 area 2
ANSWER: A
