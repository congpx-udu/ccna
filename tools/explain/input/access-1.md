# Network Access (part 1)

## access-1  (Question 5.4)
A network administrator needs to aggregate 4 ports into a single logical link which must negotiate layer 2 connectivity to ports on another switch. What must be configured when using active mode on both sides of the connection?
- A. 802.1q trunks
- B. Cisco vPC
- C. LLDP
- D. LACP
ANSWER: D

## access-2  (Question 5.6)
Aside from discarding, which two states does the switch port transition through while using RSTP (802.1w)? (Choose two)
- A. listening
- B. blocking
- C. forwarding
- D. learning
- E. speaking
ANSWER: C, D

## access-3  (Question 5.7)
What is a role of wireless controllers in an enterprise network?
- A. serve as the first line of defense in an enterprise network
- B. support standalone or controller-based architectures
- C. centralize the management of access points in an enterprise network
- D. provide secure user logins to devices on the network
ANSWER: C

## access-4  (Question 5.12)
Which device controls the forwarding of authentication requests for users when connecting to the network using a lightweight access point?
- A. TACACS server
- B. wireless access point
- C. RADIUS server
- D. wireless LAN controller
ANSWER: D

## access-5  (Question 5.15)
Refer to the exhibit. PC1 is trying to ping PC3 for the first time and sends out an ARP to S1. Which action is taken by S1?
[IMAGE: D:\CCNA_ontap\web\img/ae2b8f04a971d13c.jpeg]
- A. It forwards it out G0/3 only
- B. It is flooded out every port except G0/0
- C. It drops the frame
- D. It forwards it out interface G0/2 only
ANSWER: B

## access-6  (Question 5.16)
Refer to the exhibit. What is the result if Gig1/11 receives an STP BPDU?
[TABLE]
switch(config)#interface gigabitEthernet 1/11 
switch(config-if)#switchport mode access 
switch(config-if)#spanning-tree portfast 
switch(config-if)#spanning-tree bpduguard enable
[/TABLE]
- A. The port transitions to STP blocking
- B. The port transitions to the root port
- C. The port immediately transitions to STP forwarding
- D. The port goes into error-disable state
ANSWER: D

## access-7  (Question 5.17)
An engineer must configure traffic for a VLAN that is untagged by the switch as it crosses a trunk link. Which command should be used?
- A. switchport trunk allowed vlan 10
- B. switchport trunk native vlan 10
- C. switchport mode trunk
- D. switchport trunk encapsulation dot1q
ANSWER: B

## access-8  (Question 5.19)
How does a Cisco Unified Wireless network respond to Wi-Fi channel overlap?
- A. It alternates automatically between 2.4 GHz and 5 GHz on adjacent access points
- B. It allows the administrator to assign channels on a per-device or per-interface basis.
- C. It segregates devices from different manufacturers onto different channels.
- D. It analyzes client load and background noise and dynamically assigns a channel.
ANSWER: D

## access-9  (Question 5.20)
What does a switch use to build its MAC address table?
- A. VTP
- B. DTP
- C. egress traffic
- D. ingress traffic
ANSWER: D

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

## access-12  (Question 5.26)
How does a switch process a frame received on Fa0/1 with the destination MAC address of 0e38.7363.657b when the table is missing the address?
- A. It floods the frame to all interfaces except Fa0/1.
- B. It forwards the frame back out of interface Fa0/1.
- C. It drops the frame immediately.
- D. It holds the frame until the MAC address timer expires and then drops the frame.
ANSWER: A

## access-13  (Question 5.36)
If a switch port receives a new frame while it is actively transmitting a previous frame, how does it process the frames?
- A. The previous frame is delivered, the new frame is dropped, and a retransmission request is sent.
- B. The new frame is delivered first, the previous frame is dropped, and a retransmission request is sent.
- C. The two frames are processed and delivered at the same time.
- D. The new frame is placed in a queue for transmission after the previous frame.
ANSWER: D

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

## access-15  (Question 5.40)
Why does a switch flood a frame to all ports?
- A. The destination MAC address of the frame is unknown
- B. The source MAC address of the frame is unknown
- C. The source and destination MAC addresses of the frame are the same
- D. The frame has zero destination MAC addresses
ANSWER: A

## access-16  (Question 5.43)
How is the native VLAN secured in a network?
- A. separate from other VLANs within the administrative domain
- B. give it a value in the private VLAN range
- C. assign it as VLAN 1
- D. configure it as a different VLAN ID on each end of the link
ANSWER: A

## access-17  (Question 5.44)
Which command on a port enters the forwarding state immediately when a PC is connected to it?
- A. switch(config)#spanning-tree portfast default
- B. switch(config)#spanning-tree portfast bpduguard default
- C. switch(config-if)#spanning-tree portfast trunk
- D. switch(config-if)#no spanning-tree portfast
ANSWER: A

## access-18  (Question 6.3)
An engineer observes high usage on the 2.4GHz channels and lower usage on the 5GHz channels. What must be configured to allow clients to preferentially use 5GHz access points?
- A. Client Band Select
- B. OEAP Split Tunnel
- C. 11ac MU-MIMO
- D. Re-Anchor Roamed Clients
ANSWER: A

## access-19  (Question 6.8)
An administrator must secure the WLC from receiving spoofed association requests. Which steps must be taken to configure the WLC to restrict the requests and force the user to wait 10 ms to retry an association request?
- A. Enable Security Association Teardown Protection and set the SA Query timeout to 10
- B. Enable the Protected Management Frame service and set the Comeback timer to 10
- C. Enable 802.1x Layer 2 security and set the Comeback timer to 10
- D. Enable MAC filtering and set the SA Query timeout to 10
ANSWER: B

## access-20  (Question 6.10)
Which 802.11 management frame type is sent when a client roams between access points on the same SSID?
- A. Authentication Request
- B. Probe Request
- C. Reassociation Request
- D. Association Request
ANSWER: C

## access-21  (Question 6.12)
Which protocol does an access point use to draw power from a connected switch?
- A. Internet Group Management Protocol
- B. Cisco Discovery Protocol
- C. Adaptive Wireless Path Protocol
- D. Neighbor Discovery Protocol
ANSWER: B

## access-22  (Question 6.14)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/604e00cb1ce5453e.jpeg]
Which command must be executed for Gi1/1 on SW1 to passively become a trunk port if Gi1/1 on SW2 is configured in desirable or trunk mode?
- A. switchport mode trunk
- B. switchport mode dot1-tunnel
- C. switchport mode dynamic auto
- D. switchport mode dynamic desirable
ANSWER: C

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

## access-24  (Question 6.17)
What is a role of access points in an enterprise network?
- A. connect wireless devices to a wired network
- B. support secure user logins to devices or the network
- C. integrate with SNMP in preventing DDoS attacks
- D. serve as a first line of defense in an enterprise network
ANSWER: A

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

## access-27  (Question 6.24)
What occurs when overlapping Wi-Fi channels are implemented?
- A. The wireless network becomes vulnerable to unauthorized access
- B. Wireless devices are unable to distinguish between different SSIDs
- C. Network communications are open to eavesdropping
- D. Users experience poor wireless network performance
ANSWER: D

## access-28  (Question 6.26)
An engineer needs to add an old switch back into a network. To prevent the switch from corrupting the VLAN database which action must be taken?
- A. Add the switch in the VTP domain with a lower revision number
- B. Add the switch in the VTP domain with a higher revision number
- C. Add the switch with DTP set to dynamic desirable
- D. Add the switch with DTP set to desirable
ANSWER: A

## access-29  (Question 6.27)
Which WLC port connects to a switch to pass normal access-point traffic?
- A. distribution system
- B. service
- C. redundancy
- D. console
ANSWER: A

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

## access-31  (Question 7.9)
When a switch receives a frame for a known destination MAC address, how is the frame handed?
- A. flooded to all ports except the one from which it originated
- B. broadcast to all ports
- C. forwarded to the first available port
- D. sent to the port identified for the known MAC address
ANSWER: D

## access-32  (Question 7.23)
What is the benefit of configuring PortFast on an interface?
- A. After the cable is connected, the interface uses the fastest speed setting available for that cable type
- B. The frames entering the interface are marked with higher priority and then processed faster by a switch
- C. After the cable is connected, the interface is available faster to send and receive user data
- D. Real-time voice and video frames entering the interface are processed faster
ANSWER: C

## access-33  (Question 7.28)
How are the switches in a spine-and-leaf topology interconnected?
- A. Each leaf switch is connected to two spine switches, making a loop.
- B. Each leaf switch is connected to a central leaf switch, then uplinked to a core spine switch.
- C. Each leaf switch is connected to each spine switch.
- D. Each leaf switch is connected to one of the spine switches.
ANSWER: C

## access-34  (Question 7.42)
What must be considered when using 802.11a?
- A. It is compatible with 802.11g and 802.11-compliant wireless devices
- B. It is chosen over 802.11b/g when a lower-cost solution is necessary
- C. It is susceptible to interference from 2.4 GHz devices such as microwave ovens.
- D. It is used in place of 802.11b/g when many nonoverlapping channels are required
ANSWER: D

## access-35  (Question 7.44)
An engineer configures interface Gi1/0 on the company PE router to connect to an ISP.
Neighbor discovery is disabled.
interface Gi1/0
description HQ_DC3392-9383
duplex full
speed 100
negotiation auto
lldp transmit
lldp receive
Which action is necessary to complete the configuration if the ISP uses third-party network devices?
- A. Enable LLDP globally
- B. Disable autonegotiation
- C. Disable Cisco Discovery Protocol on the interface
- D. Enable LLDP-MED on the ISP device
ANSWER: A

## access-36  (Question 7.48)
A network administrator is asked to configure VLANs 2, 3 and 4 for a new implementation. Some ports must be assigned to the new VLANs with unused remaining. Which action should be taken for the unused ports?
- A. configure port in the native VLAN
- B. configure ports in a black hole VLAN
- C. configure in a nondefault native VLAN
- D. configure ports as access ports
ANSWER: B

## access-37  (Question 8.4)
Which mode must be set for APs to communicate to a Wireless LAN Controller using the Control and Provisioning of Wireless Access Points (CAPWAP) protocol?
- A. bridge
- B. route
- C. autonomous
- D. lightweight
ANSWER: D

## access-38  (Question 8.5)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d000311ae63ee13c.jpeg]
Which change to the configuration on Switch2 allows the two switches to establish an EtherChannel?
- A. Change the protocol to EtherChannel mode on
- B. Change the LACP mode to active
- C. Change the LACP mode to desirable
- D. Change the protocol to PAgP and use auto mode
ANSWER: B

## access-39  (Question 8.6)
Where does wireless authentication happen?
- A. SSID
- B. radio
- C. band
- D. Layer 2
ANSWER: D

## access-40  (Question 8.7)
What is the path for traffic sent from one user workstation to another workstation on a separate switch in a three-layer architecture model?
- A. access – core – distribution – access
- B. access – distribution – distribution – access
- C. access – core – access
- D. access -distribution – core – distribution – access
ANSWER: B

## access-41  (Question 8.9)
What is the purpose of an SSID?
- A. It provides network security
- B. It differentiates traffic entering access points
- C. It identities an individual access point on a WLAN
- D. It identifies a WLAN
ANSWER: D

## access-42  (Question 8.10)
What are two characteristics of an SSID? (Choose two)
- A. It can be hidden or broadcast in a WLAN
- B. It uniquely identifies an access point in a WLAN
- C. It uniquely identifies a client in a WLAN
- D. It is at most 32 characters long
- E. It provides secured access to a WLAN
ANSWER: A, D

## access-43  (Question 8.13)
Which port type supports the spanning-tree portfast command without additional configuration?
- A. access ports
- B. Layer 3 main interfaces
- C. Layer 3 subinterfaces
- D. trunk ports
ANSWER: A

## access-44  (Question 8.17)
What prevents a workstation from receiving a DHCP address?
- A. DTP
- B. STP
- C. VTP
- D. 802.10
ANSWER: B

## access-45  (Question 8.23)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/d4a50dddcaa26d3d.jpeg]
Between which zones do wireless users expect to experience intermittent connectivity?
- A. between zones 1 and 2
- B. between zones 2 and 5
- C. between zones 3 and 4
- D. between zones 3 and 6
ANSWER: C

## access-46  (Question 8.29)
Which 802.11 frame type is indicated by a probe response after a client sends a probe request?
- A. action
- B. management
- C. control
- D. data
ANSWER: B

## access-47  (Question 8.30)
What is recommended for the wireless infrastructure design of an organization?
- A. group access points together to increase throughput on a given channel
- B. configure the first three access points are configured to use channels 1, 6, and 11
- C. include a least two access points on nonoverlapping channels to support load balancing
- D. assign physically adjacent access points to the same Wi-Fi channel
ANSWER: B

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

## access-51  (Question 8.56)
Which two spanning-tree states are bypassed on an interface running PortFast? (Choose two)
- A. forwarding
- B. blocking
- C. disabled
- D. learning
- E. listening
ANSWER: D, E

## access-52  (Question 8.57)
What is a requirement when configuring or removing LAG on a WLC?
- A. The incoming and outgoing ports for traffic flow must be specified if LAG is enabled.
- B. The controller must be rebooted after enabling or reconfiguring LAG.
- C. The management interface must be reassigned if LAG is disabled.
- D. Multiple untagged interfaces on the same port must be supported.
ANSWER: B

## access-53  (Question 8.58)
What is a requirement for nonoverlapping WI-FI channels?
- A. different security settings
- B. different transmission speeds
- C. discontinuous frequency ranges
- D. unique SSIDs
ANSWER: C

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

## access-55  (Question 8.66)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/26bc9e2bc3c006b7.png]
An engineer built a new L2 LACP EtherChannel between SW1 and SW2 and executed these show commands to verify the work. Which additional task allows the two switches to establish an LACP port channel?
- A. Change the channel-group mode on SW1 to desirable.
- B. Change the channel-group mode on SW1 to active or passive.
- C. Change the channel-group mode on SW2 to auto.
- D. Configure the interface port-channel 1 command on both switches.
ANSWER: B

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

## access-57  (Question 8.72)
What provides centralized control of authentication and roaming in an enterprise network?
- A. a LAN switch
- B. a firewall
- C. a lightweight access point
- D. a wireless LAN controller
ANSWER: D

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

## access-59  (Question 9.1)
Refer to the exhibit.
Switch#show etherchannel summary
[output omitted]
Group   Port-channel  Protocol   Ports
-------+--------------+---------+---------------------
10      Po10(SU)       LACP      Gi0/0(P)  Gi0/1(P)
20      Po20(SU)       LACP      Gi0/2(P)  Gi0/3(P)
Which two commands when used together create port channel 10? (Choose two)
- A. int range g0/0-1
channel-group 10 mode active
- B. int range g0/0-1
channel-group 10 mode desirable
- C. int range g0/0-1
channel-group 10 mode passive
- D. int range g0/0-1
channel-group 10 mode auto
- E. int range g0/0-1
channel-group 10 mode on
ANSWER: A, C

## access-60  (Question 9.19)
Which interface mode must be configured to connect the lightweight APs in a centralized architecture?
- A. WLAN dynamic
- B. management
- C. trunk
- D. access
ANSWER: D

## access-61  (Question 9.23)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ade282f4b25b01b8.jpeg]
The link between PC1 and the switch is up, but it is performing poorly. Which interface condition is causing the performance problem?
- A. There is a duplex mismatch on the interface
- B. There is an issue with the fiber on the switch interface
- C. There is a speed mismatch on the interface
- D. There is an interface type mismatch
ANSWER: A

## access-62  (Question 9.24)
What provides centralized control of authentication and roaming in an enterprise network?
- A. a lightweight access point
- B. a firewall
- C. a wireless LAN controller
- D. a LAN switch
ANSWER: C

## access-63  (Question 9.31)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/22b5d93bad1ab37d.png]
An engineer is asked to insert the new VLAN into the existing trunk without modifying anything previously configured Which command accomplishes this task?
- A. switchport trunk allowed vlan 100-104
- B. switchport trunk allowed vlan all
- C. switchport trunk allowed vlan add 104
- D. switchport trunk allowed vlan 104
ANSWER: C

## access-64  (Question 9.36)
What is one reason to implement LAG on a Cisco WLC?
- A. to increase security and encrypt management frames
- B. to provide link redundancy and load balancing
- C. to allow for stateful and link-state failover
- D. to enable connected switch ports to failover and use different VLANs
ANSWER: B

## access-65  (Question 9.39)
A Cisco engineer must configure a single switch interface to meet these requirements
* accept untagged frames and place them in VLAN 20
* accept tagged frames in VLAN 30 when CDP detects a Cisco IP phone
Which command set must the engineer apply?
- A. switchport mode access
switchport access vlan 20
switchport voice vlan 30
- B. switchport mode trunk
switchport access vlan 20
switchport voice vlan 30
- C. switchport mode dynamic auto
switchport trunk native vlan 20
switchport trunk allowed vlan 30
switchport voice vlan 30
- D. switchport mode dynamic desirable
switchport access vlan 20
switchport trunk allowed vlan 30
switchport voice vlan 30
ANSWER: A

## access-66  (Question 9.41)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/6d5584c3cbfe0571.jpeg]
Users need to connect to the wireless network with IEEE 802.11r-compatible devices. The connection must be maintained as users travel between floors or to other areas in the building. What must be the configuration of the connection?
- A. Select the WPA Policy option with the CCKM option
- B. Disable AES encryption
- C. Enable Fast Transition and select the FT 802.1x option
- D. Enable Fast Transition and select the FT PSK option
ANSWER: C

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

## access-69  (Question 9.47)
Which value is the unique identifier that an access point uses to establish and maintain wireless connectivity to wireless network devices?
- A. VLANID
- B. SSID
- C. RFID
- D. WLANID
ANSWER: B

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

## access-71  (Question 9.52)
Which Layer 2 switch function encapsulates packets for different VLANs so that the packets traverse the same port and maintain traffic separation between the VLANs?
- A. VLAN numbering
- B. VLAN DSCP
- C. VLAN tagging
- D. VLAN marking
ANSWER: C

## access-72  (Question 9.56)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f0bcd568b3510547.jpeg]
SW2 is replaced due to a hardware failure. A network engineer starts to configure SW2 by copying the Fa0/1 interface configuration from SW1. Which command must be configured on the Fa0/1 interface of SW2 to enable PC1 to connect to PC2?
- A. switchport mode trunk
- B. switchport trunk native vlan 10
- C. switchport trunk allowed remove 10
- D. switchport mode access
ANSWER: A

## access-73  (Question 9.59)
Which port type does a lightweight AP use to connect to the wired network when configured in FlexConnect mode with local switching and VLAN tagging?
- A. EtherChannel
- B. access
- C. LAG
- D. trunk
ANSWER: D

## access-74  (Question 9.60)
An engineer is installing a new wireless printer with a static IP address on the Wi-Fi network. Which feature must be enabled and configured to prevent connection issues with the printer?
- A. passive client
- B. static IP tunneling
- C. DHCP address assignment
- D. client exclusion
ANSWER: A

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

## access-77  (Question 9.105)
What is a function of MAC learning on a switch?
- A. A static MAC address is manually added to the MAC table.
- B. MAC address learning is disabled by default on all VLANs.
- C. Frames received for a destination MAC address not listed in the address table are dropped.
- D. The MAC address table is used to populate the ARP table.
ANSWER: A

## access-78  (Question 10.7)
Which set of 2.4 GHz nonoverlapping wireless channels is standard in the United States?
- A. channels 2, 7, 9, and 11
- B. channels 1, 6, 11, and 14
- C. channels 2, 7, and 11
- D. channels 1, 6, and 11
ANSWER: D

## access-79  (Question 10.8)
Which command entered on a switch configured with Rapid-PVST+ listens and learns for a specific time period?
- A. switch(config)#spanning-tree vlan 1 max-age 6
- B. switch(config)#spanning-tree vlan 1 hello-time 10
- C. switch(config)#spanning-tree vlan 1 priority 4096
- D. switch(config)#spanning-tree vlan 1 forward-time 20
ANSWER: D

## access-80  (Question 10.10)
Refer to the exhibit.
interface g2/0/0
channel-group 1 mode active
interface g4/0/0
channel-group 1 mode active
interface Port-channel1
ip address 203.0.113.65 255.255.255.252
%LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to down
An engineer is configuring a Layer 3 port-channel interface with LACP. The configuration on the first device is complete, and it is verified that both interfaces have registered the neighbor device in the CDP table. Which task on the neighbor device enables the new port channel to come up without negotiating the channel?
- A. Bring up the neighboring interfaces using the no shutdown command.
- B. Change the EtherChannel mode on the neighboring interfaces to auto
- C. Modify the static EtherChannel configuration of the device to passive mode
- D. Configure the IP address of the neighboring device
ANSWER: C

## access-81  (Question 10.20)
Which access point mode relies on a centralized controller tor management, roaming, and SSID configuration?
- A. repeater mode
- B. bridge mode
- C. lightweight mode
- D. autonomous mode
ANSWER: C

## access-82  (Question 10.27)
What is a function of spine-and-leaf architecture?
- A. mitigates oversubscription by adding a layer of leaf switches
- B. limits payload size of traffic within the leaf layer
- C. offers predictable latency of the traffic path between end devices
- D. exclusively sends multicast traffic between servers that are directly connected to the spine
ANSWER: C

## access-83  (Question 10.34)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c81c78837a75c26b.jpeg]
Clients on the WLAN are required to use 802.11r. What action must be taken to meet the requirement?
- A. Enable CCKM under Authentication Key Management
- B. Under Protected Management Frames, set the PMF option to Required
- C. Set the Fast Transition option to Enable and enable FT 802.1X under Authentication Key Management
- D. Set the Fast Transition option and the WPA gtk-randomize State to disable
ANSWER: C

## access-84  (Question 10.35)
When a switch receives a frame for an unknown destination MAC address, how is the frame handled?
- A. broadcast to all ports on the switch
- B. flooded to all ports except the origination port
- C. forwarded to the first available port
- D. inspected and dropped by the switch
ANSWER: B

## access-85  (Question 10.47)
What must be considered for a locally switched FlexConnect AP if the VLANs that are used by the AP and client access are different?
- A. The APs must be connected to the switch with multiple links in LAG mode.
- B. The native VLAN must match the management VLAN of the AP.
- C. The switch port mode must be set to trunk.
- D. IEEE 802.1Q trunking must be disabled on the switch port.
ANSWER: C

## access-86  (Question 10.48)
Which command configures the Cisco WLC to prevent a serial session with the WLC CLI from being automatically logged out?
- A. config sessions maxsessions 0
- B. config serial timeout 9600
- C. config serial timeout 0
- D. config sessions timeout 0
ANSWER: C

## access-87  (Question 10.50)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/84cfbc1b2443c905.jpeg]
An architect is managing a wireless network with APs from several branch offices connecting to the WLC in the data center. There is a new requirement for a single WLAN to process the client data traffic without sending it to the WLC. Which action must be taken to complete the request?
- A. Enable local HTTP profiling
- B. Enable FlexConnect Local Switching
- C. Enable local DHCP Profiling
- D. Enable Disassociation Imminent
ANSWER: B

## access-88  (Question 10.51)
What is a function of MAC address learning?
- A. It is disabled by default on all interfaces connected to trunks
- B. It increases security on the management VLAN
- C. It is enabled by default on all VLANs and interfaces
- D. It increases the potential for MAC address flooding
ANSWER: C

## access-89  (Question 10.52)
A Cisco engineer at a new branch office is configuring a wireless network with access points that connect to a controller that is based at corporate headquarters. Wireless client traffic must terminate at the branch office and access-point survivability is required in the event of a WAN outage. Which access point mode must be selected?
- A. Lightweight with local switching disabled
- B. Local with AP fallback enabled
- C. OfficeExtend with high availability disabled
- D. FlexConnect with local switching enabled
ANSWER: D

## access-90  (Question 10.62)
Which two functions does a WLC perform in the lightweight access-point architecture that an AP performs independently in an autonomous architecture? (Choose two)
- A. handling the association, authentication, and roaming of wireless clients
- B. encrypting and decrypting traffic that uses the WAP protocol family
- C. preventing collisions between wireless clients on the same RF channel
- D. managing RF channels, including transmission power
- E. sending and processing beacon frames
ANSWER: A, D

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

## access-92  (Question 10.67)
Refer to the exhibit.
SW1#show ip interface brief
Interface        IP-Address   OK? Method Status Protocol
FastEthernet0/1  unassigned   YES manual down   down
SW1#show interface fa0/1 status
Port     Name  Status      Vlan   Duplex   Speed  Type
Fa0/1          notconnect  1      a-full   a-100  10/100BaseTX
What is the cause of the issue?
- A. STP
- B. shutdown command
- C. port security
- D. wrong cable type
ANSWER: D

## access-93  (Question 10.70)
What is a function of Layer 3 switches?
- A. They route traffic between devices in different VLANs.
- B. They transmit broadcast traffic when operating in Layer 3 mode exclusively.
- C. They forward Ethernet frames between VLANs using only MAC addresses.
- D. They move frames between endpoints limited to IP addresses.
ANSWER: A

## access-94  (Question 10.77)
A network administrator plans an update to the Wi-Fi networks in multiple branch offices. Each location is configured with an SSID called “Office”. The administrator wants every user who connects to the SSID at any location to have the same access level. What must be set the same on each network to meet the requirement?
- A. radio policy
- B. security policies
- C. NAS-ID configuration
- D. profile name
ANSWER: B

## access-95  (Question 11.6)
Which type of port is used to connect to the wired network when an autonomous AP maps two VLANs to its WLANs?
- A. LAG
- B. EtherChannel
- C. trunk
- D. access
ANSWER: C

## access-96  (Question 11.13)
What is a reason to configure a trunk port that connects to a WLC distribution port?
- A. Eliminate redundancy with a link failure in the data path.
- B. Allow multiple VLAN to be used in the data path.
- C. Provide redundancy if there is a link failure for out-of-band management.
- D. Permit multiple VLANs to provide out-of-band management.
ANSWER: B

## access-97  (Question 11.21)
What does a switch do when it receives a frame whose destination MAC address is missing from the MAC address table?
- A. It floods the frame unchanged across all remaining ports in the incoming VLAN.
- B. It appends the table with a static entry for the MAC and shuts down the port.
- C. It updates the CAM table with the destination MAC address of the frame.
- D. It changes the checksum of the frame to a value that indicates an invalid frame.
ANSWER: A

## access-98  (Question 11.24)
What are two reasons a switch experiences frame flooding? (Choose two)
- A. A defective patch cable is connected to the switch port
- B. Topology changes are occurring within spanning-tree
- C. An aged MAC table entry is causing excessive updates
- D. Port-security is configured globally
- E. The forwarding table has overflowed
ANSWER: B, E

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

## access-100  (Question 11.37)
What is a specification for SSIDS?
- A. They are a Cisco proprietary security feature.
- B. They must include one number and one letter.
- C. They define the VLAN on a switch.
- D. They are case sensitive.
ANSWER: D
