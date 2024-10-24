# OTI-DC01-Leaf1

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
| Management1 | OOB_MANAGEMENT | oob | default | 192.168.255.13/24 | - |

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
   ip address 192.168.255.13/24
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
| 55 | HYPER_PROD | - |
| 100 | Compute | - |
| 101 | Data | - |
| 201 | VMOTION_A | - |
| 202 | VXRAIL | - |
| 400 | VMWARE_REPL | - |
| 500 | Compute_Backup | - |
| 501 | Data_Backup | - |
| 821 | SAN_Disk | - |
| 887 | NOCB_WORKLOAD1 | - |
| 888 | NOCB_WORKLOAD2 | - |
| 899 | NAS | - |
| 999 | BWS | - |
| 1000 | SRVR_FARM_BLADE | - |
| 1100 | SRVR_FARM_BLADE_0 | - |
| 1101 | SRVR_FARM_BLADE_1 | - |
| 1102 | SRVR_FARM_BLADE_2 | - |
| 1201 | UCP_MGMT_1 | - |
| 1202 | UCP_MGMT_2 | - |
| 2000 | Data_Prod | - |
| 2500 | Scada_Dev | - |
| 2821 | Users_Dev | - |
| 2822 | Voice_Dev | - |
| 2833 | Broadcast1 | - |
| 2834 | Broadcast2 | - |
| 3401 | L2_VLAN3401 | - |
| 3402 | L2_VLAN3402 | - |
| 3434 | VM_Servers | - |
| 3911 | SCADA_PROD | - |

### VLANs Device Configuration

```eos
!
vlan 21
   name VRF11_VLAN21
!
vlan 22
   name VRF11_VLAN22
!
vlan 55
   name HYPER_PROD
!
vlan 100
   name Compute
!
vlan 101
   name Data
!
vlan 201
   name VMOTION_A
!
vlan 202
   name VXRAIL
!
vlan 400
   name VMWARE_REPL
!
vlan 500
   name Compute_Backup
!
vlan 501
   name Data_Backup
!
vlan 821
   name SAN_Disk
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
vlan 1000
   name SRVR_FARM_BLADE
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
vlan 1201
   name UCP_MGMT_1
!
vlan 1202
   name UCP_MGMT_2
!
vlan 2000
   name Data_Prod
!
vlan 2500
   name Scada_Dev
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
vlan 3401
   name L2_VLAN3401
!
vlan 3402
   name L2_VLAN3402
!
vlan 3434
   name VM_Servers
!
vlan 3911
   name SCADA_PROD
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | SERVER_DC01-0601-ESX01_Onboard_NIC_1 | *trunk | *- | *- | *- | 1 |
| Ethernet25 | SERVER_DC01-0601-ESX01_Onboard_NIC_2 | *trunk | *- | *- | *- | 25 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet55/1 | P2P_OTI-DC01-Spine1_Ethernet1/1 | - | 192.168.11.1/31 | default | 1500 | False | - | - |
| Ethernet56/1 | P2P_OTI-DC01-Spine2_Ethernet1/1 | - | 192.168.11.3/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description SERVER_DC01-0601-ESX01_Onboard_NIC_1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet25
   description SERVER_DC01-0601-ESX01_Onboard_NIC_2
   no shutdown
   channel-group 25 mode active
!
interface Ethernet55/1
   description P2P_OTI-DC01-Spine1_Ethernet1/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.11.1/31
!
interface Ethernet56/1
   description P2P_OTI-DC01-Spine2_Ethernet1/1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.11.3/31
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | SERVER_DC01-0601-ESX01 | trunk | - | - | - | - | - | - | 0000:0000:ac9b:deb4:3bc0 |
| Port-Channel25 | SERVER_DC01-0601-ESX01 | trunk | - | - | - | - | - | - | 0000:0000:c8d4:663f:a199 |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel1 | 0000:0000:ac9b:deb4:3bc0 | all-active | ac:9b:de:b4:3b:c0 |
| Port-Channel25 | 0000:0000:c8d4:663f:a199 | all-active | c8:d4:66:3f:a1:99 |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description SERVER_DC01-0601-ESX01
   no shutdown
   mtu 9214
   switchport mode trunk
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:ac9b:deb4:3bc0
      route-target import ac:9b:de:b4:3b:c0
   lacp system-id ac9b.deb4.3bc0
   spanning-tree portfast
!
interface Port-Channel25
   description SERVER_DC01-0601-ESX01
   no shutdown
   mtu 9214
   switchport mode trunk
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:c8d4:663f:a199
      route-target import c8:d4:66:3f:a1:99
   lacp system-id c8d4.663f.a199
   spanning-tree portfast
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.245.217.3/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 10.245.217.35/32 |
| Loopback10 | DIAG_VRF_Production | Production | 10.1.10.3/32 |
| Loopback11 | DIAG_VRF_Development | Development | 10.1.11.3/32 |

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
   ip address 10.245.217.3/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 10.245.217.35/32
!
interface Loopback10
   description DIAG_VRF_Production
   no shutdown
   vrf Production
   ip address 10.1.10.3/32
!
interface Loopback11
   description DIAG_VRF_Development
   no shutdown
   vrf Development
   ip address 10.1.11.3/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan21 | VRF11_VLAN21 | Development | - | False |
| Vlan22 | VRF11_VLAN22 | Development | - | False |
| Vlan55 | HYPER_PROD | Production | - | False |
| Vlan100 | Compute | Production | - | False |
| Vlan101 | Data | Production | - | False |
| Vlan201 | VMOTION_A | Production | - | False |
| Vlan202 | VXRAIL | Production | - | False |
| Vlan400 | VMWARE_REPL | Production | - | False |
| Vlan500 | Compute_Backup | Production | - | False |
| Vlan501 | Data_Backup | Production | - | False |
| Vlan821 | SAN_Disk | Production | - | False |
| Vlan887 | NOCB_WORKLOAD1 | Production | - | False |
| Vlan888 | NOCB_WORKLOAD2 | Production | - | False |
| Vlan899 | NAS | Production | - | False |
| Vlan999 | BWS | Production | - | False |
| Vlan1000 | SRVR_FARM_BLADE | Production | - | False |
| Vlan1100 | SRVR_FARM_BLADE_0 | Production | - | False |
| Vlan1101 | SRVR_FARM_BLADE_1 | Production | - | False |
| Vlan1102 | SRVR_FARM_BLADE_2 | Production | - | False |
| Vlan1201 | UCP_MGMT_1 | Production | - | False |
| Vlan1202 | UCP_MGMT_2 | Production | - | False |
| Vlan2000 | Data_Prod | Production | - | False |
| Vlan2500 | Scada_Dev | Development | - | False |
| Vlan2821 | Users_Dev | Development | - | False |
| Vlan2822 | Voice_Dev | Development | - | False |
| Vlan2833 | Broadcast1 | Development | - | False |
| Vlan2834 | Broadcast2 | Development | - | False |
| Vlan3434 | VM_Servers | Production | - | False |
| Vlan3911 | SCADA_PROD | Production | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan21 |  Development  |  -  |  10.10.21.1/24  |  -  |  -  |  -  |
| Vlan22 |  Development  |  -  |  10.10.22.1/24  |  -  |  -  |  -  |
| Vlan55 |  Production  |  -  |  10.10.55.1/24  |  -  |  -  |  -  |
| Vlan100 |  Production  |  -  |  10.10.100.1/24  |  -  |  -  |  -  |
| Vlan101 |  Production  |  -  |  10.10.101.1/24  |  -  |  -  |  -  |
| Vlan201 |  Production  |  -  |  10.0.201.1/24  |  -  |  -  |  -  |
| Vlan202 |  Production  |  -  |  10.0.202.1/24  |  -  |  -  |  -  |
| Vlan400 |  Production  |  -  |  10.40.0.1/24  |  -  |  -  |  -  |
| Vlan500 |  Production  |  -  |  10.50.0.1/24  |  -  |  -  |  -  |
| Vlan501 |  Production  |  -  |  10.50.1.1/24  |  -  |  -  |  -  |
| Vlan821 |  Production  |  -  |  10.82.1.1/24  |  -  |  -  |  -  |
| Vlan887 |  Production  |  -  |  10.88.7.1/24  |  -  |  -  |  -  |
| Vlan888 |  Production  |  -  |  10.88.8.1/24  |  -  |  -  |  -  |
| Vlan899 |  Production  |  -  |  10.89.9.1/24  |  -  |  -  |  -  |
| Vlan999 |  Production  |  -  |  10.99.9.1/24  |  -  |  -  |  -  |
| Vlan1000 |  Production  |  -  |  10.0.0.1/24  |  -  |  -  |  -  |
| Vlan1100 |  Production  |  -  |  11.0.0.1/24  |  -  |  -  |  -  |
| Vlan1101 |  Production  |  -  |  11.0.1.1/24  |  -  |  -  |  -  |
| Vlan1102 |  Production  |  -  |  11.0.2.1/24  |  -  |  -  |  -  |
| Vlan1201 |  Production  |  -  |  12.0.1.1/24  |  -  |  -  |  -  |
| Vlan1202 |  Production  |  -  |  12.0.2.1/24  |  -  |  -  |  -  |
| Vlan2000 |  Production  |  -  |  20.0.0.1/24  |  -  |  -  |  -  |
| Vlan2500 |  Development  |  -  |  12.50.0.1/24  |  -  |  -  |  -  |
| Vlan2821 |  Development  |  -  |  10.28.21.1/24  |  -  |  -  |  -  |
| Vlan2822 |  Development  |  -  |  10.28.22.1/24  |  -  |  -  |  -  |
| Vlan2833 |  Development  |  -  |  10.28.33.1/24  |  -  |  -  |  -  |
| Vlan2834 |  Development  |  -  |  10.28.34.1/24  |  -  |  -  |  -  |
| Vlan3434 |  Production  |  -  |  10.34.34.1/24  |  -  |  -  |  -  |
| Vlan3911 |  Production  |  -  |  10.39.11.1/24  |  -  |  -  |  -  |

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
interface Vlan55
   description HYPER_PROD
   no shutdown
   vrf Production
   ip address virtual 10.10.55.1/24
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
interface Vlan201
   description VMOTION_A
   no shutdown
   vrf Production
   ip address virtual 10.0.201.1/24
!
interface Vlan202
   description VXRAIL
   no shutdown
   vrf Production
   ip address virtual 10.0.202.1/24
!
interface Vlan400
   description VMWARE_REPL
   no shutdown
   vrf Production
   ip address virtual 10.40.0.1/24
!
interface Vlan500
   description Compute_Backup
   no shutdown
   vrf Production
   ip address virtual 10.50.0.1/24
!
interface Vlan501
   description Data_Backup
   no shutdown
   vrf Production
   ip address virtual 10.50.1.1/24
!
interface Vlan821
   description SAN_Disk
   no shutdown
   vrf Production
   ip address virtual 10.82.1.1/24
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
interface Vlan1000
   description SRVR_FARM_BLADE
   no shutdown
   vrf Production
   ip address virtual 10.0.0.1/24
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
interface Vlan1201
   description UCP_MGMT_1
   no shutdown
   vrf Production
   ip address virtual 12.0.1.1/24
!
interface Vlan1202
   description UCP_MGMT_2
   no shutdown
   vrf Production
   ip address virtual 12.0.2.1/24
!
interface Vlan2000
   description Data_Prod
   no shutdown
   vrf Production
   ip address virtual 20.0.0.1/24
!
interface Vlan2500
   description Scada_Dev
   no shutdown
   vrf Development
   ip address virtual 12.50.0.1/24
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
interface Vlan3434
   description VM_Servers
   no shutdown
   vrf Production
   ip address virtual 10.34.34.1/24
!
interface Vlan3911
   description SCADA_PROD
   no shutdown
   vrf Production
   ip address virtual 10.39.11.1/24
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
| 55 | 10055 | - | - |
| 100 | 10100 | - | - |
| 101 | 10101 | - | - |
| 201 | 10201 | - | - |
| 202 | 10202 | - | - |
| 400 | 10400 | - | - |
| 500 | 10500 | - | - |
| 501 | 10501 | - | - |
| 821 | 10821 | - | - |
| 887 | 10887 | - | - |
| 888 | 10888 | - | - |
| 899 | 10899 | - | - |
| 999 | 10999 | - | - |
| 1000 | 11000 | - | - |
| 1100 | 11100 | - | - |
| 1101 | 11101 | - | - |
| 1102 | 11102 | - | - |
| 1201 | 11201 | - | - |
| 1202 | 11202 | - | - |
| 2000 | 12000 | - | - |
| 2500 | 12500 | - | - |
| 2821 | 12821 | - | - |
| 2822 | 12822 | - | - |
| 2833 | 12833 | - | - |
| 2834 | 12834 | - | - |
| 3401 | 13401 | - | - |
| 3402 | 13402 | - | - |
| 3434 | 13434 | - | - |
| 3911 | 13911 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Development | 11 | - |
| Production | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description OTI-DC01-Leaf1_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 21 vni 10021
   vxlan vlan 22 vni 10022
   vxlan vlan 55 vni 10055
   vxlan vlan 100 vni 10100
   vxlan vlan 101 vni 10101
   vxlan vlan 201 vni 10201
   vxlan vlan 202 vni 10202
   vxlan vlan 400 vni 10400
   vxlan vlan 500 vni 10500
   vxlan vlan 501 vni 10501
   vxlan vlan 821 vni 10821
   vxlan vlan 887 vni 10887
   vxlan vlan 888 vni 10888
   vxlan vlan 899 vni 10899
   vxlan vlan 999 vni 10999
   vxlan vlan 1000 vni 11000
   vxlan vlan 1100 vni 11100
   vxlan vlan 1101 vni 11101
   vxlan vlan 1102 vni 11102
   vxlan vlan 1201 vni 11201
   vxlan vlan 1202 vni 11202
   vxlan vlan 2000 vni 12000
   vxlan vlan 2500 vni 12500
   vxlan vlan 2821 vni 12821
   vxlan vlan 2822 vni 12822
   vxlan vlan 2833 vni 12833
   vxlan vlan 2834 vni 12834
   vxlan vlan 3401 vni 13401
   vxlan vlan 3402 vni 13402
   vxlan vlan 3434 vni 13434
   vxlan vlan 3911 vni 13911
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
| 65001 | 10.245.217.3 |

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
| 10.245.217.1 | 65000 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.245.217.2 | 65000 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.11.0 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.11.2 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 21 | 10.245.217.3:10021 | 10021:10021 | - | - | learned |
| 22 | 10.245.217.3:10022 | 10022:10022 | - | - | learned |
| 55 | 10.245.217.3:10055 | 10055:10055 | - | - | learned |
| 100 | 10.245.217.3:10100 | 10100:10100 | - | - | learned |
| 101 | 10.245.217.3:10101 | 10101:10101 | - | - | learned |
| 201 | 10.245.217.3:10201 | 10201:10201 | - | - | learned |
| 202 | 10.245.217.3:10202 | 10202:10202 | - | - | learned |
| 400 | 10.245.217.3:10400 | 10400:10400 | - | - | learned |
| 500 | 10.245.217.3:10500 | 10500:10500 | - | - | learned |
| 501 | 10.245.217.3:10501 | 10501:10501 | - | - | learned |
| 821 | 10.245.217.3:10821 | 10821:10821 | - | - | learned |
| 887 | 10.245.217.3:10887 | 10887:10887 | - | - | learned |
| 888 | 10.245.217.3:10888 | 10888:10888 | - | - | learned |
| 899 | 10.245.217.3:10899 | 10899:10899 | - | - | learned |
| 999 | 10.245.217.3:10999 | 10999:10999 | - | - | learned |
| 1000 | 10.245.217.3:11000 | 11000:11000 | - | - | learned |
| 1100 | 10.245.217.3:11100 | 11100:11100 | - | - | learned |
| 1101 | 10.245.217.3:11101 | 11101:11101 | - | - | learned |
| 1102 | 10.245.217.3:11102 | 11102:11102 | - | - | learned |
| 1201 | 10.245.217.3:11201 | 11201:11201 | - | - | learned |
| 1202 | 10.245.217.3:11202 | 11202:11202 | - | - | learned |
| 2000 | 10.245.217.3:12000 | 12000:12000 | - | - | learned |
| 2500 | 10.245.217.3:12500 | 12500:12500 | - | - | learned |
| 2821 | 10.245.217.3:12821 | 12821:12821 | - | - | learned |
| 2822 | 10.245.217.3:12822 | 12822:12822 | - | - | learned |
| 2833 | 10.245.217.3:12833 | 12833:12833 | - | - | learned |
| 2834 | 10.245.217.3:12834 | 12834:12834 | - | - | learned |
| 3401 | 10.245.217.3:13401 | 13401:13401 | - | - | learned |
| 3402 | 10.245.217.3:13402 | 13402:13402 | - | - | learned |
| 3434 | 10.245.217.3:13434 | 13434:13434 | - | - | learned |
| 3911 | 10.245.217.3:13911 | 13911:13911 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Development | 10.245.217.3:11 | connected |
| Production | 10.245.217.3:10 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 10.245.217.3
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
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.245.217.1 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.217.1 remote-as 65000
   neighbor 10.245.217.1 description OTI-DC01-Spine1_Loopback0
   neighbor 10.245.217.2 peer group EVPN-OVERLAY-PEERS
   neighbor 10.245.217.2 remote-as 65000
   neighbor 10.245.217.2 description OTI-DC01-Spine2_Loopback0
   neighbor 192.168.11.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.11.0 remote-as 65000
   neighbor 192.168.11.0 description OTI-DC01-Spine1_Ethernet1/1
   neighbor 192.168.11.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.11.2 remote-as 65000
   neighbor 192.168.11.2 description OTI-DC01-Spine2_Ethernet1/1
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 21
      rd 10.245.217.3:10021
      route-target both 10021:10021
      redistribute learned
   !
   vlan 22
      rd 10.245.217.3:10022
      route-target both 10022:10022
      redistribute learned
   !
   vlan 55
      rd 10.245.217.3:10055
      route-target both 10055:10055
      redistribute learned
   !
   vlan 100
      rd 10.245.217.3:10100
      route-target both 10100:10100
      redistribute learned
   !
   vlan 101
      rd 10.245.217.3:10101
      route-target both 10101:10101
      redistribute learned
   !
   vlan 201
      rd 10.245.217.3:10201
      route-target both 10201:10201
      redistribute learned
   !
   vlan 202
      rd 10.245.217.3:10202
      route-target both 10202:10202
      redistribute learned
   !
   vlan 400
      rd 10.245.217.3:10400
      route-target both 10400:10400
      redistribute learned
   !
   vlan 500
      rd 10.245.217.3:10500
      route-target both 10500:10500
      redistribute learned
   !
   vlan 501
      rd 10.245.217.3:10501
      route-target both 10501:10501
      redistribute learned
   !
   vlan 821
      rd 10.245.217.3:10821
      route-target both 10821:10821
      redistribute learned
   !
   vlan 887
      rd 10.245.217.3:10887
      route-target both 10887:10887
      redistribute learned
   !
   vlan 888
      rd 10.245.217.3:10888
      route-target both 10888:10888
      redistribute learned
   !
   vlan 899
      rd 10.245.217.3:10899
      route-target both 10899:10899
      redistribute learned
   !
   vlan 999
      rd 10.245.217.3:10999
      route-target both 10999:10999
      redistribute learned
   !
   vlan 1000
      rd 10.245.217.3:11000
      route-target both 11000:11000
      redistribute learned
   !
   vlan 1100
      rd 10.245.217.3:11100
      route-target both 11100:11100
      redistribute learned
   !
   vlan 1101
      rd 10.245.217.3:11101
      route-target both 11101:11101
      redistribute learned
   !
   vlan 1102
      rd 10.245.217.3:11102
      route-target both 11102:11102
      redistribute learned
   !
   vlan 1201
      rd 10.245.217.3:11201
      route-target both 11201:11201
      redistribute learned
   !
   vlan 1202
      rd 10.245.217.3:11202
      route-target both 11202:11202
      redistribute learned
   !
   vlan 2000
      rd 10.245.217.3:12000
      route-target both 12000:12000
      redistribute learned
   !
   vlan 2500
      rd 10.245.217.3:12500
      route-target both 12500:12500
      redistribute learned
   !
   vlan 2821
      rd 10.245.217.3:12821
      route-target both 12821:12821
      redistribute learned
   !
   vlan 2822
      rd 10.245.217.3:12822
      route-target both 12822:12822
      redistribute learned
   !
   vlan 2833
      rd 10.245.217.3:12833
      route-target both 12833:12833
      redistribute learned
   !
   vlan 2834
      rd 10.245.217.3:12834
      route-target both 12834:12834
      redistribute learned
   !
   vlan 3401
      rd 10.245.217.3:13401
      route-target both 13401:13401
      redistribute learned
   !
   vlan 3402
      rd 10.245.217.3:13402
      route-target both 13402:13402
      redistribute learned
   !
   vlan 3434
      rd 10.245.217.3:13434
      route-target both 13434:13434
      redistribute learned
   !
   vlan 3911
      rd 10.245.217.3:13911
      route-target both 13911:13911
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
      rd 10.245.217.3:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 10.245.217.3
      redistribute connected
   !
   vrf Production
      rd 10.245.217.3:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 10.245.217.3
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
| 10 | permit 10.245.217.0/27 eq 32 |
| 20 | permit 10.245.217.32/27 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.245.217.0/27 eq 32
   seq 20 permit 10.245.217.32/27 eq 32
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
| Development | 10.1.11.3 |
| Production | 10.1.10.3 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Development address 10.1.11.3
ip address virtual source-nat vrf Production address 10.1.10.3
```
