# DC01_Fabric

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)
- [Connected Endpoints](#connected-endpoints)
  - [Connected Endpoint Keys](#connected-endpoint-keys)
  - [Servers](#servers)
  - [Port Profiles](#port-profiles)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC01_Pod1 | l3leaf | OTI-DC01-Leaf1 | 192.168.255.13/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Leaf1 |
| DC01_Pod1 | l3leaf | OTI-DC01-Leaf2 | 192.168.255.14/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Leaf2 |
| DC01_Pod1 | l3leaf | OTI-DC01-Leaf3 | 192.168.255.15/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Leaf3 |
| DC01_Pod1 | l3leaf | OTI-DC01-Leaf4 | 192.168.255.16/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Leaf4 |
| DC01_Pod1 | l3leaf | OTI-DC01-Leaf5A | 192.168.255.17/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Leaf5A |
| DC01_Pod1 | l3leaf | OTI-DC01-Leaf5B | 192.168.255.18/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Leaf5B |
| DC01_Pod1 | spine | OTI-DC01-Spine1 | 192.168.255.11/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Spine1 |
| DC01_Pod1 | spine | OTI-DC01-Spine2 | 192.168.255.12/24 | vEOS-lab | Provisioned | SN-OTI-DC01-Spine2 |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | OTI-DC01-Leaf1 | Ethernet55/1 | spine | OTI-DC01-Spine1 | Ethernet1/1 |
| l3leaf | OTI-DC01-Leaf1 | Ethernet56/1 | spine | OTI-DC01-Spine2 | Ethernet1/1 |
| l3leaf | OTI-DC01-Leaf2 | Ethernet55/1 | spine | OTI-DC01-Spine1 | Ethernet2/1 |
| l3leaf | OTI-DC01-Leaf2 | Ethernet56/1 | spine | OTI-DC01-Spine2 | Ethernet2/1 |
| l3leaf | OTI-DC01-Leaf3 | Ethernet55/1 | spine | OTI-DC01-Spine1 | Ethernet3/1 |
| l3leaf | OTI-DC01-Leaf3 | Ethernet56/1 | spine | OTI-DC01-Spine2 | Ethernet3/1 |
| l3leaf | OTI-DC01-Leaf4 | Ethernet55/1 | spine | OTI-DC01-Spine1 | Ethernet4/1 |
| l3leaf | OTI-DC01-Leaf4 | Ethernet56/1 | spine | OTI-DC01-Spine2 | Ethernet4/1 |
| l3leaf | OTI-DC01-Leaf5A | Ethernet53/1 | mlag_peer | OTI-DC01-Leaf5B | Ethernet53/1 |
| l3leaf | OTI-DC01-Leaf5A | Ethernet54/1 | mlag_peer | OTI-DC01-Leaf5B | Ethernet54/1 |
| l3leaf | OTI-DC01-Leaf5A | Ethernet55/1 | spine | OTI-DC01-Spine1 | Ethernet5/1 |
| l3leaf | OTI-DC01-Leaf5A | Ethernet56/1 | spine | OTI-DC01-Spine2 | Ethernet5/1 |
| l3leaf | OTI-DC01-Leaf5B | Ethernet55/1 | spine | OTI-DC01-Spine1 | Ethernet6/1 |
| l3leaf | OTI-DC01-Leaf5B | Ethernet56/1 | spine | OTI-DC01-Spine2 | Ethernet6/1 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.11.0/26 | 64 | 24 | 37.5 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| OTI-DC01-Leaf1 | Ethernet55/1 | 192.168.11.1/31 | OTI-DC01-Spine1 | Ethernet1/1 | 192.168.11.0/31 |
| OTI-DC01-Leaf1 | Ethernet56/1 | 192.168.11.3/31 | OTI-DC01-Spine2 | Ethernet1/1 | 192.168.11.2/31 |
| OTI-DC01-Leaf2 | Ethernet55/1 | 192.168.11.5/31 | OTI-DC01-Spine1 | Ethernet2/1 | 192.168.11.4/31 |
| OTI-DC01-Leaf2 | Ethernet56/1 | 192.168.11.7/31 | OTI-DC01-Spine2 | Ethernet2/1 | 192.168.11.6/31 |
| OTI-DC01-Leaf3 | Ethernet55/1 | 192.168.11.9/31 | OTI-DC01-Spine1 | Ethernet3/1 | 192.168.11.8/31 |
| OTI-DC01-Leaf3 | Ethernet56/1 | 192.168.11.11/31 | OTI-DC01-Spine2 | Ethernet3/1 | 192.168.11.10/31 |
| OTI-DC01-Leaf4 | Ethernet55/1 | 192.168.11.13/31 | OTI-DC01-Spine1 | Ethernet4/1 | 192.168.11.12/31 |
| OTI-DC01-Leaf4 | Ethernet56/1 | 192.168.11.15/31 | OTI-DC01-Spine2 | Ethernet4/1 | 192.168.11.14/31 |
| OTI-DC01-Leaf5A | Ethernet55/1 | 192.168.11.17/31 | OTI-DC01-Spine1 | Ethernet5/1 | 192.168.11.16/31 |
| OTI-DC01-Leaf5A | Ethernet56/1 | 192.168.11.19/31 | OTI-DC01-Spine2 | Ethernet5/1 | 192.168.11.18/31 |
| OTI-DC01-Leaf5B | Ethernet55/1 | 192.168.11.21/31 | OTI-DC01-Spine1 | Ethernet6/1 | 192.168.11.20/31 |
| OTI-DC01-Leaf5B | Ethernet56/1 | 192.168.11.23/31 | OTI-DC01-Spine2 | Ethernet6/1 | 192.168.11.22/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.245.217.0/27 | 32 | 8 | 25.0 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC01_Pod1 | OTI-DC01-Leaf1 | 10.245.217.3/32 |
| DC01_Pod1 | OTI-DC01-Leaf2 | 10.245.217.4/32 |
| DC01_Pod1 | OTI-DC01-Leaf3 | 10.245.217.5/32 |
| DC01_Pod1 | OTI-DC01-Leaf4 | 10.245.217.6/32 |
| DC01_Pod1 | OTI-DC01-Leaf5A | 10.245.217.7/32 |
| DC01_Pod1 | OTI-DC01-Leaf5B | 10.245.217.8/32 |
| DC01_Pod1 | OTI-DC01-Spine1 | 10.245.217.1/32 |
| DC01_Pod1 | OTI-DC01-Spine2 | 10.245.217.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 10.245.217.32/27 | 32 | 6 | 18.75 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC01_Pod1 | OTI-DC01-Leaf1 | 10.245.217.35/32 |
| DC01_Pod1 | OTI-DC01-Leaf2 | 10.245.217.36/32 |
| DC01_Pod1 | OTI-DC01-Leaf3 | 10.245.217.37/32 |
| DC01_Pod1 | OTI-DC01-Leaf4 | 10.245.217.38/32 |
| DC01_Pod1 | OTI-DC01-Leaf5A | 10.245.217.39/32 |
| DC01_Pod1 | OTI-DC01-Leaf5B | 10.245.217.39/32 |

## Connected Endpoints

### Connected Endpoint Keys

| Key | Type | Description |
| --- | ---- | ----------- |
| servers | server | Server |

### Servers

| Name | Port | Fabric Device | Fabric Port | Description | Shutdown | Mode | Access VLAN | Trunk Allowed VLANs | Profile |
| ---- | ---- | ------------- | ------------| ----------- | -------- | ---- | ----------- | ------------------- | ------- |
| DC01-0601-ESX01 | Onboard_NIC_1 | OTI-DC01-Leaf1 | Ethernet1 | SERVER_DC01-0601-ESX01_Onboard_NIC_1 | False | trunk | - | - | Access |
| DC01-0601-ESX01 | Onboard_NIC_2 | OTI-DC01-Leaf1 | Ethernet25 | SERVER_DC01-0601-ESX01_Onboard_NIC_2 | False | trunk | - | - | Access |
| DC01-0601-ESX01 | PCI_slot_1_Port_1 | OTI-DC01-Leaf2 | Ethernet1 | SERVER_DC01-0601-ESX01_PCI_slot_1_Port_1 | False | trunk | - | - | Access |
| DC01-0601-ESX01 | PCI_slot_2_Port_2 | OTI-DC01-Leaf2 | Ethernet25 | SERVER_DC01-0601-ESX01_PCI_slot_2_Port_2 | False | trunk | - | - | Access |
| DC01-0601-ESX01 | PCI_slot_1_Port_2 | OTI-DC01-Leaf5A | Ethernet1 | SERVER_DC01-0601-ESX01_PCI_slot_1_Port_2 | False | trunk | - | 2821, 2822, 2833, 2834 | Access |
| DC01-0601-ESX01 | PCI_slot_2_Port_1 | OTI-DC01-Leaf5B | Ethernet1 | SERVER_DC01-0601-ESX01_PCI_slot_2_Port_1 | False | trunk | - | 2821, 2822, 2833, 2834 | Access |
| DC01-0601-ESX03 | Onboard_NIC_1 | OTI-DC01-Leaf1 | Ethernet11 | SERVER_DC01-0601-ESX03_Onboard_NIC_1 | False | trunk | - | - | Access |
| DC01-0601-ESX03 | PCI_slot_1_Port_1 | OTI-DC01-Leaf2 | Ethernet11 | SERVER_DC01-0601-ESX03_PCI_slot_1_Port_1 | False | trunk | - | - | Access |
| DC01-0601-ESX03 | Onboard_NIC_2 | OTI-DC01-Leaf3 | Ethernet1 | SERVER_DC01-0601-ESX03_Onboard_NIC_2 | False | trunk | - | - | Access |
| DC01-0601-ESX03 | PCI_slot_2_Port_2 | OTI-DC01-Leaf4 | Ethernet1 | SERVER_DC01-0601-ESX03_PCI_slot_2_Port_2 | False | trunk | - | - | Access |
| DC01-0601-ESX03 | PCI_slot_1_Port_2 | OTI-DC01-Leaf5A | Ethernet3 | SERVER_DC01-0601-ESX03_PCI_slot_1_Port_2 | False | access | 55 | - | Access |
| DC01-0601-ESX03 | PCI_slot_2_Port_1 | OTI-DC01-Leaf5B | Ethernet3 | SERVER_DC01-0601-ESX03_PCI_slot_2_Port_1 | False | access | 55 | - | Access |
| DC01-0601-ESX04 | Onboard_NIC_1 | OTI-DC01-Leaf1 | Ethernet12 | SERVER_DC01-0601-ESX04_Onboard_NIC_1 | False | trunk | - | - | Access |
| DC01-0601-ESX04 | PCI_slot_1_Port_1 | OTI-DC01-Leaf2 | Ethernet12 | SERVER_DC01-0601-ESX04_PCI_slot_1_Port_1 | False | trunk | - | - | Access |
| DC01-0601-ESX04 | Onboard_NIC_2 | OTI-DC01-Leaf3 | Ethernet2 | SERVER_DC01-0601-ESX04_Onboard_NIC_2 | False | trunk | - | - | Access |
| DC01-0601-ESX04 | PCI_slot_2_Port_2 | OTI-DC01-Leaf4 | Ethernet2 | SERVER_DC01-0601-ESX04_PCI_slot_2_Port_2 | False | trunk | - | - | Access |
| DC01-0601-ESX04 | PCI_slot_1_Port_2 | OTI-DC01-Leaf5A | Ethernet4 | SERVER_DC01-0601-ESX04_PCI_slot_1_Port_2 | False | access | 55 | - | Access |
| DC01-0601-ESX04 | PCI_slot_2_Port_1 | OTI-DC01-Leaf5B | Ethernet4 | SERVER_DC01-0601-ESX04_PCI_slot_2_Port_1 | False | access | 55 | - | Access |
| DC01-0601-ESX05 | Onboard_NIC_1 | OTI-DC01-Leaf1 | Ethernet30 | SERVER_DC01-0601-ESX05_Onboard_NIC_1 | False | trunk | - | - | Access |
| DC01-0601-ESX05 | PCI_slot_1_Port_1 | OTI-DC01-Leaf2 | Ethernet30 | SERVER_DC01-0601-ESX05_PCI_slot_1_Port_1 | False | trunk | - | - | Access |
| DC01-0601-ESX05 | Onboard_NIC_2 | OTI-DC01-Leaf3 | Ethernet3 | SERVER_DC01-0601-ESX05_Onboard_NIC_2 | False | trunk | - | - | Access |
| DC01-0601-ESX05 | PCI_slot_2_Port_2 | OTI-DC01-Leaf4 | Ethernet3 | SERVER_DC01-0601-ESX05_PCI_slot_2_Port_2 | False | trunk | - | - | Access |
| DC01-0601-ESX05 | PCI_slot_1_Port_2 | OTI-DC01-Leaf5A | Ethernet5 | SERVER_DC01-0601-ESX05_PCI_slot_1_Port_2 | False | trunk | - | 2821, 2822, 2833, 2834 | Access |
| DC01-0601-ESX05 | PCI_slot_2_Port_1 | OTI-DC01-Leaf5B | Ethernet5 | SERVER_DC01-0601-ESX05_PCI_slot_2_Port_1 | False | trunk | - | 2821, 2822, 2833, 2834 | Access |
| DC01-0601-ESX06 | Onboard_NIC_1 | OTI-DC01-Leaf1 | Ethernet31 | SERVER_DC01-0601-ESX06_Onboard_NIC_1 | False | trunk | - | - | Access |
| DC01-0601-ESX06 | PCI_slot_1_Port_1 | OTI-DC01-Leaf2 | Ethernet31 | SERVER_DC01-0601-ESX06_PCI_slot_1_Port_1 | False | trunk | - | - | Access |
| DC01-0601-ESX06 | Onboard_NIC_2 | OTI-DC01-Leaf3 | Ethernet4 | SERVER_DC01-0601-ESX06_Onboard_NIC_2 | False | trunk | - | - | Access |
| DC01-0601-ESX06 | PCI_slot_2_Port_2 | OTI-DC01-Leaf4 | Ethernet4 | SERVER_DC01-0601-ESX06_PCI_slot_2_Port_2 | False | trunk | - | - | Access |
| DC01-0601-ESX06 | PCI_slot_1_Port_2 | OTI-DC01-Leaf5A | Ethernet6 | SERVER_DC01-0601-ESX06_PCI_slot_1_Port_2 | False | access | 821 | - | Access |
| DC01-0601-ESX06 | PCI_slot_2_Port_1 | OTI-DC01-Leaf5B | Ethernet6 | SERVER_DC01-0601-ESX06_PCI_slot_2_Port_1 | False | access | 821 | - | Access |
| DC01-0601-SRVA | Port_0 | OTI-DC01-Leaf3 | Ethernet11 | SERVER_DC01-0601-SRVA_Port_0 | False | trunk | - | - | Access |
| DC01-0601-SRVA | Port_1 | OTI-DC01-Leaf4 | Ethernet11 | SERVER_DC01-0601-SRVA_Port_1 | False | trunk | - | - | Access |
| DC01-0601-SRVB | Port_0 | OTI-DC01-Leaf3 | Ethernet12 | SERVER_DC01-0601-SRVB_Port_0 | False | trunk | - | - | Access |
| DC01-0601-SRVB | Port_1 | OTI-DC01-Leaf4 | Ethernet12 | SERVER_DC01-0601-SRVB_Port_1 | False | trunk | - | - | Access |
| DC01-0601-SRVC | Port_0 | OTI-DC01-Leaf3 | Ethernet13 | SERVER_DC01-0601-SRVC_Port_0 | False | trunk | - | - | Access |
| DC01-0601-SRVC | Port_1 | OTI-DC01-Leaf4 | Ethernet13 | SERVER_DC01-0601-SRVC_Port_1 | False | trunk | - | - | Access |
| DC01-0601-SRVD | Port_0 | OTI-DC01-Leaf3 | Ethernet14 | SERVER_DC01-0601-SRVD_Port_0 | False | trunk | - | - | Access |
| DC01-0601-SRVD | Port_1 | OTI-DC01-Leaf4 | Ethernet14 | SERVER_DC01-0601-SRVD_Port_1 | False | trunk | - | - | Access |
| DC01-0601-SRVD | Port_2 | OTI-DC01-Leaf5A | Ethernet25 | SERVER_DC01-0601-SRVD_Port_2 | False | trunk | - | 3911, 2500 | Access |
| DC01-0601-SRVD | Port_3 | OTI-DC01-Leaf5B | Ethernet25 | SERVER_DC01-0601-SRVD_Port_3 | False | trunk | - | 3911, 2500 | Access |

### Port Profiles

| Profile Name | Parent Profile |
| ------------ | -------------- |
| Access | - |
