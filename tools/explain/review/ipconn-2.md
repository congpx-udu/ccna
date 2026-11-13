## ipconn-52  (Question 10.29)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/64b434b218f0b5d2.jpeg]
Router R1 is added to the network and configured with the 10.0.0.64/26 and 10.0.20.0/24 subnets. However, traffic destined for the LAN on R3 is not accessible. Which command when executed on R1 defines a static route to reach the R3 LAN?
- A. ip route 10.0.15.0 255.255.255.0 10.0.20.1
- B. ip route 10.0.15.0 255.255.255.192 10.0.20.1
- C. ip route 10.0.0.64 255.255.255.192 10.0.20.3
- D. ip route 10.0.15.0 255.255.255.0 10.0.20.3
ANSWER: D
CURRENT_EXPLANATION: {"e": "Mạng LAN của R3 là 10.0.15.0/24 nên dùng mask 255.255.255.0, next hop là IP của R3 trên link 10.0.20.0/24 (10.0.20.3). Các option khác dùng mask /26, sai next hop hoặc trỏ tới mạng của chính R1."}

## ipconn-54  (Question 10.44)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d0656be0fd5586ae.jpeg]
A network engineer must configure router R1 with a host route to the server. Which command must the engineer configure?
- A. R1(config)#ip route 10.10.10.10 255.255.255.255 192.168.0.2
- B. R1(config)#ip route 10.10.10.0 255.255.255.0 192.168.0.2
- C. R1(config)#ip route 0.0.0.0 0.0.0.0 192.168.0.2
- D. R1(config)#ip route 192.168.0.2 255.255.255.255 10.10.10.10
ANSWER: A
CURRENT_EXPLANATION: {"e": "Host route là route /32 tới một host cụ thể: `ip route 10.10.10.10 255.255.255.255 192.168.0.2` (next hop là router kế tiếp). Mask /24 hay 0.0.0.0 là network/default route, còn đảo địa chỉ đích và next hop là sai."}

## ipconn-57  (Question 10.76)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c5d5d23ec7c5b4a1.jpeg]
After applying this configuration to router R1, a network engineer is verifying the implementation. If all links are operating normally, and the engineer sends a series of packets from PC1 to PC3, how are the packets routed?
- A. They are routed to 172.16.20.2.
- B. They are distributed sent round robin to interfaces S0/0/0 and S0/0/1.
- C. They are routed to 192.168.100.2.
- D. They are routed to 10.0.0.2.
ANSWER: A
CURRENT_EXPLANATION: {"e": "R1 có hai default route: AD 1 via 172.16.20.2 và AD 20 via 10.0.0.2 (floating). Khi mọi link hoạt động, route AD thấp hơn được dùng, nên packet đi tới 172.16.20.2. Không round robin vì AD khác nhau."}

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
CURRENT_EXPLANATION: {"e": "Load-balancing qua hai ISP cần hai default route có AD bằng nhau, hoặc chia dải 0.0.0.0/1 và 128.0.0.0/1 mỗi nửa qua một ISP. Hai lệnh default route cùng AD (hai next hop) tạo ECMP; bộ lệnh chia hai nửa 0/1 và 128/1 cũng chia tải theo dải đích. Default route có AD khác nhau (floating) thì chỉ failover, không load-balance."}

## ipconn-72  (Question 12.12)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7bce5d5785b6f9e9.png]
Router R14 is in the process of being configured. Which configuration must be used to establish a host route to PC 10?
- A. ip route 10.80.65.10 255.255.255.254 10.80.65.1
- B. ip route 10.73.65.66 0.0.0.255 10.80.65.10
- C. ip route 10.80.65.10 255.255.255.255 10.73.65.66
- D. ip route 10.73.65.65 255.0.0.0 10.80.65.10
ANSWER: C
CURRENT_EXPLANATION: {"e": "Host route dùng mask /32 và next hop là địa chỉ của router kế tiếp: `ip route 10.80.65.10 255.255.255.255 10.73.65.66`. Các option khác dùng mask không phải /32, wildcard hoặc đảo đích và next hop."}

## ipconn-73  (Question 12.13)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/379b790dbccc8b90.jpeg]
A static route must be configured on R86 to forward traffic for the 172.16.34.0/29 network, which resides on R14. Which command must be used to fulfill the request?
- A. ip route 172.16.34.0 255.255.255.248 10.73.65.65
- B. ip route 172.16.34.0 255.255.255.224 10.73.65.66
- C. ip route 10.73.65.65 255.255.255.248 172.16.34.0
- D. ip route 172.16.34.0 0.0.0.7 10.73.65.64
ANSWER: A
CURRENT_EXPLANATION: {"e": "Mạng 172.16.34.0/29 có mask 255.255.255.248, và next hop từ R86 là địa chỉ của R14 trên link, 10.73.65.65. Các option khác có mask sai, next hop là chính R86 hoặc dùng wildcard."}

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
CURRENT_EXPLANATION: {"e": "Để PC1 tới cả mạng 10.10.10.0/24 cần route /24 tới next hop R3 (`ip route 10.10.10.0 255.255.255.0 192.168.2.3`) và route host riêng /32 tới host ngoại lệ qua R2 (`ip route 10.10.10.10 255.255.255.255 192.168.2.2`). Hai route này bao phủ cả mạng lẫn host ngoại lệ; các route /29 hoặc dùng interface thoát thì không bao phủ đúng."}

## ipconn-81  (Question 12.53)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ec49b4982ded46d7.png]
Each router must be configured with the last usable IP address in the subnet. Which configuration fulfills this requirement?
- A. Option A R7# interface FastEthernet1/0 ip address 10.88.31.126 255.255.255.192 R8# interface FastEthernet0/0 ip address 10.19.63.95 255.255.255.192 R9# interface FastEthernet1/1 ip address 10.23.98.159 255.255.255.248
- B. Option B R7# interface FastEthernet1/0 ip address 10.88.31.126 255.255.255.240 R8# interface FastEthernet0/0 ip address 10.19.63.94 255.255.255.192 R9# interface FastEthernet1/1 ip address 10.23.98.158 255.255.255.248
- C. Option C R7# interface FastEthernet1/0 ip address 10.88.31.127 255.255.255.192 R8# interface FastEthernet0/0 ip address 10.19.63.95 255.255.255.240 R9# interface FastEthernet1/1 ip address 10.23.98.159 255.255.255.224
- D. Option D R7# interface FastEthernet1/0 ip address 10.88.31.127 255.255.255.240 R8# interface FastEthernet0/0 ip address 10.19.63.95 255.255.255.192 R9# interface FastEthernet1/1 ip address 10.23.98.159 255.255.255.248
ANSWER: B
CURRENT_EXPLANATION: {"e": "Phải chọn mask phù hợp cho từng subnet rồi lấy địa chỉ usable cuối. Option B có R7 10.88.31.126/28, R8 10.19.63.94/26, R9 10.23.98.158/29, đều là địa chỉ cuối usable (trước broadcast) của subnet tương ứng. Các option khác dùng địa chỉ broadcast (ví dụ .127, .95, .159) hoặc mask không khớp."}

## ipconn-82  (Question 12.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d2cec875c8e2abbf.png]
A network engineer is updating the configuration on router R1 to connect a new branch office to the company network. R2 has been configured correctly. Which command must the engineer configure so that devices at the new site communicate with the main office?
- A. ip route 172.25.25.1 255.255.255.255 g0/2
- B. ip route 172.25.25.0 255.255.255.0 192.168.2.1
- C. ip route 172.25.25.1 255.255.255.255 g0/1
- D. ip route 172.25.25.0 255.255.255.0 192.168.2.2
ANSWER: D
CURRENT_EXPLANATION: {"e": "R1 cần route tới mạng 172.25.25.0/24 ở site R2 với next hop là IP của R2 trên link, 192.168.2.2. Next hop 192.168.2.1 là IP của chính R1, còn các route /32 chỉ cho một host."}

## ipconn-86  (Question 12.70)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/469829a900b6b989.png]
Routers R1 and R2 are configured with RIP as the dynamic routing protocol. A network engineer must configure R1 with floating static route to serve as a backup route to network 192.168.23.0. Which command must the engineer configure on R1?
- A. ip route 192.168.23.0 255.255.255.255 192.168.13.3 121
- B. ip route 192.168.23.0 255.255.255.0 192.168.13.3 100
- C. ip route 192.168.23.0 255.255.255.0 192.168.13.3
- D. ip route 192.168.23.0 255.255.255.0 192.168.13.3 121
ANSWER: D
CURRENT_EXPLANATION: {"e": "Floating static route phải có AD cao hơn RIP (120), vì vậy dùng AD 121: `ip route 192.168.23.0 255.255.255.0 192.168.13.3 121`. Mask /32 sai mạng, AD 100 thấp hơn RIP, và không có AD (1) sẽ thắng RIP."}

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
CURRENT_EXPLANATION: {"e": "Để R14 và R86 thành adjacency và R14 làm DR (điểm trung tâm), cần priority 255 trên R14, MTU giống nhau (1500) và cùng network trong area 0. Option đúng đặt `ip ospf 10 area 0` trên interface, MTU 1500 cả hai và priority 255 cho R14. Option priority 0 trên R14 không làm được DR; các option còn lại bị lệch MTU 1500/1400."}

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
CURRENT_EXPLANATION: {"e": "Địa chỉ đích 10.225.34.225 khớp nhiều route BGP/static: 10.0.0.0/8, 10.128.0.0/9, 10.224.0.0/11 và 10.224.0.0/15 (10.224.0.0-10.225.255.255). Router chọn route có prefix dài nhất (longest match) là /15, next hop 10.224.1.4, chính là router C. Route /11 (router D) và /8 (router A) khớp nhưng kém cụ thể hơn."}

## ipconn-103  (Question 13.89)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/1b5b9010ec3380b2.png]
An engineer just installed network 10.120.10.0/24. Which configuration must be applied to the R14 router to add the new network to its OSPF routing table?
- A. router ospf 100 network 10.120.10.0 0.0.0.255 area 0
- B. router ospf 100 area 0 network 10.120.10.0 0.0.0.255
- C. router ospf 120 network 10.120.10.0 255.255.255.0 area 0 ip route 10.120.10.0 255.255.255.0 fa0/1
- D. router ospf 100 network 10.120.10.0 255.255.255.0 area 0
ANSWER: A
CURRENT_EXPLANATION: {"e": "Để R14 quảng bá mạng 10.120.10.0/24 vào OSPF process 100 area 0 cần lệnh `network 10.120.10.0 0.0.0.255 area 0` trong `router ospf 100`. Lệnh network dùng wildcard mask (0.0.0.255), không phải subnet mask, và cú pháp là `network <địa chỉ> <wildcard> area <id>`. Process ID phải là 100 theo sơ đồ, và không cần thêm static route."}

## ipconn-104  (Question 14.4)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b95cd60e48870ec3.png]
Router R1 receives static routing updates from routers A, B, C. and D. The network engineer wants R1 to advertise static routes in OSPF area 1. Which summary address must be advertised in OSPF?
- A. 10.1.40.0/25
- B. 10.1.40.0/24
- C. 10.1.41.0/25
- D. 10.1.40.0/23
ANSWER: D
CURRENT_EXPLANATION: {"e": "Bốn mạng 10.1.40.0/25, 10.1.40.128/25, 10.1.40.176/28 và 10.1.41.224/29 nằm trong dải 10.1.40.0 - 10.1.41.255. Summary nhỏ nhất bao trùm tất cả là 10.1.40.0/23, vì mạng 10.1.41.x nằm ngoài /24 của 10.1.40.0. Các prefix /24 hoặc /25 còn lại không bao phủ hết các mạng."}

## ipconn-109  (Question 14.49)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/280475aa67926127.png]
A network engineer is verifying the settings on a new OSPF network. All OSPF configurations use the default values unless otherwise indicated. Which router does the engineer expect will be elected as the DR when all devices boot up simultaneously?
- A. R1
- B. R2
- C. R3
- D. R4
ANSWER: D
CURRENT_EXPLANATION: {"e": "Trên segment multi-access, DR là router có OSPF priority cao nhất; nếu bằng nhau mới xét router ID cao nhất. R4 có priority 204 lớn nhất (R1 108, R3 106, R2 1) nên được bầu làm DR khi tất cả boot đồng thời. Nhãn 'DR' ghi sẵn ở R1 không quyết định kết quả vì câu hỏi nói các thiết bị khởi động cùng lúc."}

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
CURRENT_EXPLANATION: {"e": "Đích 10.227.151.255 khớp 10.0.0.0/8 (static), 10.128.0.0/9 (static) và 10.224.0.0/11 (BGP, dải 10.224-10.255). Route /15 chỉ phủ 10.224-10.225 nên không khớp. Longest match là /11 với next hop 10.224.4.5, chính là router D."}

## ipconn-111  (Question 14.78)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/bd37ea6738371d90.png]
What is preventing host A from reaching the internet?
- A. LAN and WAN network segments are different.
- B. IP address assignment is incorrect.
- C. The default gateway should be the first usable IP address.
- D. The domain name server is unreachable.
ANSWER: D
CURRENT_EXPLANATION: {"e": "DNS server thật nằm ở 196.1.38.132, nhưng host chỉ cấu hình preferred DNS là 192.168.1.254 (router, không chạy DNS) và alternate 196.1.38.254 (sai địa chỉ). Vì vậy host không phân giải được tên miền nên không ra được internet. IP, mask và default gateway 192.168.1.254 đều đúng."}

## ipconn-117  (Question 15.10)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/dfa90d58a4309fa5.png]
Which configuration parameter is preventing host С from reaching the internet?
- A. IP address assignment
- B. default gateway
- C. IP network mask
- D. automatic DNS
ANSWER: B
CURRENT_EXPLANATION: {"e": "Host C được cấu hình default gateway 192.168.1.1, trong khi gateway thật là interface của Router A, 192.168.1.254. Do gateway sai nên host không gửi được traffic ra ngoài subnet, còn IP/mask và DNS đều đúng."}

## ipconn-118  (Question 15.38)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e7eb29be80debff7.png]
With a reference bandwidth of 100 Gb on all routers, which path does router Y use to get to network 192.168.1.0/24?
- A. router C > D > A > F
- B. router E > B > F
- C. router E > F
- D. router C > D > A > B > F
ANSWER: D
CURRENT_EXPLANATION: {"e": "Với reference bandwidth 100 Gb: link 10Gig có cost 10, link 100Gig có cost 1. Đường Y-C-D-A-B-F đi qua 10 + 1 + 1 + 1 + 1 = 14, thấp nhất. Y-E-F có tổng 20, Y-E-B-F là 21, còn Y-C-D-A-F là 10+1+1+10 = 22, đều lớn hơn nên OSPF chọn đường C > D > A > B > F."}

## ipconn-119  (Question 15.44)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/01a577a8d4415953.png]
Inter-VLAN routing is configured on SW1. Client A is running Linux as an OS in VLAN 10 with a default gateway IP 10.0.0.1 but cannot ping client B in VLAN 20 running Windows. What action must be taken to verify that client A has the correct IP settings?
- A. Run the ifconfig command on client A to confirm that its IP and subnet mask fall within 255.254.0.0.
- B. Run the ipconfig command on client A and ensure that the IP address is within the host range of 10.0.0.1 – 10.0.255.254.
- C. Run the ipconfig command on client A to confirm that the correct 10.0.0.1 default gateway is used.
- D. Run the ifconfig command on client A to confirm that the subnet mask is set to 255.255.128.0
ANSWER: A
CURRENT_EXPLANATION: {"e": "VLAN 10 dùng 10.0.0.0/15, tức subnet mask 255.254.0.0 (dải 10.0.0.1 - 10.1.255.254). Client Linux dùng `ifconfig` (Windows mới dùng `ipconfig`), cần kiểm tra IP và mask nằm đúng subnet 255.254.0.0 của SVI 10.0.0.1/15. Đáp án 255.255.128.0 hay dải /16 là sai mask."}

## ipconn-121  (Question 15.83)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ecc18bcdbb4252b5.png]
Configurations for the switch and PCs are complete. Which configuration must be applied so that VLANs 2 and 3 communicate back and forth?
- A. interface GigabitEthernet0/0 ip address 10.10.2.10 255.255.252.0
- B. interface GigabitEthernet0/0.3 encapsulation dot1Q 10 ip address 10.10.2.10 255.255.255.252
- C. interface GigabitEthernet0/0.10 encapsulation dot1Q 3 ip address 10.10.2.10 255.255.254.0
- D. interface GigabitEthernet0/0.3 encapsulation dot1Q 3 native ip address 10.10.2.10 255.255.252.0
ANSWER: C
CURRENT_EXPLANATION: {"e": "VLAN 3 dùng 10.10.2.1/23, nên subinterface router-on-a-stick cần `encapsulation dot1Q 3` và IP 10.10.2.10 với mask 255.255.254.0 (/23). Số subinterface (.10) chỉ là nhãn, quan trọng là tag dot1Q khớp VLAN. Các đáp án khác sai mask (/22, /30) hoặc sai tag VLAN."}

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
CURRENT_EXPLANATION: {"e": "Địa chỉ 172.16.1.8 với mask /28 là sai so với gateway và mạng thiết kế; cần mask 255.255.255.248 (/29) để dải host là .1-.6. Khi đó IP 172.16.1.6 nằm cùng subnet với gateway 172.16.1.1 và là host hợp lệ. Đổi chỉ DNS hoặc gateway sẽ không sửa được lỗi subnet."}

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
CURRENT_EXPLANATION: {"e": "Workstation 1 ở VLAN 71 (10.0.71.0/27) nên cần IP trong subnet đó (10.0.71.16), mask 255.255.255.224, default gateway 10.0.71.1 là router. Để truy cập server bằng FQDN thì phải có DNS server 10.0.63.5. Các lựa chọn khác sai subnet, mask, gateway (10.0.71.0 là network address) hoặc chỉ liệt kê DHCP server."}

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
CURRENT_EXPLANATION: {"e": "Traffic internet không khớp route cụ thể nào nên dùng default route S* 0.0.0.0/0 qua 10.10.11.2 (gateway of last resort). Các prefix còn lại là mạng cụ thể, không phải đường ra internet."}

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
CURRENT_EXPLANATION: {"e": "Đích 10.10.13.165 khớp 10.10.13.160/29 (dải .160-.167), là route cụ thể nhất, đi qua next hop 10.10.10.5 trên Gi0/1, tức Router3. Prefix /25 và /28 không chứa địa chỉ này, và default route chỉ dùng khi không có route cụ thể hơn."}

## ipconn-129  (Question 15.102)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e77785dbfbefb71a.jpeg]
Router R1 is running three different routing protocols. Which route characteristic is used by the router to forward the packet that it receives for destination IP 172.16.32.1?
- A. longest prefix
- B. metric
- C. cost
- D. administrative distance
ANSWER: A
CURRENT_EXPLANATION: {"e": "Địa chỉ 172.16.32.1 khớp cả ba route (EIGRP /27, OSPF /19, RIP /24). Router luôn chọn theo longest prefix match trước, nên route /27 được dùng. AD và metric chỉ xét khi các prefix bằng nhau."}

## ipconn-130  (Question 15.107)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/05db370ffdf8b988.png]
A packet is being sent across router R1 to host 172.16.3.14. To which destination does the router send the packet?
- A. 207.165.200.246 via Serial0/1/0
- B. 207.165.200.254 via Serial0/0/0
- C. 207.165.200.254 via Serial0/0/1
- D. 207.165.200.250 via Serial0/0/0
ANSWER: C
CURRENT_EXPLANATION: {"e": "Đích 172.16.3.14 khớp static 172.16.3.0/24 và OSPF 172.16.3.0/28 (dải .0-.15). Longest prefix match chọn /28, nên gói đi qua next hop 207.165.200.254 trên Serial0/0/1, dù static có AD thấp hơn."}

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
CURRENT_EXPLANATION: {"e": "Với 192.168.2.86, route cụ thể nhất là 192.168.2.80/29 (dải .80-.87) nên dùng next hop 172.16.1.3. Với 10.20.1.50, route cụ thể nhất là 10.20.1.32/27 (dải .32-.63) cũng next hop 172.16.1.3. Cả hai đích dùng chung next hop theo longest prefix match.", "warn": "Theo longest prefix match, cả hai địa chỉ đều đi qua 172.16.1.3 (route /29 và /27), nên đáp án đúng là 172.16.1.3, không phải 172.16.1.2 như answer key."}

## ipconn-140  (Question 16.49)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/efc8488964f7d08f.png]
The loopback IP of R3 has been learned via the two interfaces on R1. R1 is configured with a reference bandwidth of 10 Gbps. Based on the metric calculations, which next hop IP would be used for outgoing routing?
- A. 10.12.0.5
- B. 10.12.0.2
- C. 10.12.0.1
- D. 10.12.0.6
ANSWER: D
CURRENT_EXPLANATION: {"e": "Với reference bandwidth 10 Gbps: link 1 Gbps có cost 10, link 10 Gbps có cost 1. Đường qua 10.12.0.6 (link 10 Gbps) có cost 1, trong khi đường qua 10.12.0.2 (link 1 Gbps) là 10, cộng đoạn R2-R3 giống nhau. Vì vậy next hop dùng là 10.12.0.6."}

## ipconn-142  (Question 16.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5d6208ff75529395.png]
OSPF neighbors routers A, B, C, and D are sending a route for 10.227.150.160/27. When the current route for 10.227.150.160/27 becomes unavailable, which cost will router Y use to route traffic to 10.227.150.160/27?
- A. Cost 20
- B. Cost 30
- C. Cost 40
- D. Cost 50
ANSWER: B
CURRENT_EXPLANATION: {"e": "Route hiện tại tốt nhất là qua router A (cost 20). Khi route đó mất, router Y dùng route có cost thấp tiếp theo là router D với cost 30 (B là 40, C là 50). OSPF chọn đường có tổng cost thấp nhất trong các route còn lại."}

## ipconn-145  (Question 16.67)
[IMAGE: D:\CCNA_ontap\web\img/5ebfb6eb993c781b.png]
Refer to the exhibit.
A packet is being sent across router R1 to host 172.16.0.14. To which destination does the router send the packet?
- A. 209.165.200.246 via Serial0/1/0
- B. 209.165.200.254 via Serial0/0/0
- C. 209.165.200.254 via Serial0/0/1
- D. 209.165.200.250 via Serial0/0/0
ANSWER: A
CURRENT_EXPLANATION: {"e": "Đích 172.16.0.14 không khớp route 172.16.3.0/24 hay /28 (chỉ ở dải 172.16.3.x), nên chỉ khớp default route S* 0.0.0.0/0. Gói được gửi tới 209.165.200.246 qua Serial0/1/0."}

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
CURRENT_EXPLANATION: {"e": "Đích 172.16.153.154 không khớp /32 (172.16.153.153 chỉ cho đúng host đó). Route khớp dài nhất còn lại là 172.16.0.0/16, next hop 10.56.22.23; /8 và default route kém cụ thể hơn."}
