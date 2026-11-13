# IP Services (part 1)

## ipsvc-1  (Question 5.1)
Which two QoS tools are used to guarantee minimum bandwidth to certain traffic? (Choose two)
- A. FIFO
- B. CBWFQ
- C. LLC
- D. WFQ
- E. RSVP
ANSWER: B, E

## ipsvc-2  (Question 5.14)
A network administrator must enable DHCP services between two sites. What must be configured for the router to pass DHCPDISCOVER messages on to the server?
- A. a DHCP Relay Agent
- B. DHCP Binding
- C. a DHCP Pool
- D. DHCP Snooping
ANSWER: A

## ipsvc-3  (Question 5.22)
What does a router do when configured with the default DNS lookup settings, and a URL is entered on the CLI?
- A. initiates a ping request to the URL
- B. prompts the user to specify the desired IP address
- C. continuously attempts to resolve the URL until the command is cancelled
- D. sends a broadcast message in an attempt to resolve the URL
ANSWER: D

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

## ipsvc-5  (Question 5.28)
Which protocol does an IPv4 host use to obtain a dynamically assigned IP address?
- A. ARP
- B. DNS
- C. CDP
- D. DHCP
ANSWER: D

## ipsvc-6  (Question 5.30)
Which condition must be met before an NMS handles an SNMP trap from an agent?
- A. The NMS must be configured on the same router as the SNMP agent
- B. The NMS must receive a trap and an inform message from the SNMP agent within a configured interval
- C. The NMS software must be loaded with the MIB associated with the trap
- D. The NMS must receive the same trap from two different SNMP agents to verify that it is reliable
ANSWER: C

## ipsvc-7  (Question 5.38)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/8e8a3ffa014021f6.jpeg]
The ntp server 192.168.0.3 command has been configured on Router1 to make it an NTP client of router 2. Which command must be configured on Router2 so that it operates in server-only mode and relies only on its internal clock?
- A. Router2(config)#ntp passive
- B. Router2(config)#ntp master 4
- C. Router2(config)#ntp server 172.17.0.1
- D. Router2(config)#ntp server 192.168.0.2
ANSWER: B

## ipsvc-8  (Question 5.41)
When DHCP is configured on a router, which command must be entered so the default gateway is automatically distributed?
- A. default-router
- B. default-gateway
- C. ip helper-address
- D. dns-server
ANSWER: A

## ipsvc-9  (Question 6.23)
Which two QoS tools provides congestion management? (Choose two)
- A. FRTS
- B. CAR
- C. PQ
- D. PBR
- E. CBWFQ
ANSWER: C, E

## ipsvc-10  (Question 7.1)
Which level of severity must be set to get informational syslogs?
- A. alert
- B. critical
- C. notice
- D. debug
ANSWER: D

## ipsvc-11  (Question 7.3)
A network analyst is tasked with configured the date and time on a router using EXEC mode. The date must be set to 12:00am. Which command should be used?
- A. Clock timezone
- B. Clock summer-time-recurring
- C. Clock summer-time date
- D. Clock set
ANSWER: D

## ipsvc-12  (Question 7.17)
Which protocol requires authentication to transfer a backup configuration file from a router to a remote server?
- A. TFTP
- B. FTP
- C. DTP
- D. SMTP
ANSWER: B

## ipsvc-13  (Question 7.31)
When a client and server are not on the same physical network, which device is used to forward requests and replies between client and server for DHCP?
- A. DHCP relay agent
- B. DHCP server
- C. DHCPDISCOVER
- D. DHCPOFFER
ANSWER: A

## ipsvc-14  (Question 7.34)
Which QoS tool can you use to optimize voice traffic on a network that is primarily intended for data traffic?
- A. WRED
- B. FIFO
- C. PQ
D.WFQ
ANSWER: C

## ipsvc-15  (Question 7.35)
On workstations running Microsoft Windows, which protocol provides the default gateway for the device?
- A. STP
- B. DNS
- C. SNMP
- D. DHCP
ANSWER: D

## ipsvc-16  (Question 7.45)
How does QoS optimize voice traffic?
- A. reducing bandwidth usage
- B. by reducing packet loss
- C. by differentiating voice and video traffic
- D. by increasing jitter
ANSWER: C

## ipsvc-17  (Question 8.11)
In QoS, which prioritization method is appropriate for interactive voice and video?
- A. expedited forwarding
- B. traffic policing
- C. round-robin scheduling
- D. low-latency queuing
ANSWER: D

## ipsvc-18  (Question 8.14)
What is a syslog facility?
- A. host that is configured for the system to send log messages
- B. password that authenticates a Network Management System to receive log messages
- C. group of log messages associated with the configured severity level
- D. set of values that represent the processes that can generate a log message
ANSWER: D

## ipsvc-19  (Question 8.18)
What is a capability of FTP in network management operations?
- A. uses separate control and data connections to move files between server and client
- B. devices are directly connected and use UDP to pass file information
- C. encrypts data before sending between data resources
- D. offers proprietary support at the session layer when transferring data
ANSWER: A

## ipsvc-20  (Question 8.33)
What is a DNS lookup operation?
- A. serves requests over destination port 53
- B. DNS server pings the destination to verify that it is available
- C. DNS server forwards the client to an alternate IP address when the primary IP is down
- D. responds to a request for IP address to domain name resolution to the DNS server
ANSWER: A

## ipsvc-21  (Question 8.36)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/0afc6c998d119de6.jpeg]
The DHCP server and clients are connected to the same switch. What is the next step to complete the DHCP configuration to allow clients on VLAN 1 to receive addresses from the DHCP server?
- A. Configure the ip dhcp snooping trust command on the interface that is connected to the DHCP server
- B. Configure the ip dhcp relay information option command on the interface that is connected to the DHCP server
- C. Configure the ip dhcp relay information option command on the interface that is connected to the DHCP client
- D. Configure the ip dhcp snooping trust command on the interface that is connected to the DHCP client
ANSWER: A

## ipsvc-22  (Question 8.44)
Refer to the exhibit.
[TABLE]
interface FastEthernet0/10
description WAN_INTERFACE 
ip address 10.0.1.2 255.255.255.252 
ip access-group 100 in
!
interface FastEthernet0/1 
description LAN INTERFACE 
ip address 10.148.2.1 255.255.255.0
duplex auto
speed auto
!
ip forward-protocol nd
!
access-list 100 permit eigrp any any 
access-list 100 permit icmp any any
access-list 100 permit tcp 10.149.3.0 0.0.0.255 host 10.0.1.2 eq 22 
access-list 100 permit tcp any any eq 80 
access-list 100 permit tcp any any eq 443
access-list 100 deny ip any any log
[/TABLE]
Which configuration enables DHCP addressing for hosts connected to interface FastEthernet0/1 on router R4?
- A. interface FastEthernet0/1
ip helper-address 10.0.1.1
!
access-list 100 permit tcp host 10.0.1.1 eq 67 host 10.148.2.1
- B. interface FastEthernet0/0
ip helper-address 10.0.1.1
!
access-list 100 permit host 10.0.1.1 host 10.148.2.1 eq bootps
- C. interface FastEthernet0/0
ip helper-address 10.0.1.1
!
access-list 100 permit udp host 10.0.1.1 eq bootps host 10.148.2.1
- D. interface FastEthernet0/1
ip helper-address 10.0.1.1
!
access-list 100 permit udp host 10.0.1.1 eq bootps host 10.148.2.1
ANSWER: D

## ipsvc-23  (Question 8.74)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/a7444ab5f589a4bb.jpeg]
How should the configuration be updated to allow PC1 and PC2 access to the Internet?
- A. Modify the configured number of the second access list
- B. Remove the overload keyword from the ip nat inside source command
- C. Add either the ip nat {inside|outside} command under both interfaces
- D. Change the ip nat inside source command to use interface GtgabitEthernet0/0
ANSWER: C

## ipsvc-24  (Question 8.79)
What is the purpose of the ip address dhcp command?
- A. to configure an interface as a DHCP server
- B. to configure an interface as a DHCP relay
- C. to configure an interface as a DHCP helper
- D. to configure an interface as a DHCP client
ANSWER: D

## ipsvc-25  (Question 8.82)
A network engineer is installing an IPv6-only capable device. The client has requested that the device IP address be reachable only from the internal network. Which type of IPv6 address must the engineer assign?
- A. unique local address
- B. link-local address
- C. IPv4-compatibie IPv6 address
- D. aggregatable global address
ANSWER: A

## ipsvc-26  (Question 9.10)
R1 as an NTP server must have:
* NTP authentication enabled
* NTP packets sourced from Interface loopback 0
* NTP stratum 2
* NTP packets only permitted to client IP 209.165.200.225
How should R1 be configured?
[TABLE]
Option A
ntp authenticate
ntp authentication-key 2 sha1 CISCO123
ntp source Loopback0
ntp access-group server-only 10
ntp master 2
!
access-list 10 permit udp host 209.165.200.225 any eq 123 | Option B
ntp authenticate
ntp authentication-key 2 md5 CISCO123
ntp source Loopback0
ntp access-group server-only 10
ntp stratum 2
!
access-list 10 permit udp host 209.165.200.225 any eq 123
---
Option C
ntp authenticate
ntp authentication-key 2 md5 CISCO123
ntp interface Loopback0
ntp access-group server-only 10
ntp stratum 2
!
access-list 10 permit 209.165.200.225 | Option D
ntp authenticate
ntp authentication-key 2 md5 CISCO123
ntp source Loopback0
ntp access-group server-only 10
ntp master 2
!
access-list 10 permit 209.165.200.225
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: D

## ipsvc-27  (Question 9.26)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/998d1b383987e8e7.jpeg]
An engineer is configuring a new router on the network and applied this configuration. Which additional configuration allows the PC to obtain its IP address from a DHCP server?
- A. Configure the ip dhcp relay information command under interface Gi0/1
- B. Configure the ip dhcp smart-relay command globally on the router
- C. Configure the ip helper-address 172.16.2.2 command under interface Gi0/0
- D. Configure the ip address dhcp command under interface Gi0/0
ANSWER: C

## ipsvc-28  (Question 9.34)
Which QoS per-hop behavior changes the value of the ToS field in the IPv4 packet header?
- A. shaping
- B. marking
- C. policing
- D. classification
ANSWER: B

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

## ipsvc-30  (Question 9.50)
Which QoS traffic handling technique retains excess packets in a queue and reschedules these packets for later transmission when the configured maximum bandwidth has been surpassed?
- A. traffic shaping
- B. traffic policing
- C. weighted random early detection
- D. traffic prioritization
ANSWER: A

## ipsvc-31  (Question 9.67)
Which QoS queuing method discards or marks packets that exceed the desired bit rate of traffic flow?
- A. shaping
- B. policing
- C. CBWFQ
- D. LLQ
ANSWER: B

## ipsvc-32  (Question 9.82)
How does TFTP operate in a network?
- A. relies on the well-known TCP port 20 to transmit data
- B. requires two separate connections for control and data traffic
- C. uses block numbers to identify and mitigate data-transfer errors
- D. provides secure data transfer
ANSWER: C

## ipsvc-33  (Question 9.86)
An engineer is configuring switch SW1 to act as an NTP server when all upstream NTP server connectivity fails. Which configuration must be used?
- A. SW1# config t
SW1(config)#ntp server 192.168.1.1
SW1(config)#ntp access-group server accesslist1
- B. SW1# config t
SW1(config)3 ntp peer 192.168.1.1
SW1(config)#ntp access-group peer accesslist1
- C. SW1# config t
SW1(config)#ntp backup
SW1(config)#ntp server 192.168.1.1
- D. SW1# config t
SW1(config)#ntp master
SW1(config)#ntp server 192.168.1.1
ANSWER: D

## ipsvc-34  (Question 9.100)
What is a function performed by a web server?
- A. provide an application that is transmitted over HTTP
- B. send and retrieve email from client devices
- C. securely store files for FTP access
- D. authenticate and authorize a user’s identity
ANSWER: A

## ipsvc-35  (Question 10.19)
What is a feature of TFTP?
- A. provides secure data transfer
- B. relies on the well-known TCP port 20 to transmit data
- C. uses two separate connections for control and data traffic
- D. offers anonymous user login ability
ANSWER: D

## ipsvc-36  (Question 10.21)
Which command creates a static NAT binding for a PC address of 10.1.1.1 to the public routable address 209.165.200.225 assigned to the PC?
- A. R1(config)#ip nat outside source static 209.165.200.225 10.1.1.1
- B. R1(config)#ip nat inside source static 209.165.200.225 10.1.1.1
- C. R1(config)#ip nat outside source static 10.1.1.1 209.165.200.225
- D. R1(config)#ip nat inside source static 10.1.1.1 209.165.200.225
ANSWER: D

## ipsvc-37  (Question 10.33)
Which command implies the use of SNMPv3?
- A. snmp-server community
- B. snmp-server host
- C. snmp-server enable traps
- D. snmp-server user
ANSWER: D

## ipsvc-38  (Question 10.43)
What are two features of the DHCP relay agent? (Choose two)
- A. minimizes the necessary number of DHCP servers
- B. assigns DNS locally and then forwards request to DHCP server
- C. is configured under the Layer 3 interface of a router on the client subnet
- D. allows only MAC-to-IP reservations to determine the local subnet of a client
- E. permits one IP helper command under an individual Layer 3 interface
ANSWER: A, C

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

## ipsvc-40  (Question 10.92)
Which two actions are taken as the result of traffic policing? (Choose two)
- A. bursting
- B. fragmentation
- C. dropping
- D. remarking
- E. buffering
ANSWER: C, D

## ipsvc-41  (Question 11.4)
What is a purpose of traffic shaping?
- A. It enables dynamic flow identification.
- B. It enables policy-based routing.
- C. It provides best-effort service.
- D. It limits bandwidth usage.
ANSWER: D

## ipsvc-42  (Question 11.9)
What is the purpose of configuring different levels of syslog for different devices on the network?
- A. to rate-limit messages for different severity levels from each device
- B. to set the severity of syslog messages from each device
- C. to identify the source from which each syslog message originated
- D. to control the number of syslog messages from different devices that are stored locally
ANSWER: B

## ipsvc-43  (Question 11.17)
Which two features introduced in SNMPv2 provide the ability to retrieve large amounts of data in one request? (Choose two)
- A. Get
- B. GetNext
- C. Set
- D. GetBulk
- E. Inform
ANSWER: D, E

## ipsvc-44  (Question 11.23)
Which type of address is shared by routers in a HSRP implementation and used by hosts on the subnet as their default gateway address?
- A. multicast address
- B. loopback IP address
- C. virtual IP address
- D. broadcast address
ANSWER: C

## ipsvc-45  (Question 11.40)
Which is a fact related to FTP?
- A. It uses block numbers to identify and mitigate data-transfer errors
- B. It always operates without user authentication
- C. It relies on the well-known UDP port 69.
- D. It uses two separate connections for control and data traffic
ANSWER: D

## ipsvc-46  (Question 11.52)
Which QoS feature drops traffic that exceeds the committed access rate?
- A. weighted fair queuing
- B. FIFO
- C. shaping
- D. policing
ANSWER: D

## ipsvc-47  (Question 12.25)
Which two server types support domain name to IP address resolution? (Choose two)
- A. ESX host
- B. web
- C. resolver
- D. authoritative
- E. file transfer
ANSWER: C, D

## ipsvc-48  (Question 12.46)
What does the implementation of a first-hop redundancy protocol protect against on a network?
- A. BGP neighbor flapping
- B. default gateway failure
- C. root-bridge loss
- D. spanning-tree loops
ANSWER: B

## ipsvc-49  (Question 12.55)
Which two transport layer protocols carry syslog messages? (Choose two)
- A. TCP
- B. UDP
- C. ARP
- D. RTP
- E. IP
ANSWER: A, B

## ipsvc-50  (Question 12.62)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/99789725229275d6.png]
The DHCP server is configured with a DHCP pool for each of the subnets represented. Which command must be configured on switch SW1 to allow DHCP clients on VLAN 10 to receive dynamic IP addresses from the DHCP server?
- A. SW1(config-if)#ip helper-address 192.168.10.2
- B. SW1(config-if)#ip helper-address 192.168.20.1
- C. SW1(config-if)#ip helper-address 192.168.20.2
- D. SW1(config-if)#ip helper-address 192.168.10.1
ANSWER: C

## ipsvc-51  (Question 12.85)
The clients and DHCP server reside on different subnets. Which command must be used to forward requests and replies between clients on the 10.10.0.1/24 subnet and the DHCP server at 192.168.10.1?
- A. ip route 192.168.10.1
- B. ip helper-address 192.168.10.1
- C. ip dhcp address 192.168.10.1
- D. ip default-gateway 192.168.10.1
ANSWER: B

## ipsvc-52  (Question 12.105)
What is the role of community strings in SNMP operations?
- A. It serves as a sequence tag on SNMP traffic messages.
- B. It serves as a password to protect access to MIB objects.
- C. It passes the Active Directory username and password that are required for device access.
- D. It translates alphanumeric MIB output values to numeric values.
ANSWER: B

## ipsvc-53  (Question 13.11)
Which Cisco proprietary protocol ensures traffic recovers immediately, transparently, and automatically when edge devices or access circuits fail?
- A. SLB
- B. FHRP
- C. VRRP
- D. HSRP
ANSWER: D

## ipsvc-54  (Question 13.19)
What is the purpose of classifying network traffic in QoS?
- A. services traffic according to its class
- B. identifies the type of traffic that will receive a particular treatment
- C. writes the class identifier of a packet to a dedicated field in the packet header
- D. configures traffic-matching rules on network devices
ANSWER: B

## ipsvc-55  (Question 13.69)
What are two purposes of HSRP? (Choose two)
- A. It groups two or more routers to operate as one virtual router.
- B. It improves network availability by providing redundant gateways.
- C. It passes configuration information to hosts in a TCP/IP network.
- D. It helps hosts on the network to reach remote subnets without a default gateway.
- E. It provides a mechanism for diskless clients to autoconfigure their IP parameters during boot.
ANSWER: A, B

## ipsvc-56  (Question 13.71)
A DHCP pool has been created with the name NOCC. The pool is using 192.168.20.0/24 and must use the next to last usable IP address as the default gateway for the DHCP clients. What is the next step in the process?
- A. default-router 192.168.20.253
- B. network 192.168.20.254 255.255.255.0 secondary
- C. ip default-gateway 0.0.0.0 0.0.0.0 192.168.20.253
- D. next-server 192.168.20.254
ANSWER: A

## ipsvc-57  (Question 13.72)
What is the role of SNMP in the network?
- A. to monitor network devices and functions using a TCP underlay that operates on the presentation layer
- B. to collect data directly from network devices using an SSL underlay that operates on the transport layer
- C. to monitor and manage network devices using a UDP underlay that operates on the application layer
- D. to collect telemetry and critical information from network devices using an SSH underlay that operates on the network layer
ANSWER: C

## ipsvc-58  (Question 13.75)
What are two reasons to implement DHCP in a network? (Choose two)
- A. manually control and configure IP addresses on network devices
- B. reduce administration time in managing IP address ranges for clients
- C. control the length of time an IP address is used by a network device
- D. dynamic control over the best path to reach an IP address
- E. access a website by name instead of by IP address
ANSWER: B, C

## ipsvc-59  (Question 13.76)
What does traffic shaping do?
- A. It modifies the QoS attributes of a packet
- B. It sets QoS attributes within a packet
- C. It queues excess traffic
- D. It organizes traffic into classes
ANSWER: C

## ipsvc-60  (Question 13.99)
Which protocol is implemented when an organization must verify network performance, troubleshoot issues and use an agent to communicate between monitoring tools and end devices?
- A. FTP
- B. NTP
- C. NFS
- D. SNMP
ANSWER: D

## ipsvc-61  (Question 14.15)
What is used to identify spurious DHCP servers?
- A. DHCPREQUEST
- B. DHCPDISCOVER
- C. DHCPACK
- D. DHCPOFFER
ANSWER: B

## ipsvc-62  (Question 14.16)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/c808af92088ac28c.png]
Which per-hop QoS behavior is R1 applying to incoming packets?
- A. queuing
- B. marking
- C. shaping
- D. policing
ANSWER: A

## ipsvc-63  (Question 14.47)
A DHCP pool has been created with the name CONTROL. The pool uses the next to last usable IP address as the default gateway for the DHCP clients. The server is located at 172.16.32.15. What is the next step in the process for clients on the 192.168.52.0/24 subnet to reach the DHCP server?
- A. ip forward-protocol udp 137
- B. ip default-network 192.168.52.253
- C. ip default-gateway 192.168.52.253
- D. ip helper-address 172.16.32.15
ANSWER: D

## ipsvc-64  (Question 14.71)
Which capability does TFTP provide?
- A. loads configuration files on systems without data storage devices
- B. provides secure file access within the LAN
- C. provides encryption mechanisms for file transfer across a WAN
- D. provides authentication for data communications over a private data network
ANSWER: A

## ipsvc-65  (Question 14.81)
An on-site service desk technician must verify the IP address and DNS server information on a user’s Windows computer. Which command must the technician enter at the command prompt on the user’s computer?
- A. ipconfig /all
- B. show interface
- C. netstat -r
- D. ifconfig -a
ANSWER: A

## ipsvc-66  (Question 14.82)
What are two functions of DHCP servers? (Choose two)
- A. support centralized IP management
- B. issue DHCPDISCOVER messages when added to the network
- C. respond to client DHCPOFFER requests by Issuing an IP address
- D. prevent users from assigning their own IP addresses to hosts
- E. assign dynamic IP configurations to hosts in a network
ANSWER: A, E

## ipsvc-67  (Question 14.83)
Which SNMP message type is reliable and precedes an acknowledgment response from the SNMP manager?
- A. Inform
- B. Get
- C. Traps
- D. Set
ANSWER: A

## ipsvc-68  (Question 14.87)
Refer to the exhibit.
wireless LAN adapter Wi-Fi
Connection-specific DNS Suffix
Description ..........         : Intel(R) dual Band wireless-AC 7265
Physical Address........       : C8-21-5B-B4-D3-E0
DHCP Enabled..........	       : YES
Autoconfiguration Enabled . . .: YES
Link-local IPv6 Address . . . .: fe80::45a1:b3fa:2f37:bf37%2(Preferred)
IPv4 Address..........	       : 192.168.25.103((Preferred)
Subnet Mask..........          : 255.255.255.0
Lease Obtained.........	       : June 11, 2019 10:21:31 AM
Lease Expires .........        : June 12, 2019 10:21:36 AM
Default Gateway ........       : 192.168.25.1
DHCP Server ..........	       : 192.168.25.100
DHCPV6 IAID..........	       : 46670168
DHCPv6 Client DUID.......      : 00-01-00-20-FF-05-55-3C-52-82-33-D3-84
DNS Servers ..........	       : 192.168.25.254
Which address will the client contact to renew their IP address when the current lease expires?
- A. 192.168.25.103
- B. 192.168.25.100
- C. 192.168.25.1
- D. 192.168.25.254
ANSWER: B

## ipsvc-69  (Question 14.103)
What is a function of FTP?
- A. relies on the well-known UDP port 69 for data transfer
- B. uses block numbers to identify and mitigate data-transfer errors
- C. uses two separate connections for control and data traffic
- D. always operates without user connection validation
ANSWER: C

## ipsvc-70  (Question 15.14)
Which protocol should be used to transfer large files on a company intranet that allows TCP 20 and 21 through the firewall?
- A. FTP
- B. REST API
- C. TFTP
- D. SMTP
ANSWER: A

## ipsvc-71  (Question 15.60)
A network engineer must replicate the AccessSw1 NTP configuration on a new switch. The engineer could not access privileged mode on AccessSw1 to view its configuration. Which command must be applied to the new switch to replicate the configuration?
- A. ntp server 2001:db8:12::1
- B. ntp master 3
- C. ntp master
- D. ntp server 127.127.1.1
ANSWER: A

## ipsvc-72  (Question 15.63)
Which file transfer protocol omits a username or password requirement and acknowledges all data sent?
- A. FTP
- B. TFTP
- C. SCP
- D. SFTP
ANSWER: B

## ipsvc-73  (Question 15.76)
What is the purpose of a CNAME record?
- A. to associate an alias to a canonical domain name
- B. to map a domain name to an IP address
- C. to identify the authoritative name server for a domain
- D. to direct email to a mail server
ANSWER: A

## ipsvc-74  (Question 15.81)
Why would a network administrator implement the HSRP protocol?
- A. To provide network redundancy in the case of a router failure
- B. To use an open standard protocol that is configured on Cisco and third-party routers
- C. To allow hosts in a network to use the same default gateway virtual IP when load-balancing traffic
- D. To allow clients to be configured with multiple default gateway IPs
ANSWER: A

## ipsvc-75  (Question 15.97)
Which command must be entered to configure a DHCP relay?
- A. ip helper-address
- B. ip address dhcp
- C. ip dhcp relay
- D. ip dhcp pool
ANSWER: A

## ipsvc-76  (Question 15.110)
Which technology must be implemented to configure network device monitoring with the highest security?
- A. SNMPv3
- B. IP SLA
- C. NetFlow
- D. syslog
ANSWER: A

## ipsvc-77  (Question 15.116)
An engineer is configuring NAT to translate the source subnet of 10.10.0.0/24 to any one of three addresses: 192.168.3.1, 192.168.3.2, or 192.168.3.3. Which configuration must be used?
Option A enable configure terminal ip nat pool mypool 192.168.3.1 192.168.3.3 prefix-length 30 access-list 1 permit 10.10.0.0 0.0.0.255 ip nat outside source list 1 pool mypool interface g1/1 ip nat inside interface g1/2 ip nat outside
Option B enable configure terminal ip nat pool mypool 192.168.3.1 192.168.3.3 prefix-length 30 access-list 1 permit 10.10.0.0 0.0.0.254 ip nat outside source list 1 pool mypool interface g1/1 ip nat inside interface g1/2 ip nat outside
Option C enable configure terminal ip nat pool mypool 192.168.3.1 192.168.3.3 prefix-length 30 access-list 1 permit 10.10.0.0 0.0.0.255 ip nat inside source list 1 pool mypool interface g1/1 ip nat inside interface g1/2 ip nat outside
Option D enable configure terminal ip nat pool mypool 192.168.3.1 192.168.3.3 prefix-length 30 access-list 1 permit 10.10.0.0 0.0.0.254 ip nat inside source list 1 pool mypool interface g1/1 ip nat inside interface g1/2 ip nat outside
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: C

## ipsvc-78  (Question 15.118)
How does HSRP provide first hop redundancy?
- A. It load-balances traffic by assigning the same metric value to more than one route to the same destination in the IP routing table
- B. It load-balances Layer 2 traffic along the path by flooding traffic out all interfaces configured with the same VLAN
- C. It forwards multiple packets to the same destination over different routed links and data path
- D. It uses a shared virtual MAC and a virtual IP address to a group of routers that serve as the default gateway for hosts on a LAN
ANSWER: D

## ipsvc-79  (Question 15.119)
What is a function of TFTP in network operations?
- A. transfers a configuration files from a server to a router on a congested link
- B. transfers IOS images from a server to a router for firmware upgrades
- C. transfers a backup configuration file from a server to a switch using a username and password
- D. transfers files between file systems on a router
ANSWER: B

## ipsvc-80  (Question 16.12)
Which action prevents debug messages from being sent via syslog while allowing other messages when an abnormally high number of syslog messages are generated by a device with the debug process turned on?
- A. Use an access list to filter out the syslog messages.
- B. Turn off the logging monitor in global configuration mode.
- C. Disable logging to the console.
- D. Set the logging trap severity level to informational.
ANSWER: D

## ipsvc-81  (Question 16.13)
Which interface on the WLC is used exclusively as a DHCP relay?
- A. distribution
- B. service
- C. AP-manager
- D. virtual
ANSWER: D

## ipsvc-82  (Question 16.17)
Which two statements about traffic shaping and policing are true? (Choose two)
- A. Policing levels out traffic bursts by delaying excess traffic.
- B. Shaping is performed in the inbound and outbound directions.
- C. Shaping drops excessive traffic without adding traffic delay.
- D. Shaping levels out traffic bursts by delaying excess traffic.
- E. Policing is performed in the inbound and outbound directions.
ANSWER: D, E

## ipsvc-83  (Question 16.47)
What is a reason to implement HSRP on a network?
- A. to ensure that user traffic in a LAN rapidly recovers from the failure of an edge routing device
- B. to provide load balancing over multiple gateways in a LAN network
- C. to optimally route traffic based on the forwarding capacity of the edge routing devices in the LAN network
- D. to identify the closest hop to the default gateway in a LAN network
ANSWER: A

## ipsvc-84  (Question 15.4)
A network engineer is configuring a new router at a branch office. The router is connected to an upstream WAN network that allows the branch to communicate with the head office. The central time server with IP address 172.24.54.8 is located behind a firewall at the head office. Which command must the engineer configure so that the software clock of the new router synchronizes with the time server?
- A. ntp client 172.24.54.8
- B. ntp master 172.24.54.8
- C. ntp peer 172.24.54.8
- D. ntp server 172.24.54.8
ANSWER: D

## ipsvc-85  (Question 15.14)
Which protocol should be used to transfer large files on a company intranet that allows TCP 20 and 21 through the firewall?
- A. FTP
- B. REST API
- C. TFTP
- D. SMTP
ANSWER: A

## ipsvc-86  (Question 15.30)
Which function does an iterative DNS query serve in the domain name resolution process?
- A. Encrypt communication automatically between DNS clients and servers.
- B. Allow a DNS client to contact several DNS servers until the correct information is found.
- C. Obtain information directly from all root DNS servers configured within the scope.
- D. Update records dynamically across multiple DNS servers at the same time.
ANSWER: B

## ipsvc-87  (Question 15.65)
What is the role of syslog level 7 in network device health monitoring?
- A. It provides information about error conditions visible on the network device.
- B. It shares normal operational messages from the network equipment.
- C. It sends outputs from various debug commands on the device.
- D. It warns about emergency conditions on the network appliance.
ANSWER: C

## ipsvc-88  (Question 15.81)
Why would a network administrator implement the HSRP protocol?
- A. To provide network redundancy in the case of a router failure
- B. To use an open standard protocol that is configured on Cisco and third-party routers
- C. To allow hosts in a network to use the same default gateway virtual IP when load-balancing traffic
- D. To allow clients to be configured with multiple default gateway IPs
ANSWER: A

## ipsvc-89  (Question 15.97)
Which command must be entered to configure a DHCP relay?
- A. ip helper-address
- B. ip address dhcp
- C. ip dhcp relay
- D. ip dhcp pool
ANSWER: A

## ipsvc-90  (Question 15.118)
How does HSRP provide first hop redundancy?
- A. It load-balances traffic by assigning the same metric value to more than one route to the same destination in the IP routing table
- B. It load-balances Layer 2 traffic along the path by flooding traffic out all interfaces configured with the same VLAN
- C. It forwards multiple packets to the same destination over different routed links and data path
- D. It uses a shared virtual MAC and a virtual IP address to a group of routers that serve as the default gateway for hosts on a LAN
ANSWER: D

## ipsvc-91  (Question 15.119)
What is a function of TFTP in network operations?
- A. transfers a configuration files from a server to a router on a congested link
- B. transfers IOS images from a server to a router for firmware upgrades
- C. transfers a backup configuration file from a server to a switch using a username and password
- D. transfers files between file systems on a router
ANSWER: B

## ipsvc-92  (Question 16.13)
Which interface on the WLC is used exclusively as a DHCP relay?
- A. distribution
- B. service
- C. AP-manager
- D. virtual
ANSWER: D

## ipsvc-93  (Question 16.23)
What is a functionality of HSRP?
- A. It provides router redundancy and route reconvergence when a router fails.
- B. It enlists gratuitous ARP to update a client’s ARP cache when the active router switches over.
- C. It requires active and standby routes to provide failover in the case of a router failure.
- D. It uses virtual MAC addressing to provide gateway redundancy on a LAN.
ANSWER: D

## ipsvc-94  (Question 16.47)
What is a reason to implement HSRP on a network?
- A. to ensure that user traffic in a LAN rapidly recovers from the failure of an edge routing device
- B. to provide load balancing over multiple gateways in a LAN network
- C. to optimally route traffic based on the forwarding capacity of the edge routing devices in the LAN network
- D. to identify the closest hop to the default gateway in a LAN network
ANSWER: A

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

## ipsvc-96  (Question 16.63)
Which file transfer protocol omits a username or password requirement and acknowledges all data sent?
- A. FTP
- B. TFTP
- C. SCP
- D. SFTP
ANSWER: B

## ipsvc-97  (Question 16.64)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/9fec119f7a8438bc.png]
A network engineer must configure the CPE router to allow computers in the 172.20.1.0/24 network to obtain their IP configurations from the central DHCP server. Which configuration must the engineer apply to the CPE?
- A. interface GigabitEthernet0/1 ip helper-address 172.20.255.11
- B. interface GigabitEthernet0/0 ip helper-address 172.20.255.1
- C. interface GigabitEthernet0/0 ip helper-address 172.20.1.1
- D. interface GigabitEthernet0/1 ip helper-address 172.20.254.1
ANSWER: A

## ipsvc-98  (Question 16.76)
What is the purpose of a CNAME record?
- A. to associate an alias to a canonical domain name
- B. to map a domain name to an IP address
- C. to identify the authoritative name server for a domain
- D. to direct email to a mail server
ANSWER: A
