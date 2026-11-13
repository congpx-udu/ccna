# Network Access (part 2)

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

## access-102  (Question 11.53)
Two switches have been implemented and all interfaces are at the default configuration level. A trunk link must be implemented between two switches with these requirements:
using an industry-standard trunking protocol
permitting VLANs 1-10 and denying other VLANs How must the interconnecting ports be configured?
- A. switchport mode trunk
switchport trunk allowed vlans 1-10
switchport trunk native vlan 11
- B. switchport mode trunk
switchport trunk encapsulation dot1q
switchport trunk allowed vlans 1-10
- C. switchport mode dynamic desirable
channel-group 1 mode desirable
switchport trunk encapsulation isl
switchport trunk allowed vlan except 11-4094
- D. switchport mode dynamic
channel-protocol lacp
switchport trunk allowed vlans 1-10
ANSWER: B

## access-103  (Question 11.54)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/803c0f72332c511a.jpeg]
A network engineer is configuring a WLAN to connect with the 172.16.10.0/24 network on VLAN 20. The engineer wants to limit the number of devices that connect to the WLAN on the USERWL SSID to 125. Which configuration must the engineer perform on the WLC?
- A. In the WLAN configuration, set the Maximum Allowed Clients value to 125.
- B. In the Advanced configuration, set the DTIM value to 125.
- C. In the Controller IPv6 configuration, set the Throttle value to 125.
- D. In the Management Software activation configuration, set the Clients value to 125.
ANSWER: A

## access-104  (Question 11.61)
Which interface or port on the WLC is the default for in-band device administration and communications between the controller and access points?
- A. virtual interface
- B. management interface
- C. console port
- D. service port
ANSWER: B

## access-105  (Question 11.63)
A company has each office using wireless access with multiple SSIDs while limiting roaming capabilities, covering different locations on the internal office LAN, guest networks, and BYOD access for employees. Which change must be enabled to improve the customer experience during SSID changes?
- A. Assisted Roaming Prediction Optimization
- B. Fast Transition
- C. Neighbor List Dual Band
- D. Fast SSID Change
ANSWER: D

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

## access-107  (Question 11.68)
Refer to the exhibit.
SW1#show etherchannel
Channel-group listing:
----------------------
Group: 2
--------
Group state = L2
Ports: 1 Maxports = 8
Port-channels: 1 Max Portchannels = 1
Protocol: PAGP
A network engineer updates the existing configuration on interface fastethernet1/1 switch SW1. It must establish an EtherChannel by using the same group designation with another vendor switch. Which configuration must be performed to complete the process?
- A. interface port-channel 2
channel-group 2 mode desirable
- B. interface fastethernet 1/1
channel-group 2 mode on
- C. interface port-channel 2
channel-group 2 mode auto
- D. interface fastethernet 1/1
channel-group 2 mode active
ANSWER: D

## access-108  (Question 11.72)
When an access point is seeking to join a wireless LAN controller, which message is sent to the AP-Manager interface?
- A. DHCP request
- B. DHCP discover
- C. discovery response
- D. discovery request
ANSWER: D

## access-109  (Question 11.78)
What is the operating mode and role of a backup port on a shared LAN segment in Rapid PVST+?
- A. blocking mode and provides an alternate path toward the designated bridge
- B. listening mode and provides an alternate path toward the root bridge
- C. forwarding mode and provides the lowest-cost path to the root bridge for each VLAN
- D. learning mode and provides the shortest path toward the root bridge handling traffic away from the LAN
ANSWER: A

## access-110  (Question 11.80)
What occurs when a switch receives a frame that has a destination that is an unknown MAC address?
- A. The frame is flooded to all interfaces in the VLAN to which the frame belongs.
- B. The frame is flooded to all interfaces in the switch.
- C. The frame is discarded
- D. The MAC address table of the switch is flushed
ANSWER: A

## access-111  (Question 11.82)
SIP-based Call Admission Control must be configured in the Cisco WLC GUI. SIP call-snooping ports are configured. Which two actions must be completed next? (Choose two)
- A. Set the QoS level to silver or greater for voice traffic
- B. Enable Media Session Snooping on the WLAN
- C. Configure two different QoS roles for data and voice traffic
- D. Set the QoS level to platinum for voice traffic
- E. Enable traffic shaping for the LAN interface of the WLC
ANSWER: B, D

## access-112  (Question 12.14)
Refer to the exhibit.
The network engineer is configuring a new WLAN and is told to use a setup password for authentication instead of the RADIUS servers. Which additional set of tasks must the engineer perform to complete the configuration?
- A. Disable PMF Enable PSK Enable 802.1x
- B. Select WPA Policy Select WPA2 Policy Enable FT PSK
- C. Select WPA2 Policy Disable PMF Enable PSK
- D. Select WPA Policy Enable CCKM Enable PSK
ANSWER: C

## access-113  (Question 12.21)
Which channel-group mode must be configured when multiple distribution switch interfaces connected to a WLC are bundled?
- A. channel-group mode active
- B. channel-group mode on
- C. channel-group mode desirable
- D. channel-group mode passive
ANSWER: B

## access-114  (Question 12.37)
Which port type does a lightweight AP use to connect to the wired network when it is configured in local mode?
- A. access
- B. trunk
- C. EtherChannel
- D. LAG
ANSWER: A

## access-115  (Question 12.38)
Refer to the exhibit.
Cat9300-1# show interface g1/0/1 switchport
Name: Gi1/0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 321 (VLAN0321)
Administrative Native VLAN tagging: enabled
Trunking VLANs Enabled: 100,200,300
Pruning VLANs Enabled: 2-1001
A network administrator configures an interface on a new switch so that it connects to interface Gi1/0/1 on switch Cat9300-1. Which configuration must be applied to the new interface?
- A. switchport trunk encapsulation dot1q switchport trunk native vlan 321 switchport trunk allowed vlan 100-300
- B. switchport mode dynamic desirable switchport trunk native vlan 321 switchport trunk allowed vlan 100,200,300
- C. switchport nonegotiate switchport access vlan 321 switchport trunk allowed vlan except 2-1001
- D. switchport mode trunk switchport trunk native vlan 321 switchport trunk allowed vlan 100,200,300
ANSWER: D

## access-116  (Question 12.42)
Which command enables HTTP access to the Cisco WLC?
- A. config network secureweb enable
- B. config certificate generate webadmin
- C. config network webmode enable
- D. config network telnet enable
ANSWER: C

## access-117  (Question 12.44)
What is the primary purpose of a console port on a Cisco WLC?
- A. out-of-band management via an IP transport
- B. out-of-band management via an asynchronous transport
- C. in-band management via an asynchronous transport
- D. in-band management via an IP transport
ANSWER: B

## access-118  (Question 12.48)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/ea9f53807a83bf03.png]
SW_1 and SW_12 represent two companies that are merging. They use separate network vendors. The VLANs on both sides have been migrated to share IP subnets. Which command sequence must be issued on both sides to join the two companies and pass all VLANs between the companies?
- A. switchport mode trunk switchport trunk encapsulation dot1q
- B. switchport mode trunk switchport trunk allowed vlan all switchport dot1q ethertype 0800
- C. switchport mode dynamic desirable switchport trunk allowed vlan all switchport trunk native vlan 7
- D. switchport dynamic auto switchport nonegotiate
ANSWER: A

## access-119  (Question 12.52)
What are two differences between WPA2 and WPA3 wireless security? (Choose two)
- A. WPA3 uses SAE for stronger protection than WPA2, which uses AES
- B. WPA2 uses 128-bit key encryption, and WPA3 supports 128-bit and 192-bit key encryption
- C. WPA3 uses AES for stronger protection than WPA2, which uses SAE
- D. WPA3 uses AES for stronger protection than WPA2, which uses TKIP
- E. WPA2 uses 192-bit key encryption, and WPA3 requires 256-bit key encryption
ANSWER: A, B

## access-120  (Question 12.59)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e2fed7ac14e7f636.jpeg]
SW1 supports connectivity for a lobby conference room and must be secured. The engineer must limit the connectivity from PC1 to the SW1 and SW2 network. The MAC addresses allowed must be limited to two. Which configuration secures the conference room connectivity?
- A. interface gi1/0/15 switchport port-security switchport port-security mac-address 0000.abcd.0004 vlan 100
- B. interface gi1/0/15 switchport port-security mac-address 0000.abcd.0004 vlan 100
- C. interface gi1/0/15 switchport port-security mac-address 0000.abcd.0004 vlan 100 interface switchport secure-mac limit 2
- D. interface gi1/0/15 switchport port-security switchport port-security maximum 2
ANSWER: D

## access-121  (Question 12.67)
What is a reason to implement LAG on a Cisco WLC?
- A. Enable the connected switch ports to use different Layer 2 configurations.
- B. Increase the available throughput on the link.
- C. Allow for stateful failover between WLCs.
- D. Increase security by encrypting management frames.
ANSWER: B

## access-122  (Question 12.81)
When a switch receives a frame from an unknown source MAC address, which action does the switch take with the frame?
- A. It floods the frame out all interfaces, including the interface it was received on.
- B. It attempts to send the frame back to the source to ensure that the source MAC address is still available for transmissions.
- C. It sends the frame to ports within the CAM table identified with an unknown source MAC address.
- D. It associate the source MAC address with the LAN port on which it was received and saves it to the MAC address table.
ANSWER: D

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

## access-124  (Question 12.109)
How will Link Aggregation be implemented on a Cisco Wireless LAN Controller?
- A. To pass client traffic, two or more ports must be configured
- B. The EtherChannel must be configured in “mode active”
- C. When enabled, the WLC bandwidth drops to 500 Mbps
- D. One functional physical port is needed to pass client traffic
ANSWER: D

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

## access-126  (Question 12.113)
Which functionality is provided by the console connection on a Cisco WLC?
- A. secure In-band connectivity for device administration
- B. out-of-band management
- C. HTTP-based GUI connectivity
- D. unencrypted in-band connectivity for file transfers
ANSWER: B

## access-127  (Question 13.6)
Refer to Exhibit.
[IMAGE: D:\CCNA_ontap\web\img/74683b1773099bcf.png]
An engineer is building a new Layer 2 LACP EtherChannel between SW1 and SW2. and they executed the given show commands to verify the work. Which additional task must be performed so that the switches successfully bundle the second member in the LACP port-channel?
- A. Configure the switchport trunk allowed vlan 300 command on SW1 port-channel 1
- B. Configure the switchport trunk allowed vlan 300 command on interface Fa0/2 on SW1
- C. Configure the switchport trunk allowed vlan add 300 command on interface Fa0/2 on SW2
- D. Configure the switchport trunk allowed vlan add 300 command on SW1 port-channel 1
ANSWER: D

## access-128  (Question 13.18)
How does MAC learning function on a switch?
- A. broadcasts frames to all ports without queueing
- B. adds unknown source MAC addresses to the address table
- C. sends a retransmission request when a new frame is received
- D. sends frames with unknown destinations to a multicast group
ANSWER: B

## access-129  (Question 13.28)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0ba81d872ef100b0.png]
Which switch becomes the root bridge?
- A. SW 1 Bridge Priority – 32768 mac-address 0f:d7:9e:13:ab:82
- B. SW 4 Bridge Priority – 40960 mac-address 05:d8:33:09:8f:89
- C. SW3 Bridge Priority – 32768 mac-address 01:1c:6c:66:b7:70
- D. SW2 Bridge Priority – 40960 mac-address 04:44:97:51:63:17
ANSWER: C

## access-130  (Question 13.36)
What is a characteristic of an SSID in wireless networks?
- A. uses policies to prevent unauthorized users
- B. identifies an access point on a WLAN
- C. prompts a user for a login ID
- D. associates a name to a WLAN
ANSWER: D

## access-131  (Question 13.47)
What is a characteristic of an SSID in wireless networks?
- A. broadcasts a beacon signal to announce its presence by default
- B. uses policies to prevent unauthorized users
- C. converts electrical current to radio waves
- D. prompts a user for a login ID
ANSWER: A

## access-132  (Question 13.48)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/bda094608c65dfc2.png]
The P2P Blocking Action option is disabled on the WLC. The security team has a new requirement for each client to retain their assigned IP addressing as the clients move between locations in the campus network. Which action completes this configuration?
- A. Set the P2P Blocking Action option to Forward-UpStream.
- B. Enable the Static IP Tunneling option.
- C. Check the DHCP Addr. Assignment check box.
- D. Disable the Coverage Hole Detection option.
ANSWER: B

## access-133  (Question 13.52)
Which WLC interface provides out-of-band management in the Cisco Unified Wireless Network Architecture?
- A. dynamic
- B. AP-Manager
- C. virtual
- D. service port
ANSWER: D

## access-134  (Question 13.60)
What is the root port in STP?
- A. It is the port with the highest priority toward the root bridge.
- B. It is the port that is elected only when the root bridge has precisely one port on a single LAN segment.
- C. It is the port on a switch with the lowest cost to reach the root bridge.
- D. It is the port on the root switch that leads to the designated port on another switch.
ANSWER: C

## access-135  (Question 13.61)
An Ethernet frame arrived at switch interface G0/1, but the destination MAC address is missing from the MAC address table. How does the switch process the frame?
- A. It sends an ARP request to attempt to locate the destination.
- B. It updates the destination to FFFF.FFFF.FFFF.
- C. It drops the frame and notifies the sending host.
- D. It floods the frame out of the remaining switch interfaces.
ANSWER: D

## access-136  (Question 13.64)
What differentiates the Cisco OfficeExtend AP mode from FlexConnect AP mode?
- A. FlexConnect allows a personal SSID to be configured on the AP, and personal SSIDs are not supported with OfficeExtend.
- B. OfficeExtend does not support DTLS tunneling of traffic to the WLC, and FlexConnect tunnels traffic to the WLC with DTLS.
- C. OfficeExtend tunnels all traffic through the WLC, and FlexConnect terminates client traffic at the AP switch port.
- D. FlexConnect must be deployed behind a router that NATs the client traffic, and OfficeExtend uses public IP sources.
ANSWER: C

## access-137  (Question 13.79)
How is a configuration change made to a wireless AP in lightweight mode?
- A. SSH connection to the management IP of the AP
- B. HTTPS connection directly to the out-of-band address of the AP
- C. CAPWAP/LWAPP connection via the parent WLC
- D. EoIP connection via the parent WLC
ANSWER: C

## access-138  (Question 13.81)
How is noise defined in Wi-Fi?
- A. signals from other Wi-Fi networks that interfere with the local signal
- B. measured difference between the desired Wi-Fi signal and an interfering Wi-Fi signal
- C. ratio of signal-to-noise rating supplied by the wireless device
- D. any interference that is not Wi-Fi traffic that degrades the desired signal
ANSWER: D

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

## access-141  (Question 13.96)
What is the purpose of the service-set identifier?
- A. It identifies a wireless network for a mobile device to connect
- B. It identifies the wired network to which a network device is connected
- C. It identifies the wireless network to which an application must connect
- D. It identifies the wired network to which a user device is connected
ANSWER: A

## access-142  (Question 13.98)
How does a network administrator securely manage an AP in lightweight mode?
- A. using the WLC GUI via HTTPS
- B. using the CLI via an out-of-band connection
- C. using the CLI via a virtual interface with SSH
- D. using the AP GUI via an in-band SSH connection
ANSWER: A

## access-143  (Question 13.102)
Which standard is required when more than one distribution system port and only one IP address are configured for a Cisco WLC?
- A. 802.3ad
- B. 802.1q
- C. 802.1d
- D. 802.1af
ANSWER: A

## access-144  (Question 14.2)
What is a characteristic of frame switching?
- A. populates the ARP table với the egress port
- B. drops received MAC addresses not listed in the address table
- C. stores and forwards frames in a buffer and uses error checking
- D. rewrites the source and destination MAC address
ANSWER: C

## access-145  (Question 14.5)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/a9a8442b80343a6e.png]
Which switch becomes the root bridge?
- A. SW 1 Bridge Priority – 28672 mac-address 00:10:a1:51:57:51
- B. SW 2 Bridge Priority – 28672 mac-address 00:10:a1:82:03:94
- C. SW3 Bridge Priority – 12288 mac-address 00:10:a1:95:2b:77
- D. SW4 Bridge Priority – 12288 mac-address 00:10:a1:03:42:e8
ANSWER: D

## access-146  (Question 14.6)
Which two values or settings must be entered when configuring a new WLAN in the Cisco Wireless LAN Controller GUI? (Choose two)
- A. management interface settings
- B. QoS settings
- C. ip address of one or more access points
- D. SSID
- E. Profile name
ANSWER: D, E

## access-147  (Question 14.11)
What is the role of the root port in a switched network?
- A. It replaces the designated port when the designated port fails
- B. It is the best path to the root from a nonroot switch
- C. It replaces the designated port when the root port fails
- D. It is administratively disabled until a failover occurs
ANSWER: B

## access-148  (Question 14.14)
What happens when a switch receives a frame with a destination MAC address that recently aged out?
- A. The switch references the MAC address aging table for historical addresses on the port that received the frame
- B. The switch floods the frame to all ports in all VLANs except the port that received the frame
- C. The switch drops the frame and learns the destination MAC address again from the port that received the frame
- D. The switch floods the frame to all ports in the VLAN except the port that received the frame
ANSWER: D

## access-149  (Question 14.18)
A wireless access point is needed and must meet these requirements:
“zero-touch” deployed and managed by a WLC
process only real-time MAC functionality
used in a split-MAC architecture. Which access point type must be used?
- A. autonomous
- B. lightweight
- C. mesh
- D. cloud-based
ANSWER: B

## access-150  (Question 14.21)
Which interface IP address serves as the tunnel source for CAPWAP packets from the WLC to an AP?
- A. service
- B. trunk
- C. AP-manager
- D. virtual AP connection
ANSWER: C

## access-151  (Question 14.22)
What does a switch search for in the CAM table when forwarding a frame?
- A. source MAC address and aging time
- B. destination MAC address and flush time
- C. source MAC address and source port
- D. destination MAC address and destination port
ANSWER: D

## access-152  (Question 14.26)
How does MAC learning function?
- A. restricts ports to a maximum of 10 dynamically-learned addresses
- B. increases security on the management VLAN
- C. associates the MAC address with the port on which it is received
- D. drops received MAC addresses not listed in the address table
ANSWER: C

## access-153  (Question 14.33)
Which AP mode is used for capturing wireless traffic and forwarding that traffic to a PC that is running a packet analyzer?
- A. monitor
- B. sniffer
- C. bridge
- D. rouge detector
ANSWER: B

## access-154  (Question 14.34)
What is a characteristic of a Layer 2 switch?
- A. provides a single broadcast domain for all connected devices
- B. tracks the number of active TCP connections
- C. offers one collision domain for all connected devices
- D. makes forwarding decisions based on MAC addresses
ANSWER: D

## access-155  (Question 14.35)
What is a characteristic of frame switching?
- A. inspects and drops frames from unknown destinations
- B. floods unknown destinations to all ports except the receiving port
- C. forwards frames to a neighbor port using CDP
- D. protects against denial of service attacks
ANSWER: B

## access-156  (Question 14.36)
Which interface is used for out-of-band management on a WLC?
- A. dynamic
- B. management
- C. service port
- D. virtual
ANSWER: C

## access-157  (Question 14.40)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0a4de83282044a4e.png]
A Cisco WLC administrator is creating a new wireless network with enhanced SSID security. The new network must operate at 2.4 GHz with 54 Mbps of throughput. Which set of tasks must the administrator perform to complete the configuration?
- A. Check the Broadcast SSID check box and set the Radio Policy to 802.11a only.
- B. Uncheck the Broadcast SSID check box and set the Radio Policy to 802.11a/g only.
- C. Check the Broadcast SSID check box and set the Radio Policy to 802.11g only.
- D. Uncheck the Broadcast SSID check box and set the Radio Policy to 802.11g only.
ANSWER: D

## access-158  (Question 14.46)
A network architect is deciding whether to implement Cisco autonomous access points or lightweight access points. Which fact about firmware updates must the architect consider?
- A. Unlike autonomous access points, lightweight access points require a WLC to implement remote firmware updates.
- B. Unlike lightweight access points, autonomous access points can recover automatically from a corrupt firmware update
- C. Unlike lightweight access points, which require redundant WLCs to support firmware upgrades, autonomous access points require only one WLC.
- D. Unlike autonomous access points, lightweight access points store a complete copy of the current firmware for backup.
ANSWER: A

## access-159  (Question 14.52)
By default, how long will the switch continue to know a workstation MAC address after the workstation stops sending traffic?
- A. 200 seconds
- B. 300 seconds
- C. 600 seconds
- D. 900 seconds
ANSWER: B

## access-160  (Question 14.53)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3a8e4cb5e526bab0.png]
Rapid PVST+ mode is on the same VLAN on each switch. Which switch becomes the root bridge and why?
- A. SW3, because its priority is the highest
- B. SW2, because its MAC address is the highest
- C. SW4, because its priority is highest and its MAC address is lower
- D. SW1, because its priority is the lowest and its MAC address is higher
ANSWER: C

## access-161  (Question 14.56)
How does a hub handle a frame traveling to a known destination MAC address differently than a switch?
- A. The hub forwards the frame to all ports in the FIB table, and a switch forwards the frame the destination MAC is known.
- B. The hub forwards the frame to all ports, and a switch forwards the frame to the known destination.
- C. The hub forwards the frame using the information in the MAC table, and a switch uses data in its routing table.
- D. The hub forwards the frame only to the port connected to the known MAC address,and a switch forwards the frame to all ports.
ANSWER: B

## access-162  (Question 14.73)
Which connection type is used when an engineer connects to an AP without a configured IP address or dial-up number to manage the device?
- A. VIY
- B. console
- C. AUX
- D. Ethernet
ANSWER: B

## access-163  (Question 14.75)
Which type of wired port is required when an AP offers one unique SSID, passes client data and management traffic, and is in autonomous mode?
- A. default
- B. trunk
- C. access
- D. LAG
ANSWER: C

## access-164  (Question 14.80)
Refer to the exhibit.
configure terminal
interface range GigabitEthernet 0/1-2
switchport mode trunk
channel-group 1 mode active
SW2
configure terminal
interface range GigabitEthernet 0/1-2
switchport mode trunk
interface Port-channel1
switchport mode trunk
An LACP EtherChannel between two directly connected switches is in the configuration process. Which command must be configured on switch SW2s Gi0/1-2 interfaces to establish the channel to SW1?
- A. channel-group 1 mode desirable
- B. channel-group 1 mode on
- C. channel-group 1 mode active
- D. channel-group 1 mode auto
ANSWER: C

## access-165  (Question 14.85)
What is a service that is provided by a wireless controller?
- A. It issues IP addresses to wired devices.
- B. It manages interference in a dense network.
- C. It provides Layer 3 routing between wired and wireless devices.
- D. It mitigates threats from the internet.
ANSWER: B

## access-166  (Question 14.91)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/7bb8803adce3c0dc.png]
The LACP EtherChannel is configured, and the last change is to modify the interfaces on SwitchA to respond to packets received, but not to initiate negotiation. The interface range gigabitethernet0/0/0-15 command is entered. What must be configured next?
- A. SwitchA(config-if-range)#channel-group 1 mode desirable
- B. SwitchA(config-if-range)#channel-group 1 mode passive
- C. SwitchA(config-if-range)#channel-group 1 mode auto
- D. SwitchA(config-if-range)#channel-group 1 mode active
ANSWER: B

## access-167  (Question 14.93)
Which EtherChannel mode must be configured when using LAG on a WLC?
- A. On
- B. active
- C. auto
- D. passive
ANSWER: A

## access-168  (Question 14.96)
What is the maximum number of concurrent Telnet sessions that a Cisco WLC supports?
- A. 3
- B. 5
- C. 6
- D. 15
ANSWER: B

## access-169  (Question 14.101)
What is the recommended switch load-balancing mode for Cisco WLCs?
- A. source-destination MAC address
- B. destination IP address
- C. destination MAC address
- D. source-destination IP address
ANSWER: D

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

## access-171  (Question 15.7)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/2010f5d15b6efb65.png]
Which switch in this configuration will be elected as the root bridge?
- A. SW1: 0C:4A:82.:65:62:72
- B. SW2: 0C:0A:A8:1A:3C:9D
- C. SW3: 0C:0A:18:81:B3:19
- D. SW4: 0C:0A:05:22:05:97
ANSWER: D

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

## access-175  (Question 15.33)
What is the default interface for in-band wireless network management on a WLC?
- A. wireless management
- B. redundant port
- C. service port
- D. out-of-band
ANSWER: A

## access-176  (Question 15.50)
A network engineer starts to implement a new wireless LAN by configuring the authentication server and creating the dynamic interface. What must be performed next to complete the basic configuration?
- A. Install the management interface and add the management IP.
- B. Configure high availability and redundancy for the access points.
- C. Enable Telnet and RADIUS access on the management interface.
- D. Create the new WLAN and bind the dynamic interface to it.
ANSWER: D

## access-177  (Question 15.53)
Which AP feature provides a captive portal for users to authenticate register and accept terms before accessing the internet?
- A. One-Click
- B. Hotspot
- C. Enhanced Bluetooth
- D. Whole Home
ANSWER: B

## access-178  (Question 15.60)
Which AP mode serves as the primary hub in a point-to-multipoint network topology?
- A. bridge
- B. SE-Connect
- C. FlexConnect
- D. local
ANSWER: A

## access-179  (Question 15.79)
What is the maximum length of characters used in an SSID?
- A. 16
- B. 32
- C. 48
- D. 64
ANSWER: B

## access-180  (Question 15.82)
Refer to the exhibit.
SW1#show etherchannel summary
Flags:   D - down         P - in port-channel
I - stand-alone  s - suspended
H - Hot-standby (LACP only)
R - Layer3       S - Layer2
U - in use       f - failed to allocate aggregator
u - unsuitable for bundling
w - waiting to be aggregated
d - default port
A - formed by auto LAG
Number of channel-groups in use: 1
Number of aggregators: 2
Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1 (RU)        LACP       Et0/0(P)    Et0/1(P)  A network engineer is adding another physical interface as a new member to the existing Port-Channel1 bundle. Which command set must be configured on the new interface to complete the process?
- A. switchport mode trunk channel-group 1 mode active
- B. no switchport channel-group 1 mode active
- C. no switchport channel-group 1 mode on
- D. switchport switchport mode trunk
ANSWER: B

## access-181  (Question 15.87)
What is the term used to describe a method of connecting multiple switches in a network to allow traffic to flow between them, typically used for larger networks to increase bandwidth?
- A. LAG
- B. trunk
- C. EtherChannel
- D. access
ANSWER: B

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

## access-183  (Question 16.2)
Which default condition must be considered when an encrypted mobility tunnel is used between two Cisco WLCs?
- A. The tunnel uses the EoIP protocol to transmit data traffic.
- B. TCP port 443 and UDP 21 are used.
- C. The tunnel uses the IPsec protocol for encapsulation.
- D. Control and data traffic encryption are enabled.
ANSWER: D

## access-184  (Question 16.10)
Which AP mode wirelessly connects two separate network segments each set up within a different campus building?
- A. mesh
- B. local
- C. bridge
- D. point-to-point
ANSWER: C

## access-185  (Question 16.16)
Which IP address is used when an administrator must open a web-based management session with a lightweight AP?
- A. WLC IP
- B. gateway IP
- C. autonomous AP IP
- D. ACS IP
ANSWER: A

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

## access-187  (Question 16.28)
What is a characteristic of a Layer 2 switch?
- A. transfers all frames received to every connected device
- B. maintains stateful transaction information
- C. offers link bundling to servers
- D. transmits exclusively at half duplex
ANSWER: C

## access-188  (Question 16.35)
Which interface is used by an administrator to access the WLC GUI to update configuration settings?
- A. management
- B. service
- C. dynamic
- D. virtual
ANSWER: A

## access-189  (Question 16.36)
A switch receives a frame with the destination MAC address
Switch# show ethernet-frame-and-mac-address-table
Ethernet Frame:
+----------------------------------------------------+
| Destination MAC Address: 3C:5D:7E:9F:1A:2B         |
| Source MAC Address: D3:F4:47:57:67:46              |
| EtherType/Length: 0x0800 (IPv4)                    |
| Payload: [Data]                                    |
| Frame Check Sequence: [CRC]                        |
+----------------------------------------------------+
MAC Address Table:
VLAN   MAC Address         Type      Ports
----   -----------------   --------  ----------
12     D3:F4:47:57:67:46   Dynamic   Gi1/0/1
16     20:31:42:53:64:DE   Static    Gi1/0/2
24     A0:B3:C4:D3:B4:48   Secure    Gi1/0/3
31     B5:16:32:12:6B:68   Dynamic   Gi1/0/4
44     8F:A0:B3:C4:34:50   Static    Gi1/0/5
How does the switch handle the frame?
- A. It floods the frame to all ports except the incoming port.
- B. It switches the frame to a predetermined port based on settings.
- C. It ages out the frame until the MAC address becomes known.
- D. It drops the frame to avoid unnecessary network congestion.
ANSWER: A

## access-190  (Question 16.46)
Which switch port configuration must be configured when connected to an AP running in FlexConnect mode, and the WLANs use flex local switching?
- A. access port with one VLAN
- B. trunk port with pruned VLANs
- C. Layer 3 port with an IP address
- D. tagged port with MAC Filtering enabled
ANSWER: B

## access-191  (Question 16.53)
Which option in the port configuration of an Ethernet switch allows traffic from multiple VLANs to travel over the same physical link?
- A. LAG
- B. EtherChannel
- C. trunk
- D. access
ANSWER: C

## access-192  (Question 16.62)
What is a characteristic of a Layer 2 switch?
- A. maintains stateful transaction information
- B. prioritizes traffic using deep packet inspection
- C. uses the data link layer for communications
- D. provides a-single broadcast domain for all connected devices
ANSWER: C

## access-193  (Question 16.71)
What is the role of nonoverlapping channels in a wireless environment?
- A. to reduce interference
- B. to allow for channel bonding
- C. to enable faster roaming
- D. to increase bandwidth
ANSWER: A

## access-194  (Question 16.75)
Which AP mode provides a wireless connection between two network segments?
- A. root
- B. local
- C. FlexConnect
- D. bridge
ANSWER: D
