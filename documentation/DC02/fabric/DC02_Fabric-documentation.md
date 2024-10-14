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

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| Pod1 | l3leaf | OTI-DC02-Leaf1 | 192.168.255.23/24 | 7050SX3-48YC8 | Provisioned | SN-OTI-DC02-Leaf1 |
| Pod1 | l3leaf | OTI-DC02-Leaf2 | 192.168.255.24/24 | 7050SX3-48YC8 | Provisioned | SN-OTI-DC02-Leaf2 |
| Pod1 | l3leaf | OTI-DC02-Leaf3 | 192.168.255.25/24 | 7050SX3-48YC8 | Provisioned | SN-OTI-DC02-Leaf3 |
| Pod1 | l3leaf | OTI-DC02-Leaf4 | 192.168.255.26/24 | 7050SX3-48YC8 | Provisioned | SN-OTI-DC02-Leaf4 |
| Pod1 | l3leaf | OTI-DC02-Leaf5A | 192.168.255.27/24 | 7050SX3-48YC8 | Provisioned | SN-OTI-DC02-Leaf5A |
| Pod1 | l3leaf | OTI-DC02-Leaf5B | 192.168.255.28/24 | 7050SX3-48YC8 | Provisioned | SN-OTI-DC02-Leaf5B |
| Pod1 | spine | OTI-DC02-Spine1 | 192.168.255.21/24 | 7050CX3 | Provisioned | SN-OTI-DC02-Spine1 |
| Pod1 | spine | OTI-DC02-Spine2 | 192.168.255.22/24 | 7050CX3 | Provisioned | SN-OTI-DC02-Spine2 |

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
| Pod1 | OTI-DC02-Leaf1 | 10.245.218.3/32 |
| Pod1 | OTI-DC02-Leaf2 | 10.245.218.4/32 |
| Pod1 | OTI-DC02-Leaf3 | 10.245.218.5/32 |
| Pod1 | OTI-DC02-Leaf4 | 10.245.218.6/32 |
| Pod1 | OTI-DC02-Leaf5A | 10.245.218.7/32 |
| Pod1 | OTI-DC02-Leaf5B | 10.245.218.8/32 |
| Pod1 | OTI-DC02-Spine1 | 10.245.218.1/32 |
| Pod1 | OTI-DC02-Spine2 | 10.245.218.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.245.218.32/27 | 32 | 6 | 18.75 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| Pod1 | OTI-DC02-Leaf1 | 10.245.218.35/32 |
| Pod1 | OTI-DC02-Leaf2 | 10.245.218.36/32 |
| Pod1 | OTI-DC02-Leaf3 | 10.245.218.37/32 |
| Pod1 | OTI-DC02-Leaf4 | 10.245.218.38/32 |
| Pod1 | OTI-DC02-Leaf5A | 10.245.218.39/32 |
| Pod1 | OTI-DC02-Leaf5B | 10.245.218.39/32 |
