## fund-20  (Question 8.47)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/757c0504c35595b7.jpeg]
A network engineer must provide configured IP addressing details to investigate a firewall rule issue. Which subnet and mask identify what is configured on the en0 interface?
- A. 10.8.0.0/16
- B. 10.8.64.0/18
- C. 10.8.128.0/19
- D. 10.8.138.0/24
ANSWER: C
CURRENT_EXPLANATION: {"e": "Interface en0 có địa chỉ 10.8.138.14 với netmask 0xffffe000 = 255.255.224.0, tức /19 (block size 32 ở octet thứ ba). 138 nằm trong khối 128-159 nên subnet là 10.8.128.0/19 (broadcast 10.8.159.255)."}

## fund-21  (Question 8.51)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/a908f363124bb2f3.jpeg]
SiteA#show interface TenGigabitEthernet0/1/0
TenGigabitEthernet0/1/0 is up, line protocol is up
Hardware is BUILT-IN-EPA-8x10G, address is aabb.cc00.0100 (bia aabb.cc00.0100)
Description: Connection to SiteB
Internet address is 10.10.10.1/30
MTU 8146 bytes, BW 10000000 Kbit/sec, DLY 10 usec,
reliability 255/255, txload 1/255, rxload 1/255
Full Duplex, 10000Mbps, link type is force-up, media type is SFP-SR
5 minute input rate 264797000 bits/sec, 26672 packets/sec
5 minute output rate 122464000 bits/sec, 15724 packets/sec
SiteB#show interface TenGigabitEthernet0/1/0
TenGigabitEthernet0/1/0 is up, line protocol is up
Hardware is BUILT-IN-EPA-8x10G, address is 0000.0c00.750c (bia 0000.0c00.750c)
Description: Connection to SiteA
Internet address is 10.10.10.2/30
MTU 8146 bytes, BW 10000000 Kbit/sec, DLY 10 usec,
reliability 255/255, txload 1/255, rxload 1/255
Full Duplex, 10000Mbps, link type is force-up, media type is SFP-LR
5 minute input rate 123245000 bits/sec, 15343 packets/sec
5 minute output rate 265746000 bits/sec, 12453 packets/sec
Shortly after SiteA was connected to SiteB over a new single-mode fiber path, users at SiteA report intermittent connectivity issues with applications hosted at SiteB. What is the cause of the intermittent connectivity issue?
- A. An incorrect type of transceiver has been inserted into a device on the link.
- B. The wrong cable type was used to make the connection.
- C. Heavy usage is causing high latency.
- D. Physical network errors are being transmitted between the two sites.
ANSWER: A
CURRENT_EXPLANATION: {"e": "Hai đầu link dùng transceiver khác loại: SiteA dùng SFP-SR (multimode, tầm ngắn) còn SiteB dùng SFP-LR (single-mode, tầm xa), trong khi đường cáp là single-mode. Transceiver SR không khớp với LR/single-mode gây tín hiệu quang không ổn định và kết nối chập chờn. Không có lỗi vật lý nào trong counters và tải thấp nên không phải latency do traffic hay lỗi cáp."}

## fund-29  (Question 9.108)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/51cd22497e999ee1.jpeg]
What is expected when PC_A sends data to PC_B after their initial communication?
- A. The source and destination MAC addresses remain the same
- B. The switch rewrites the source and destination MAC addresses with its own
- C. The source MAC address is changed
- D. The destination MAC address is replaced with ffff.ffff.ffff
ANSWER: A
CURRENT_EXPLANATION: {"e": "PC_A và PC_B cùng VLAN 200 trên một switch, nên switch chỉ chuyển tiếp frame ở Layer 2 mà không sửa header. Source và destination MAC giữ nguyên; switch không viết lại MAC, và sau lần giao tiếp đầu (ARP) đích đã biết nên không flood bằng ffff.ffff.ffff."}

## fund-31  (Question 10.18)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/20cf054331d374f9.jpeg]
The given Windows PC is requesting the IP address of the host at www.cisco.com. To which IP address is the request sent?
- A. 192.168.1.226
- B. 192.168.1.253
- C. 192.168.1.100
- D. 192.168.1.254
ANSWER: B
CURRENT_EXPLANATION: {"e": "Trong ipconfig /all, yêu cầu phân giải tên www.cisco.com được gửi tới DNS server đã cấu hình, là 192.168.1.253. 192.168.1.100 là default gateway, 192.168.1.254 là DHCP server và 192.168.1.226 là IP của chính PC."}

## fund-34  (Question 10.69)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/33b5887512eeffb0.png]
A network engineer must configure the link with these requirements:
• Consume as few IP addresses as possible.
• Leave at least two additional useable IP addresses for future growth.
Which set of configurations must be applied?
- A. R1(config-if)#ip address 10.10.10.1 255.255.255.248
R2(config-if)#ip address 10.10.10.4 255.255.255.248
- B. R1(config-if)#ip address 10.10.10.1 255.255.255.240
R2(config-if)#ip address 10.10.10.12 255.255.255.240
- C. R1 (config-if)#ip address 10.10.10.1 255.255.255.252
R2(config-if)#ip address 10.10.10.2 255.255.255.252
- D. R1 (config-if)#ip address 10.10.10.1 255.255.255.0
R2(config-if)#ip address 10.10.10.5 255.255.255.0
ANSWER: A
CURRENT_EXPLANATION: {"e": "Cần subnet ít địa chỉ nhất nhưng còn dư ít nhất 2 địa chỉ usable cho tương lai, tức tối thiểu 4 host usable: /29 (6 usable). /30 chỉ có 2 usable nên không dư, còn /28 và /24 lãng phí hơn. Cặp 10.10.10.1 và 10.10.10.4 mask 255.255.255.248 cùng thuộc 10.10.10.0/29 và hợp lệ."}

## fund-39  (Question 11.20)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/524c710ad747826d.png]
A newly configured PC fails to connect to the internet using TCP port 80 to www.cisco.com. Which setting must be modified for the connection to work?
- A. Subnet Mask
- B. DNS Servers
- C. Default Gateway
- D. DHCP Server
ANSWER: A
CURRENT_EXPLANATION: {"e": "PC có mask 255.255.255.192 (/26) trong khi router/subnet dùng /27 (10.2.2.1/27). Mask sai khiến PC nhận định sai phạm vi mạng cục bộ nên cần sửa Subnet Mask thành 255.255.255.224. Default gateway 10.2.2.1, DNS 8.8.8.8 và DHCP đều không phải nguyên nhân."}

## fund-54  (Question 12.76)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d1614d65079f241e.png]
The switches are connected via a Cat5 Ethernet cable that was successfully tested. The interfaces are configured as access ports and are both in a “down” status. What is the cause of this issue?
- A. The switches are configured with incompatible duplex settings.
- B. The speed settings on the switches are mismatched.
- C. The distance between the two switches is not supported by Cat5.
- D. The portfast command is missing from the configuration.
ANSWER: B
CURRENT_EXPLANATION: {"e": "Hai switch nối bằng cáp Cat5 đã test tốt nhưng cả hai port access đều down, cho thấy cấu hình speed hai đầu không khớp (speed cố định khác nhau) nên link không lên. Cat5 vẫn hỗ trợ tới 100 m; duplex mismatch thường khiến link vẫn up nhưng lỗi, còn portfast không ảnh hưởng trạng thái link vật lý."}

## fund-59  (Question 13.29)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9ed8f8a14122332e.png]
A newly configured PC fails to connect to the internet using TCP port 80 to www.cisco.com. Which setting must be modified for the connection to work?
- A. Subnet Mask
- B. DNS Servers
- C. Default Gateway
- D. DHCP Server
ANSWER: C
CURRENT_EXPLANATION: {"e": "Subnet là 10.2.2.0/29 (host 10.2.2.1-10.2.2.6), nhưng default gateway cấu hình là 10.2.2.10 nằm ngoài subnet nên PC không tới được gateway. Cần sửa Default Gateway về địa chỉ trong subnet (ví dụ 10.2.2.1). Mask /29 và DNS 8.8.8.8 phù hợp."}

## fund-68  (Question 14.20)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/701512b044570dba.png]
An engineer assigns IP addressing to the current VLAN with three PCs. The configuration must also account for the expansion of 30 additional VLANs using the same Class C subnet for subnetting and host count. Which command set fulfills the request while reserving address space for the expected growth?
- A. Switch(config)#interface vlan 10 Switch(config-if)#ip address 192.168.0.1 255.255.255.252
- B. Switch(config)#interface vlan 10 Switch(config-if)#ip address 192.168.0.1 255.255.255.248
- C. Switch(config)#interface vlan 10 Switch(config-if)#ip address 192.168.0.1 255.255.255.0
- D. Switch(config)#interface vlan 10 Switch(config-if)#ip address 192.168.0.1 255.255.255.128
ANSWER: B
CURRENT_EXPLANATION: {"e": "Cần subnet cho 3 PC cộng dự trữ cho 30 VLAN thêm trong cùng Class C, nên mỗi VLAN dùng subnet nhỏ: /29 (255.255.255.248, 6 host) vừa đủ 3 PC, và 256/8 = 32 subnet đủ cho 1 + 30 VLAN. /30 chỉ có 2 host usable (thiếu), còn /25 và /24 quá lớn nên không đủ chỗ cho 30 VLAN nữa."}

## fund-86  (Question 15.108)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/4a9a1188810cbd5d.png]
An engineer must add a subnet for a new office that will add 20 users to the network. Which IPv4 network and subnet mask combination does the engineer assign to minimize wasting addresses?
- A. 10.10.225.48 255.255.255.240
- B. 10.10.225.32 255.255.255.240
- C. 10.10.225.48 255.255.255.224
- D. 10.10.225.32 255.255.255.224
ANSWER: D
CURRENT_EXPLANATION: {"e": "Cần 20 host nên cần ít nhất 5 bit host: /27 (255.255.255.224, 30 host usable). Các subnet đã dùng là .0/28, .16/28 và .64/28; block 10.10.225.32/27 (.32-.63) không trùng lặp với chúng. 10.10.225.48/27 không đúng ranh giới /27 và /28 chỉ có 14 host."}

## access-5  (Question 5.15)
Refer to the exhibit. PC1 is trying to ping PC3 for the first time and sends out an ARP to S1. Which action is taken by S1?
[IMAGE: D:\CCNA_ontap\web\img/ae2b8f04a971d13c.jpeg]
- A. It forwards it out G0/3 only
- B. It is flooded out every port except G0/0
- C. It drops the frame
- D. It forwards it out interface G0/2 only
ANSWER: B
CURRENT_EXPLANATION: {"e": "ARP request là broadcast (FF:FF:FF:FF:FF:FF), nên switch flood ra mọi port cùng VLAN trừ port nhận vào (G0/0). Switch không forward broadcast tới một port cụ thể hay drop nó."}

## access-10  (Question 5.23)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5a7d5105c11d1b29.jpeg]
[TABLE]
Switch 1
VLAN 110 – 32778 0018.184e.3c00
Switch 2
VLAN 110 – 24586 001a.e3ff.a680
Switch 3
VLAN 110 – 28682 0022.55cf.cc00
Switch 4
VLAN 110 – 64000 0e38.7363.657f
[/TABLE]
Which switch becomes the root of the spanning tree for VLAN 110?
- A. Switch 1
- B. Switch 2
- C. Switch 3
- D. Switch 4
ANSWER: B
CURRENT_EXPLANATION: {"e": "Root bridge là switch có Bridge ID thấp nhất, so priority trước rồi mới tới MAC. Switch 2 có priority 24586, thấp nhất trong 32778, 24586, 28682 và 64000, nên là root của VLAN 110."}

## access-11  (Question 5.24)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ddbe446de0313a52.jpeg]
An administrator must configure interfaces Gi1/1 and Gi1/3 on switch SW11 PC-1 and PC-2 must be placed in the Data VLAN and Phone-1 must be placed in the Voice VLAN. Which configuration meets these requirements?
[TABLE]
Option A
interface gigabitethernet1/1
switchport mode access
switchport access vlan 8
!
interface gigabitethernet1/3
switchport mode access
switchport voice vlan 8
switchport access vlan 9 | Option B
interface gigabitethernet1/1
switchport mode access
switchport access vlan 9
!
interface gigabitethernet1/3
switchport mode trunk
switchport voice vlan 8
switchport access vlan 9
---
Option C
interface gigabitethernet1/1
switchport mode access
switchport access vlan 8
!
interface gigabitethernet1/3
switchport mode access
switchport access vlan 8
switchport voice vlan 9 | Option D
interface gigabitethernet1/1
switchport mode access
switchport access vlan 8
!
interface gigabitethernet1/3
switchport mode trunk
switchport voice vlan 8
switchport access vlan 9
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: C
CURRENT_EXPLANATION: {"e": "PC-1/PC-2 thuộc Data VLAN nên cổng nối PC chỉ cần `switchport mode access` + access vlan của data, còn cổng nối Phone-1 kèm PC phải là access port có `switchport access vlan` cho data và `switchport voice vlan` cho phone (khác VLAN). Option đúng là option đặt cả hai cổng ở access mode với data VLAN 8 và voice VLAN 9; các option dùng trunk hoặc đặt voice trùng data VLAN thì sai."}

## access-14  (Question 5.39)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/24db3694da6622d9.jpeg]
[IMAGE: D:\CCNA_ontap\web\img/b8c95752bfac4014.jpeg]
A network engineer must configured communication between PC A and the File Server. To prevent interruption for any other  communications, which command must be configured?
- A. Switch trunk allowed vlan 12
- B. Switchport trunk allowed vlan none
- C. Switchport trunk allowed vlan add 13
- D. Switchport trunk allowed vlan remove 10-11
ANSWER: C
CURRENT_EXPLANATION: {"e": "Để thêm VLAN cần thiết mà không ảnh hưởng các VLAN đang chạy, dùng `switchport trunk allowed vlan add 13` (thêm vào danh sách hiện có). Lệnh không có `add` sẽ ghi đè danh sách, còn `none` hay `remove 10-11` sẽ cắt các VLAN khác đang dùng."}

## access-22  (Question 6.14)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/604e00cb1ce5453e.jpeg]
Which command must be executed for Gi1/1 on SW1 to passively become a trunk port if Gi1/1 on SW2 is configured in desirable or trunk mode?
- A. switchport mode trunk
- B. switchport mode dot1-tunnel
- C. switchport mode dynamic auto
- D. switchport mode dynamic desirable
ANSWER: C
CURRENT_EXPLANATION: {"e": "Để SW1 trở thành trunk một cách thụ động (chỉ chờ đàm phán DTP), đặt `switchport mode dynamic auto`; mode auto sẽ thành trunk khi phía bên kia là desirable hoặc trunk. `dynamic desirable` là chủ động gửi DTP, `mode trunk` là cố định, `dot1q-tunnel` là QinQ."}

## access-23  (Question 6.15)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7d2dc47d1a65708b.jpeg]
An engineer must configure GigabitEthernet1/1 to accommodate voice and data traffic. Which configuration accomplishes this task?
[TABLE]
Option A
interface gigabitethernet1/1
switchport mode access
switchport access vlan 300
switchport voice vlan 400 | Option B
interface gigabitethernet1/1
switchport mode access
switchport access vlan 400
switchport voice vlan 300
---
Option C
interface gigabitethernet1/1
switchport mode trunk
switchport access vlan 300
switchport voice vlan 400 | Option D
interface gigabitethernet1/1
switchport mode trunk
switchport trunk vlan 300
switchport trunk vlan 400
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: A
CURRENT_EXPLANATION: {"e": "Cổng gắn IP phone + PC cần `switchport mode access`, `switchport access vlan 300` cho data và `switchport voice vlan 400` cho voice theo exhibit. Option đảo VLAN hoặc dùng mode trunk / `switchport trunk vlan` thì sai cú pháp hoặc sai VLAN."}

## access-25  (Question 6.19)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ee3c65e44c2fecf3.jpeg]
Only four switches are participating in the VLAN spanning-tree process.
Branch-1: priority 614440
Branch-2: priority 39082416
Branch-3: priority 0
Branch-4: root primary
Which switch becomes the permanent root bridge for VLAN 5?
- A. Branch-1
- B. Branch-2
- C. Branch-3
- D. Branch-4
ANSWER: C
CURRENT_EXPLANATION: {"e": "Root bridge là switch có priority thấp nhất; Branch-3 có priority 0 là nhỏ nhất có thể nên luôn thắng. Branch-4 dùng `root primary` chỉ hạ priority xuống khoảng 24576 (hoặc thấp hơn root hiện tại một bước) nên không thể thấp hơn 0."}

## access-26  (Question 6.20)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c66951445cdb5467.jpeg]
[IMAGE: D:\CCNA_ontap\web\img/0f6b1ea92d0577ec.jpeg]
The entire contents of the MAC address table are shown. Sales-4 sends a data frame to Sales-1. What does the switch do as it receives the frame from Sales-4?
- A. Map the Layer 2 MAC address to the Layer 3 IP address and forward the frame
- B. Insert the source MAC address and port into the forwarding table and forward the frame to Sales-1
- C. Perform a lookup in the MAC address table and discard the frame due to a missing entry
- D. Flood the frame out of all ports except on the port where Sales-1 is connected
ANSWER: B
CURRENT_EXPLANATION: {"e": "Switch học source MAC của Sales-4 (ghi MAC + port vào bảng) rồi tra MAC đích Sales-1 và forward ra đúng port. Việc ánh xạ MAC sang IP là của ARP, không phải của switch; frame không bị flood hay drop vì thiếu entry nguồn."}

## access-30  (Question 6.31)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/77af29f4314c56f5.jpeg]
How must router A be configured so that it only sends Cisco Discovery Protocol Information to router C?
[TABLE]
Option A
conf t
RouterA(config)#no cdp run
RouterA(config)#interface gi0/0/1
RouterA(config)#cdp enable | Option B
conf t
RouterA(config)#cdp run
RouterA(config)#interface gi0/0/1
RouterA(config)#cdp enable
---
Option C
conf t
RouterA(config)#cdp run
RouterA(config)#interface gi0/0/0
RouterA(config)#cdp enable | Option D
conf t
RouterA(config)#cdp run
RouterA(config)#interface gi0/0/0
RouterA(config)#no cdp enable
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: D
CURRENT_EXPLANATION: {"e": "Router A cần chạy CDP toàn cục (`cdp run`) và tắt CDP trên interface hướng tới router khác bằng `no cdp enable`, để chỉ còn gửi CDP tới router C qua interface còn lại. `no cdp run` tắt CDP hoàn toàn nên option đó sai."}

## access-38  (Question 8.5)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d000311ae63ee13c.jpeg]
Which change to the configuration on Switch2 allows the two switches to establish an EtherChannel?
- A. Change the protocol to EtherChannel mode on
- B. Change the LACP mode to active
- C. Change the LACP mode to desirable
- D. Change the protocol to PAgP and use auto mode
ANSWER: B
CURRENT_EXPLANATION: {"e": "Hai switch chỉ tạo được EtherChannel khi dùng cùng giao thức và mode tương thích: với LACP cần ít nhất một phía active. Vì Switch2 đang dùng LACP không phù hợp, đổi sang LACP active là hợp lệ (desirable thuộc PAgP, `on` không thương lượng và không ghép với LACP)."}

## access-45  (Question 8.23)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d4a50dddcaa26d3d.jpeg]
Between which zones do wireless users expect to experience intermittent connectivity?
- A. between zones 1 and 2
- B. between zones 2 and 5
- C. between zones 3 and 4
- D. between zones 3 and 6
ANSWER: C
CURRENT_EXPLANATION: {"e": "Vùng intermittent xảy ra giữa các cell/zone mà vùng phủ sóng không chồng nhau đủ, hoặc chồng lấn cùng channel; theo exhibit đó là giữa zone 3 và zone 4."}

## access-48  (Question 8.49)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3fb4c560ed8f2df2.jpeg]
An administrator must connect SW_1 and the printer to the network. SW_2 requires DTP to be used for the connection to SW_1. The printer is configured as an access port with VLAN 5. Which set of commands completes the connectivity?
- A. switchport mode trunk
switchport trunk pruning vlan add 5
- B. switchport mode dynamic desirable
switchport trunk allowed vlan add 5
- C. switchport mode dynamic auto
switchport private-vlan association host 5
- D. switchport mode dynamic auto
switchport trunk encapsulation negotiate
ANSWER: B
CURRENT_EXPLANATION: {"e": "SW_2 dùng DTP nên phải ở mode dynamic desirable (đầu kia chủ động đàm phán), và thêm VLAN 5 vào trunk bằng `switchport trunk allowed vlan add 5`. Các option dùng private-vlan, trunk pruning hay dynamic auto + encapsulation negotiate không đáp ứng yêu cầu."}

## access-49  (Question 8.53)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5c2a1a8fe0d21369.jpeg]
Host A sent a data frame destined for host D.
What does the switch do when it receives the frame from host A? 
- A. It shuts down the port Fa0/1 and places it in err-disable mode.
- B. It experiences a broadcast storm,
- C. It floods the frame out of all ports except port Fa0/1.
- D. It drops the frame from the switch CAM table.
ANSWER: C
CURRENT_EXPLANATION: {"e": "Host D chưa có trong bảng MAC (unknown unicast), nên switch flood frame ra mọi port cùng VLAN trừ Fa0/1 nơi nhận. Đây không phải broadcast storm hay err-disable."}

## access-50  (Question 8.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0ac8c70e4eb08c7e.png]
An engineer has started to configure replacement switch SW1. To verify part of the configuration, the engineer issued the commands as shown and noticed that the entry for PC2 is missing. Which change must be applied to SW1 so that PC1 and PC2 communicate normally?
- A. SW1(config)#interface fa0/2
SW1(config-if)#no switchport access vlan 2
SW1(config-if)#no switchport trunk allowed vlan 3
SW1 (config-if)#switchport trunk allowed vlan 2
- B. SW1(config)#interface fa0/1
SW1(config-if)#no switchport access vlan 2
SW1(config-if)#switchport trunk native vlan 2
SW1(config-if)#switchport trunk allowed vlan 3
- C. SW1(config-if)#interface fa0/2
SW1(config-if)#no switchport mode trunk
SW1(config-if)#no switchport trunk allowed vlan 3
SW1(config-if)#switchport mode access
- D. SW1(config)#interface fa0/1
SW1(config-if)#no switchport access vlan 2
SW1(config-if)#switchport access vlan 3
SW1(config-if)#switchport trunk allowed vlan 2
ANSWER: C
CURRENT_EXPLANATION: {"e": "PC2 không có trong bảng MAC vì cổng Fa0/2 đang cấu hình sai (trunk với allowed VLAN 3). Phải bỏ trunk, xóa allowed VLAN và đặt `switchport mode access` để cổng nối PC2 hoạt động đúng."}

## access-54  (Question 8.60)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9e50b021ea84bdab.jpeg]
Which configuration enables an EtherChannel to form dynamically between SW1 and SW2 by using an industry-standard protocol, and to support full IP connectivity between all PCs?
[TABLE]
Option A
SW1#
interface Gi0/1 
switchport
switchport mode trunk 
channel-group 1 mode on
!
interface Gi0/2 
switchport
switchport mode trunk 
channel-group 1 mode auto
SW2# 
interface Gi0/1 
switchport 
switchport mode trunk 
channel-group 1 mode auto
! 
interface Gi0/2 
switchport 
switchport mode trunk 
channel-group 1 mode on 
interface port-channel 1 
switchport 
switchport mode trunk | Option B
SW1# 
interface Gi0/1 
switchport
switchport mode trunk 
channel-group 1 mode auto
!
interface Gi0/2 
switchport 
switchport mode access
channel-group 1 mode active
SW2# 
interface gi0/1
switchport 
switchport mode access 
channel-group 1 mode desirable
!
interface Gi0/2 
switchport 
switchport mode access 
channel-group 1 mode desirable
---
Option C
SW1#
interface Gi0/1 
switchport
switchport mode trunk 
channel-group 1 mode active
!
interface Gi0/2 
switchport
switchport mode trunk 
channel-group 1 mode active
SW2# 
interface Gi0/1 
switchport 
switchport mode trunk 
channel-group 1 mode passive
! 
interface Gi0/2 
switchport 
switchport mode trunk 
channel-group 1 mode passive | Option D
SW1#
interface Gi0/1 
switchport
switchport mode access
channel-group 1 mode active
!
interface Gi0/2 
switchport
switchport mode access
channel-group 1 mode active
SW2# 
interface Gi0/1 
switchport 
switchport mode access
channel-group 1 mode desirable
! 
interface Gi0/2 
switchport 
switchport mode access
channel-group 1 mode desirable
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: C
CURRENT_EXPLANATION: {"e": "EtherChannel động dùng chuẩn mở là LACP với mode active/passive; trunk ở hai phía cho phép mọi VLAN đi qua đầy đủ nên PC liên lạc được. PAgP (desirable/auto) là Cisco proprietary, mode `on` không thương lượng, và access mode không mang nhiều VLAN."}

## access-55  (Question 8.66)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/26bc9e2bc3c006b7.png]
An engineer built a new L2 LACP EtherChannel between SW1 and SW2 and executed these show commands to verify the work. Which additional task allows the two switches to establish an LACP port channel?
- A. Change the channel-group mode on SW1 to desirable.
- B. Change the channel-group mode on SW1 to active or passive.
- C. Change the channel-group mode on SW2 to auto.
- D. Configure the interface port-channel 1 command on both switches.
ANSWER: B
CURRENT_EXPLANATION: {"e": "LACP cần ít nhất một phía ở mode active hoặc passive; nếu SW1 đang ở mode không phù hợp thì EtherChannel không lên. Đổi SW1 sang active hoặc passive sẽ cho phép LACP thương lượng với SW2 (desirable/auto là của PAgP)."}

## access-56  (Question 8.67)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ae3a0200b3bccde2.jpeg]
A network engineer must update the configuration on Switch2 so that it sends LLDP packets every minute and the information sent via LLDP is refreshed every 3 minutes. Which configuration must the engineer apply?
- A. Switch2(config)#lldp timer 60
Switch2(config)# lldp tlv-select 180
- B. Switch2(config)#lldp timer 60
Switch2(config)#lldp holdtime 180
- C. Switch2(config)#lldp timer 1
Switch2(config)#lldp tlv-select 3
- D. Switch2(config)#lldp timer 1
Switch2(config)#lldp holdtime 3
ANSWER: B
CURRENT_EXPLANATION: {"e": "`lldp timer 60` đặt chu kỳ gửi LLDP là 60 giây (1 phút), và `lldp holdtime 180` đặt thời gian thông tin còn hiệu lực là 180 giây (3 phút). Đơn vị là giây nên timer 1 hay holdtime 3 sai, còn `tlv-select` chỉ chọn TLV."}

## access-58  (Question 8.76)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f7721fd201c1f01b.jpeg]
All VLANs are present in the VLAN database. Which command sequence must be applied to complete the configuration?
- A. interface FastEthernet0/1
switchport trunk native vlan 10
switchport trunk allowed vlan 10,15
- B. interface FastEthernet0/1
switchport mode trunk
switchport trunk allowed vlan 10,15
- C. interface FastEthernet0/1
switchport trunk allowed vlan add 10
vlan 10
private-vlan isolated
- D. interface FastEthernet0/1
switchport mode access
switchport voice vlan 10
ANSWER: D
CURRENT_EXPLANATION: {"e": "Cổng nối IP phone cần `switchport mode access` kèm `switchport voice vlan 10` theo exhibit. Các option dùng trunk native/allowed, hoặc private-vlan không phù hợp với cổng access của phone."}

## access-61  (Question 9.23)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ade282f4b25b01b8.jpeg]
The link between PC1 and the switch is up, but it is performing poorly. Which interface condition is causing the performance problem?
- A. There is a duplex mismatch on the interface
- B. There is an issue with the fiber on the switch interface
- C. There is a speed mismatch on the interface
- D. There is an interface type mismatch
ANSWER: A
CURRENT_EXPLANATION: {"e": "Link up nhưng chậm, kèm collision/late collision trong exhibit, là dấu hiệu duplex mismatch (một đầu full, một đầu half). Speed mismatch thường làm link không lên."}

## access-63  (Question 9.31)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/22b5d93bad1ab37d.png]
An engineer is asked to insert the new VLAN into the existing trunk without modifying anything previously configured Which command accomplishes this task?
- A. switchport trunk allowed vlan 100-104
- B. switchport trunk allowed vlan all
- C. switchport trunk allowed vlan add 104
- D. switchport trunk allowed vlan 104
ANSWER: C
CURRENT_EXPLANATION: {"e": "Để thêm VLAN mới vào trunk mà không đổi cấu hình hiện có, dùng `switchport trunk allowed vlan add 104`. Không dùng `add` thì danh sách allowed bị thay thế, còn `all` mở thêm cả những VLAN không mong muốn."}

## access-66  (Question 9.41)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6d5584c3cbfe0571.jpeg]
Users need to connect to the wireless network with IEEE 802.11r-compatible devices. The connection must be maintained as users travel between floors or to other areas in the building. What must be the configuration of the connection?
- A. Select the WPA Policy option with the CCKM option
- B. Disable AES encryption
- C. Enable Fast Transition and select the FT 802.1x option
- D. Enable Fast Transition and select the FT PSK option
ANSWER: C
CURRENT_EXPLANATION: {"e": "Để hỗ trợ 802.11r (fast roaming) bật Fast Transition và chọn FT 802.1X khi WLAN dùng xác thực 802.1X; FT PSK dành cho mạng dùng pre-shared key. CCKM là cơ chế riêng của Cisco, không phải 802.11r."}

## access-67  (Question 9.42)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7ae2d3dd052b5b02.jpeg]
An engineer is configuring an EtherChannel using LACP between Switches 1 and 2. Which configuration must be applied so that only Switch 1 sends LACP initiation packets?
- A. Switch1(config-if)#channel-group 1 mode on
Switch2(config-if)#channel-group 1 mode passive
- B. Switch1(config-if)#channel-group 1 mode passive
Switch2(config-if)#channel-group 1 mode active
- C. Switch1(config-if)#channel-group 1 mode active
Switch2(config-if)#channel-group 1 mode passive
- D. Switch1(config-if)#channel-group 1 mode on
Switch2(config-if)#channel-group 1 mode active
ANSWER: C
CURRENT_EXPLANATION: {"e": "Chỉ Switch1 gửi LACPDU chủ động khi Switch1 để `active` và Switch2 để `passive` (passive chỉ trả lời). Mode `on` không dùng LACP, còn đặt Switch1 passive thì Switch2 active mới là bên khởi tạo."}

## access-68  (Question 9.43)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/895f1b70aa44d37b.jpeg]
[TABLE]
SW1 = 24596 0018.184e.3c00
SW2 = 28692 004a.14e5.4077
SW3 = 32788 0022.55cf.dd00
SW4 = 64000 0041.454d.407f
[/TABLE]
Which switch becomes the root of a spanning tree for VLAN 20 if all links are of equal speed?
- A. SW1
- B. SW2
- C. SW3
- D. SW4
ANSWER: A
CURRENT_EXPLANATION: {"e": "Root bridge là switch có Bridge ID thấp nhất: SW1 có priority 24596 thấp nhất trong 24596, 28692, 32788 và 64000 nên là root cho VLAN 20."}

## access-70  (Question 9.49)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/8a3a2bc610e8ab3c.jpeg]
Switch A is newly configured. All VLANs are present in the VLAN database. The IP phone and PC A on Gi0/1 must be configured for the appropriate VLANs to establish connectivity between the PCs. Which command set fulfills the requirement?
- A. SwitchA(config-if)#switchport mode access
SwitchA(config-if)#switchport access vlan 50
SwitchA(config-if)#switchport voice vlan 51
- B. SwitchA(config-if)#switchport mode access
SwitchA(config-if)#switchport access vlan 50
SwitchA(config-if)#switchport voice vlan untagged
- C. SwitchA(config-if)#switchport mode trunk
SwitchA(config-if)#switchport trunk allowed vlan add 50, 51
SwitchA(config-if)#switchport voice vlan dot1p
- D. SwitchA(config-if)#switchport mode trunk
SwitchA(config-if)#switchport trunk allowed vlan 50, 51
SwitchA(config-if)#switchport qos trust cos
ANSWER: A
CURRENT_EXPLANATION: {"e": "Cổng nối IP phone + PC dùng `switchport mode access`, `switchport access vlan 50` cho PC và `switchport voice vlan 51` cho phone. Các option dùng trunk hoặc `voice vlan untagged/dot1p` không khớp yêu cầu hai VLAN riêng biệt."}

## access-72  (Question 9.56)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f0bcd568b3510547.jpeg]
SW2 is replaced due to a hardware failure. A network engineer starts to configure SW2 by copying the Fa0/1 interface configuration from SW1. Which command must be configured on the Fa0/1 interface of SW2 to enable PC1 to connect to PC2?
- A. switchport mode trunk
- B. switchport trunk native vlan 10
- C. switchport trunk allowed remove 10
- D. switchport mode access
ANSWER: A
CURRENT_EXPLANATION: {"e": "Link giữa SW1 và SW2 phải là trunk để PC1 và PC2 liên lạc; cần `switchport mode trunk` trên Fa0/1 của SW2, giống SW1. Mode access chỉ mang một VLAN."}

## access-75  (Question 9.65)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f0d3851053e0c785.jpeg]
Which configuration establishes a Layer 2 LACP EtherChannel when applied to both switches?
- A. interface range G1/1 -1/3
switchport mode access
channel-group 1 mode passive
no shutdown
- B. interface range G1/1 -1/3
switchport mode trunk
channel-group 1 mode desirable
no shutdown
- C. interface range G1/1 -1/3
switchport mode trunk
channel-group 1 mode active
no shutdown
- D. interface range G1/1 -1/3
switchport mode access
channel-group 1 mode on
no shutdown
ANSWER: C
CURRENT_EXPLANATION: {"e": "EtherChannel LACP layer 2 cần mode LACP active (hoặc passive) và trunk để mang VLAN. Desirable là PAgP, `on` là tĩnh không dùng LACP, và passive-passive thì không phía nào khởi tạo."}

## access-76  (Question 9.85)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c71ffc6c8bb5d514.jpeg]
The following must be considered
+ SW1 is fully configured for all traffic
+ The SW4 and SW9 links to SW1 have been configured
+ The SW4 interface Gi0/1 and Gi0/0 on SW9 have been configured
+ The remaining switches have had all VLANs added to their VLAN database
Which configuration establishes a successful ping from PC2 to PC7 without interruption to traffic flow between other PCs?
[TABLE]
Option A
SW4#
interface Gi0/2
switchport mode trunk
switchport trunk allowed vlan 14,108
SW11#
interface Gi0/2
switchport mode trunk
switchport trunk allowed vlan 14,108
!
interface Gi0/1
switchport mode trunk
switchport trunk allowed vlan 14,108
SW9#
interface Gi0/2 
switchport mode trunk 
switchport trunk allowed vlan 14 | Option B
SW4
interface Gi0/7 
switchport mode trunk 
switchport trunk allowed vlan 108
!
interface Gi0/2
switchport mode access 
switchport access vlan 14
SW11#
interface Gi0/2
switchport mode trunk 
switchport trunk allowed vlan 14,108
!
interface Gi0/1
switchport mode trunk 
switchport trunk allowed vlan 14,108
SW9#
interface Gi0/2 
switchport mode access 
switchport access vlan 14
---
Option C
SW4
interface Gi0/2
switchport mode trunk 
switchport trunk allowed vlan 14
SW11#
interface Gi0/1
switchport mode trunk 
switchport trunk allowed vlan 14
SW9#
interface Gi0/2 
switchport mode trunk
switchport trunk allowed vlan 108 | Option D
SW4
interface Gi0/2
switchport mode access 
switchport access vlan 14
SW11#
interface Gi0/2
switchport mode access 
switchport access vlan 14
!
interface Gi0/0
switchport mode access 
switchport access vlan 14
!
interface Gi0/1
switchport mode trunk
SW9#
interface Gi0/2 
switchport mode access 
switchport access vlan 14
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: A
CURRENT_EXPLANATION: {"e": "Đáp ứng ping từ PC2 tới PC7 mà không ảnh hưởng traffic khác đòi hỏi các trunk giữa SW4, SW11, SW9 cho phép đúng VLAN 14 và 108. Option đúng là option cấu hình trunk với allowed VLAN 14,108 trên các link trung gian, các option khác thiếu VLAN hoặc dùng access port sai."}

## access-83  (Question 10.34)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c81c78837a75c26b.jpeg]
Clients on the WLAN are required to use 802.11r. What action must be taken to meet the requirement?
- A. Enable CCKM under Authentication Key Management
- B. Under Protected Management Frames, set the PMF option to Required
- C. Set the Fast Transition option to Enable and enable FT 802.1X under Authentication Key Management
- D. Set the Fast Transition option and the WPA gtk-randomize State to disable
ANSWER: C
CURRENT_EXPLANATION: {"e": "Để yêu cầu 802.11r, đặt Fast Transition ở Enable và bật FT 802.1X trong Authentication Key Management. CCKM, PMF Required và gtk-randomize không liên quan 802.11r."}

## access-87  (Question 10.50)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/84cfbc1b2443c905.jpeg]
An architect is managing a wireless network with APs from several branch offices connecting to the WLC in the data center. There is a new requirement for a single WLAN to process the client data traffic without sending it to the WLC. Which action must be taken to complete the request?
- A. Enable local HTTP profiling
- B. Enable FlexConnect Local Switching
- C. Enable local DHCP Profiling
- D. Enable Disassociation Imminent
ANSWER: B
CURRENT_EXPLANATION: {"e": "Để traffic của một WLAN được xử lý ở chi nhánh mà không gửi về WLC, bật FlexConnect Local Switching. HTTP/DHCP profiling và Disassociation Imminent không làm việc đó."}

## access-91  (Question 10.66)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/89833b90c7c5d573.jpeg]
The SW1 and SW2 Gi0/0 ports have been preconfigured. An engineer is given these requirements:
+ Allow all PCs to communicate with each other at Layer 3.
+ Configure untagged traffic to use VLAN 5.
+ Disable VLAN 1 from being used.
Which configuration set meets these requirements?
[TABLE]
Option A
SW1#
interface Gi0/1
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108
interface Gi0/2
switchport mode trunk
switchport trunk allowed vlan 7,9,108
SW2#
interface Gi0/1 
switchport mode trunk 
switchport trunk allowed vlan 7
interface Gi0/7
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108 | Option B
SW1#
interface Gi0/1
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108
switchport trunk native vlan 5
interface Gi0/2
switchport mode access
switchport trunk allowed vlan 7,9,108
SW2#
interface Gi0/1
switchport mode access
no switchport access vlan 1
switchport access vlan 7
interface Gi0/7
switchport mode trunk
switchport trunk allowed vlan 7,9,108
switchport trunk native vlan 5
---
Option C
SW1#
interface Gi0/1
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108
switchport trunk native vlan 5
interface Gi0/2
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108
SW2#
interface Gi0/1
switchport mode access
switchport access vlan 7
interface Gi0/7
switchport mode trunk
switchport trunk allowed vlan 7,9,108 | Option D
SW1#
interface Gi0/1
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108
switchport trunk native vlan 5
interface Gi0/2
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108
SW2#
interface Gi0/1
switchport mode access
switchport access vlan 7
interface Gi0/7
switchport mode trunk
switchport trunk allowed vlan 5,7,9,108
switchport trunk native vlan 5
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: D
CURRENT_EXPLANATION: {"e": "Option đúng cấu hình trunk có native VLAN 5 (untagged dùng VLAN 5, bỏ VLAN 1), đặt PC vào access VLAN 7 và cho phép VLAN 5,7,9,108 trên trunk giữa hai switch. Các option khác thiếu native VLAN hoặc thiếu VLAN 5 trong allowed list."}

## access-99  (Question 11.30)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0523d1251f27b52b.jpeg]
PC1 regularly sends 1800 Mbps of traffic to the server. A network engineer needs to configure the EtherChannel to disable Port Channel 1 between SW1 and SW2 when the Ge0/0 and Ge0/1 ports on SW2 go down. Which configuration must the engineer apply to the switch?
- A. SW2#configure terminal
SW2(config)# interface port-channel 1
SW2(config-if)#lacp port-priority 32000
- B. SW2#configure terminal
SW2(config)#interface port-channel 1
SW2(config-if)#lacp max-bundle 2
- C. SW2#configure terminal
SW2(config)#lacp system-priority 32000
- D. SW2#configure terminal
SW2(config)#interface port-channel 1
SW2(config-if)#port-channel min-links 2
ANSWER: D
CURRENT_EXPLANATION: {"e": "Muốn tắt Port Channel 1 khi số link hoạt động giảm xuống dưới ngưỡng, cấu hình `port-channel min-links 2` trên interface port-channel. `lacp max-bundle` và các priority không đặt ngưỡng tối thiểu."}

## access-101  (Question 11.38)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6526c366774a498c.jpeg]
An engineer is configuring a new Cisco switch NewSW, to replace SW2. Which configuration must be applied?
- A. Option A
NewSW(config)#interface f0/0
NewSW(config-if)#switchport mode trunk
NewSW(config-if)#switchport trunk allowed vlan 2,10
NewSW(config-if)#switchport trunk native vlan 2
- B. Option B
NewSW(config)#interface f0/0
NewSW(config-if)#switchport mode trunk
NewSW(config-if)#switchport trunk allowed vlan 10
NewSW(config-if)#switchport trunk native vlan 10
- C. Option C
NewSW(config)#interface f0/0
NewSW(config-if)#switchport mode access
NewSW(config-if)#switchport trunk allowed vlan 2,10
- D. Option D
NewSW(config)#interface f0/0
NewSW(config-if)#switchport mode access
NewSW(config-if)#switchport trunk allowed vlan 2,10
NewSW(config-if)#switchport trunk native vlan 10
NewSW(config-if)#switchport trunk native vlan 2
ANSWER: A
CURRENT_EXPLANATION: {"e": "NewSW thay SW2 nên cổng f0/0 phải là trunk mang cả VLAN 2 (hiện có) và VLAN 10 (mới). Native VLAN phải là 2 để khớp với cổng access VLAN 2 phía SW1 (traffic untagged của SW1 thuộc VLAN 2). Đáp án có `mode trunk`, allowed vlan 2,10 và native vlan 2 là đúng; đáp án chỉ cho phép VLAN 10 sẽ làm mất VLAN 2, còn các đáp án `switchport mode access` thì không thể mang nhiều VLAN."}

## access-103  (Question 11.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/803c0f72332c511a.jpeg]
A network engineer is configuring a WLAN to connect with the 172.16.10.0/24 network on VLAN 20. The engineer wants to limit the number of devices that connect to the WLAN on the USERWL SSID to 125. Which configuration must the engineer perform on the WLC?
- A. In the WLAN configuration, set the Maximum Allowed Clients value to 125.
- B. In the Advanced configuration, set the DTIM value to 125.
- C. In the Controller IPv6 configuration, set the Throttle value to 125.
- D. In the Management Software activation configuration, set the Clients value to 125.
ANSWER: A
CURRENT_EXPLANATION: {"e": "Giới hạn số client kết nối vào một SSID được cấu hình trong phần WLAN (tab Advanced) của WLC bằng tham số Maximum Allowed Clients = 125. DTIM chỉ liên quan đến chu kỳ beacon cho thiết bị tiết kiệm pin, Throttle của IPv6 và Software activation không giới hạn số client của WLAN."}

## access-106  (Question 11.64)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/a1c92b35f6c3f8cc.png]
The EtherChannel is configured with a speed of 1000 and duplex as full on both ends of channel group 1. What is the next step to configure the channel on switch A to respond to but not initiate LACP communication?
- A. interface range gigabitethernet0/0/0 -15
channel-group 1 mode desirable
- B. interface range gigabitethernet0/0/0 -15
channel-group 1 mode on
- C. interface port-channel 1
channel-group 1 mode auto
- D. interface port-channel 1
channel-group 1 mode passive
ANSWER: D
CURRENT_EXPLANATION: {"e": "Để switch chỉ phản hồi LACP mà không chủ động khởi tạo thì dùng mode passive của LACP (`channel-group 1 mode passive`). Các mode desirable và auto thuộc PAgP, còn mode on không dùng giao thức đàm phán nào. Lưu ý đáp án chọn có vẻ cấu hình trên port-channel nhưng ý chính là mode passive; thực tế lệnh channel-group được nhập trên interface vật lý."}

## access-118  (Question 12.48)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ea9f53807a83bf03.png]
SW_1 and SW_12 represent two companies that are merging. They use separate network vendors. The VLANs on both sides have been migrated to share IP subnets. Which command sequence must be issued on both sides to join the two companies and pass all VLANs between the companies?
- A. switchport mode trunk switchport trunk encapsulation dot1q
- B. switchport mode trunk switchport trunk allowed vlan all switchport dot1q ethertype 0800
- C. switchport mode dynamic desirable switchport trunk allowed vlan all switchport trunk native vlan 7
- D. switchport dynamic auto switchport nonegotiate
ANSWER: A
CURRENT_EXPLANATION: {"e": "Hai công ty dùng hãng khác nhau nên phải dùng trunk chuẩn mở 802.1Q: `switchport mode trunk` kèm `switchport trunk encapsulation dot1q`; mặc định trunk cho phép tất cả VLAN. ISL là độc quyền Cisco, còn các đáp án với dynamic auto/nonegotiate không tạo trunk ổn định giữa hai switch."}

## access-120  (Question 12.59)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e2fed7ac14e7f636.jpeg]
SW1 supports connectivity for a lobby conference room and must be secured. The engineer must limit the connectivity from PC1 to the SW1 and SW2 network. The MAC addresses allowed must be limited to two. Which configuration secures the conference room connectivity?
- A. interface gi1/0/15 switchport port-security switchport port-security mac-address 0000.abcd.0004 vlan 100
- B. interface gi1/0/15 switchport port-security mac-address 0000.abcd.0004 vlan 100
- C. interface gi1/0/15 switchport port-security mac-address 0000.abcd.0004 vlan 100 interface switchport secure-mac limit 2
- D. interface gi1/0/15 switchport port-security switchport port-security maximum 2
ANSWER: D
CURRENT_EXPLANATION: {"e": "Cần bật port-security trên cổng (`switchport port-security`) rồi giới hạn số MAC bằng `switchport port-security maximum 2`. Các đáp án khác thiếu một trong hai lệnh hoặc dùng lệnh không tồn tại (secure-mac limit), và chỉ khai báo một MAC tĩnh thì không giới hạn đúng 2 địa chỉ."}

## access-123  (Question 12.89)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6af3f62189e5b42c.png]
A Cisco engineer creates a new WLAN called lantest. Which two actions must be performed so that only high-speed 2.4-Ghz clients connect? (Choose two)
- A. Enable the Status option.
- B. Set the Interface/Interface Group(G) to an interface other than guest.
- C. Set the Radio Policy option to 802.11g only.
- D. Set the Radio Policy option to 802.11a only.
- E. Enable the Broadcast SSID option.
ANSWER: A, C
CURRENT_EXPLANATION: {"e": "Muốn chỉ client 2.4 GHz tốc độ cao (802.11g) kết nối thì đặt Radio Policy là 802.11g only và bật Status để WLAN hoạt động. 802.11a là băng 5 GHz nên sai; Broadcast SSID và Interface không ảnh hưởng đến yêu cầu này."}

## access-125  (Question 12.112)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/065a69260db08e10.png]
Host A switch interface is configured in VLAN 2. Host D sends a unicast packet destined for the IP address of host A.
Sw1#show mac-address table
Mac Address Table
-----------------------------
Vlan   Mac Address     Type    Ports
----   -----------     ------- ----
2      000c.859c.bb7b  DYNAMIC e0/1
3      000c.85dc.bb7b  DYNAMIC e0/1
2      0010.11dc.3e91  DYNAMIC e0/2
3      0010.11dC.3e91  DYNAMIC e0/2
2      0044.42d9.c693  DYNAMIC e0/3
Sw1#
What does the switch do when it receives the frame from host D?
- A. It floods the frame out of every port except the source port.
- B. It shuts down the source port and places It in err-disable mode.
- C. It drops the frame from the MAC table of the switch.
- D. It creates a broadcast storm.
ANSWER: A
CURRENT_EXPLANATION: {"e": "Bảng MAC cho VLAN 2 không có địa chỉ đích (host A) nên là unknown unicast; switch flood frame ra mọi cổng thuộc VLAN đó trừ cổng nguồn. Switch không đưa cổng vào err-disable và không tạo broadcast storm trong tình huống này."}

## access-127  (Question 13.6)
Refer to Exhibit.
[IMAGE: D:\CCNA_ontap\web\img/74683b1773099bcf.png]
An engineer is building a new Layer 2 LACP EtherChannel between SW1 and SW2. and they executed the given show commands to verify the work. Which additional task must be performed so that the switches successfully bundle the second member in the LACP port-channel?
- A. Configure the switchport trunk allowed vlan 300 command on SW1 port-channel 1
- B. Configure the switchport trunk allowed vlan 300 command on interface Fa0/2 on SW1
- C. Configure the switchport trunk allowed vlan add 300 command on interface Fa0/2 on SW2
- D. Configure the switchport trunk allowed vlan add 300 command on SW1 port-channel 1
ANSWER: D
CURRENT_EXPLANATION: {"e": "Fa0/2 trên SW1 chỉ cho phép VLAN 100,200 trong khi Fa0/1 cho phép 100,200,300 nên cấu hình hai member không đồng nhất, port thứ hai không thể bundle vào LACP. Cần thêm VLAN 300 bằng `switchport trunk allowed vlan add 300` (dùng từ khóa add để không ghi đè các VLAN hiện có); cấu hình trên port-channel sẽ được áp xuống các member. Lệnh `allowed vlan 300` không có add sẽ ghi đè danh sách chỉ còn VLAN 300.", "warn": "Cách sửa chuẩn là thêm VLAN 300 trực tiếp trên interface Fa0/2 của SW1; đáp án này cấu hình trên port-channel 1 vẫn hoạt động vì được áp xuống member, và là đáp án đúng trong các lựa chọn."}
