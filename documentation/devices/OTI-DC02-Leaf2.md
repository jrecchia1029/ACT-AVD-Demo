# OTI-DC02-Leaf2

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
| Management1 | oob_management | oob | default | 192.168.255.24/24 | - |

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
   ip address 192.168.255.24/24
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

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
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
| 21 | VRF11_VLAN21 | - |
| 22 | VRF11_VLAN22 | - |
| 100 | Compute | - |
| 101 | Data | - |
| 3401 | L2_VLAN3401 | - |
| 3402 | L2_VLAN3402 | - |
| 3434 | Server_MGMT | - |
| 3545 | Server_MGMT | - |

### VLANs Device Configuration

```eos
!
vlan 21
   name VRF11_VLAN21
!
vlan 22
   name VRF11_VLAN22
!
vlan 100
   name Compute
!
vlan 101
   name Data
!
vlan 3401
   name L2_VLAN3401
!
vlan 3402
   name L2_VLAN3402
!
vlan 3434
   name Server_MGMT
!
vlan 3545
   name Server_MGMT
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet6 | DC02-0901-ESX06_PCI_slot_1_Port_1 | *trunk | *3434 | *- | *- | 6 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet55/1 | P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet2/1 | routed | - | 192.168.12.5/31 | default | 1500 | False | - | - |
| Ethernet56/1 | P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet2/1 | routed | - | 192.168.12.7/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet6
   description DC02-0901-ESX06_PCI_slot_1_Port_1
   no shutdown
   channel-group 6 mode active
!
interface Ethernet55/1
   description P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet2/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.12.5/31
!
interface Ethernet56/1
   description P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet2/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.12.7/31
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel6 | DC02-0901-ESX06_PortChanne1 | switched | trunk | 3434 | - | - | - | - | - | 0000:0000:6ec9:e834:38c2 |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel6 | 0000:0000:6ec9:e834:38c2 | all-active | 6e:c9:e8:34:38:c2 |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel6
   description DC02-0901-ESX06_PortChanne1
   no shutdown
   switchport
   switchport trunk allowed vlan 3434
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:6ec9:e834:38c2
      route-target import 6e:c9:e8:34:38:c2
   lacp system-id 6ec9.e834.38c2
   spanning-tree portfast
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.245.218.4/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 10.245.218.36/32 |
| Loopback10 | Production_VTEP_DIAGNOSTICS | Production | 10.2.10.4/32 |
| Loopback11 | Development_VTEP_DIAGNOSTICS | Development | 10.2.11.4/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback10 | Production_VTEP_DIAGNOSTICS | Production | - |
| Loopback11 | Development_VTEP_DIAGNOSTICS | Development | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.245.218.4/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 10.245.218.36/32
!
interface Loopback10
   description Production_VTEP_DIAGNOSTICS
   no shutdown
   vrf Production
   ip address 10.2.10.4/32
!
interface Loopback11
   description Development_VTEP_DIAGNOSTICS
   no shutdown
   vrf Development
   ip address 10.2.11.4/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan21 | VRF11_VLAN21 | Development | - | False |
| Vlan22 | VRF11_VLAN22 | Development | - | False |
| Vlan100 | Compute | Production | - | False |
| Vlan101 | Data | Production | - | False |
| Vlan3434 | Server_MGMT | Production | - | False |
| Vlan3545 | Server_MGMT | Production | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan21 |  Development  |  -  |  10.10.21.1/24  |  -  |  -  |  -  |  -  |
| Vlan22 |  Development  |  -  |  10.10.22.1/24  |  -  |  -  |  -  |  -  |
| Vlan100 |  Production  |  -  |  10.10.100.1/24  |  -  |  -  |  -  |  -  |
| Vlan101 |  Production  |  -  |  10.10.101.1/24  |  -  |  -  |  -  |  -  |
| Vlan3434 |  Production  |  -  |  10.34.34.1/24  |  -  |  -  |  -  |  -  |
| Vlan3545 |  Production  |  -  |  10.35.45.1/24  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan21
   description VRF11_VLAN21
   no shutdown
   vrf Development
   ip address virtual 10.10.21.1/24
!
interface Vlan22
   description VRF11_VLAN22
   no shutdown
   vrf Development
   ip address virtual 10.10.22.1/24
!
interface Vlan100
   description Compute
   no shutdown
   vrf Production
   ip address virtual 10.10.100.1/24
!
interface Vlan101
   description Data
   no shutdown
   vrf Production
   ip address virtual 10.10.101.1/24
!
interface Vlan3434
   description Server_MGMT
   no shutdown
   vrf Production
   ip address virtual 10.34.34.1/24
!
interface Vlan3545
   description Server_MGMT
   no shutdown
   vrf Production
   ip address virtual 10.35.45.1/24
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 21 | 10021 | - | - |
| 22 | 10022 | - | - |
| 100 | 10100 | - | - |
| 101 | 10101 | - | - |
| 3401 | 13401 | - | - |
| 3402 | 13402 | - | - |
| 3434 | 13434 | - | - |
| 3545 | 13545 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Development | 11 | - |
| Production | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description OTI-DC02-Leaf2_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 21 vni 10021
   vxlan vlan 22 vni 10022
   vxlan vlan 100 vni 10100
   vxlan vlan 101 vni 10101
   vxlan vlan 3401 vni 13401
   vxlan vlan 3402 vni 13402
   vxlan vlan 3434 vni 13434
   vxlan vlan 3545 vni 13545
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
| 65102 | 10.245.218.4 |

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

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.245.218.1 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.245.218.2 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.12.4 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.12.6 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 21 | 10.245.218.4:10021 | 10021:10021 | - | - | learned |
| 22 | 10.245.218.4:10022 | 10022:10022 | - | - | learned |
| 100 | 10.245.218.4:10100 | 10100:10100 | - | - | learned |
| 101 | 10.245.218.4:10101 | 10101:10101 | - | - | learned |
| 3401 | 10.245.218.4:13401 | 13401:13401 | - | - | learned |
| 3402 | 10.245.218.4:13402 | 13402:13402 | - | - | learned |
| 3434 | 10.245.218.4:13434 | 13434:13434 | - | - | learned |
| 3545 | 10.245.218.4:13545 | 13545:13545 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Development | 10.245.218.4:11 | connected |
| Production | 10.245.218.4:10 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65102
   router-id 10.245.218.4
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
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.245.218.1 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.218.1 remote-as 65100
   neighbor 10.245.218.1 description OTI-DC02-Spine1
   neighbor 10.245.218.2 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.218.2 remote-as 65100
   neighbor 10.245.218.2 description OTI-DC02-Spine2
   neighbor 192.168.12.4 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.12.4 remote-as 65100
   neighbor 192.168.12.4 description OTI-DC02-Spine1_Ethernet2/1
   neighbor 192.168.12.6 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.12.6 remote-as 65100
   neighbor 192.168.12.6 description OTI-DC02-Spine2_Ethernet2/1
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 100
      rd 10.245.218.4:10100
      route-target both 10100:10100
      redistribute learned
   !
   vlan 101
      rd 10.245.218.4:10101
      route-target both 10101:10101
      redistribute learned
   !
   vlan 21
      rd 10.245.218.4:10021
      route-target both 10021:10021
      redistribute learned
   !
   vlan 22
      rd 10.245.218.4:10022
      route-target both 10022:10022
      redistribute learned
   !
   vlan 3401
      rd 10.245.218.4:13401
      route-target both 13401:13401
      redistribute learned
   !
   vlan 3402
      rd 10.245.218.4:13402
      route-target both 13402:13402
      redistribute learned
   !
   vlan 3434
      rd 10.245.218.4:13434
      route-target both 13434:13434
      redistribute learned
   !
   vlan 3545
      rd 10.245.218.4:13545
      route-target both 13545:13545
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf Development
      rd 10.245.218.4:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 10.245.218.4
      redistribute connected
   !
   vrf Production
      rd 10.245.218.4:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 10.245.218.4
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

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
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
| Development | 10.2.11.4 |
| Production | 10.2.10.4 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Development address 10.2.11.4
ip address virtual source-nat vrf Production address 10.2.10.4
```
