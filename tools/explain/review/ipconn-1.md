## ipconn-2  (Question 7.5)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b0c723805ba033aa.jpeg]
When PC-A sends traffic to PC-B, which network component is in charge of receiving the packet from PC-A verifying the IP addresses, and forwarding the packet to PC-B?
- A. Layer 2 switch
- B. firewall
- C. Load balancer
- D. Router
ANSWER: D
CURRENT_EXPLANATION: {"e": "Khi hai PC nằm ở hai subnet khác nhau, router là thiết bị nhận gói, kiểm tra địa chỉ IP đích trong routing table rồi chuyển tiếp sang mạng của PC-B (Layer 3). Switch Layer 2 chỉ chuyển frame theo MAC, firewall chủ yếu lọc traffic và load balancer phân phối tải tới server, không đảm nhiệm vai trò định tuyến này."}

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
CURRENT_EXPLANATION: {"e": "Route toward cả mạng 2001:db8:23::/64 qua R2 là `ipv6 route 2001:db8:23::/64 fd00:12::2`. Host 2001:db8:23::14 cần đi qua R3 nên cấu hình host route /128 `ipv6 route 2001:db8:23::14/128 fd00:13::3`; do longest prefix match, route /128 được ưu tiên hơn /64. Các lệnh dùng /128 cho cả mạng hoặc /64 kèm địa chỉ host đều sai prefix."}

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
CURRENT_EXPLANATION: {"e": "DR/BDR được bầu theo OSPF priority cao nhất (dải hợp lệ 0-255; priority 0 không tham gia). Đặt R3 priority 255 và R2 priority 240 cao hơn mặc định 1, nên R3 thành DR và R2 thành BDR (sau khi reset OSPF process). Option dùng priority 259 hoặc 256 là không hợp lệ, các option còn lại giữ R4/R5 ở vị trí cũ."}

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
CURRENT_EXPLANATION: {"e": "Cần route cho mạng đối diện; cách đơn giản là default route trỏ next hop là địa chỉ IP của router đầu kia. Theo hình, R1 phải trỏ tới 209.165.200.226 và R2 trỏ tới 209.165.200.225, tức địa chỉ phía đối diện của link giữa hai router. Các đáp án trỏ sai next hop (chính IP của mình) hoặc dùng địa chỉ host với mask /24 là sai."}

## ipconn-13  (Question 8.39)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d5f3441b0abf5404.jpeg]
Which command must be issued to enable a floating static default route on router A?
- A. ip route 0.0.0.0 0.0.0.0 192.168.2.1 10
- B. ip route 0.0.0.0 0.0.0.0 192.168.1.2
- C. ip route 0.0.0.0 0.0.0.0 192.168.1.2 10
- D. ip default-gateway 192.168.2.1
ANSWER: C
CURRENT_EXPLANATION: {"e": "Floating static route là route có administrative distance cao hơn route chính nên chỉ vào routing table khi route chính mất. Theo hình, link dự phòng đi qua 192.168.1.2, nên lệnh đúng là `ip route 0.0.0.0 0.0.0.0 192.168.1.2 10` (AD 10 > AD 1 của static chính). Không có AD thì thành static thường (AD 1), còn `ip default-gateway` dùng cho thiết bị không định tuyến."}

## ipconn-14  (Question 8.40)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d330b01fa1efe7a5.jpeg]
Router R1 currently is configured to use R3 as the primary route to the Internet, and the route uses the default administrative distance settings. A network engineer must configure R1 so that it uses R2 as a backup, but only if R3 goes down. Which command must the engineer configure on R1 so that it correctly uses R2 as a backup route, without changing the administrative distance configuration on the link to R3?
- A. ip route 0.0.0.0 0.0.0.0 g0/1 6
- B. ip route 0.0.0.0 0.0.0.0 g0/1 1
- C. ip route 0.0.0.0 0.0.0.0 209.165.201.5 10
- D. ip route 0.0.0.0 0.0.0.0 209.165.200.226 1
ANSWER: A
CURRENT_EXPLANATION: {"e": "Route chính qua R3 là static có AD mặc định 1, nên backup qua R2 phải có AD lớn hơn 1. Lệnh `ip route 0.0.0.0 0.0.0.0 g0/1 6` tạo floating static route với AD 6, chỉ dùng khi route qua R3 biến mất. AD 1 sẽ tải cân bằng với route chính, còn các lệnh dùng next hop 209.165.201.5/209.165.200.226 không đúng đường qua R2 theo hình."}

## ipconn-15  (Question 8.41)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/455eaf0a9f7eebf6.jpeg]
An engineer is updating the R1 configuration to connect a new server to the management network. The PCs on the management network must be blocked from pinging the default gateway of the new server. Which command must be configured on R1 to complete the task?
- A. R1(config)#ip route 172.16.2.0 255.255.255.0 192.168.1.15
- B. R1(config)#ip route 172.16.2.2 255.255.255.255 gi0/0
- C. R1(config)#ip route 172.16.2.0 255.255.255.0 192.168.1.5
- D. R1(config)#ip route 172.16.2.2 255.255.255.248 gi0/1
ANSWER: B
CURRENT_EXPLANATION: {"e": "Để chặn PC mạng management ping default gateway của server mới (172.16.2.2), cần route host /32 trỏ ra interface khác để ping không tới được: `ip route 172.16.2.2 255.255.255.255 gi0/0`. Host route /32 có prefix dài nhất nên thắng mọi route khác. Các lệnh còn lại dùng next hop sai hoặc mask /29, /24 không đúng host."}

## ipconn-18  (Question 8.50)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3fb338377947522d.jpeg]
Traffic sourced from the loopback0 interface is trying to connect via ssh to the host at 10.0.1.15. What is the next hop to the destination address?
- A. 192.168.0.7
- B. 192.168.0.4
- C. 192.168.0.40
- D. 192.168.3.5
ANSWER: A
CURRENT_EXPLANATION: {"e": "Đích 10.0.1.15 khớp 10.0.1.0/24 và 10.0.1.0/28 (dải .0-.15). Theo longest prefix match, route /28 học qua EIGRP via 192.168.0.7 được chọn. Route /24 chỉ là mạng kết nối trực tiếp nên kém cụ thể hơn, còn /32 của 10.0.1.3 và 10.0.1.190 không chứa đích."}

## ipconn-19  (Question 8.52)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/cfc7348dcd52127c.jpeg]
Which action must be taken to ensure that router A is elected as the DR for OSPF area 0?
- A. Configure the OSPF priority on router A with the lowest value between the three routers
- B. Configure the router A interfaces with the highest OSPF priority value within the area.
- C. Configure router A with a fixed OSPF router ID.
- D. Configure router B and router C as OSPF neighbors of router A.
ANSWER: B
CURRENT_EXPLANATION: {"e": "Router có OSPF priority cao nhất trong segment sẽ thắng bầu DR (router ID chỉ dùng để phá hòa). Do đó cấu hình interface router A với priority cao nhất trong area. Đặt priority thấp nhất làm A khó thành DR, fixed router ID hay khai báo neighbor không quyết định kết quả bầu."}

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
CURRENT_EXPLANATION: {"e": "Số host: 923 cần /22 (1022 host, đủ cả 10% tăng trưởng), 225 cần /24 (254 host), 3641 cần /20 (4094 host). Vậy R7 dùng 255.255.252.0, R8 dùng 255.255.255.0, R9 dùng 255.255.240.0. Các option khác mask quá nhỏ hoặc quá lớn so với yêu cầu."}

## ipconn-21  (Question 8.65)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9b80b7999062b4ad.jpeg]
Which network prefix was learned via EIGRP?
- A. 172.16.0.0/16
- B. 207.165.200.0/24
- C. 192.168.2.0/24
- D. 192.168.1.0/24
ANSWER: C
CURRENT_EXPLANATION: {"e": "Route EIGRP có mã D trong routing table. Theo exhibit, 192.168.2.0/24 là route có mã D [90/...] (AD 90 của EIGRP). Các prefix còn lại là static, connected, RIP hoặc OSPF."}

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
CURRENT_EXPLANATION: {"e": "Để R1 thành DR: tăng priority R1 lên 200 (`ip ospf priority 200` trên fa0/0) và đặt R3 priority 0 để R3 không tham gia bầu. Priority 0 trên R1 làm R1 không bao giờ là DR; đặt priority 200 trên R3 làm R3 thành DR; router-id không phải tiêu chí chính khi đã có priority."}

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
CURRENT_EXPLANATION: {"e": "Cần 380 user nên dùng /23 (510 host): subnet 10.7.54.0, mask 255.255.254.0, broadcast 10.7.55.255, dải usable 10.7.54.1 - 10.7.55.254. Các đáp án khác có broadcast hoặc mask không khớp với dải 10.7.54.1 - 10.7.55.254."}

## ipconn-27  (Question 9.11)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/58a3f7a8bc8f6f74.jpeg]
Which route must be configured on R1 so that OSPF routing is used when OSPF is up. But the server is still reachable when OSPF goes down?
- A. ip route 10.1.1.10 255.255.255.255 172.16.2.2 100
- B. ip route 10.1.1.0 255.255.255.0 gi0/1 125
- C. ip route 10.1.1.0 255.255.255.0 172.16.2.2 100
- D. ip route 10.1.1.10 255.255.255.255 gi0/0 125
ANSWER: D
CURRENT_EXPLANATION: {"e": "Cần static route có AD cao hơn OSPF (110) để chỉ dùng khi OSPF down: AD 125. Route host /32 tới 10.1.1.10 qua gi0/0 AD 125 là floating route; khi OSPF còn, route OSPF (AD 110) được dùng. AD 100 thấp hơn 110 sẽ lấn át OSPF, còn các option kia trỏ sai interface/next hop theo hình."}

## ipconn-28  (Question 9.14)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6a1ff273265c9d00.jpeg]
Which command configures OSPF on the point-to-point link between routers R1 and R2?
- A. network 10.0.0.0 0.0.0.255 area 0
- B. neighbor 10.1.2.0 cost 180
- C. ip ospf priority 100
- D. router-id 10.0.0.15
ANSWER: A
CURRENT_EXPLANATION: {"e": "Lệnh kích hoạt OSPF trên link point-to-point là `network 10.0.0.0 0.0.0.255 area 0` (wildcard mask), khớp mạng của link giữa R1 và R2. `neighbor`, `priority` và `router-id` không đưa interface vào OSPF."}

## ipconn-31  (Question 9.27)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9b22465db2b33447.png]
A static route must be configured on R14 to forward traffic for the 172.21.34.0/25 network that resides on R86. Which command must be used to fulfill the request?
- A. ip route 172.21.34.0 255.255.255.192 10.73.65.65
- B. ip route 172.21.34.0 255.255.255.0 10.73.65.65
- C. ip route 172.21.34.0 255.255.128.0 10.73.65.64
- D. ip route 172.21.34.0 255.255.255.128 10.73.65.66
ANSWER: D
CURRENT_EXPLANATION: {"e": "Mạng 172.21.34.0/25 có mask 255.255.255.128, và next hop phải là địa chỉ IP đầu kia của R86 trên link (10.73.65.66). Các đáp án khác dùng sai mask hoặc trỏ về chính R14 (10.73.65.65) / địa chỉ mạng (.64)."}

## ipconn-32  (Question 9.29)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5b588f7319736056.jpeg]
A company is configuring a failover plan and must implement the default routes in such a way that a floating static route will assume traffic forwarding when the primary link goes down. Which primary route configuration must be used?
- A. ip route 0.0.0.0 0.0.0.0 192.168.0.2 GigabitEthernet1/0
- B. ip route 0.0.0.0 0.0.0.0 192.168.0.2 tracked
- C. ip route 0.0.0.0 0.0.0.0 192.168.0.2 floating
- D. ip route 0.0.0.0 0.0.0.0 192.168.0.2
ANSWER: D
CURRENT_EXPLANATION: {"e": "Primary route là static route thường (AD 1) tới next hop 192.168.0.2: `ip route 0.0.0.0 0.0.0.0 192.168.0.2`. Floating static route backup sẽ có AD cao hơn. Các từ khóa `tracked` hay `floating` không tồn tại trong cú pháp lệnh này."}

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
CURRENT_EXPLANATION: {"e": "Router R2 priority 99, R1 và R3 mặc định 1; để R3 thành DR cần priority cao hơn 99, ví dụ 100 trên interface nối vào mạng 10.0.4.0/24 (Gig0/1 theo hình). Priority 0 hoặc 1 không thắng, và Gig0/0 là interface sang mạng khác."}

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
CURRENT_EXPLANATION: {"e": "Host 10.10.13.158 nằm trong 10.10.13.144/28 (dải .144-.159). Route này học qua OSPF via 10.10.10.9; /25 (.0-.127) và /29 (.160) không chứa host, còn default route kém cụ thể hơn. Vậy next hop là 10.10.10.9."}

## ipconn-35  (Question 9.37)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d6b9bed1a2c41b6c.jpeg]
Web traffic is coming in from the WAN interface. Which route takes precedence when the router is processing traffic destined for the LAN network at 10.0.10.0/24?
- A. via next-hop 10.0.1.5
- B. via next-hop 10.0.1.4
- C. via next-hop 10.0.1.50
- D. via next-hop 10.0.1.100
ANSWER: A
CURRENT_EXPLANATION: {"e": "Đích 10.0.10.0/24 có hai route: OSPF [110/10] via 10.0.1.4 và EIGRP [90/10] via 10.0.1.5. Router chọn route có administrative distance thấp hơn, tức EIGRP (90), nên next hop là 10.0.1.5."}

## ipconn-36  (Question 9.51)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7b1a7d293374432e.jpeg]
R1 learns all routes via OSPF. Which command configures a backup static route on R1 to reach the 192.168.20.0/24 network via R3?
- A. R1(config)#ip route 192.168.20.0 255.255.255.0 192.168.30.2 111
- B. R1(config)#ip route 192.168.20.0 255.255.255.0 192.168.30.2 90
- C. R1(config)#ip route 192.168.20.0 255.255.0.0 192.168.30.2
- D. R1(config)#ip route 192.168.20.0 255.255.255.0 192.168.30.2
ANSWER: A
CURRENT_EXPLANATION: {"e": "Backup (floating) static route phải có AD cao hơn OSPF (110), nên dùng AD 111: `ip route 192.168.20.0 255.255.255.0 192.168.30.2 111`. AD 90 hay mặc định 1 sẽ thắng OSPF; mask /16 là sai mạng."}

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
CURRENT_EXPLANATION: {"e": "Secondary route phải có AD lớn hơn AD của route chính (OSPF 110) nên chọn AD 111/112, trỏ qua link phụ theo hình (172.16.0.5/.6). Các option AD 113/114, 89 hay 110 không phù hợp: AD 89 thấp hơn OSPF, 110 bằng OSPF."}

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
CURRENT_EXPLANATION: {"e": "R1 là DROTHER, muốn thành DR thì tăng priority interface của chính R1 lên 200 (cao nhất) rồi `clear ip ospf process` để bầu lại (DR không tự preempt). Đặt priority 1 là mặc định, và đổi priority trên R2/R3 không giúp R1."}

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
CURRENT_EXPLANATION: {"e": "R1 chỉ được thiết lập neighbor với R2, không tham gia bầu DR (`ip ospf priority 0`) và dùng `router-id 10.1.1.1`. Option B đáp ứng đủ ba yêu cầu này, các option khác thiếu một yếu tố hoặc có priority/router-id sai."}

## ipconn-41  (Question 9.92)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/2d3649cdca22c974.jpeg]
Router R1 must be configured to reach the 10.0.3.0 network from the 10.0.1.0/24 segment. Which command must be used to configure the route?
- A. route add 10.0.3.0 0.255.255.255 10.0.4.2
- B. route add 10.0.3.0 mask 255.255.255.0 10.0.4.3
- C. ip route 10.0.3.0 0.255.255.255 10.0.4.2
- D. ip route 10.0.3.0 255.255.255.0 10.0.4.3
ANSWER: D
CURRENT_EXPLANATION: {"e": "Trên router Cisco dùng `ip route <network> <subnet mask> <next-hop>`. Mạng 10.0.3.0/24 dùng mask 255.255.255.0 qua next hop 10.0.4.3 (router láng giềng theo hình). `route add` là cú pháp Windows, và wildcard mask 0.255.255.255 không dùng cho ip route."}

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
CURRENT_EXPLANATION: {"e": "Để có failover, cần floating static default route với AD cao hơn (AD 2) trỏ qua link dự phòng 10.10.10.6 / 10.10.10.5. Static route AD 1 mặc định sẽ cạnh tranh với route chính; các route host với next hop sai không tạo failover đúng."}

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
CURRENT_EXPLANATION: {"e": "Lệnh network dùng wildcard mask, không phải subnet mask. Link giữa R1 và R2 là 10.0.0.0/30 nên dùng `network 10.0.0.0 0.0.0.3 area 0`, mạng LAN của R1 theo hình là 10.0.1.0/24 nên dùng `network 10.0.1.0 0.0.0.255 area 0`. Các option khác dùng sai prefix, sai wildcard (0.0.0.252) hoặc dùng subnet mask."}

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
CURRENT_EXPLANATION: {"e": "R1 đang là DR; để R2 thành DR phải tăng OSPF priority của R2 lên cao hơn R1 (ví dụ 100) trên gi0/0. Priority 1 là mặc định và không đủ; thay router-id không đáng tin vì priority được so sánh trước router ID."}

## ipconn-48  (Question 10.11)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5f46be83bbff6b86.jpeg]
What is the next hop for traffic entering R1 with a destination of 10.1.2.126?
- A. 10.165.20.126
- B. 10.165.20.146
- C. 10.165.20.166
- D. 10.165.20.226
ANSWER: C
CURRENT_EXPLANATION: {"e": "Đích 10.1.2.126 khớp 10.1.2.0/25 (EIGRP, AD 90) và static 10.1.2.112/28 (dải .112-.127). Route /28 có prefix dài nhất nên được chọn, next hop 10.165.20.166. Longest prefix match được xét trước administrative distance."}

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
CURRENT_EXPLANATION: {"e": "Mạng 10.0.0.0/24 cần đi qua R3 và host PC1 10.0.0.5/32 qua R2. Trên R1 cấu hình route /24 tới next hop 192.168.0.2 và route /32 tới next hop 172.16.0.2 theo hình; route /32 cụ thể hơn nên thắng với PC1. Các option mask /16 hoặc đổi next hop sai thì không đáp ứng yêu cầu."}

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
CURRENT_EXPLANATION: {"e": "R2 phải thuộc đúng subnet WAN (mask /27, IP 10.0.0.34) và có OSPF priority cao nhất (100) để thành DR. Option khác dùng sai địa chỉ/mask (10.0.1.x), priority 0 (không bao giờ là DR) hoặc priority thấp hơn."}

## ipconn-51  (Question 10.17)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/da93b314fd075c17.jpeg]
R1 has just received a packet from host A that is destined to host B. Which route in the routing table is used by R1 to reach host B?
- A. 10.10.13.0/25[1/0] via 10.10.10.2
- B. 10.10.13.0/25[110/2] via 10.10.10.6
- C. 10.10.13.0/25[110/2] via 10.10.10.2
- D. 10.10.13.0/25[108/0] via 10.10.10.10
ANSWER: D
CURRENT_EXPLANATION: {"e": "Đích host B 10.10.13.10 thuộc 10.10.13.0/25. Có ba static route tới prefix này với AD 111, 112 và 108; route có AD thấp nhất (108) via 10.10.10.10 được chọn. Route default AD 1 kém cụ thể hơn nên không dùng."}
