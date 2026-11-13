# Security Fundamentals (part 2)

## sec-101  (Question 14.12)
Which type of encryption does WPA1 use for data protection?
- A. AES
- B. TKIP
- C. PEAP
- D. EAP
ANSWER: B

## sec-102  (Question 14.42)
Which device protects an internal network from the Internet?
- A. firewall
- B. Layer 2 switch
- C. router
- D. access point
ANSWER: A

## sec-103  (Question 14.55)
Which selections must be used on the WLC when implementing a RADIUS server for wireless authentication?
- A. Client Exclusion and SSH
- B. Network Access Control State and SSH
- C. 802.1x and the MAC address of the server
- D. AAA Override and the IP address of the server
ANSWER: D

## sec-104  (Question 14.58)
Which port-security violation mode drops traffic from unknown MAC addresses and forwards an SNMP trap?
- A. restrict
- B. protect
- C. shutdown VLAN
- D. shutdown
ANSWER: A

## sec-105  (Question 14.64)
Which two tasks support the physical access control element of a security program? (Choose two)
- A. Deploy a video surveillance system
- B. Run a workshop on corporate security policies
- C. Implement badge access to critical locations
- D. Develop slideshows about new security regulations
- E. Disperse information about how to protect the organization’s confidential data
ANSWER: A, C

## sec-106  (Question 14.67)
Network security team noticed that an increasing number of employees are becoming victims of phishing attacks. Which security program should be implemented to mitigate the problem?
- A. user awareness training
- B. email system patches
- C. software firewall enabled on all PCs
- D. physical access control
ANSWER: A

## sec-107  (Question 14.68)
How does IPsec provide secure networking for applications within an organization?
- A. It leverages TFTP providing secure file transfers among peers on the network.
- B. It provides GRE tunnels to transmit traffic securely between network nodes.
- C. It enables sets of security associations between peers.
- D. It takes advantage of FTP to secure file transfers between nodes on the network.
ANSWER: C

## sec-108  (Question 14.69)
Company has decided to require multifactor authentication for all systems. Which set of parameters meets the requirement?
- A. personal 10-digit PIN and RSA certificate
- B. complex password and personal 10-digit PIN
- C. password of 8 to 15 characters and personal 12-digit PIN
- D. fingerprint scanning and facial recognition
ANSWER: A

## sec-109  (Question 14.95)
A network administrator is evaluating network security in the aftermath of an attempted ARP spoofing attack. If Port-channel1 is the uplink interface of the access-layer switch toward the distribution-layer switch, which two configurations must the administrator configure on the access-layer switch to provide adequate protection? (Choose two)
Option A ip dhcp snooping ! interface Port-channel1 switchport port-security
[TABLE]
Option A
ip dhcp snooping
!
interface Port-channel1
switchport port-security maximum 1
switchport port-security
---
Option C
ip dhcp snooping vlan 1-4094
!
interface Port-channel1
switchport protected
switchport port-security maximum 1
---
Option E
ip arp inspection vlan 1-4094
!
interface Port-channel1
ip arp inspection trust
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
- E. Option E
ANSWER: B, E

## sec-110  (Question 14.97)
What are two functions of a firewall within an enterprise? (Choose two)
- A. It serves as an endpoint for a site-to-site VPN in standalone mode.
- B. It enables traffic filtering based on URLs.
- C. It provides support as an endpoint for a remote access VPN in multiple context mode.
- D. It offers Layer 2 services between hosts.
- E. It enables wireless devices to connect to the network.
ANSWER: B, C

## sec-111  (Question 14.105)
Which two statements distinguish authentication from accounting? (Choose two)
- A. Only authentication challenges users for their credentials and returns a response.
- B. Only authentication supports user-activity audits.
- C. Only authentication validates “who you are.”
- D. Only authentication records the duration of a user’s connection.
- E. Only authentication provides supporting information for billing users.
ANSWER: A, C

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

## sec-113  (Question 15.15)
Which alternative to password authentication is implemented to allow enterprise devices to log in to the corporate network?
- A. digital certificates
- B. magic links
- C. one-time passwords
- D. 90-day renewal policies
ANSWER: A

## sec-114  (Question 15.16)
Which guideline helps to create a secure password policy?
- A. forbidding users from storing passwords in a password manager
- B. allowing passwords used by service accounts to never expire
- C. requiring complex, lengthy passwords instead of simple, short ones
- D. restricting password sharing to a very small group
ANSWER: C

## sec-115  (Question 15.17)
Refer to the exhibit.
SW1#conf t
Enter configuration commands, one per line. End with CNTL/Z.
SW1(config)#enable password test!2E
SW1(config)#line con 0
SW1(config-line)#password Labtest32!
SH1(config-line)#exit
SW1(config)#
A network engineer started to change default settings on SW1 to allow remote access and has entered the following in the configuration mode:
[TABLE]
SW1#(config)#line vty 0 15
SW1#(config-line)#password Labtest32!
[/TABLE]
Which set of commands are needed to allow only SSH access and hide passwords in the running configuration?
[TABLE]
Option A
SW1(config-line)#login local
SW1(config-line)#exit
SW1(config)#enable secret test!2E | Option B
SW1(config-line)#transport input ssh
SW1(config-line)#exit
SW1(config)#service password-encryption
---
Option C
SW1(config-line)#login local
SW1(config-line)#exit | Option D
SW1(config-line)#exit
SW1(config)#aaa new-model
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: B

## sec-116  (Question 15.18)
How does machine learning contribute to the effectiveness of intrusion detection systems?
- A. It assigns security clearance levels.
- B. It dictates security policy updates.
- C. It monitors for outdated software.
- D. It identifies patterns indicating intrusions.
ANSWER: D

## sec-117  (Question 15.20)
What must be considered when planning an IPsec VPN deployment?
- A. IPsec transport mode allows intermediate devices to see the final destination of the packet
- B. In IPsec tunnel mode, only the IP payload is encrypted
- C. IPsec transport mode increases GRE tunnel security over tunnel mode.
- D. IPsec transport mode does not encrypt the Layer 4 header, which allow full examination of the packet
ANSWER: A

## sec-118  (Question 15.23)
Which IPsec mode encapsulates the entire IP packet?
- A. tunnel
- B. transport
- C. SSL VPN
- D. Q-in-Q
ANSWER: A

## sec-119  (Question 15.24)
Which mechanism allows WPA3 to provide a higher degree of security than its predecessors?
- A. automatic device pairing
- B. special-character support in preshared keys
- C. certificate-based authentication
- D. SAE password-based key exchange
ANSWER: D

## sec-120  (Question 15.27)
Which authentication method requires the user to provide a physical attribute to authenticate successfully?
- A. certificate
- B. password
- C. multifactor
- D. biometric
ANSWER: D

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

## sec-122  (Question 15.32)
Which factor must be considered during the implementation of an IPsec VPN?
- A. IPsec transport mode leaves the Layer 4 header unencrypted for inspection.
- B. IPsec transport mode increases GRE tunnel security over tunnel mode.
- C. In IPsec tunnel mode, only the IP payload is encrypted.
- D. In IPsec tunnel mode, the entire original IP datagram is encrypted.
ANSWER: D

## sec-123  (Question 15.35)
What are the two main capabilities of tunnel mode in IPsec site-to-site VPNs ? (Choose two.)
- A. It authenticates the data field in original packet.
- B. It encrypts the complete IP packet with the data field.
- C. It secures only the data field in the packet.
- D. It transmits with the original packet header visible.
- E. It inserts a new IPsec header with new IP address.
ANSWER: B, E

## sec-124  (Question 15.37)
Which type of traffic is sent with pure IPsec?
- A. spanning-tree updates between switches that are at two different sites
- B. unicast messages from a host at a remote site to a server at headquarters
- C. broadcast packets from a switch that is attempting to locate a MAC address at one of several remote sites
- D. multicast traffic from a server at one site to hosts at another location
ANSWER: B

## sec-125  (Question 15.39)
What is a characteristic of RSA?
- A. It requires both sides to have identical keys.
- B. it is a private-key gencryption algorithm.
- C. It uses preshared keys for encryption.
- D. it is a public-key cryptosystem.
ANSWER: D

## sec-126  (Question 15.45)
Refer to the exhibit.
CPE# show ip access-list Services
Extended IP access list Services
10 permit tcp 10.0.0.0 0.255.255.255 any eq www
20 permit tcp 10.0.0.0 0.255.255.255 any eq 443
30 permit udp 10.0.0.0 0.255.255.255 host 198.51.100.11 eq domain
40 deny ip any any log
This ACL is configured to allow client access only to HTTP, HTTPS, and DNS services via UDP. The new administrator wants to add TCP access to the DNS service. Which configuration updates the ACL efficiently?
[TABLE]
Option A
ip access-list extended Services
 permit tcp 10.0.0.0 0.255.255.255 host 198.51.100.11 eq domain | Option B
no ip access-list extended Services
ip access-list extended Services
 30 permit tcp 10.0.0.0 0.255.255.255 host 198.51.100.11 eq domain
---
 | 
---
Option C
no ip access-list extended Services
ip access-list extended Services
 permit udp 10.0.0.0 0.255.255.255 any eq 53
 permit tcp 10.0.0.0 0.255.255.255 host 198.51.100.11 eq domain
 deny ip any any log | Option D
ip access-list extended Services
 35 permit tcp 10.0.0.0 0.255.255.255 host 198.51.100.11 eq domain
[/TABLE]
- A. Option A
- B. Option B
- C. Option C
- D. Option D
ANSWER: D

## sec-127  (Question 15.49)
Which solution is appropriate when mitigating password attacks where the attacker was able to sniff the clear-text password of the system administrator?
- A. next-generation firewall to keep stateful packet inspection
- B. multifactor authentication using two separate authentication sources
- C. ACL to restrict incoming Telnet sessions “admin” accounts
- D. IPS with a block list of known attack vectors
ANSWER: B

## sec-128  (Question 15.52)
Which advantage does machine learning offer for network security?
- A. It improves real-time threat detection.
- B. It manages firewall rule sets.
- C. It enforces password complexity requirements.
- D. It controls VPN access permissions.
ANSWER: A

## sec-129  (Question 15.56)
How does machine learning improve the detection of unauthorized network access?
- A. It monitors for outdated software.
- B. It dictates security policy updates.
- C. It identifies patterns indicating intrusions.
- D. It assigns security clearance levels.
ANSWER: C

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

## sec-131  (Question 15.73)
What is the main purpose of SSH management access?
- A. To validate management access with username and domain name only
- B. To allow passwords protected with HTTPS encryption to be sent
- C. To support DES 56-bit and 3DES (168-bit) ciphers
- D. To enable secured access to the inbound management interface
ANSWER: D

## sec-132  (Question 15.76)
An organization developed new security policies and decided to print the policies and distribute them to all personnel so that employees review and apply the policies. Which element of a security program is the organization implementing?
- A. Asset identification
- B. User training
- C. Physical access control
- D. Vulnerability control
ANSWER: B

## sec-133  (Question 15.88)
What is an advantage of using SDN versus traditional networking when it comes to security?
- A. It creates a unified control point making security policies consistent across all devices
- B. It exposes an API to configure locally per device for security policies
- C. Security is managed near the perimeter of the network with firewalls, VPNs, and IPS
- D. Devices communicate with each other to establish a security policy
ANSWER: A

## sec-134  (Question 15.89)
What is a difference between RADIUS and TACACS+?
- A. RADIUS is most appropriate for dial authentication, but TACACS+ can be used for multiple types of authentication
- B. TACACS+ encrypts only password information and RADIUS encrypts the entire payload
- C. TACACS+ separates authentication and authorization, and RADIUS merges them
- D. RADIUS logs all commands that are entered by the administrator, but TACACS+ logs only start, stop, and interim commands
ANSWER: C

## sec-135  (Question 15.93)
How do AAA operations compare regarding user identification, user services and access control?
- A. Authorization provides access control and authentication tracks user services
- B. Authentication identifies users and accounting tracks user services
- C. Accounting tracks user services, and authentication provides access control
- D. Authorization identifies users and authentication provides access control
ANSWER: B

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

## sec-137  (Question 15.100)
Refer to the exhibit. If the network environment is operating normally, which type of device must be connected to interface FastEthernet 0/1?
ip arp inspection vlan 2-10
interface fastethernet 0/1
ip arp inspection trust A. DHCP client
- B. access point
- C. router
- D. PC
ANSWER: C

## sec-138  (Question 15.104)
When a WPA2-PSK WLAN is configured in the Wireless LAN Controller, what is the minimum number of characters that is required for the passphrase?
- A. 6
- B. 8
- C. 12
- D. 18
ANSWER: B

## sec-139  (Question 15.109)
What are two recommendations for protecting network ports from being exploited when located in an office space outside of an IT closet? (Choose two)
- A. shut down unused ports
- B. enable the PortFast feature on ports
- C. implement port-based authentication
- D. configure ports to a fixed speed
- E. configure static ARP entries
ANSWER: A, C

## sec-140  (Question 15.114)
Which type of traffic is sent with pure IPsec?
- A. multicast traffic from a server at one site to hosts at another location
- B. spanning-tree updates between switches that are at two different sites
- C. broadcast packets from a switch that is attempting to locate a MAC address at one of several remote sites
- D. unicast messages from a host at a remote site to a server at headquarters
ANSWER: D

## sec-141  (Question 16.7)
Which security element uses a combination of one-time passwords, a login name, and a personal smartphone?
- A. software-defined segmentation
- B. multifactor authentication
- C. attribute-based access control
- D. rule-based access control
ANSWER: B

## sec-142  (Question 16.15)
Why does an administrator choose to implement a remote access IPsec VPN?
- A. to establish an encrypted tunnel between a remote user and a private network over the internet
- B. to allow access to an enterprise network using any internet-enabled location via a web browser using SSL
- C. to provide a secure link between an HTTPS server, authentication subsystem, and an end-user
- D. to use cryptography for authentication between a device and user over a negotiated VPN gateway
ANSWER: A

## sec-143  (Question 16.26)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/3cdd8c4829ce4d69.jpeg]
A network engineer is configuring a wireless LAN with Web Passthrough Layer 3 Web Policy. Which action must the engineer take to complete the configuration?
- A. Enable the WPA Policy.
- B. Set the Layer 2 Security to 802.1X.
- C. Enable TKIP and CCMP256 WPA2 Encryption.
- D. Set the Layer 2 Security to None.
ANSWER: D

## sec-144  (Question 16.38)
Which combination of methods satisfies the minimum security requirements when a new multifactor authentication solution is deployed?
- A. password of 8 to 15 characters and personal 12-digit PIN
- B. authorized USB dongle and mobile phone
- C. complex password and time-based one-time password
- D. fingerprint scanning and facial recognition
ANSWER: C

## sec-145  (Question 16.44)
What is the main capability of multifactor authentication?
- A. Identifying permissions for end users using three authentication factors
- B. Authenticating and authorizing end users using two authentication factors
- C. Confirming end-user identity using two or more authentication factors
- D. Verifying end-user access permissions using two authentication factors
ANSWER: C

## sec-146  (Question 16.48)
Which feature is mandatory when configuring a new SSID for a wireless network running WPA3-Personal mode?
- A. Opportunistic Wireless Encryption
- B. Protected Management Frame
- C. Enhanced Open
- D. Fast Transition
ANSWER: B

## sec-147  (Question 16.50)
Which feature of Digest Authentication prevents credentials from being sent in plaintext?
- A. SSL/TLS encryption
- B. Challenge-response mechanism
- C. Token-based authorization
- D. Public key infrastructure
ANSWER: B

## sec-148  (Question 16.59)
Which security protocol is appropriate for a WPA3 implementation?
- A. TKIP
- B. GCMP
- C. MD5
- D. CCMP
ANSWER: B

## sec-149  (Question 16.68)
Refer to the exhibit.
[IMAGE: D:\CCNA_ontap\web\img/e8ee9f8a4f80e8ab.jpeg]
Users will be using a preconfigured secret key and SSID and must have a secured key hashing algorithm configured. The AAA server must not be used for the user authentication method. Which action completes the task?
- A. Configure PSK-SHA2.
- B. Configure PSK Format HEX with key string.
- C. Set CCMP128(AES).
- D. Enable AutoConfig iPSK.
ANSWER: A

## sec-150  (Question 16.70)
Which type of VPN connection is used when an employee accesses a secure server from a public Wi-Fi?
- A. site-to-site
- B. router-to-router
- C. remote
- D. open
ANSWER: C

## sec-151  (Question 16.73)
Which security program element helps protect against employees unintentionally leaking sensitive information via email?
- A. workstation screen recordings
- B. user awareness campaigns
- C. controlled internet access
- D. physical access controls
ANSWER: B
