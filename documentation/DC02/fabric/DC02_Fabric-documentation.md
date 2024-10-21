# DC02_Fabric

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
| DC02_Pod1 | l3leaf | OTI-DC02-Leaf1 | 192.168.255.23/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Leaf1 |
| DC02_Pod1 | l3leaf | OTI-DC02-Leaf2 | 192.168.255.24/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Leaf2 |
| DC02_Pod1 | l3leaf | OTI-DC02-Leaf3 | 192.168.255.25/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Leaf3 |
| DC02_Pod1 | l3leaf | OTI-DC02-Leaf4 | 192.168.255.26/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Leaf4 |
| DC02_Pod1 | l3leaf | OTI-DC02-Leaf5A | 192.168.255.27/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Leaf5A |
| DC02_Pod1 | l3leaf | OTI-DC02-Leaf5B | 192.168.255.28/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Leaf5B |
| DC02_Pod1 | spine | OTI-DC02-Spine1 | 192.168.255.21/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Spine1 |
| DC02_Pod1 | spine | OTI-DC02-Spine2 | 192.168.255.22/24 | vEOS-lab | Provisioned | SN-OTI-DC02-Spine2 |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | OTI-DC02-Leaf1 | Ethernet55/1 | spine | OTI-DC02-Spine1 | Ethernet1/1 |
| l3leaf | OTI-DC02-Leaf1 | Ethernet56/1 | spine | OTI-DC02-Spine2 | Ethernet1/1 |
| l3leaf | OTI-DC02-Leaf2 | Ethernet55/1 | spine | OTI-DC02-Spine1 | Ethernet2/1 |
| l3leaf | OTI-DC02-Leaf2 | Ethernet56/1 | spine | OTI-DC02-Spine2 | Ethernet2/1 |
| l3leaf | OTI-DC02-Leaf3 | Ethernet55/1 | spine | OTI-DC02-Spine1 | Ethernet3/1 |
| l3leaf | OTI-DC02-Leaf3 | Ethernet56/1 | spine | OTI-DC02-Spine2 | Ethernet3/1 |
| l3leaf | OTI-DC02-Leaf4 | Ethernet55/1 | spine | OTI-DC02-Spine1 | Ethernet4/1 |
| l3leaf | OTI-DC02-Leaf4 | Ethernet56/1 | spine | OTI-DC02-Spine2 | Ethernet4/1 |
| l3leaf | OTI-DC02-Leaf5A | Ethernet53/1 | mlag_peer | OTI-DC02-Leaf5B | Ethernet53/1 |
| l3leaf | OTI-DC02-Leaf5A | Ethernet54/1 | mlag_peer | OTI-DC02-Leaf5B | Ethernet54/1 |
| l3leaf | OTI-DC02-Leaf5A | Ethernet55/1 | spine | OTI-DC02-Spine1 | Ethernet5/1 |
| l3leaf | OTI-DC02-Leaf5A | Ethernet56/1 | spine | OTI-DC02-Spine2 | Ethernet5/1 |
| l3leaf | OTI-DC02-Leaf5B | Ethernet55/1 | spine | OTI-DC02-Spine1 | Ethernet6/1 |
| l3leaf | OTI-DC02-Leaf5B | Ethernet56/1 | spine | OTI-DC02-Spine2 | Ethernet6/1 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.12.0/26 | 64 | 24 | 37.5 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| OTI-DC02-Leaf1 | Ethernet55/1 | 192.168.12.1/31 | OTI-DC02-Spine1 | Ethernet1/1 | 192.168.12.0/31 |
| OTI-DC02-Leaf1 | Ethernet56/1 | 192.168.12.3/31 | OTI-DC02-Spine2 | Ethernet1/1 | 192.168.12.2/31 |
| OTI-DC02-Leaf2 | Ethernet55/1 | 192.168.12.5/31 | OTI-DC02-Spine1 | Ethernet2/1 | 192.168.12.4/31 |
| OTI-DC02-Leaf2 | Ethernet56/1 | 192.168.12.7/31 | OTI-DC02-Spine2 | Ethernet2/1 | 192.168.12.6/31 |
| OTI-DC02-Leaf3 | Ethernet55/1 | 192.168.12.9/31 | OTI-DC02-Spine1 | Ethernet3/1 | 192.168.12.8/31 |
| OTI-DC02-Leaf3 | Ethernet56/1 | 192.168.12.11/31 | OTI-DC02-Spine2 | Ethernet3/1 | 192.168.12.10/31 |
| OTI-DC02-Leaf4 | Ethernet55/1 | 192.168.12.13/31 | OTI-DC02-Spine1 | Ethernet4/1 | 192.168.12.12/31 |
| OTI-DC02-Leaf4 | Ethernet56/1 | 192.168.12.15/31 | OTI-DC02-Spine2 | Ethernet4/1 | 192.168.12.14/31 |
| OTI-DC02-Leaf5A | Ethernet55/1 | 192.168.12.17/31 | OTI-DC02-Spine1 | Ethernet5/1 | 192.168.12.16/31 |
| OTI-DC02-Leaf5A | Ethernet56/1 | 192.168.12.19/31 | OTI-DC02-Spine2 | Ethernet5/1 | 192.168.12.18/31 |
| OTI-DC02-Leaf5B | Ethernet55/1 | 192.168.12.21/31 | OTI-DC02-Spine1 | Ethernet6/1 | 192.168.12.20/31 |
| OTI-DC02-Leaf5B | Ethernet56/1 | 192.168.12.23/31 | OTI-DC02-Spine2 | Ethernet6/1 | 192.168.12.22/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.245.218.0/27 | 32 | 8 | 25.0 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC02_Pod1 | OTI-DC02-Leaf1 | 10.245.218.3/32 |
| DC02_Pod1 | OTI-DC02-Leaf2 | 10.245.218.4/32 |
| DC02_Pod1 | OTI-DC02-Leaf3 | 10.245.218.5/32 |
| DC02_Pod1 | OTI-DC02-Leaf4 | 10.245.218.6/32 |
| DC02_Pod1 | OTI-DC02-Leaf5A | 10.245.218.7/32 |
| DC02_Pod1 | OTI-DC02-Leaf5B | 10.245.218.8/32 |
| DC02_Pod1 | OTI-DC02-Spine1 | 10.245.218.1/32 |
| DC02_Pod1 | OTI-DC02-Spine2 | 10.245.218.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.245.218.32/27 | 32 | 6 | 18.75 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC02_Pod1 | OTI-DC02-Leaf1 | 10.245.218.35/32 |
| DC02_Pod1 | OTI-DC02-Leaf2 | 10.245.218.36/32 |
| DC02_Pod1 | OTI-DC02-Leaf3 | 10.245.218.37/32 |
| DC02_Pod1 | OTI-DC02-Leaf4 | 10.245.218.38/32 |
| DC02_Pod1 | OTI-DC02-Leaf5A | 10.245.218.39/32 |
| DC02_Pod1 | OTI-DC02-Leaf5B | 10.245.218.39/32 |

## Connected Endpoints

### Connected Endpoint Keys

| Key | Type | Description |
| --- | ---- | ----------- |
| access_points | access_point | Access Point |
| cameras | camera | Camera |
| cpes | cpe | CPE |
| firewalls | firewall | Firewall |
| generic_devices | generic_device | Generic Device |
| load_balancers | load_balancer | Load Balancer |
| phones | phone | Phone |
| printers | printer | Printer |
| routers | router | Router |
| servers | server | Server |
| storage_arrays | storage_array | Storage Array |
| workstations | workstation | Workstation |

### Servers

| Name | Port | Fabric Device | Fabric Port | Description | Shutdown | Type | Mode | VLANs | Profile |
| ---- | ---- | ------------- | ------------| ----------- | -------- | ---- | ---- | ----- | ------- |
| DC02-0901-ESX01 | Onboard_NIC_1 | OTI-DC02-Leaf1 | Ethernet1 | DC02-0901-ESX01_Onboard_NIC_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX01 | Onboard_NIC_2 | OTI-DC02-Leaf1 | Ethernet48 | DC02-0901-ESX01_Onboard_NIC_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX01 | PCI_slot_1_Port_1 | OTI-DC02-Leaf2 | Ethernet1 | DC02-0901-ESX01_PCI_slot_1_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX01 | PCI_slot_2_Port_2 | OTI-DC02-Leaf2 | Ethernet48 | DC02-0901-ESX01_PCI_slot_2_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX01 | PCI_slot_1_Port_2 | OTI-DC02-Leaf3 | Ethernet1 | DC02-0901-ESX01_PCI_slot_1_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX01 | PCI_slot_2_Port_1 | OTI-DC02-Leaf4 | Ethernet1 | DC02-0901-ESX01_PCI_slot_2_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX02 | Onboard_NIC_1 | OTI-DC02-Leaf1 | Ethernet2 | DC02-0901-ESX02_Onboard_NIC_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX02 | Onboard_NIC_2 | OTI-DC02-Leaf1 | Ethernet47 | DC02-0901-ESX02_Onboard_NIC_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX02 | PCI_slot_1_Port_1 | OTI-DC02-Leaf2 | Ethernet2 | DC02-0901-ESX02_PCI_slot_1_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX02 | PCI_slot_2_Port_2 | OTI-DC02-Leaf2 | Ethernet47 | DC02-0901-ESX02_PCI_slot_2_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX02 | PCI_slot_1_Port_2 | OTI-DC02-Leaf3 | Ethernet2 | DC02-0901-ESX02_PCI_slot_1_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX02 | PCI_slot_2_Port_1 | OTI-DC02-Leaf4 | Ethernet2 | DC02-0901-ESX02_PCI_slot_2_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX03 | Onboard_NIC_1 | OTI-DC02-Leaf1 | Ethernet3 | DC02-0901-ESX03_Onboard_NIC_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX03 | PCI_slot_1_Port_1 | OTI-DC02-Leaf2 | Ethernet3 | DC02-0901-ESX03_PCI_slot_1_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX03 | Onboard_NIC_2 | OTI-DC02-Leaf3 | Ethernet3 | DC02-0901-ESX03_Onboard_NIC_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX03 | PCI_slot_1_Port_2 | OTI-DC02-Leaf3 | Ethernet49/1 | DC02-0901-ESX03_PCI_slot_1_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX03 | PCI_slot_2_Port_2 | OTI-DC02-Leaf4 | Ethernet3 | DC02-0901-ESX03_PCI_slot_2_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX03 | PCI_slot_2_Port_1 | OTI-DC02-Leaf4 | Ethernet49/1 | DC02-0901-ESX03_PCI_slot_2_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX04 | Onboard_NIC_1 | OTI-DC02-Leaf1 | Ethernet4 | DC02-0901-ESX04_Onboard_NIC_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX04 | PCI_slot_1_Port_1 | OTI-DC02-Leaf2 | Ethernet4 | DC02-0901-ESX04_PCI_slot_1_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX04 | PCI_slot_1_Port_2 | OTI-DC02-Leaf3 | Ethernet50/1 | DC02-0901-ESX04_PCI_slot_1_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX04 | PCI_slot_2_Port_1 | OTI-DC02-Leaf4 | Ethernet50/1 | DC02-0901-ESX04_PCI_slot_2_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX04 | Onboard_NIC_2 | OTI-DC02-Leaf5A | Ethernet1 | DC02-0901-ESX04_Onboard_NIC_2 | False | switched | trunk | 899, 999 | Access |
| DC02-0901-ESX04 | PCI_slot_2_Port_2 | OTI-DC02-Leaf5B | Ethernet1 | DC02-0901-ESX04_PCI_slot_2_Port_2 | False | switched | trunk | 899, 999 | Access |
| DC02-0901-ESX05 | Onboard_NIC_1 | OTI-DC02-Leaf1 | Ethernet5 | DC02-0901-ESX05_Onboard_NIC_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX05 | PCI_slot_1_Port_1 | OTI-DC02-Leaf2 | Ethernet5 | DC02-0901-ESX05_PCI_slot_1_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX05 | Onboard_NIC_2 | OTI-DC02-Leaf3 | Ethernet4 | DC02-0901-ESX05_Onboard_NIC_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX05 | PCI_slot_2_Port_2 | OTI-DC02-Leaf4 | Ethernet4 | DC02-0901-ESX05_PCI_slot_2_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-ESX05 | PCI_slot_1_Port_2 | OTI-DC02-Leaf5A | Ethernet49/1 | DC02-0901-ESX05_PCI_slot_1_Port_2 | False | switched | trunk | 1100, 1101, 1102 | Access |
| DC02-0901-ESX05 | PCI_slot_2_Port_1 | OTI-DC02-Leaf5B | Ethernet49/1 | DC02-0901-ESX05_PCI_slot_2_Port_1 | False | switched | trunk | 1100, 1101, 1102 | Access |
| DC02-0901-ESX06 | Onboard_NIC_1 | OTI-DC02-Leaf1 | Ethernet6 | DC02-0901-ESX06_Onboard_NIC_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX06 | PCI_slot_1_Port_1 | OTI-DC02-Leaf2 | Ethernet6 | DC02-0901-ESX06_PCI_slot_1_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-ESX06 | Onboard_NIC_2 | OTI-DC02-Leaf5A | Ethernet2 | DC02-0901-ESX06_Onboard_NIC_2 | False | switched | trunk | 899, 999 | Access |
| DC02-0901-ESX06 | PCI_slot_1_Port_2 | OTI-DC02-Leaf5A | Ethernet50/1 | DC02-0901-ESX06_PCI_slot_1_Port_2 | False | switched | trunk | 887, 888 | Access |
| DC02-0901-ESX06 | PCI_slot_2_Port_2 | OTI-DC02-Leaf5B | Ethernet2 | DC02-0901-ESX06_PCI_slot_2_Port_2 | False | switched | trunk | 899, 999 | Access |
| DC02-0901-ESX06 | PCI_slot_2_Port_1 | OTI-DC02-Leaf5B | Ethernet50/1 | DC02-0901-ESX06_PCI_slot_2_Port_1 | False | switched | trunk | 887, 888 | Access |
| DC02-0901-SRVA | Port_0 | OTI-DC02-Leaf1 | Ethernet25 | DC02-0901-SRVA_Port_0 | False | switched | trunk | - | Access |
| DC02-0901-SRVA | Port_1 | OTI-DC02-Leaf2 | Ethernet25 | DC02-0901-SRVA_Port_1 | False | switched | trunk | - | Access |
| DC02-0901-SRVA | Port_2 | OTI-DC02-Leaf3 | Ethernet5 | DC02-0901-SRVA_Port_2 | False | switched | trunk | - | Access |
| DC02-0901-SRVA | Port_3 | OTI-DC02-Leaf4 | Ethernet5 | DC02-0901-SRVA_Port_3 | False | switched | trunk | - | Access |
| DC02-0901-SRVB | Port_0 | OTI-DC02-Leaf3 | Ethernet25 | DC02-0901-SRVB_Port_0 | False | switched | access | - | Access |
| DC02-0901-SRVB | Port_1 | OTI-DC02-Leaf4 | Ethernet25 | DC02-0901-SRVB_Port_1 | False | switched | access | - | Access |
| DC02-0901-SRVC | Port_0 | OTI-DC02-Leaf3 | Ethernet26 | DC02-0901-SRVC_Port_0 | False | switched | access | - | Access |
| DC02-0901-SRVC | Port_1 | OTI-DC02-Leaf4 | Ethernet26 | DC02-0901-SRVC_Port_1 | False | switched | access | - | Access |

### Port Profiles

| Profile Name | Parent Profile |
| ------------ | -------------- |
| Access | - |
