# Security Fundamentals (part 1)

## sec-1  (Question 5.3)
Which type of security program is violated when a group of employees enters a building using the ID badge of only one person?
- A. intrusion detection
- B. user awareness
- C. physical access control
- D. network authorization
ANSWER: C

## sec-2  (Question 5.11)
Which device tracks the state of active connections in order to make a decision to forward a packet through?
- A. firewall
- B. wireless access point
- C. router
- D. wireless LAN controller
ANSWER: A

## sec-3  (Question 5.13)
Refer to the exhibit. A network administrator has been tasked with securing VTY access to a router. Which access-list entry accomplishes this task?
[IMAGE: D:\CCNA_ontap\web\img/56d951323eae161c.jpeg]
- A. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq ssh
- B. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq scp
- C. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq telnet
- D. access-list 101 permit tcp 10.1.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq https
ANSWER: A

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

## sec-5  (Question 5.33)
Which implementation provides the strongest encryption combination for the wireless environment?
- A. WPA2 + AES
- B. WPA + AES
- C. WEP
- D. WPA + TKIP
ANSWER: A

## sec-6  (Question 5.42)
What is a network appliance that checks the state of a packet to determine whether the packet is legitimate?
- A. Layer 2 switch
- B. LAN controller
- C. load balancer
- D. firewall
ANSWER: D

## sec-7  (Question 5.47)
What causes a port to be placed in the err-disabled state?
- A. latency
- B. nothing plugged into the port
- C. shutdown command issued on the port
- D. port security violation
ANSWER: D

## sec-8  (Question 5.49)
Which security program element involves installing badge readers on data-center doors to allow workers to enter and exit based on their job roles?
- A. physical access control
- B. biometrics
- C. role-based access control
- D. multifactor authentication
ANSWER: A

## sec-9  (Question 6.2)
A network administrator must to configure SSH for remote access to router R1. The requirement is to use a public and private key pair to encrypt management traffic to and from the connecting client. Which configuration, when applied, meets the requirements?
- A. R1#enable
R1#configure terminal
R1(config)#ip domain-name cisco.com
R1(config)#crypto key generate ec keysize 1024
- B. R1#enable
R1#configure terminal
R1(config)#ip domain-name cisco.com
R1(config)#crypto key generate rsa modulus 1024
- C. R1#enable
R1#configure terminal
R1(config)#ip domain-name cisco.com
R1(config)#crypto key generate ec keysize 2048
- D. R1#enable
R1#configure terminal
R1(config)#ip domain-name cisco.com
R1(config)#crypto key encrypt rsa name myKey
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B

## sec-10  (Question 6.4)
When a WLAN with WPA2 PSK is configured in the Wireless LAN Controller GUI which format is supported?
- A. Unicode
- B. base64
- C. ASCII
- D. decimal
ANSWER: C

## sec-11  (Question 6.30)
Which two protocols are supported on service-port interfaces? (Choose two)
- A. RADIUS
- B. TACACS+
- C. Telnet
- D. SCP
- E. SSH
ANSWER: C, E

## sec-12  (Question 6.33)
Which global command encrypts all passwords in the running configuration?
- A. enable secret
- B. enable password-encryption
- C. service password-encryption
- D. password-encrypt
ANSWER: C

## sec-13  (Question 7.20)
When a site-to-site VPN is configured, which IPsec mode provides encapsulation and encryption of the entire original IP packet?
- A. IPsec tunnel mode with AH
- B. IPsec transport mode with AH
- C. IPsec tunnel mode with ESP
- D. IPsec transport mode with ESP
ANSWER: C

## sec-14  (Question 7.22)
What is the role of a firewall in an enterprise network?
- A. determines which packets are allowed to cross from unsecured to secured networks
- B. processes unauthorized packets and allows passage to less secure segments of the network
- C. forwards packets based on stateless packet inspection
- D. explicitly denies all packets from entering an administrative domain
ANSWER: A

## sec-15  (Question 7.24)
How are VLAN hopping attacks mitigated?
- A. manually implement trunk ports and disable DTP
- B. configure extended VLANs
- C. activate all ports and place in the default VLAN
- D. enable dynamic ARP inspection
ANSWER: A

## sec-16  (Question 7.30)
Which two protocols must be disabled to increase security for management connections to a Wireless LAN Controller? (Choose two)
- A. Telnet
- B. SSH
- C. HTTP
- D. HTTPS
- E. TFTP
ANSWER: A, C

## sec-17  (Question 7.40)
What does physical access control regulate?
- A. access to specific networks based on business function
- B. access to servers to prevent malicious activity
- C. access to computer networks and file systems
- D. access to networking equipment and facilities
ANSWER: D

## sec-18  (Question 7.49)
Which function is performed by DHCP snooping?
- A. rate-limits certain traffic
- B. listens to multicast traffic for packet forwarding
- C. provides DDoS mitigation
- D. propagates VLAN information between switches
ANSWER: A

## sec-19  (Question 7.55)
Which access layer threat-mitigation technique provides security based on identity?
- A. using a non-default native VLAN
- B. Dynamic ARP Inspection
- C. DHCP snooping
- D. 802.1x
ANSWER: D

## sec-20  (Question 8.3)
How does WPA3 improve security?
- A. It uses SAE for authentication.
- B. It uses a 4-way handshake for authentication.
- C. It uses RC4 for encryption.
- D. It uses TKIP for encryption.
ANSWER: A

## sec-21  (Question 8.16)
Which type of traffic is sent with pure IPsec?
- A. broadcast packets from a switch that is attempting to locate a MAC address at one of several remote sites
- B. multicast traffic from a server at one site to hosts at another location
- C. spanning-tree updates between switches that are at two different sites
- D. unicast messages from a host at a remote site to a server at headquarters
ANSWER: D

## sec-22  (Question 8.24)
Which device permits or denies network traffic based on a set of rules?
- A. access point
- B. switch
- C. wireless controller
- D. firewall
ANSWER: D

## sec-23  (Question 8.34)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/f0aa37bc4c69de1b.jpeg]
Refer to the exhibit. The access list denies Telnet access from PC-1 to RTR-1 and should allow it from other hosts. PC-2 gets “% Connection refused by remote host” when trying to Telnet. Without permitting Telnet from PC-1, what must be done to allow the traffic?
- A. Add the access-list 10 permit any command to the configuration
- B. Remove the access-class 10 in command from line vty 0 4.
- C. Add the ip access-group 10 out command to interface g0/0.
- D. Remove the password command from line vty 0 4.
ANSWER: A

## sec-24  (Question 8.37)
Which two components comprise part of a PKI? (Choose two)
- A. RSA token
- B. clear-text password that authenticates connections
- C. one of more CRLs
- D. preshared key that authenticates connections
- E. CA that grants certificates
ANSWER: C, E

## sec-25  (Question 8.46)
Which wireless security protocol relies on Perfect Forward Secrecy?
- A. WPA
- B. WPA3
- C. WPA2
- D. WEP
ANSWER: B

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

## sec-27  (Question 8.59)
An engineer must configure R1 for a new user account. The account must meet these requirements:
* It must be configured in the local database.
* The username is engineer2
* It must use the strongest password configurable.
Which command must the engineer configure on the router?
- A. R1(config)# username engineer2 algorithm-type scrypt secret test2021
- B. R1(config)# username engineer2 secret 5 password $1$bUu$kZbBS1Pyh4QzwXyZ
- C. R1(config)# username engineer2 privilege 1 password 7 test2021
- D. R1(config)# username engineer2 secret 4 $1Sb1Ju$kZbBSlFyh4QxwXyZ
ANSWER: A

## sec-28  (Question 8.69)
An engineer is configuring remote access to a router from IP subnet 10.139.58.0/28. The domain name, crypto keys, and SSH have been configured. Which configuration enables the traffic on the destination router?
- A. interface FastEthernet0/0
ip address 10.122.49.1 255.255.255.252
ip access-group 10 in
!
ip access-list standard 10
permit udp 10.139.58.0 0.0.0.7 host 10.122.49.1 eq 22
- B. line vty 0 15
access-class 120 in
!
ip access-list extended 120
permit tcp 10.139.58.0 0.0.0.15 any eq 22
- C. line vty 0 15
access-group 120 in
!
ip access-list extended 120
permit tcp 10.139.58.0 0.0.0.15 any eq 22
- D. interface FastEthernet0/0
ip address 10.122.49.1 255.255.255.252
ip access-group 110 in
!
ip access-list standard 110
permit tcp 10.139.58.0 0.0.0.15 eq 22 host 10.122.49.1
ANSWER: B

## sec-29  (Question 8.70)
Which protocol is used for secure remote CLI access?
- A. HTTP
- B. Telnet
- C. SSH
- D. HTTPS
ANSWER: C

## sec-30  (Question 8.77)
A Cisco engineer is configuring a factory-default router with these three passwords:
* The user EXEC password for console access is p4ssw0rd1.
* The user EXEC password for Telnet access is s3cr3t2.
* The password for privileged EXEC mode is priv4t3p4ss.
Which command sequence must the engineer configure?
[TABLE]
Option A
enable secret priv4t3p4ss
!
line con 0
password p4ssw0rd1 
login
!
line vty 0 15 
password s3cr3t2 
login | Option B
enable secret privilege 15 priv4t3p4ss
!
line con 0
password p4ssw0rdi 
login
!
line vty 0 15 
password s3cr3t2
login
---
Option C
enable secret priv413p4ss
!
line con 0
password login p4ssw0rd1
!
line vty 0 15 
password login s3cr3t2 
login | Option D
enable secret priv4t3p4ss
!
line con 0
password p4ssw0rd1 
!
line vty 0 15 
password s3cr3t2
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: A

## sec-31  (Question 9.3)
Which field within the access-request packet is encrypted by RADIUS?
- A. authorized services
- B. authenticator
- C. username
- D. password
ANSWER: D

## sec-32  (Question 9.6)
What is a function of a Next-Generation IPS?
- A. makes forwarding decisions based on learned MAC addresses
- B. serves as a controller within a controller-based network
- C. integrates with a RADIUS server to enforce Layer 2 device authentication rules
- D. correlates user activity with network events
ANSWER: D

## sec-33  (Question 9.8)
Refer to the exhibit.
Which two commands must be added to update the configuration of router R1 so that it accepts only encrypted connections? (Choose two)
- A. username CNAC secret R!41!4319115@
- B. crypto key generate rsa 1024
- C. ip ssh version 2
- D. line vty 0 4
- E. transport input ssh
ANSWER: B, E

## sec-34  (Question 9.13)
Which WLC management connection type is vulnerable to man-in-the-middle attacks?
- A. SSH
- B. HTTPS
- C. Telnet
- D. console
ANSWER: C

## sec-35  (Question 9.15)
Which characteristic differentiates the concept of authentication from authorization and accounting?
- A. user-activity logging
- B. service limitations
- C. consumption-based billing
- D. identity verification
ANSWER: D

## sec-36  (Question 9.18)
Which type of network attack overwhelms the target server by sending multiple packets to a port until the half-open TCP resources of the target are exhausted?
- A. SYN flood
- B. reflection
- C. teardrop
- D. amplification
ANSWER: A

## sec-37  (Question 9.28)
What is a function of Opportunistic Wireless Encryption in an environment?
- A. offer compression
- B. increase security by using a WEP connection
- C. provide authentication
- D. protect traffic on open networks
ANSWER: D

## sec-38  (Question 9.30)
Which action implements physical access control as part of the security program of an organization?
- A. setting up IP cameras to monitor key infrastructure
- B. backing up syslogs at a remote location
- C. configuring enable passwords on network devices
- D. configuring a password for the console port
ANSWER: A

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

## sec-40  (Question 9.45)
Which protocol uses the SSL?
- A. HTTP
- B. HTTPS
- C. SSH
- D. Telnet
ANSWER: B

## sec-41  (Question 9.48)
A network engineer is configuring a switch so that it is remotely reachable via SSH. The engineer has already configured the host name on the router. Which additional command must the engineer configure before entering the command to generate the RSA key?
- A. password password
- B. crypto key generate rsa modulus 1024
- C. ip domain-name domain
- D. ip ssh authentication-retries 2
ANSWER: C

## sec-42  (Question 9.62)
Refer to the exhibit. What must be configured to enable 802.11w on the WLAN?
[IMAGE: D:\CCNA_ontap\web\img/3065179247ec7a2a.jpeg]
- A. Set PMF to Required
- B. Enable MAC Filtering
- C. Enable WPA Policy
- D. Set Fast Transition to Enabled
ANSWER: A

## sec-43  (Question 9.66)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/081f24ce8011e38f.jpeg]
A network engineer configures the Cisco WLC to authenticate local wireless clients against a RADIUS server. Which task must be performed to complete the process?
- A. Disable the Server Status option
- B. Enable the Management option
- C. Enable the Network User option
- D. Enable the Support for CoA option
ANSWER: C

## sec-44  (Question 9.71)
What is the function of Cisco Advanced Malware protection for next-generation IPS?
- A. authorizing potentially compromised wireless traffic
- B. URL filtering
- C. authenticating end users
- D. inspecting specific files and files types for malware
ANSWER: D

## sec-45  (Question 9.72)
An administrator must use the password complexity not manufacturer-name command to prevent users from adding “cisco” as a password. Which command must be issued before this command?
- A. Password complexity enable
- B. confreg 0x2142
- C. login authentication my-auth-list
- D. service password-encryption
ANSWER: A

## sec-46  (Question 9.74)
Which two practices are recommended for an acceptable security posture in a network? (Choose two)
- A. Maintain network equipment in a secure location
- B. Backup device configurations to encrypted USB drives for secure retrieval
- C. Use a cryptographic keychain to authenticate to network devices
- D. Place internal email and file servers in a designated DMZ
- E. Disable unused or unnecessary ports, interfaces and services
ANSWER: A, E

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

## sec-48  (Question 9.78)
What is a feature of WPA?
- A. 802.1x authentication
- B. preshared key
- C. TKIP/MIC encryption
- D. small Wi-Fi application
ANSWER: C

## sec-49  (Question 9.88)
How does authentication differ from authorization?
- A. Authentication verifies the identity of a person accessing a network, and authorization determines what resource a user can access.
- B. Authentication is used to determine what resources a user is allowed to access, and authorization is used to track what equipment is allowed access to the network
- C. Authentication is used to verify a person’s identity, and authorization is used to create syslog messages for logins
- D. Authentication is used to record what resource a user accesses, and authorization is used to determine what resources a user can access
ANSWER: A

## sec-50  (Question 9.90)
Refer to the exhibit.
ip arp inspection vlan 5-10
interface fastethernet0/1
switchport mode access
switchport access vlan 5
What is the effect of this configuration?
- A. Egress traffic is passed only if the destination is a DHCP server.
- B. All ingress and egress traffic is dropped because the interface is untrusted.
- C. All ARP packets are dropped by the switch.
- D. The switch discards all ingress ARP traffic with invalid MAC-to-IP address bindings.
ANSWER: D

## sec-51  (Question 9.102)
Which two wireless security standards use Counter Mode Cipher Block Chaining Message Authentication Code Protocol for encryption and data integrity? (Choose two)
- A. WPA2
- B. WPA3
- C. WEP
- D. WPA
- E. Wi-Fi 6
ANSWER: A, B

## sec-52  (Question 9.103)
What is a practice that protects a network from VLAN hopping attacks?
- A. Implement port security on internet-facing VLANs.
- B. Configure an ACL to prevent traffic from changing VLANs.
- C. Assign all access ports to VLANs other than the native VLAN.
- D. Enable dynamic ARP inspection.
ANSWER: C

## sec-53  (Question 10.24)
An engineer has configured the domain name, user name, and password on the local router. What is the next step to complete the configuration for a Secure Shell access RSA key?
- A. crypto key generate rsa
- B. crypto key pubkey-chain rsa
- C. crypto key import rsa pem
- D. crypto key zeroize rsa
ANSWER: A

## sec-54  (Question 10.25)
Which encryption method is used by WPA3?
- A. TKIP
- B. SAE
- C. PSK
- D. AES
ANSWER: D

## sec-55  (Question 10.26)
An engineer is configuring remote access to a router from IP subnet 10.139.58.0/28. The domain name, crypto keys, and SSH have been configured. Which configuration enables the traffic on the destination router?
- A. interface FastEthernet0/0
ip address 10.122.49.1 255.255.255.248
ip access-group 10 in
ip access-list standard 10
permit udp 10.139.58.0 0.0.0.7 host 10.122.49.1 eq 22
- B. interface FastEthernet0/0
ip address 10.122.49.1 255.255.255.252
ip access-group 105 in
ip access-list standard 105
permit tcp 10.139.58.0 0.0.0.7 eq 22 host 10.122.49.1
- C. interface FastEthernet0/0
ip address 10.122.49.1 255.255.255.252
ip access-group 110 in
ip access-list extended 110
permit tcp 10.139.58.0 0.0.0.15 host 10.122.49.1 eq 22
- D. interface FastEthernet0/0
ip address 10.122.49.1 255.255.255.240
access-group 120 in
ip access-list extended 120
permit tcp 10.139.58.0 255.255.255.248 any eq 22
ANSWER: C

## sec-56  (Question 10.31)
What is a zero-day exploit?
- A. It is when an attacker inserts malicious code into a SQL server.
- B. It is when a new network vulnerability is discovered before a fix is available.
- C. It is when the perpetrator inserts itself in a conversation between two parties and captures or alters data.
- D. It is when the network is saturated with malicious traffic that overloads resources and bandwidth.
ANSWER: B

## sec-57  (Question 10.32)
After a recent security breach and a RADIUS failure, an engineer must secure the console port of each enterprise router with a local username and password. Which configuration must the engineer apply to accomplish this task?
[TABLE]
Option A
aaa new-model
aaa authorization exec default local 
aaa authentication login default radius
username localuser privilege 15 secret plaintextpassword | Option B
username localuser secret plaintextpassword 
line con 0
login authentication default 
privilege level 15
---
Option C
username localuser secret plaintextpassword 
line con 0 
no login local 
privilege level 15 | Option D
aaa new-model 
line con 0
password plaintextpassword 
privilege level 15
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B (?)

## sec-58  (Question 10.36)
What is the default port-security behavior on a trunk link?
- A. It causes a network loop when a violation occurs.
- B. It disables the native VLAN configuration as soon as port security is enabled.
- C. It places the port in the err-disabled state if it learns more than one MAC address.
- D. It places the port in the err-disabled state after 10 MAC addresses are statically configured.
ANSWER: C

## sec-59  (Question 10.38)
What are two examples of multifactor authentication? (Choose two)
- A. single sign-on
- B. unique user knowledge
- C. passwords that expire
- D. soft tokens
- E. shared password responsibility
ANSWER: B, D

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

## sec-61  (Question 10.57)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/1635810037bda5bd.jpeg]
Wireless LAN access must be set up to force all clients from the NA WLAN to authenticate against the local database. The WLAN is configured for local EAP authentication. The time that users access the network must not be limited. Which action completes this configuration?
- A. Check the Guest User Role check box
- B. Clear the Lifetime (seconds) value
- C. Set the Lifetime (seconds) value to 0
- D. Uncheck the Guest User check box
ANSWER: D

## sec-62  (Question 10.58)
Which remote access protocol provides unsecured remote CLI access?
- A. Telnet
- B. SSH
- C. console
- D. Bash
ANSWER: A

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

## sec-64  (Question 10.73)
A network engineer is replacing the switches that belong to a managed-services client with new Cisco Catalyst switches. The new switches will be configured for updated security standards, including replacing Telnet services with encrypted connections and doubling the modulus size from 1024. Which two commands must the engineer configure on the new switches? (Choose two)
- A. transport input ssh
- B. transport input all
- C. crypto key generate rsa general-keys modulus 1024
- D. crypto key generate rsa usage-keys
- E. crypto key generate rsa modulus 2048
ANSWER: A, E

## sec-65  (Question 10.84)
Refer to the exhibit.
[TABLE]
access-list 10 permit 10.0.0.0 0.0.0.255 
interface Serial0
ip access-list 10 in
[/TABLE]
A network administrator must permit traffic from the 10.10.0.0/24 subnet to the WAN on interface Serial0. What is the effect of the configuration as the administrator applies the command?
- A. The sourced traffic from IP range 10.0.0.0 – 10.0.0.255 is allowed on Serial0.
- B. The permit command fails and returns an error code.
- C. The router fails to apply the access list to the interface.
- D. The router accepts all incoming traffic to Serial0 with the last octet of the source IP set to 0.
ANSWER: C

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

## sec-67  (Question 10.89)
Which IPsec transport mode encrypts the IP header and the payload?
- A. pipe
- B. tunnel
- C. control
- D. transport
ANSWER: B

## sec-68  (Question 10.90)
What does WPA3 provide in wireless networking?
- A. increased security and requirement of a complex configuration
- B. backward compatibility with WPA and WPA2
- C. optional Protected Management Frame negotiation
- D. safeguards against brute force attacks with SAE
ANSWER: D

## sec-69  (Question 10.94)
A WLC sends alarms about a rogue AP, and the network administrator verifies that the alarms are caused by a legitimate autonomous AP. How must the alarms be stopped for the MAC address of the AP?
- A. Place the AP into manual containment.
- B. Remove the AP from WLC management.
- C. Manually remove the AP from Pending state.
- D. Set the AP Class Type to Friendly.
ANSWER: D

## sec-70  (Question 10.95)
Which security method is used to prevent man-in-the-middle attack?
- A. authorization
- B. authentication
- C. anti-replay
- D. accounting
ANSWER: C

## sec-71  (Question 11.15)
Which cipher is supported for wireless encryption only with the WPA2 standard?
- A. AES256
- B. AES
- C. RC4
- D. SHA
ANSWER: B

## sec-72  (Question 11.22)
Which enhancement is implemented in WPA3?
- A. applies 802.1x authentication
- B. uses TKIP
- C. employs PKI to identify access points
- D. protects against brute force attacks
ANSWER: D

## sec-73  (Question 11.26)
To improve corporate security, an organization is planning to implement badge authentication to limit access to the data center. Which element of a security program is being deployed?
- A. user training
- B. user awareness
- C. vulnerability verification
- D. physical access control
ANSWER: D

## sec-74  (Question 11.33)
An engineer is configuring a switch port that is connected to a VoIP handset. Which command must the engineer configure to enable port security with a manually assigned MAC address of abcd.abcd.abcd on voice VLAN 4?
- A. switchport port-security mac-address abcd.abcd.abcd
- B. switchport port-security mac-address abcd.abcd.abcd vlan 4
- C. switchport port-security mac-address sticky abcd.abcd.abcd vlan 4
- D. switchport port-security mac-address abcd.abcd.abcd vlan voice
ANSWER: D

## sec-75  (Question 11.35)
How does encryption protect the wireless network?
- A. via integrity checks to identify wireless forgery attacks in the frame
- B. via specific ciphers to detect and prevent zero-day network attacks
- C. via an algorithm to change wireless data so that only the access point and client understand it
- D. via a policy to prevent unauthorized users from communicating on the wireless network
ANSWER: C

## sec-76  (Question 11.36)
Which device segregates a network into separate zones that have their own security policies?
- A. IPS
- B. firewall
- C. access point
- D. switch
ANSWER: B

## sec-77  (Question 11.41)
Which two protocols are used by an administrator for authentication and configuration on access points? (Choose two)
- A. Kerberos
- B. 802.1Q
- C. 802.1x
- D. TACACS+
- E. RADIUS
ANSWER: C, E

## sec-78  (Question 11.58)
Refer to the exhibit.
Router#conf t
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#hostname R1
R1(config)#ip domain-name CC-Net.com
R1(config)#enable secret Passfornewuser
R1(config)#line vty 0 15
R1(config-line)#transport input ssh
R1(config-line)#login local
A network administrator is configuring a router for user access via SSH. The service-password encryption command has been issued. The configuration must meet these requirements:
Create the username as CCUser.
Create the password as NA!2$cc.
Encrypt the user password.
What must be configured to meet the requirements?
- A. username CCUser password NA!2cc
- B. username CCUser privilege 15 password NA!2cc
- C. username CCUser secret NA!2$cc
- D. username CCUser privilege 10 password NA!2$cc
ANSWER: C

## sec-79  (Question 11.65)
Which two VPN technologies are recommended by Cisco for multiple branch offices and large-scale deployments? (Choose two)
- A. IPsec remote access
- B. site-to-site VPN
- C. clientless VPN
- D. GETVPN
- E. DMVPN
ANSWER: D, E

## sec-80  (Question 11.69)
Refer to the exhibit. Local access for R4 must be established and these requirements must be met: Only Telnet access is allowed. The enable password must be stored securely. The enable password must be applied in plain text Full access to R4 must be permitted upon successful login
Which configuration script meets the requirements?
- A. Option A ! conf t ! username test1 password testpass1
- B. Option B conf t ! username test1 password testpass1 enable secret level 15 0 Test123 ! line vty 0 15 login local transport input telnet
- C. Option C ! config t ! username test1 password testpass1 enable secret level 1 0 Test123 ! line vty 0 15 login authentication password Test123 transport input telnet
- D. Option D ! config t ! username test1 password testpass1 enable password level 15 0 Test123 ! line vty 0 15 password Test123 transport input all
ANSWER: B

## sec-81  (Question 11.71)
Which action must be taken when password protection is implemented?
- A. Store passwords as contacts on a mobile device with single-factor authentication.
- B. Share passwords with senior IT management to ensure proper oversight.
- C. Include special characters and make passwords as long as allowed.
- D. Use less than eight characters in length when passwords are complex.
ANSWER: C

## sec-82  (Question 11.74)
Which device separates networks by security domains?
- A. access point
- B. firewall
- C. intrusion protection system
- D. wireless controller
ANSWER: B

## sec-83  (Question 12.9)
What are two protocols within the IPsec suite? (Choose two)
- A. 3DES
- B. AH
- C. ESP
- D. TLS
- E. AES
ANSWER: B, C

## sec-84  (Question 12.15)
Refer to the exhibit.
SW1#show run
Building configuration...
!
hostname SW1
!
ip domain-name test
!
username CCNA privilege 1 password 0 ciscol23
!
interface FastEthernet0/1
switchport access vlan 10
!
interface Vlan10
ip address 192.168.1.2 255.255.255.0
!
line vty 0 4
login local
transport input telnet
line vty 5 15
login local
transport input telnet
SW1#show crypto key mypubkey rsa
% Key pair was generated at: 0:1:23 UTC Mar 1 2021
Key name: SW1.test
An engineer is updating the management access configuration of switch SW1 to allow secured, encrypted remote configuration. Which two commands or command sequences must the engineer apply to the switch? (Choose two)
- A. SW1(config)#line vty 0 15 SW1(config-line)#transport input ssh
- B. SW1(config)# crypto key generate rsa
- C. SW1(config)# interface f0/1 SW1(config-if)# switch port mode trunk
- D. SW1(config)#enable secret ccnaTest123
- E. SW1(config)# username NEW secret R3mote123
ANSWER: A, D

## sec-85  (Question 12.33)
What is a characteristic of RSA?
- A. It uses preshared keys for encryption
- B. It is an asymmetric encryption algorithm
- C. It requires both sides to have identical keys for encryption
- D. It is a symmetric decryption algorithm.
ANSWER: B

## sec-86  (Question 12.65)
Refer to the exhibit.
hostname CPE service password-encryption ip domain name ccna.cisco.com ip name-server 198.51.100.210 crypto key generate rsa modulus 1024 username admin privilege 15 secret S0m3s3cr3t line vty 0 4 transport input ssh login local
An engineer executed the script and added commands that were not necessary for SSH and now must remove the commands. Which two commands must be executed to correct the configuration? (Choose two)
- A. no ip domain name ccna.cisco.com
- B. no login local
- C. no ip name-server 198.51.100.210
- D. no service password-encryption
- E. no hostname CPE
ANSWER: C, D

## sec-87  (Question 12.110)
Refer to the exhibit.
Switch(config)#hostname R1
R1(config)#interface FastEthernet0/1
R1(config-if)#no switchport
R1(config-if)#ip address 10.100.20.42 255.255.255.0
R1(config-if)#line vty 0 4
R1(config-line)#login
An engineer booted a new switch and applied this configuration via the console port. Which additional configuration must be applied to allow administrators to authenticate directly to global configuration mode via Telnet using a local username and password?
- A. R1(config)#username admin R1(config-if)#line vty 0 4 R1(config-line)#password p@ss1234
- B. R1(config)#username admin R1(config-if)#line vty 0 4 R1(config-line)#password p@ss1234 R1(config-line)#transport input telnet
- C. R1(config)#username admin secret p@ss1234 R1(config-if)#line vty 0 4 R1(config-line)#login local R1(config)#enable secret p@ss1234
- D. R1(config)#username admin privilege 15 secret p@ss1234 R1(config-if)#line vty 0 4 R1(config-line)#login local
ANSWER: D

## sec-88  (Question 12.111)
What is the definition of backdoor malware?
- A. malicious program that is used to launch other malicious programs
- B. malicious code that infects a user machine and then uses that machine to send spam
- C. malicious code with the main purpose of downloading other malicious code
- D. malicious code that is installed onto a computer to allow access by an unauthorized user
ANSWER: D

## sec-89  (Question 13.5)
What is used as a solution for protecting an individual network endpoint from attack?
- A. Router
- B. Wireless controller
- C. Antivirus software
- D. Cisco DNA Center
ANSWER: C

## sec-90  (Question 13.13)
What is an enhancement implemented in WPA3?
- A. employs PKI and RADIUS to identify access points
- B. applies 802.1x authentication and AES-128 encryption
- C. uses TKIP and per-packet keying
- D. defends against deauthentication and disassociation attacks
ANSWER: D

## sec-91  (Question 13.24)
Which WPA mode uses PSK authentication?
- A. Local
- B. Client
- C. Enterprise
- D. Personal
ANSWER: D

## sec-92  (Question 13.42)
What is a characteristic of encryption in wireless networks?
- A. uses policies to prevent unauthorized users
- B. prevents the interception of data as it transits a network
- C. provides increased protection against spyware
- D. converts electrical current to radio waves
ANSWER: B

## sec-93  (Question 13.54)
Which IPsec encryption mode is appropriate when the destination of a packet differs from the security termination point?
- A. tunnel
- B. main
- C. aggressive
- D. transport
ANSWER: A

## sec-94  (Question 13.70)
A network engineer must configure an access list on a new Cisco IOS router. The access list must deny HTTP traffic to network 10.125.128.32/27 from the 192.168.240.0/20 network, but it must allow the 192.168.240.0/20 network to reach the rest of the 10.0.0.0/8 network. Which configuration must the engineer apply?
[TABLE]
Option A
ip access-list extended deny_outbound 
 10 deny tcp 10.125.128.32 255.255.255.224 192.168.240.0 255.255.240.0 eq 443 
 20 deny tcp 192.168.240.0 255.255.240.0 10.125.128.32 255.255.255.224 eq 443 
 30 permit ip 192.168.240.0 255.255.240.0 10.0.0.0 255.0.0.0
---
Option B
ip access-list extended deny_outbound
  10 permit ip 192.168.240.0 255.255.240.0 10.0.0.0 255.0.0.0
  20 deny tcp 192.168.240.0 255.255.240.0 10.125.128.32 255.255.255.224 eq 443
  30 permit ip any any
---
Option C
ip access-list extended deny_outbound 
  10 deny tcp 192.168.240.0 0.0.15.255 10.125.128.32 0.0.0.31 eq 80 
  20 permit ip 192.168.240.0 0.0.15.255 10.0.0.0 0.255.255.255 
  30 deny ip any any log
---
Option D
ip access-list extended deny_outbound 
  10 deny tcp 192.168.240.0 0.0.15.255 any eq 80 
  20 deny tcp 192.168.240.0 0.0.15.255 10.125.128.32 0.0.0.31 eq 80 
  30 permit ip 192.168.240.0 0.0.15.255 10.0.0.0 0.255.255.255
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: C

## sec-95  (Question 13.78)
Which enhancements were implemented as part of WPA3?
- A. TKIP encryption improving WEP and per-packet keying
- B. forward secrecy and SAE in personal mode for secure initial key exchange
- C. 802.1x authentication and AES-128 encryption
- D. AES-64 in personal mode and AES-128 in enterprise mode
ANSWER: B

## sec-96  (Question 13.83)
An administrator is configuring a Cisco Catalyst switch so that it will accept management connections only from hosts in the 203.0.113.0/24 network. Other traffic passing through the switch must transit without interruption. Which two configurations must the engineer apply to the router? (Choose two)
- A. ip access-list extended Management permit tcp any range 22 23 203.0.113.0 0.0.0.255
- B. line vty 0 15 access-class Management in
- C. ip access-list standard Management permit 203.0.113.0 255.255.255.0
- D. interface range vlan 1 – 4094 ip access-group Management out
- E. ip access-list standard Management permit 203.0.113.0 0.0.0.255
ANSWER: B, E

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

## sec-98  (Question 13.87)
What is a function of a firewall on an enterprise network?
- A. It acts as the intermediary device between the enterprise and its ISP
- B. It serves as a default gateway to hosts on the internet
- C. It processes traffic based on stateless inspection
- D. It allows and denies ingress and egress traffic
ANSWER: D

## sec-99  (Question 13.88)
Which encryption mode is used when a packet is sent from a site-to-site VPN connection where the source and destination IP address portion of a packet is unencrypted?
- A. PPTP
- B. Secure Shell
- C. Transport
- D. PPPoE
ANSWER: C

## sec-100  (Question 13.100)
What is the difference between AAA authentication and authorization?
- A. Authentication controls the system processes a user accesses, and authorization logs the activities the user initiates.
- B. Authentication identifies a user who is attempting to access a system, and authorization validates the user s password
- C. Authentication identifies and verifies a user who is attempting to access a system, and authorization controls the tasks the user performs
- D. Authentication verifies a username and password, and authorization handles the communication between the authentication agent and the user database
ANSWER: C
