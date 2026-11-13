## access-129  (Question 13.28)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0ba81d872ef100b0.png]
Which switch becomes the root bridge?
- A. SW 1 Bridge Priority – 32768 mac-address 0f:d7:9e:13:ab:82
- B. SW 4 Bridge Priority – 40960 mac-address 05:d8:33:09:8f:89
- C. SW3 Bridge Priority – 32768 mac-address 01:1c:6c:66:b7:70
- D. SW2 Bridge Priority – 40960 mac-address 04:44:97:51:63:17
ANSWER: C
CURRENT_EXPLANATION: {"e": "Root bridge là switch có Bridge ID thấp nhất (priority trước, rồi tới MAC). SW1 và SW3 cùng priority 32768 thấp hơn 40960 của SW2/SW4; giữa SW1 và SW3 thì MAC 01:1c:6c:66:b7:70 của SW3 nhỏ hơn 0f:d7:9e:13:ab:82 nên SW3 là root."}

## access-132  (Question 13.48)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/bda094608c65dfc2.png]
The P2P Blocking Action option is disabled on the WLC. The security team has a new requirement for each client to retain their assigned IP addressing as the clients move between locations in the campus network. Which action completes this configuration?
- A. Set the P2P Blocking Action option to Forward-UpStream.
- B. Enable the Static IP Tunneling option.
- C. Check the DHCP Addr. Assignment check box.
- D. Disable the Coverage Hole Detection option.
ANSWER: B
CURRENT_EXPLANATION: {"e": "Yêu cầu client giữ nguyên IP khi di chuyển giữa các vị trí trong campus ứng với tính năng Static IP Tunneling (hỗ trợ client dùng IP tĩnh roaming giữa các subnet/controller). P2P Blocking, DHCP Addr. Assignment và Coverage Hole Detection không liên quan đến việc giữ IP khi roaming."}

## access-139  (Question 13.82)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/4f6a180293dcaf89.jpeg]
Which set of commands must be applied to the two switches to configure an LACP Layer 2 EtherChannel?
[TABLE]
Option A
SW1(config)#interface range f0/13 -14
SW1(config-if-range)#channel-group 1 mode desirable
SW2(config)#interface range f0/13 -14
SW2(config-if-range)#channel-group 1 mode passive | Option B
SW1(config)#interface range f0/13 -14
SW1(config-if-range)#channel-group 1 mode on
SW2(config)#interface range f0/13 -14
SW2(config-if-range)#channel-group 1 mode passive
---
Option C
SW1(config)#interface range f0/13 -14
SW1(config-if-range)#channel-group 1 mode active
SW2(config)#interface range f0/13 -14
SW2(config-if-range)#channel-group 1 mode passive | Option D
SW1(config)#interface range f0/13 -14
SW1(config-if-range)#channel-group 1 mode auto
SW2(config)#interface range f0/13 -14
SW2(config-if-range)#channel-group 1 mode passive
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: C
CURRENT_EXPLANATION: {"e": "LACP dùng mode active và passive, và ít nhất một bên phải là active: active-passive hình thành channel. Desirable/auto là PAgP, `mode on` là static (không tương thích với passive), và auto không chạy cùng passive của LACP."}

## access-140  (Question 13.91)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e743f28b846f3241.png]
An engineer configures interface fa0/1 on SW1 and SW2 to pass traffic from two different VLANs. For security reasons, company policy requires the native VLAN to be set to a nondefault value. Which configuration meets this requirement?
[TABLE]
Option A
Switch(config-if)#switchport mode dynamic
Switch(config-if}#switchport access vlan 100,105
Switch(config-if)#switchport trunk native vlan 1 | Option B
Switch(config-if)#switchport mode access
Switch(config-if)#switchport trunk encapsulation dot1q
Switch(config-if)#switchport access vlan 100.105
Switch(config-if)#switchport trunk native vlan 3
---
Option C
Switch(config-if)#switchport mode trunk
Switch(config-if)# switch port trunk encapsulation isl
Switch(config-if)#switchport trunk allowed vlan 100,105
Switch(config-if)#s witch port trunk native vlan 1 | Option D
Switch(config-if)#switchport mode trunk
Switch(config-if)#switchport trunk encapsulation dot1q
Switch(config-if)#switchport trunk allowed vlan 100,105
Switch(config if)#switchport trunk native vlan 3
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: D
CURRENT_EXPLANATION: {"e": "Cần trunk để mang hai VLAN, dùng dot1q, allowed VLAN 100,105 và native VLAN khác giá trị mặc định (native vlan 3). Đáp án dùng native VLAN 1 vi phạm yêu cầu nondefault, đáp án dùng ISL không phải chuẩn/không đồng bộ, và đáp án `mode access` không thể mang hai VLAN."}

## access-145  (Question 14.5)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/a9a8442b80343a6e.png]
Which switch becomes the root bridge?
- A. SW 1 Bridge Priority – 28672 mac-address 00:10:a1:51:57:51
- B. SW 2 Bridge Priority – 28672 mac-address 00:10:a1:82:03:94
- C. SW3 Bridge Priority – 12288 mac-address 00:10:a1:95:2b:77
- D. SW4 Bridge Priority – 12288 mac-address 00:10:a1:03:42:e8
ANSWER: D
CURRENT_EXPLANATION: {"e": "Root bridge là switch có Bridge ID nhỏ nhất. SW3 và SW4 cùng priority 12288 (thấp hơn 28672), nên so sánh MAC: 00:10:a1:03:42:e8 của SW4 nhỏ hơn 00:10:a1:95:2b:77 của SW3, nên SW4 là root bridge."}

## access-157  (Question 14.40)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0a4de83282044a4e.png]
A Cisco WLC administrator is creating a new wireless network with enhanced SSID security. The new network must operate at 2.4 GHz with 54 Mbps of throughput. Which set of tasks must the administrator perform to complete the configuration?
- A. Check the Broadcast SSID check box and set the Radio Policy to 802.11a only.
- B. Uncheck the Broadcast SSID check box and set the Radio Policy to 802.11a/g only.
- C. Check the Broadcast SSID check box and set the Radio Policy to 802.11g only.
- D. Uncheck the Broadcast SSID check box and set the Radio Policy to 802.11g only.
ANSWER: D
CURRENT_EXPLANATION: {"e": "2.4 GHz với tốc độ 54 Mbps là 802.11g, nên Radio Policy phải là 802.11g only. 'Enhanced SSID security' ở đây nghĩa là ẩn SSID bằng cách bỏ chọn Broadcast SSID. 802.11a là băng 5 GHz, nên sai."}

## access-160  (Question 14.53)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3a8e4cb5e526bab0.png]
Rapid PVST+ mode is on the same VLAN on each switch. Which switch becomes the root bridge and why?
- A. SW3, because its priority is the highest
- B. SW2, because its MAC address is the highest
- C. SW4, because its priority is highest and its MAC address is lower
- D. SW1, because its priority is the lowest and its MAC address is higher
ANSWER: C
CURRENT_EXPLANATION: {"e": "Root bridge là switch có Bridge ID thấp nhất. SW1 và SW4 cùng priority thấp nhất là 8192; MAC của SW4 (00:24:98:6f:3b:40) nhỏ hơn SW1 (...3b:41), nên SW4 là root.", "warn": "Đáp án đúng là SW4 nhưng câu chữ 'priority is highest' sai về thuật ngữ: thực tế priority của SW4 thấp nhất (8192) cùng với MAC thấp hơn; vẫn chọn SW4."}

## access-166  (Question 14.91)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7bb8803adce3c0dc.png]
The LACP EtherChannel is configured, and the last change is to modify the interfaces on SwitchA to respond to packets received, but not to initiate negotiation. The interface range gigabitethernet0/0/0-15 command is entered. What must be configured next?
- A. SwitchA(config-if-range)#channel-group 1 mode desirable
- B. SwitchA(config-if-range)#channel-group 1 mode passive
- C. SwitchA(config-if-range)#channel-group 1 mode auto
- D. SwitchA(config-if-range)#channel-group 1 mode active
ANSWER: B
CURRENT_EXPLANATION: {"e": "Để switch chỉ phản hồi chứ không khởi tạo đàm phán LACP thì cấu hình `channel-group 1 mode passive`. Active chủ động khởi tạo, còn desirable/auto thuộc PAgP."}

## access-170  (Question 14.102)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/2e6f22c65be76e6f.png]
Which configuration enables SW2 to establish an LACP EtherChannel?
[TABLE]
Option A
SW2(config)#interface gigabitEthernet0/1
SW2(config-if)#channel-group 2 mode desirable
SW2(config-if)#interface gigabitEthernet0/2
SW2(config-if)#channel-group 2 mode desirable | Option B
SW2(config)#interface gigabitEthernet0/1
SW2(config-if)#channel-group 1 mode active
SW2(config-if)#interface gigabitEthernet0/2
SW2(config-if)#channel-group 1 mode active
---
Option C
SW2(config)#interface gigabitEthernet0/1
SW2(config-if)#channel-group 1 mode on
SW2(config-if)#interface glgabitEthernet0/2
SW2(config-if)#channel-group 1 mode on | Option D
SW2(config interface gigabitEthernet0/1
SW2(config-if)#channel-group 2 mode auto
SW2(config-if)#interface gigabitEthernet0/2
SW2(config-if)#channel-group 2 mode auto
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B
CURRENT_EXPLANATION: {"e": "Để SW2 tạo LACP EtherChannel với SW1 thì dùng mode active (hoặc passive) trên cả hai cổng với channel-group trùng với phía đối diện. Desirable/auto là PAgP và `mode on` là static; đáp án đúng dùng channel-group 1 mode active cho hai cổng Gi0/1 và Gi0/2."}

## access-171  (Question 15.7)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/2010f5d15b6efb65.png]
Which switch in this configuration will be elected as the root bridge?
- A. SW1: 0C:4A:82.:65:62:72
- B. SW2: 0C:0A:A8:1A:3C:9D
- C. SW3: 0C:0A:18:81:B3:19
- D. SW4: 0C:0A:05:22:05:97
ANSWER: D
CURRENT_EXPLANATION: {"e": "Cả SW3 và SW4 có priority thấp nhất là 4096. Khi priority bằng nhau, switch có MAC thấp nhất thắng: SW4 (0C:0A:05:22:05:97) thấp hơn SW3 (0C:0A:18:81:B3:19), nên SW4 là root bridge."}

## access-172  (Question 15.11)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/dd668a5810a1dd96.png]
Which switch in this configuration will be elected as the root bridge?
SW1 0С:0A:05:22:05:97
SW2 0С:4A:82:07:57:58
SW3 0C:0A:A8:1A:3C:9D
SW4 0С:0A:18:A1:B3:19
- A. SW1
- B. SW2
- C. SW3
- D. SW4
ANSWER: D
CURRENT_EXPLANATION: {"e": "SW3 và SW4 cùng priority thấp nhất là 8192. So sánh MAC: 0C:0A:18:A1:B3:19 của SW4 nhỏ hơn 0C:0A:A8:1A:3C:9D của SW3, nên SW4 là root bridge."}

## access-173  (Question 15.25)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7dd178db7a26f0be.png]
Which switch in this configuration will be elected as the root bridge?
SW1 0С:B4:86:22:42:37
SW2 0С:0B:15:22:05:97
SW3 0C:0B:15:1A:3C:9D
SW4 0С:B0:18:A1:B3:19
- A. SW1
- B. SW2
- C. SW3
- D. SW4
ANSWER: C
CURRENT_EXPLANATION: {"e": "SW3 và SW4 có priority 4096 (thấp nhất). So sánh MAC: SW3 0C:0B:15:1A:3C:9D nhỏ hơn SW4 0C:B0:18:A1:B3:19 (byte thứ hai 0B < B0), nên SW3 là root bridge."}

## access-174  (Question 15.26)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/96387f7de9258e9a.png]
Which switch in this configuration will be elected as the root bridge?
SW1 0С:E4:85:71:03:80
SW2 0С:0E:1A:22:05:97
SW3 0C:E0:A1:1A:3C:9D
SW4 0С:00:18:A1:B3:19
- A. SW1
- B. SW2
- C. SW3
- D. SW4
ANSWER: B
CURRENT_EXPLANATION: {"e": "SW2 có priority thấp nhất là 4096 nên là root bridge, không cần so sánh MAC."}

## access-182  (Question 16.1)
Refer to the exhibit.
SW1#
Name: Et0/0
Switchport: Enabled
Administrative Node: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Administrative Native VLAN tagging: enabled
Voice VLAN: none
Administrative private-vlan host-association: none
Administrative private-vlan mapping: none
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private—vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 1,22
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL
[IMAGE: D:\CCNA_ontap\web\img/3ccd9a207dfdd133.png]
VLAN 23 is being implemented between SW1 and SW2. The command show interface ethernet0/0 switchport has been issued on SW1. Ethernet0/0 on SW1 is the uplink to SW2. Which command when entered on the uplink interface allows PC 1 and PC 2 to communicate without impact to the communication between PC 11 and PC 12?
- A. switchport trunk allowed vlan 2-1001
- B. switchport trunk allowed vlan add 23
- C. switchport trunk allowed vlan 23
- D. switchport trunk allowed vlan 22-23
ANSWER: B
CURRENT_EXPLANATION: {"e": "Uplink hiện chỉ cho phép VLAN 1,22. Để thêm VLAN 23 mà không ảnh hưởng VLAN 22 cần `switchport trunk allowed vlan add 23`. Các lệnh không có add sẽ ghi đè danh sách và làm mất VLAN 1/22."}

## access-186  (Question 16.19)
What is a characteristic of an SSID in wireless networks?
[IMAGE: D:\CCNA_ontap\web\img/1918cdc3d161fe63.jpeg]
[TABLE]
R1
interface Ethernet0/0
no ip address | SW1:
interface Ethernet0/0
switchport trunk encapsulation dot1q
switchport mode trunk
!
interface Ethernet0/1
switchport trunk allowed vlan 10
switchport trunk encapsulation dot1q
switchport mode trunk | SW2:
interface Ethernet0/1
switchport trunk encapsulation dot1q
switchport mode trunk
!
interface Ethernet0/2
switchport access vlan 20
switchport mode access
[/TABLE]
- A. provides protection against spyware
- B. used to identify a Wireless LAN Controller
- C. enables wireless clients to connect to a specific network
- D. the password used to connect to an access point
ANSWER: C
CURRENT_EXPLANATION: {"e": "SSID cho phép client không dây kết nối tới một mạng không dây cụ thể. Nó không phải mật khẩu, không bảo vệ chống spyware và không định danh WLC."}

## ipsvc-4  (Question 5.25)
Refer to exhibit.
[IMAGE: D:\CCNA_ontap\web\img/1df4ad44541e44e2.jpeg]
Which configuration must be applied to the router that configures PAT to translate all addresses in VLAN 200 while allowing devices on VLAN 100 to use their own IP addresses?
[TABLE]
Option A
Router1(config)#access-list 99 permit 209.165.201.2 0.0.0.0
Router1(config)#ip nat inside source list 99 interface gi1/0/0 overload
Router1(config)#interface gi2/0/1.200
Router1(config)#ip nat inside
Router1(config)#interface gi1/0/0
Router1(config)#ip nat outside | Option B
Router1(config)#access-list 99 permit 209.165.201.2 255.255.255.255
Router1(config)#ip nat inside source list 99 interface gi1/0/0 overload
Router1(config)#interface gi2/0/1.200
Router1(config)#ip nat inside
Router1(config)#interface gi1/0/0
Router1(config)#ip nat outside
---
Option C
Router1(config)#access-list 99 permit 192.168.100.0 0.0.0.255
Router1(config)#ip nat inside source list 99 interface gi1/0/0 overload
Router1(config)#interface gi2/0/1.200
Router1(config)#ip nat inside
Router1(config)#interface gi1/0/0
Router1(config)#ip nat outside | Option D
Router1(config)#access-list 99 permit 192.168.100.32 0.0.0.31
Router1(config)#ip nat inside source list 99 interface gi1/0/0 overload
Router1(config)#interface gi2/0/1.200
Router1(config)#ip nat inside
Router1(config)#interface gi1/0/0
Router1(config)#ip nat outside
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: D
CURRENT_EXPLANATION: {"e": "VLAN 200 dùng subnet 192.168.100.32/27, nên ACL phải permit đúng dải đó với wildcard 0.0.0.31 để chỉ PAT cho VLAN 200. VLAN 100 (192.168.100.0/27) không nằm trong ACL nên không bị NAT và giữ nguyên địa chỉ của mình. Các đáp án còn lại permit địa chỉ public 209.165.201.2 hoặc cả dải 192.168.100.0/24 (bao gồm cả VLAN 100), đều sai yêu cầu."}

## ipsvc-7  (Question 5.38)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/8e8a3ffa014021f6.jpeg]
The ntp server 192.168.0.3 command has been configured on Router1 to make it an NTP client of router 2. Which command must be configured on Router2 so that it operates in server-only mode and relies only on its internal clock?
- A. Router2(config)#ntp passive
- B. Router2(config)#ntp master 4
- C. Router2(config)#ntp server 172.17.0.1
- D. Router2(config)#ntp server 192.168.0.2
ANSWER: B
CURRENT_EXPLANATION: {"e": "Lệnh `ntp master <stratum>` biến Router2 thành NTP server dựa vào đồng hồ nội bộ (không đồng bộ từ nguồn ngoài), nên đáp án `ntp master 4` đúng. `ntp server` chỉ làm Router2 thành client của nguồn khác, `ntp passive` chỉ là chế độ của association symmetric. Ngoài ra 172.17.0.1 là loopback của chính Router2 nên không dùng làm server được."}

## ipsvc-21  (Question 8.36)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0afc6c998d119de6.jpeg]
The DHCP server and clients are connected to the same switch. What is the next step to complete the DHCP configuration to allow clients on VLAN 1 to receive addresses from the DHCP server?
- A. Configure the ip dhcp snooping trust command on the interface that is connected to the DHCP server
- B. Configure the ip dhcp relay information option command on the interface that is connected to the DHCP server
- C. Configure the ip dhcp relay information option command on the interface that is connected to the DHCP client
- D. Configure the ip dhcp snooping trust command on the interface that is connected to the DHCP client
ANSWER: A
CURRENT_EXPLANATION: {"e": "Khi bật DHCP snooping, mọi cổng mặc định là untrusted và sẽ chặn DHCPOFFER/ACK đến từ cổng đó. Vì vậy cần cấu hình `ip dhcp snooping trust` trên interface nối tới DHCP server để cho phép phản hồi của server đi qua tới client. Server và client cùng switch/VLAN nên không cần relay (`ip dhcp relay information option` không giải quyết vấn đề này)."}

## ipsvc-23  (Question 8.74)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/a7444ab5f589a4bb.jpeg]
How should the configuration be updated to allow PC1 and PC2 access to the Internet?
- A. Modify the configured number of the second access list
- B. Remove the overload keyword from the ip nat inside source command
- C. Add either the ip nat {inside|outside} command under both interfaces
- D. Change the ip nat inside source command to use interface GtgabitEthernet0/0
ANSWER: C
CURRENT_EXPLANATION: {"e": "Cấu hình đã có `ip nat inside source` và ACL nhưng chưa đánh dấu interface nào là inside hay outside, nên NAT không hoạt động. Cần thêm `ip nat inside` trên interface hướng PC và `ip nat outside` trên interface hướng Internet. Overload và ACL số 1 đã đúng, và việc dùng interface GigabitEthernet0/1 (outside) là hợp lý."}

## ipsvc-27  (Question 9.26)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/998d1b383987e8e7.jpeg]
An engineer is configuring a new router on the network and applied this configuration. Which additional configuration allows the PC to obtain its IP address from a DHCP server?
- A. Configure the ip dhcp relay information command under interface Gi0/1
- B. Configure the ip dhcp smart-relay command globally on the router
- C. Configure the ip helper-address 172.16.2.2 command under interface Gi0/0
- D. Configure the ip address dhcp command under interface Gi0/0
ANSWER: C
CURRENT_EXPLANATION: {"e": "PC kết nối Gi0/0 và DHCP server ở subnet khác (172.16.2.2), nên cần relay: `ip helper-address 172.16.2.2` trên interface phía client (Gi0/0) để chuyển broadcast thành unicast tới server. `ip address dhcp` làm router thành client, `smart-relay` và `relay information` không phải điều kiện cơ bản để relay hoạt động."}

## ipsvc-29  (Question 9.44)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/80f4e920ef0f613d.jpeg]
[TABLE]
Router1(config)#interface GigabitEthernet0/0 
Router1(config-if)#ip address 209.165.200.225 255.255.255.224 
Router1(config-if)#ip nat outside 
Router1(config)#interface GigabitEthernet0/1 
Router1(config-if)#ip nat inside 
Router1(config)#interface GigabitEthernet
Router1(config-if)#encapsulation dot1Q 100 
Router1(config-if)#ip address 10.10.10.1 255.255.255.0
Router1(config)#interface GigabitEthernet0/1.200 
Router1(config-if)#encapsulation dot1Q 200
Router1(config-if)#ip address 10.10.20.1 255.255.255.0 
Router1(config)#ip access-list standard NAT_INSIDE_RANGES 
Router1(config-std-nacl)#permit 10.10.10.0 0.0.0.255
Router1(config)#ip nat inside source list NAT_INSIDE_RANGES interface GigabitEthernet0/0 overload
[/TABLE]
Users on existing VLAN 100 can reach sites on the Internet. Which action must the administrator take to establish connectivity to the Internet for users in VLAN 200?
- A. Define a NAT pool on the router.
- B. Update the NAT_INSIDE_RANGES ACL
- C. Configure the ip nat outside command on another interface for VLAN 200
- D. Configure static NAT translations for VLAN 200
ANSWER: B
CURRENT_EXPLANATION: {"e": "NAT overload dùng ACL NAT_INSIDE_RANGES để xác định địa chỉ nào được dịch, hiện chỉ permit 10.10.10.0/24 (VLAN 100). Cần cập nhật ACL thêm `permit 10.10.20.0 0.0.0.255` cho VLAN 200. Interface inside/outside đã đặt đúng (subinterface của Gi0/1 nằm trong inside), không cần pool hay static NAT."}

## ipsvc-39  (Question 10.78)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/affcc64df668a7e6.jpeg]
Which command set configures ROUTER-1 to allow Internet access for users on the 192.168.1.0/24 subnet while using 209.165.202.129 for Port Address Translation?
- A. ip nat pool CCNA 192.168.0.0 192.168.1.255 netmask 255.255.255.0
access-list 10 permit 192.168.0.0 0.0.0.255
ip nat inside source list 10 pool CCNA overload
- B. ip nat pool CCNA 209.165.202.129 209.165.202.129 netmask 255.255.255.255
access-list 10 permit 192.168.1.0 255.255.255.0
ip nat inside source list 10 pool CCNA overload
- C. ip nat pool CCNA 192.168.0.0 192.168.1.255 netmask 255.255.255.0
access-list 10 permit 192.168.0.0 255.255.255.0
ip nat inside source list 10 pool CCNA overload
- D. ip nat pool CCNA 209.165.202.129 209.165.202.129 netmask 255.255.255.255
access-list 10 permit 192.168.1.0 0.0.0.255
ip nat inside source list 10 pool CCNA overload
ANSWER: D
CURRENT_EXPLANATION: {"e": "PAT dùng đúng một địa chỉ 209.165.202.129 nên pool chỉ chứa 1 IP (netmask 255.255.255.255), kèm `overload`. ACL phải permit 192.168.1.0 với wildcard mask 0.0.0.255 (ACL dùng wildcard, không dùng subnet mask). Các đáp án khác dùng pool private 192.168.0.0 sai hoặc dùng mask 255.255.255.0 trong ACL."}

## ipsvc-50  (Question 12.62)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/99789725229275d6.png]
The DHCP server is configured with a DHCP pool for each of the subnets represented. Which command must be configured on switch SW1 to allow DHCP clients on VLAN 10 to receive dynamic IP addresses from the DHCP server?
- A. SW1(config-if)#ip helper-address 192.168.10.2
- B. SW1(config-if)#ip helper-address 192.168.20.1
- C. SW1(config-if)#ip helper-address 192.168.20.2
- D. SW1(config-if)#ip helper-address 192.168.10.1
ANSWER: C
CURRENT_EXPLANATION: {"e": "DHCP server nằm ở VLAN 20 (192.168.20.2), còn client ở VLAN 10, nên SW1 phải relay: đặt `ip helper-address 192.168.20.2` trên SVI VLAN 10. Địa chỉ trỏ tới là IP của DHCP server chứ không phải gateway của VLAN."}

## ipsvc-62  (Question 14.16)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c808af92088ac28c.png]
Which per-hop QoS behavior is R1 applying to incoming packets?
- A. queuing
- B. marking
- C. shaping
- D. policing
ANSWER: A
CURRENT_EXPLANATION: {"e": "Hình cho thấy gói vào Gi0/0 theo thứ tự AF31, AF21, AF11 nhưng ra Gi0/1 theo thứ tự đã được sắp xếp lại; marking vẫn giữ nguyên (AF vẫn là AF). Nghĩa là R1 đang áp dụng queuing (scheduling theo class), không phải marking hay policing/shaping."}

## ipsvc-95  (Question 16.56)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5a43c8fa1cdfd526.png]
HQC needs to use a configuration that:
Handles up to 150,000 concurrent connections
Minimizes consumption of public IP addresses
Which configuration meets the requirements?
- A. ip nat pool NATPOOL 209.165.201.1 209.165.201.5 netmask 255.255.255.248 ip nat inside source list HQC interface gigabitEthernet0/0 overload
- B. ip nat pool NATPOOL 209.165.200.225 209.165.200.226 netmask 255.255.255.252 ip nat outside source list HQC pool NATPOOL overload
- C. ip nat pool NATPOOL 209.165.201.1 209.165.201.3 netmask 255.255.255.248 ip nat inside source list HQC pool NATPOOL overload
- D. ip nat pool NATPOOL 209.165.201.1 209.165.201.248 netmask 255.255.255.248 ip nat outside source list HQC pool NATPOOL overload
ANSWER: C
CURRENT_EXPLANATION: {"e": "150,000 kết nối đồng thời cần nhiều port: mỗi IP public có khoảng 64k port nên cần ít nhất 3 địa chỉ (3 IP cho khoảng 196k port). Dùng pool 3 địa chỉ 209.165.201.1-.3 với `ip nat inside source list HQC pool NATPOOL overload` vừa đủ lại tiết kiệm IP public nhất. Pool 5 địa chỉ dùng thừa, còn `outside source` là sai hướng NAT."}

## ipsvc-97  (Question 16.64)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9fec119f7a8438bc.png]
A network engineer must configure the CPE router to allow computers in the 172.20.1.0/24 network to obtain their IP configurations from the central DHCP server. Which configuration must the engineer apply to the CPE?
- A. interface GigabitEthernet0/1 ip helper-address 172.20.255.11
- B. interface GigabitEthernet0/0 ip helper-address 172.20.255.1
- C. interface GigabitEthernet0/0 ip helper-address 172.20.1.1
- D. interface GigabitEthernet0/1 ip helper-address 172.20.254.1
ANSWER: A
CURRENT_EXPLANATION: {"e": "Máy tính ở mạng 172.20.1.0/24 nối với g0/1 của CPE, còn DHCP server là 172.20.255.11, nên cần `ip helper-address 172.20.255.11` trên g0/1 (interface phía client) để relay broadcast tới server. Các đáp án khác đặt trên g0/0 hoặc trỏ tới địa chỉ không phải server."}

## sec-3  (Question 5.13)
Refer to the exhibit. A network administrator has been tasked with securing VTY access to a router. Which access-list entry accomplishes this task?
[IMAGE: D:\CCNA_ontap\web\img/56d951323eae161c.jpeg]
- A. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq ssh
- B. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq scp
- C. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq telnet
- D. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq https
ANSWER: A
CURRENT_EXPLANATION: {"e": "Exhibit cho thấy ACL 101 áp dụng inbound trên Ethernet0/0 với các dòng cho phép routing/VPN, còn quản trị từ xa tới router chỉ nên dùng giao thức an toàn. Dòng cho phép TCP port 22 (`eq ssh`) từ mạng 10.1.1.0/24 tới 172.16.1.0/24 là cách bảo mật VTY bằng SSH (mã hóa). Telnet gửi clear-text nên không an toàn, `scp` không phải tên port TCP hợp lệ trong ACL và HTTPS (443) không phải dịch vụ VTY."}

## sec-4  (Question 5.29)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/cf836738e7a7d595.jpeg]
[TABLE]
Option A
ip access-list standard 99
permit 10.100.100.0 0.0.0.255
deny 192.168.0.0 0.0.255.255 | Option B
ip access-list standard 99
permit 10.100.100.0 0.0.0.255
deny 192.168.0.0 0.255.255.255
---
Option C
ip access-list standard 100
permit 10.100.100.0 0.0.0.255
deny 192.168.0.0 0.255.255.255 | Option D
ip access-list standard 199
permit 10.100.100.0 0.0.0.255
deny 192.168.0.0 0.0.255.255
[/TABLE]
An access list is required to permit traffic from any host on interface G0/0 and deny traffic from interface Gi0/1. Which access list must be applied?
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: A
CURRENT_EXPLANATION: {"e": "Cần permit mạng 10.100.100.0/24 (cổng Gi0/0) và deny mạng 192.168.0.0/16 (cổng Gi0/1). Wildcard mask của /24 là 0.0.0.255 và của /16 là 0.0.255.255, nên đáp án dùng `permit 10.100.100.0 0.0.0.255` và `deny 192.168.0.0 0.0.255.255` với standard ACL số 99 là đúng. Đáp án dùng wildcard 0.255.255.255 sẽ khớp cả /8; ACL số 100 và 199 thuộc dải extended nên không dùng được với cú pháp standard này."}

## sec-23  (Question 8.34)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f0aa37bc4c69de1b.jpeg]
Refer to the exhibit. The access list denies Telnet access from PC-1 to RTR-1 and should allow it from other hosts. PC-2 gets “% Connection refused by remote host” when trying to Telnet. Without permitting Telnet from PC-1, what must be done to allow the traffic?
- A. Add the access-list 10 permit any command to the configuration
- B. Remove the access-class 10 in command from line vty 0 4.
- C. Add the ip access-group 10 out command to interface g0/0.
- D. Remove the password command from line vty 0 4.
ANSWER: A
CURRENT_EXPLANATION: {"e": "Access-list 10 chỉ có `deny host 10.150.1.1` và có implicit deny any ở cuối, nên PC-2 cũng bị chặn khi Telnet qua `access-class 10 in`. Thêm `access-list 10 permit any` sẽ cho phép các host còn lại mà vẫn chặn PC-1. Gỡ access-class sẽ cho cả PC-1 vào, còn `ip access-group` trên g0/0 và password command không giải quyết vấn đề này."}

## sec-26  (Question 8.55)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/5501098792100671.jpeg]
Which two commands must be configured on router R1 to enable the router to accept secure remote-access connections? (Choose two)
- A. transport input telnet
- B. username cisco password 0 cisco
- C. login console
- D. ip ssh pubkey-chain
- E. crypto key generate rsa
ANSWER: B, E
CURRENT_EXPLANATION: {"e": "Để router nhận kết nối từ xa an toàn (SSH) cần tạo user cục bộ (`username cisco password 0 cisco`) cho `login local` và tạo khóa bằng `crypto key generate rsa`. `transport input telnet` là không an toàn, `login console` không dùng cho remote và `ip ssh pubkey-chain` chỉ dùng cho xác thực bằng khóa công khai."}

## sec-39  (Question 9.40)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/73c0c289d0e3928e.jpeg]
Which minimum configuration items are needed to enable Secure Shell version 2 access to R15?
- A. Router(config)#hostname R15
R15(config)#crypto key generate rsa general-keys modulus 1024
R15(config-line)#line vty 0 15
R15(config-line)# transport input ssh
R15(config)#ip ssh source-interface Fa0/0
R15(config)#ip ssh stricthostkeycheck
- B. Router(config)#ip domain-name cisco.com
Router(config)#crypto key generate rsa general-keys modulus 1024
Router(config)#ip ssh version 2
Router(config-line)#line vty 0 15
Router(config-line)# transport input all
Router(config)#ip ssh logging events
- C. Router(config)#hostname R15
R15(config)#ip domain-name cisco.com
R15(config)#crypto key generate rsa general-keys modulus 1024
R15(config)#ip ssh version 2
R15(config-line)#line vty 0 15
R15(config-line)# transport input ssh
- D. Router(config)#crypto key generate rsa general-keys modulus 1024
Router(config)#ip ssh version 2
Router(config-line)#line vty 0 15
Router(config-line)# transport input ssh
Router(config)#ip ssh logging events
R15(config)#ip ssh stricthostkeycheck
ANSWER: C
CURRENT_EXPLANATION: {"e": "Để bật SSHv2 trên R15 cần tối thiểu: hostname khác mặc định, `ip domain-name`, tạo khóa RSA (modulus 1024 trở lên), `ip ssh version 2` và `transport input ssh` trên line vty. Đáp án đúng là cái đầy đủ cả hostname lẫn domain-name; các đáp án khác thiếu domain-name hoặc dùng `transport input all`, không đảm bảo chỉ SSH."}

## sec-42  (Question 9.62)
Refer to the exhibit. What must be configured to enable 802.11w on the WLAN?
[IMAGE: D:\CCNA_ontap\web\img/3065179247ec7a2a.jpeg]
- A. Set PMF to Required
- B. Enable MAC Filtering
- C. Enable WPA Policy
- D. Set Fast Transition to Enabled
ANSWER: A
CURRENT_EXPLANATION: {"e": "802.11w là Protected Management Frames (PMF), nên để bật nó trên WLAN cần đặt PMF thành Required (hoặc Optional) trong phần Layer 2 Security. MAC Filtering, WPA Policy và Fast Transition là các tính năng khác, không bật 802.11w."}

## sec-43  (Question 9.66)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/081f24ce8011e38f.jpeg]
A network engineer configures the Cisco WLC to authenticate local wireless clients against a RADIUS server. Which task must be performed to complete the process?
- A. Disable the Server Status option
- B. Enable the Management option
- C. Enable the Network User option
- D. Enable the Support for CoA option
ANSWER: C
CURRENT_EXPLANATION: {"e": "Để WLC xác thực client không dây (network users) qua RADIUS server, cần bật tùy chọn Network User trên server RADIUS đã thêm. Management dùng cho xác thực quản trị, Support for CoA là tính năng Change of Authorization, còn tắt Server Status sẽ vô hiệu server."}

## sec-47  (Question 9.75)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/93126491ac65db17.jpeg]
What are the two steps an engineer must take to provide the highest encryption and authentication using domain credentials from LDAP? (Choose two)
- A. Select WPA policy with TKIP Encryption
- B. Select WPA + WPA2 on layer 2 security
- C. Select PSK under authentication key management
- D. Select Static-WEP + 802.1x on Layer 2 security
- E. Select 802.1x from under authentication key management
ANSWER: B, E
CURRENT_EXPLANATION: {"e": "Để có mã hóa và xác thực mạnh nhất bằng domain credentials (LDAP), chọn WPA + WPA2 trên Layer 2 security và chọn 802.1x trong Authentication Key Management (Enterprise). PSK chỉ dùng mật khẩu chung, còn TKIP và Static-WEP yếu."}

## sec-60  (Question 10.42)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/a359af1723460d6c.jpeg]
A network engineer started to configure port security on a new switch. These requirements must be met:
– MAC addresses must be learned dynamically.
– Log messages must be generated without disabling the interface when unwanted traffic is seen.
Which two commands must be configured to complete this task? (Choose two)
- A. SW(config-if)#switchport port-security mac-address 0010.7B84.45E6
- B. SW(config-if)#switchport port-security maximum 2
- C. SW(config-if)#switchport port-security mac-address sticky
- D. SW(config-if)#switchport port-security violation shutdown
- E. SW(config-if)#switchport port-security violation restrict
ANSWER: B, E
CURRENT_EXPLANATION: {"e": "Yêu cầu: MAC học động và chỉ ghi log mà không tắt interface. Dùng `switchport port-security maximum 2` để cho học động tối đa 2 MAC và `violation restrict` để drop gói vi phạm và ghi log nhưng không err-disable. `violation shutdown` sẽ tắt cổng, còn cấu hình MAC tĩnh hoặc sticky không đáp ứng yêu cầu học động thuần."}

## sec-61  (Question 10.57)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/1635810037bda5bd.jpeg]
Wireless LAN access must be set up to force all clients from the NA WLAN to authenticate against the local database. The WLAN is configured for local EAP authentication. The time that users access the network must not be limited. Which action completes this configuration?
- A. Check the Guest User Role check box
- B. Clear the Lifetime (seconds) value
- C. Set the Lifetime (seconds) value to 0
- D. Uncheck the Guest User check box
ANSWER: D
CURRENT_EXPLANATION: {"e": "Để buộc client xác thực với local database qua local EAP, cần bỏ chọn Guest User (uncheck Guest User) vì đây là user thường, không phải guest có lifetime giới hạn. Việc bỏ chọn này cũng loại bỏ giới hạn thời gian truy cập; các tùy chọn lifetime/guest role không đúng yêu cầu."}

## sec-63  (Question 10.59)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/172f7376a5713529.jpeg]
An engineer must configure the interface that connects to PC1 and secure it in a way that only PC1 is allowed to use the port. No VLAN tagging can be used except for a voice VLAN. Which command sequence must be entered to configure the switch?
- A. SW1(config-if)#switchport mode nonegotiate
SW1(config-if)#switchport port-security
SW1(config-if)#switchport port-security maximum 1
- B. SW1(config-if)#switchport mode access
SW1(config-if)#switchport port-security
SW1(config-if)#switchport port-security mac-address 0050.7966.6800
- C. SW1(config-if)#switchport mode dynamic desirable
SW1(config-if)#switchport port-security mac-address 0050.7966.6800
SW1 (config-if)#switchport port-security mac-address sticky
- D. SW1(config-if)#switchport mode dynamic auto
SW1(config-if)#switchport port-security
SW1(config-if)#switchport port-security violation restrict
ANSWER: B
CURRENT_EXPLANATION: {"e": "Để chỉ PC1 dùng cổng: đặt `switchport mode access` (không dùng VLAN tagging/trunk), bật `switchport port-security` và gán MAC tĩnh `0050.7966.6800`. Các đáp án dùng `nonegotiate`, `dynamic desirable` hoặc `dynamic auto` không đảm bảo cổng ở chế độ access, và port-security không áp dụng được trên cổng dynamic."}

## sec-66  (Question 10.87)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/99f429188de888d8.jpeg]
A guest WLAN must be created that prompts the client for a username and password on the local web page of the WLC. Which two actions must be performed on the Layer 2 tab before enabling the Authentication option on the Layer 3 tab? (Choose two)
- A. Uncheck the MAC Filtering option check box.
- B. Set the Security Type option to Personal.
- C. Change the WPA Encryption option from TKIP to CCMP128(AES).
- D. Set the Layer 2 Security option to None.
- E. Uncheck the WPA Policy option check box, and check the WPA2 Policy option check box.
ANSWER: A, D
CURRENT_EXPLANATION: {"e": "Với guest WLAN dùng web authentication (Layer 3), ở tab Layer 2 cần đặt Layer 2 Security thành None và bỏ chọn MAC Filtering trước khi bật Authentication ở Layer 3. Personal, WPA2/CCMP là bảo mật Layer 2 khác và không dùng với web auth."}

## sec-97  (Question 13.85)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b39ffa1081c06f4d.png]
Connections must be blocked from PC2 to the file server while still allowing PC2 to connect to other network hosts and devices. Which configuration must be used to complete the task?
[TABLE]
Option A
R1(config)#access-list 1 permit 192.168.2.10
R1(config)#access-list 1 deny any
R1(config)#interface g0/1
R1(config-if)#ip access-group 1 out | Option B
R2(config)#access-list 1 deny 192.168.2.10
R2(config)#access-list 1 permit any
R2(config)#interface g0/1
R2(config-if)#ip access-group 1 out
---
Option C
R2(config)#access-list 1 permit 192.168.2.10
R2(config)#access-list 1 deny 192.168.2.0 0.0.0.255
R2(config)#interface g0/1
R2(config)#ip access-group 1 in | Option D
R1(config)#access-list 1 deny 192.168.2.10
R1(config)#access-list 1 permit 192.168.2.0 0.0.0.255
R1(config)#interface g0/0
R1(config-if)#ip access-group 1 in
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B
CURRENT_EXPLANATION: {"e": "PC2 (192.168.2.10) cần bị chặn tới file server nhưng vẫn truy cập host khác. Đặt ACL trên R2 interface g0/1 (hướng tới server) outbound với `deny 192.168.2.10` rồi `permit any`, nên chỉ lưu lượng của PC2 tới server bị chặn. Các đáp án khác permit duy nhất PC2, deny sai host hoặc đặt ở hướng/interface làm chặn thêm các đích khác."}

## sec-112  (Question 15.12)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6ca2a633b2327466.jpeg]
An engineer is creating a secure preshared key based SSID using WPA2 for a wireless network running on 2.4 GHz and 5 GHz. Which two tasks must the engineer perform to complete the process? (Choose two)
- A. Select the 802.1x option for Auth Key Management
- B. Select the AES (CCMP128) option for WPA2 WPA3 Encryption
- C. Select the AES option for Auth Key Management
- D. Select the PSK option for Auth Key Management
- E. Select the WPA Policy option.
ANSWER: B, D
CURRENT_EXPLANATION: "Để tạo SSID WPA2-PSK, cần chọn mã hóa AES (CCMP128) cho WPA2/WPA3 Encryption và chọn PSK cho Auth Key Management. 802.1x dùng cho Enterprise (RADIUS); AES là kiểu mã hóa chứ không phải tùy chọn của Auth Key Management."

## sec-121  (Question 15.28)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/b6b5e2509aef42fe.jpeg]
An engineer is using the Cisco WLC GUI to configure a WLAN for WPA2 encryption with AES and preshared key Cisc0123456. After the engineer selects the WPA + WPA2 option from the Layer 2 Security drop-down list, which two tasks must they perform to complete the process? (Choose two)
- A. Select PSK from the Auth Key Mgmt drop-down list, set the PSK Format to ASCII, and enter the key
- B. Select CCKM from the Auth Key Mgmt drop-down list, set the PSK Format to Hex, and enter the key
- C. Select ASCII from the PSK Format drop-down list, enter the key, and leave the Auth Key Mgmt setting blank
- D. Select the WPA2 Policy, AES, and TKIP check boxes
- E. Select the WPA2 Policy and AES check boxes.
ANSWER: A, E
CURRENT_EXPLANATION: "Để cấu hình WPA2-PSK với AES trên WLC: chọn PSK trong Auth Key Mgmt, định dạng PSK là ASCII và nhập key, đồng thời chọn WPA2 Policy và AES. Không chọn TKIP (không cần), CCKM là cho roaming enterprise, và không được để Auth Key Mgmt trống."

## sec-130  (Question 15.58)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/1d373d0674230243.jpeg]
Company A wants to use a RADIUS server to service all user and device authentication attempts with a more secure and granular authentication approach. Not all client devices support dot1x authentication. Which two configuration changes must be made to accomplish the task? (Choose two)
- A. Enable AutoConfig iPSK under the Layer 2 tab.
- B. Select Authentication server under the AAA servers tab.
- C. Configure Enterprise Security type under the Layer 2 tab.
- D. Set Authentication under the Layer 3 tab.
- E. Enable WPA2 Policy under the Layer 2 tab.
ANSWER: A, B
CURRENT_EXPLANATION: "Để dùng RADIUS cho mọi thiết bị, kể cả thiết bị không hỗ trợ dot1x, cần bật AutoConfig iPSK (identity PSK, mỗi thiết bị có PSK riêng do RADIUS cấp) ở tab Layer 2, và chọn Authentication server ở tab AAA servers. Enterprise security (802.1X) không phù hợp vì một số client không hỗ trợ dot1x."

## sec-136  (Question 15.95)
Refer to the exhibit. An extended ACL has been configured and applied to router R2. The configuration failed to work as intended. Which two changes stop outbound traffic on TCP ports 25 and 80 to 10.0.20.0/26 from the 10.0.10.0/26 subnet while still allowing all other traffic? (Choose two)
[IMAGE: D:\CCNA_ontap\web\img/e21489d0263b5a18.jpeg]
[TABLE]
R2#config t
R2(config)#access-list 101 deny tcp 10.0.20.0 0.0.0.63 10.0.10.0 0.0.0.63 eq smtp
R2(config)#access-list 101 deny tcp 10.0.20.0 0.0.0.63 10.0.10.0 0.0.0.63 eq www
R2(config)#int gi0/2
R2(config-if)#ip access-group 101 in
[/TABLE]
- A. Add a “permit ip any any” statement to the beginning of ACL 101 for allowed traffic
- B. Add a “permit ip any any” statement at the end of ACL 101 for allowed traffic
- C. The source and destination IPs must be swapped in ACL 101
- D. The ACL must be configured the Gi0/2 interface inbound on R1
- E. The ACL must be moved to the Gi0/1 interface outbound on R2
ANSWER: B, C
CURRENT_EXPLANATION: "ACL sai vì source/destination bị đặt ngược (cần source 10.0.10.0/26 và destination 10.0.20.0/26) và thiếu `permit ip any any` ở cuối do implicit deny sẽ chặn mọi traffic khác. Đặt permit ở đầu sẽ làm các lệnh deny không bao giờ được khớp."

## sec-143  (Question 16.26)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3cdd8c4829ce4d69.jpeg]
A network engineer is configuring a wireless LAN with Web Passthrough Layer 3 Web Policy. Which action must the engineer take to complete the configuration?
- A. Enable the WPA Policy.
- B. Set the Layer 2 Security to 802.1X.
- C. Enable TKIP and CCMP256 WPA2 Encryption.
- D. Set the Layer 2 Security to None.
ANSWER: D
CURRENT_EXPLANATION: "Web Passthrough là Layer 3 security, do đó Layer 2 Security phải được đặt là None (không dùng 802.1X hay WPA). Bật WPA/TKIP/CCMP256 hoặc 802.1X mâu thuẫn với cấu hình này."

## sec-149  (Question 16.68)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e8ee9f8a4f80e8ab.jpeg]
Users will be using a preconfigured secret key and SSID and must have a secured key hashing algorithm configured. The AAA server must not be used for the user authentication method. Which action completes the task?
- A. Configure PSK-SHA2.
- B. Configure PSK Format HEX with key string.
- C. Set CCMP128(AES).
- D. Enable AutoConfig iPSK.
ANSWER: A
CURRENT_EXPLANATION: "Cần PSK dùng preconfigured key, không qua AAA server và có thuật toán hash an toàn: chọn PSK-SHA2 trong Auth Key Management. Định dạng HEX hay CCMP128 chỉ là dạng key/mã hóa, còn iPSK dùng RADIUS nên không phù hợp."

## auto-4  (Question 5.34)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/30b86bf48ff4f2c0.jpeg]
After running the code in the exhibit, which step reduces the amount of data that the NETCONF server returns to the NETCONF client, to only the interface’s configuration?
- A. Use the xml library to parse the data returned by the NETCONF server for the interface’s configuration.
- B. Create an XML filter as a string and pass it to get_config() method as an argument.
- C. Create a JSON filter as a string and pass it to the get_config() method as an argument.
- D. Use the JSON library to parse the data returned by the NETCONF server for the interface’s configuration.
ANSWER: B
CURRENT_EXPLANATION: {"e": "NETCONF get_config() có thể nhận một filter để chỉ lấy phần dữ liệu cần thiết. Vì NETCONF dùng XML, ta tạo filter dạng XML (chuỗi) rồi truyền vào get_config() để server chỉ trả về cấu hình của interface. Parse bằng thư viện xml hay JSON chỉ xử lý dữ liệu sau khi đã nhận về, không làm giảm lượng dữ liệu server trả về; JSON filter không được NETCONF dùng."}

## auto-31  (Question 9.81)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ddce9a10c22a5884.jpeg]
Which type of configuration is represented in the output?
- A. Chef
- B. JSON
- C. Ansible
- D. Puppet
ANSWER: D
CURRENT_EXPLANATION: {"e": "Cú pháp `cisco_ospf_vrf {\"R1 default\": ensure => 'present', auto_cost => '100'}` dùng khai báo resource với dấu `=>`, đặc trưng của Puppet manifest. Chef dùng Ruby recipe, Ansible dùng YAML playbook, còn JSON dùng cặp key:value với dấu hai chấm."}

## auto-32  (Question 9.84)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/fa2b25b95a904e71.jpeg]
What is represented by “R1” and “SW1” within the JSON output?
- A. array
- B. object
- C. value
- D. key
ANSWER: C
CURRENT_EXPLANATION: {"e": "Trong output, \"Routers\" và \"Switches\" là key, còn mảng [\"R1\",\"R2\",\"R3\"] là value của key đó. \"R1\" và \"SW1\" là các phần tử string nằm trong array, tức là value. Chúng không phải key hay object."}

## auto-38  (Question 10.37)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e0b5a901d1056331.jpeg]
How many objects are present in the given JSON-encoded data?
- A. one
- B. four
- C. seven
- D. nine
ANSWER: D
CURRENT_EXPLANATION: {"e": "Đếm các cặp `{}` trong JSON: object ngoài cùng, aaaUser, attributes của aaaUser, phần tử đầu của children (chứa aaaUserRole), aaaUserRole, attributes của nó, phần tử children thứ hai, aaaUserRole bên trong và attributes của nó, tổng cộng 9 object. Array `[]` không tính là object."}
