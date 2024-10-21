# OTI-DC02-Leaf5B

## Table of Contents

- [Management](#management)
  - [Agents](#agents)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
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
| Management1 | oob_management | oob | default | 192.168.255.28/24 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | default | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   ip address 192.168.255.28/24
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
| OTI-DC02-Leaf5 | Vlan4094 | 192.168.14.104 | Port-Channel531 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id OTI-DC02-Leaf5
   local-interface Vlan4094
   peer-address 192.168.14.104
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
| 887 | NOCB_WORKLOAD1 | - |
| 888 | NOCB_WORKLOAD2 | - |
| 899 | NAS | - |
| 999 | BWS | - |
| 1100 | SRVR_FARM_BLADE_0 | - |
| 1101 | SRVR_FARM_BLADE_1 | - |
| 1102 | SRVR_FARM_BLADE_2 | - |
| 3009 | MLAG_iBGP_Production | LEAF_PEER_L3 |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

### VLANs Device Configuration

```eos
!
vlan 887
   name NOCB_WORKLOAD1
!
vlan 888
   name NOCB_WORKLOAD2
!
vlan 899
   name NAS
!
vlan 999
   name BWS
!
vlan 1100
   name SRVR_FARM_BLADE_0
!
vlan 1101
   name SRVR_FARM_BLADE_1
!
vlan 1102
   name SRVR_FARM_BLADE_2
!
vlan 3009
   name MLAG_iBGP_Production
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | DC02-0901-ESX04_PCI_slot_2_Port_2 | *trunk | *899, 999 | *- | *- | 1 |
| Ethernet2 | DC02-0901-ESX06_PCI_slot_2_Port_2 | *trunk | *899, 999 | *- | *- | 2 |
| Ethernet49/1 | DC02-0901-ESX05_PCI_slot_2_Port_1 | *trunk | *1100, 1101, 1102 | *- | *- | 491 |
| Ethernet50/1 | DC02-0901-ESX06_PCI_slot_2_Port_1 | *trunk | *887, 888 | *- | *- | 501 |
| Ethernet53/1 | MLAG_PEER_OTI-DC02-Leaf5A_Ethernet53/1 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 531 |
| Ethernet54/1 | MLAG_PEER_OTI-DC02-Leaf5A_Ethernet54/1 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 531 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet52/1 | P2P_LINK_TO_OTI-DC01-Leaf5B_Ethernet52/1 | routed | - | 192.168.10.251/31 | default | 1500 | False | - | - |
| Ethernet55/1 | P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet6/1 | routed | - | 192.168.12.21/31 | default | 1500 | False | - | - |
| Ethernet56/1 | P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet6/1 | routed | - | 192.168.12.23/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description DC02-0901-ESX04_PCI_slot_2_Port_2
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description DC02-0901-ESX06_PCI_slot_2_Port_2
   no shutdown
   channel-group 2 mode active
!
interface Ethernet49/1
   description DC02-0901-ESX05_PCI_slot_2_Port_1
   no shutdown
   channel-group 491 mode active
!
interface Ethernet50/1
   description DC02-0901-ESX06_PCI_slot_2_Port_1
   no shutdown
   channel-group 501 mode active
!
interface Ethernet52/1
   description P2P_LINK_TO_OTI-DC01-Leaf5B_Ethernet52/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.10.251/31
!
interface Ethernet53/1
   description MLAG_PEER_OTI-DC02-Leaf5A_Ethernet53/1
   no shutdown
   channel-group 531 mode active
!
interface Ethernet54/1
   description MLAG_PEER_OTI-DC02-Leaf5A_Ethernet54/1
   no shutdown
   channel-group 531 mode active
!
interface Ethernet55/1
   description P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet6/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.12.21/31
!
interface Ethernet56/1
   description P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet6/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.12.23/31
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | DC02-0901-ESX04 | switched | trunk | 899, 999 | - | - | - | - | 1 | - |
| Port-Channel2 | DC02-0901-ESX06 | switched | trunk | 899, 999 | - | - | - | - | 2 | - |
| Port-Channel491 | DC02-0901-ESX05 | switched | trunk | 1100, 1101, 1102 | - | - | - | - | 491 | - |
| Port-Channel501 | DC02-0901-ESX06 | switched | trunk | 887, 888 | - | - | - | - | 501 | - |
| Port-Channel531 | MLAG_PEER_OTI-DC02-Leaf5A_Po531 | switched | trunk | - | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description DC02-0901-ESX04
   no shutdown
   mtu 9214
   switchport
   switchport trunk allowed vlan 899, 999
   switchport mode trunk
   mlag 1
   spanning-tree portfast
!
interface Port-Channel2
   description DC02-0901-ESX06
   no shutdown
   mtu 9214
   switchport
   switchport trunk allowed vlan 899, 999
   switchport mode trunk
   mlag 2
   spanning-tree portfast
!
interface Port-Channel491
   description DC02-0901-ESX05
   no shutdown
   mtu 9214
   switchport
   switchport trunk allowed vlan 1100, 1101, 1102
   switchport mode trunk
   mlag 491
   spanning-tree portfast
!
interface Port-Channel501
   description DC02-0901-ESX06
   no shutdown
   mtu 9214
   switchport
   switchport trunk allowed vlan 887, 888
   switchport mode trunk
   mlag 501
   spanning-tree portfast
!
interface Port-Channel531
   description MLAG_PEER_OTI-DC02-Leaf5A_Po531
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.245.218.8/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 10.245.218.39/32 |
| Loopback10 | Production_VTEP_DIAGNOSTICS | Production | 10.2.10.8/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback10 | Production_VTEP_DIAGNOSTICS | Production | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.245.218.8/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 10.245.218.39/32
!
interface Loopback10
   description Production_VTEP_DIAGNOSTICS
   no shutdown
   vrf Production
   ip address 10.2.10.8/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan887 | NOCB_WORKLOAD1 | Production | - | False |
| Vlan888 | NOCB_WORKLOAD2 | Production | - | False |
| Vlan899 | NAS | Production | - | False |
| Vlan999 | BWS | Production | - | False |
| Vlan1100 | SRVR_FARM_BLADE_0 | Production | - | False |
| Vlan1101 | SRVR_FARM_BLADE_1 | Production | - | False |
| Vlan1102 | SRVR_FARM_BLADE_2 | Production | - | False |
| Vlan3009 | MLAG_PEER_L3_iBGP: vrf Production | Production | 1500 | False |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 1500 | False |
| Vlan4094 | MLAG_PEER | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan887 |  Production  |  -  |  10.88.7.1/24  |  -  |  -  |  -  |  -  |
| Vlan888 |  Production  |  -  |  10.88.8.1/24  |  -  |  -  |  -  |  -  |
| Vlan899 |  Production  |  -  |  10.89.9.1/24  |  -  |  -  |  -  |  -  |
| Vlan999 |  Production  |  -  |  10.99.9.1/24  |  -  |  -  |  -  |  -  |
| Vlan1100 |  Production  |  -  |  11.0.0.1/24  |  -  |  -  |  -  |  -  |
| Vlan1101 |  Production  |  -  |  11.0.1.1/24  |  -  |  -  |  -  |  -  |
| Vlan1102 |  Production  |  -  |  11.0.2.1/24  |  -  |  -  |  -  |  -  |
| Vlan3009 |  Production  |  192.168.14.73/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  192.168.14.73/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  192.168.14.105/31  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan887
   description NOCB_WORKLOAD1
   no shutdown
   vrf Production
   ip address virtual 10.88.7.1/24
!
interface Vlan888
   description NOCB_WORKLOAD2
   no shutdown
   vrf Production
   ip address virtual 10.88.8.1/24
!
interface Vlan899
   description NAS
   no shutdown
   vrf Production
   ip address virtual 10.89.9.1/24
!
interface Vlan999
   description BWS
   no shutdown
   vrf Production
   ip address virtual 10.99.9.1/24
!
interface Vlan1100
   description SRVR_FARM_BLADE_0
   no shutdown
   vrf Production
   ip address virtual 11.0.0.1/24
!
interface Vlan1101
   description SRVR_FARM_BLADE_1
   no shutdown
   vrf Production
   ip address virtual 11.0.1.1/24
!
interface Vlan1102
   description SRVR_FARM_BLADE_2
   no shutdown
   vrf Production
   ip address virtual 11.0.2.1/24
!
interface Vlan3009
   description MLAG_PEER_L3_iBGP: vrf Production
   no shutdown
   mtu 1500
   vrf Production
   ip address 192.168.14.73/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ip address 192.168.14.73/31
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 192.168.14.105/31
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
| 887 | 10887 | - | - |
| 888 | 10888 | - | - |
| 899 | 10899 | - | - |
| 999 | 10999 | - | - |
| 1100 | 11100 | - | - |
| 1101 | 11101 | - | - |
| 1102 | 11102 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Production | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description OTI-DC02-Leaf5B_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 887 vni 10887
   vxlan vlan 888 vni 10888
   vxlan vlan 899 vni 10899
   vxlan vlan 999 vni 10999
   vxlan vlan 1100 vni 11100
   vxlan vlan 1101 vni 11101
   vxlan vlan 1102 vni 11102
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
| Production | True |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Production
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| default | false |
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
| 65105 | 10.245.218.8 |

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
| Remote AS | 65005 |
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
| Remote AS | 65105 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.245.217.7 | Inherited from peer group INTER-DC-EVPN-PEERS | default | - | Inherited from peer group INTER-DC-EVPN-PEERS | Inherited from peer group INTER-DC-EVPN-PEERS | - | - | - | - | - | - |
| 10.245.217.8 | Inherited from peer group INTER-DC-EVPN-PEERS | default | - | Inherited from peer group INTER-DC-EVPN-PEERS | Inherited from peer group INTER-DC-EVPN-PEERS | - | - | - | - | - | - |
| 10.245.218.1 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.245.218.2 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.10.250 | 65005 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.12.20 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.12.22 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.14.72 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 192.168.14.72 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Production | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |
| INTER-DC-EVPN-PEERS | True | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 887 | 10.245.218.8:10887 | 10887:10887 | - | - | learned |
| 888 | 10.245.218.8:10888 | 10888:10888 | - | - | learned |
| 899 | 10.245.218.8:10899 | 10899:10899 | - | - | learned |
| 999 | 10.245.218.8:10999 | 10999:10999 | - | - | learned |
| 1100 | 10.245.218.8:11100 | 11100:11100 | - | - | learned |
| 1101 | 10.245.218.8:11101 | 11101:11101 | - | - | learned |
| 1102 | 10.245.218.8:11102 | 11102:11102 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Production | 10.245.218.8:10 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65105
   router-id 10.245.218.8
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   bgp default ipv4-unicast
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor INTER-DC-EVPN-PEERS peer group
   neighbor INTER-DC-EVPN-PEERS remote-as 65005
   neighbor INTER-DC-EVPN-PEERS update-source Loopback0
   neighbor INTER-DC-EVPN-PEERS ebgp-multihop 10
   neighbor INTER-DC-EVPN-PEERS send-community
   neighbor INTER-DC-EVPN-PEERS maximum-routes 0 warning-limit 500000
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65105
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description OTI-DC02-Leaf5A
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 10.245.217.7 peer group INTER-DC-EVPN-PEERS
   neighbor 10.245.217.7 description OTI-DC01-Leaf5A
   neighbor 10.245.217.8 peer group INTER-DC-EVPN-PEERS
   neighbor 10.245.217.8 description OTI-DC01-Leaf5B
   neighbor 10.245.218.1 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.218.1 remote-as 65100
   neighbor 10.245.218.1 description OTI-DC02-Spine1
   neighbor 10.245.218.2 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.218.2 remote-as 65100
   neighbor 10.245.218.2 description OTI-DC02-Spine2
   neighbor 192.168.10.250 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.10.250 remote-as 65005
   neighbor 192.168.10.250 description OTI-DC01-Leaf5B
   neighbor 192.168.12.20 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.12.20 remote-as 65100
   neighbor 192.168.12.20 description OTI-DC02-Spine1_Ethernet6/1
   neighbor 192.168.12.22 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.12.22 remote-as 65100
   neighbor 192.168.12.22 description OTI-DC02-Spine2_Ethernet6/1
   neighbor 192.168.14.72 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 192.168.14.72 description OTI-DC02-Leaf5A
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 1100
      rd 10.245.218.8:11100
      route-target both 11100:11100
      redistribute learned
   !
   vlan 1101
      rd 10.245.218.8:11101
      route-target both 11101:11101
      redistribute learned
   !
   vlan 1102
      rd 10.245.218.8:11102
      route-target both 11102:11102
      redistribute learned
   !
   vlan 887
      rd 10.245.218.8:10887
      route-target both 10887:10887
      redistribute learned
   !
   vlan 888
      rd 10.245.218.8:10888
      route-target both 10888:10888
      redistribute learned
   !
   vlan 899
      rd 10.245.218.8:10899
      route-target both 10899:10899
      redistribute learned
   !
   vlan 999
      rd 10.245.218.8:10999
      route-target both 10999:10999
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
   vrf Production
      rd 10.245.218.8:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 10.245.218.8
      neighbor 192.168.14.72 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
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
| 10 | permit 10.245.218.0/27 eq 32 |
| 20 | permit 10.245.218.32/27 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.245.218.0/27 eq 32
   seq 20 permit 10.245.218.32/27 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

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
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Production | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance Production
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Production | 10.2.10.8 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Production address 10.2.10.8
```
