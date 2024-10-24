# OTI-DC01-Leaf5A

## Table of Contents

- [Management](#management)
  - [Agents](#agents)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [ARP](#arp)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)

## Management

### Agents

#### Agent KernelFib

##### Environment Variables

| Name | Value |
| ---- | ----- |
| KERNELFIB_PROGRAM_ALL_ECMP | 'true' |

#### Agents Device Configuration

```eos
!
agent KernelFib environment KERNELFIB_PROGRAM_ALL_ECMP='true'
```

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | default | 192.168.255.17/24 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | default | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   ip address 192.168.255.17/24
   no lldp transmit
   no lldp receive
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 169.254.169.254 | default | - |
| 8.8.8.8 | default | - |
| 1.1.1.1 | default | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf default 1.1.1.1
ip name-server vrf default 8.8.8.8
ip name-server vrf default 169.254.169.254
```

### NTP

#### NTP Summary

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| pool.ntp.org | default | - | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp server pool.ntp.org
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| default | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf default
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | apiserver.arista.io:443 | default | token-secure,/tmp/cv-onboarding-token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=apiserver.arista.io:443 -cvauth=token-secure,/tmp/cv-onboarding-token -cvvrf=default -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| OTI-DC01-Leaf5 | Vlan4094 | 192.168.13.105 | Port-Channel531 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id OTI-DC01-Leaf5
   local-interface Vlan4094
   peer-address 192.168.13.105
   peer-link Port-Channel531
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 4096
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 55 | HYPER_PROD | - |
| 821 | SAN_Disk | - |
| 2821 | Users_Dev | - |
| 2822 | Voice_Dev | - |
| 2833 | Broadcast1 | - |
| 2834 | Broadcast2 | - |
| 3009 | MLAG_L3_VRF_Production | MLAG |
| 3010 | MLAG_L3_VRF_Development | MLAG |
| 4093 | MLAG_L3 | MLAG |
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 55
   name HYPER_PROD
!
vlan 821
   name SAN_Disk
!
vlan 2821
   name Users_Dev
!
vlan 2822
   name Voice_Dev
!
vlan 2833
   name Broadcast1
!
vlan 2834
   name Broadcast2
!
vlan 3009
   name MLAG_L3_VRF_Production
   trunk group MLAG
!
vlan 3010
   name MLAG_L3_VRF_Development
   trunk group MLAG
!
vlan 4093
   name MLAG_L3
   trunk group MLAG
!
vlan 4094
   name MLAG
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | SERVER_DC01-0601-ESX01_PCI_slot_1_Port_2 | *trunk | *2821-2822,2833-2834 | *- | *- | 1 |
| Ethernet3 | SERVER_DC01-0601-ESX03_PCI_slot_1_Port_2 | *access | *55 | *- | *- | 3 |
| Ethernet4 | SERVER_DC01-0601-ESX04_PCI_slot_1_Port_2 | *access | *55 | *- | *- | 4 |
| Ethernet5 | SERVER_DC01-0601-ESX05_PCI_slot_1_Port_2 | *trunk | *2821-2822,2833-2834 | *- | *- | 5 |
| Ethernet6 | SERVER_DC01-0601-ESX06_PCI_slot_1_Port_2 | *access | *821 | *- | *- | 6 |
| Ethernet53/1 | MLAG_OTI-DC01-Leaf5B_Ethernet53/1 | *trunk | *- | *- | *MLAG | 531 |
| Ethernet54/1 | MLAG_OTI-DC01-Leaf5B_Ethernet54/1 | *trunk | *- | *- | *MLAG | 531 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet52/1 | P2P_OTI-DC02-Leaf5A_Ethernet52/1 | - | 192.168.10.248/31 | default | 1500 | False | - | - |
| Ethernet55/1 | P2P_OTI-DC01-Spine1_Ethernet5/1 | - | 192.168.11.17/31 | default | 1500 | False | - | - |
| Ethernet56/1 | P2P_OTI-DC01-Spine2_Ethernet5/1 | - | 192.168.11.19/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description SERVER_DC01-0601-ESX01_PCI_slot_1_Port_2
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description SERVER_DC01-0601-ESX03_PCI_slot_1_Port_2
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description SERVER_DC01-0601-ESX04_PCI_slot_1_Port_2
   no shutdown
   channel-group 4 mode active
!
interface Ethernet5
   description SERVER_DC01-0601-ESX05_PCI_slot_1_Port_2
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description SERVER_DC01-0601-ESX06_PCI_slot_1_Port_2
   no shutdown
   channel-group 6 mode active
!
interface Ethernet52/1
   description P2P_OTI-DC02-Leaf5A_Ethernet52/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.10.248/31
!
interface Ethernet53/1
   description MLAG_OTI-DC01-Leaf5B_Ethernet53/1
   no shutdown
   channel-group 531 mode active
!
interface Ethernet54/1
   description MLAG_OTI-DC01-Leaf5B_Ethernet54/1
   no shutdown
   channel-group 531 mode active
!
interface Ethernet55/1
   description P2P_OTI-DC01-Spine1_Ethernet5/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.11.17/31
!
interface Ethernet56/1
   description P2P_OTI-DC01-Spine2_Ethernet5/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.11.19/31
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | SERVER_DC01-0601-ESX01 | trunk | 2821-2822,2833-2834 | - | - | - | - | 1 | - |
| Port-Channel3 | SERVER_DC01-0601-ESX03 | access | 55 | - | - | - | - | 3 | - |
| Port-Channel4 | SERVER_DC01-0601-ESX04 | access | 55 | - | - | - | - | 4 | - |
| Port-Channel5 | SERVER_DC01-0601-ESX05 | trunk | 2821-2822,2833-2834 | - | - | - | - | 5 | - |
| Port-Channel6 | SERVER_DC01-0601-ESX06 | access | 821 | - | - | - | - | 6 | - |
| Port-Channel531 | MLAG_OTI-DC01-Leaf5B_Port-Channel531 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description SERVER_DC01-0601-ESX01
   no shutdown
   mtu 9214
   switchport trunk allowed vlan 2821, 2822, 2833, 2834
   switchport mode trunk
   switchport
   mlag 1
   spanning-tree portfast
!
interface Port-Channel3
   description SERVER_DC01-0601-ESX03
   no shutdown
   mtu 9214
   switchport access vlan 55
   switchport mode access
   switchport
   mlag 3
   spanning-tree portfast
!
interface Port-Channel4
   description SERVER_DC01-0601-ESX04
   no shutdown
   mtu 9214
   switchport access vlan 55
   switchport mode access
   switchport
   mlag 4
   spanning-tree portfast
!
interface Port-Channel5
   description SERVER_DC01-0601-ESX05
   no shutdown
   mtu 9214
   switchport trunk allowed vlan 2821, 2822, 2833, 2834
   switchport mode trunk
   switchport
   mlag 5
   spanning-tree portfast
!
interface Port-Channel6
   description SERVER_DC01-0601-ESX06
   no shutdown
   mtu 9214
   switchport access vlan 821
   switchport mode access
   switchport
   mlag 6
   spanning-tree portfast
!
interface Port-Channel531
   description MLAG_OTI-DC01-Leaf5B_Port-Channel531
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.245.217.7/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 10.245.217.39/32 |
| Loopback10 | DIAG_VRF_Production | Production | 10.1.10.7/32 |
| Loopback11 | DIAG_VRF_Development | Development | 10.1.11.7/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |
| Loopback10 | DIAG_VRF_Production | Production | - |
| Loopback11 | DIAG_VRF_Development | Development | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 10.245.217.7/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 10.245.217.39/32
!
interface Loopback10
   description DIAG_VRF_Production
   no shutdown
   vrf Production
   ip address 10.1.10.7/32
!
interface Loopback11
   description DIAG_VRF_Development
   no shutdown
   vrf Development
   ip address 10.1.11.7/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan55 | HYPER_PROD | Production | - | False |
| Vlan821 | SAN_Disk | Production | - | False |
| Vlan2821 | Users_Dev | Development | - | False |
| Vlan2822 | Voice_Dev | Development | - | False |
| Vlan2833 | Broadcast1 | Development | - | False |
| Vlan2834 | Broadcast2 | Development | - | False |
| Vlan3009 | MLAG_L3_VRF_Production | Production | 1500 | False |
| Vlan3010 | MLAG_L3_VRF_Development | Development | 1500 | False |
| Vlan4093 | MLAG_L3 | default | 1500 | False |
| Vlan4094 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan55 |  Production  |  -  |  10.10.55.1/24  |  -  |  -  |  -  |
| Vlan821 |  Production  |  -  |  10.82.1.1/24  |  -  |  -  |  -  |
| Vlan2821 |  Development  |  -  |  10.28.21.1/24  |  -  |  -  |  -  |
| Vlan2822 |  Development  |  -  |  10.28.22.1/24  |  -  |  -  |  -  |
| Vlan2833 |  Development  |  -  |  10.28.33.1/24  |  -  |  -  |  -  |
| Vlan2834 |  Development  |  -  |  10.28.34.1/24  |  -  |  -  |  -  |
| Vlan3009 |  Production  |  192.168.13.72/31  |  -  |  -  |  -  |  -  |
| Vlan3010 |  Development  |  192.168.13.72/31  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  192.168.13.72/31  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  192.168.13.104/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan55
   description HYPER_PROD
   no shutdown
   vrf Production
   ip address virtual 10.10.55.1/24
!
interface Vlan821
   description SAN_Disk
   no shutdown
   vrf Production
   ip address virtual 10.82.1.1/24
!
interface Vlan2821
   description Users_Dev
   no shutdown
   vrf Development
   ip address virtual 10.28.21.1/24
!
interface Vlan2822
   description Voice_Dev
   no shutdown
   vrf Development
   ip address virtual 10.28.22.1/24
!
interface Vlan2833
   description Broadcast1
   no shutdown
   vrf Development
   ip address virtual 10.28.33.1/24
!
interface Vlan2834
   description Broadcast2
   no shutdown
   vrf Development
   ip address virtual 10.28.34.1/24
!
interface Vlan3009
   description MLAG_L3_VRF_Production
   no shutdown
   mtu 1500
   vrf Production
   ip address 192.168.13.72/31
!
interface Vlan3010
   description MLAG_L3_VRF_Development
   no shutdown
   mtu 1500
   vrf Development
   ip address 192.168.13.72/31
!
interface Vlan4093
   description MLAG_L3
   no shutdown
   mtu 1500
   ip address 192.168.13.72/31
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 192.168.13.104/31
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 55 | 10055 | - | - |
| 821 | 10821 | - | - |
| 2821 | 12821 | - | - |
| 2822 | 12822 | - | - |
| 2833 | 12833 | - | - |
| 2834 | 12834 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Development | 11 | - |
| Production | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description OTI-DC01-Leaf5A_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 55 vni 10055
   vxlan vlan 821 vni 10821
   vxlan vlan 2821 vni 12821
   vxlan vlan 2822 vni 12822
   vxlan vlan 2833 vni 12833
   vxlan vlan 2834 vni 12834
   vxlan vrf Development vni 11
   vxlan vrf Production vni 10
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:1c:73:00:09:99

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:09:99
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| Development | True |
| Production | True |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Development
ip routing vrf Production
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| default | false |
| Development | false |
| Production | false |

### ARP

Global ARP timeout: 5400

#### ARP Device Configuration

```eos
!
arp aging timeout default 5400
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65005 | 10.245.217.7 |

| BGP Tuning |
| ---------- |
| graceful-restart restart-time 300 |
| graceful-restart |
| bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### INTER-DC-EVPN-PEERS

| Settings | Value |
| -------- | ----- |
| Remote AS | 65105 |
| Source | Loopback0 |
| Ebgp multihop | 10 |
| Send community | all |
| Maximum routes | 0 (no limit) (warning-limit 500000) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65005 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.245.217.1 | 65000 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.245.217.2 | 65000 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.245.218.7 | Inherited from peer group INTER-DC-EVPN-PEERS | default | - | Inherited from peer group INTER-DC-EVPN-PEERS | Inherited from peer group INTER-DC-EVPN-PEERS | - | - | - | - | - | - |
| 10.245.218.8 | Inherited from peer group INTER-DC-EVPN-PEERS | default | - | Inherited from peer group INTER-DC-EVPN-PEERS | Inherited from peer group INTER-DC-EVPN-PEERS | - | - | - | - | - | - |
| 192.168.10.249 | 65105 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.11.16 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.11.18 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.13.73 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 192.168.13.73 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Development | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 192.168.13.73 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Production | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |
| INTER-DC-EVPN-PEERS | True | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 55 | 10.245.217.7:10055 | 10055:10055 | - | - | learned |
| 821 | 10.245.217.7:10821 | 10821:10821 | - | - | learned |
| 2821 | 10.245.217.7:12821 | 12821:12821 | - | - | learned |
| 2822 | 10.245.217.7:12822 | 12822:12822 | - | - | learned |
| 2833 | 10.245.217.7:12833 | 12833:12833 | - | - | learned |
| 2834 | 10.245.217.7:12834 | 12834:12834 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Development | 10.245.217.7:11 | connected |
| Production | 10.245.217.7:10 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65005
   router-id 10.245.217.7
   bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor INTER-DC-EVPN-PEERS peer group
   neighbor INTER-DC-EVPN-PEERS remote-as 65105
   neighbor INTER-DC-EVPN-PEERS update-source Loopback0
   neighbor INTER-DC-EVPN-PEERS ebgp-multihop 10
   neighbor INTER-DC-EVPN-PEERS send-community
   neighbor INTER-DC-EVPN-PEERS maximum-routes 0 warning-limit 500000
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65005
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description OTI-DC01-Leaf5B
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 10.245.217.1 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.217.1 remote-as 65000
   neighbor 10.245.217.1 description OTI-DC01-Spine1_Loopback0
   neighbor 10.245.217.2 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.217.2 remote-as 65000
   neighbor 10.245.217.2 description OTI-DC01-Spine2_Loopback0
   neighbor 10.245.218.7 peer group INTER-DC-EVPN-PEERS
   neighbor 10.245.218.7 description OTI-DC02-Leaf5A
   neighbor 10.245.218.8 peer group INTER-DC-EVPN-PEERS
   neighbor 10.245.218.8 description OTI-DC02-Leaf5B
   neighbor 192.168.10.249 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.10.249 remote-as 65105
   neighbor 192.168.10.249 description OTI-DC02-Leaf5A
   neighbor 192.168.11.16 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.11.16 remote-as 65000
   neighbor 192.168.11.16 description OTI-DC01-Spine1_Ethernet5/1
   neighbor 192.168.11.18 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.11.18 remote-as 65000
   neighbor 192.168.11.18 description OTI-DC01-Spine2_Ethernet5/1
   neighbor 192.168.13.73 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 192.168.13.73 description OTI-DC01-Leaf5B_Vlan4093
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 55
      rd 10.245.217.7:10055
      route-target both 10055:10055
      redistribute learned
   !
   vlan 821
      rd 10.245.217.7:10821
      route-target both 10821:10821
      redistribute learned
   !
   vlan 2821
      rd 10.245.217.7:12821
      route-target both 12821:12821
      redistribute learned
   !
   vlan 2822
      rd 10.245.217.7:12822
      route-target both 12822:12822
      redistribute learned
   !
   vlan 2833
      rd 10.245.217.7:12833
      route-target both 12833:12833
      redistribute learned
   !
   vlan 2834
      rd 10.245.217.7:12834
      route-target both 12834:12834
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor INTER-DC-EVPN-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor INTER-DC-EVPN-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Development
      rd 10.245.217.7:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 10.245.217.7
      neighbor 192.168.13.73 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 192.168.13.73 description OTI-DC01-Leaf5B_Vlan3010
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Production
      rd 10.245.217.7:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 10.245.217.7
      neighbor 192.168.13.73 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 192.168.13.73 description OTI-DC01-Leaf5B_Vlan3009
      redistribute connected route-map RM-CONN-2-BGP-VRFS
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.245.217.0/27 eq 32 |
| 20 | permit 10.245.217.32/27 eq 32 |

##### PL-MLAG-PEER-VRFS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.13.72/31 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.245.217.0/27 eq 32
   seq 20 permit 10.245.217.32/27 eq 32
!
ip prefix-list PL-MLAG-PEER-VRFS
   seq 10 permit 192.168.13.72/31
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-CONN-2-BGP-VRFS

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | ip address prefix-list PL-MLAG-PEER-VRFS | - | - | - |
| 20 | permit | - | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP-VRFS deny 10
   match ip address prefix-list PL-MLAG-PEER-VRFS
!
route-map RM-CONN-2-BGP-VRFS permit 20
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Development | enabled |
| Production | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance Development
!
vrf instance Production
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Development | 10.1.11.7 |
| Production | 10.1.10.7 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Development address 10.1.11.7
ip address virtual source-nat vrf Production address 10.1.10.7
```
