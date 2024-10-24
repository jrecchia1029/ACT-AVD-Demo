# DC01_OOB

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
| Pod1 | leaf | OTI-DC01-OBM1 | 192.168.255.19/24 | 7050SX3-48YC8 | Provisioned | SN-OTI-DC01-OBM1 |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |

## Connected Endpoints

### Connected Endpoint Keys

| Key | Type | Description |
| --- | ---- | ----------- |
| servers | server | Server |

### Servers

| Name | Port | Fabric Device | Fabric Port | Description | Shutdown | Mode | Access VLAN | Trunk Allowed VLANs | Profile |
| ---- | ---- | ------------- | ------------| ----------- | -------- | ---- | ----------- | ------------------- | ------- |
| DC01-0601-ESX01 | idrac | OTI-DC01-OBM1 | Ethernet1 | SERVER_DC01-0601-ESX01_idrac | False | access | 3545 | - | Access |
| DC01-0601-ESX03 | idrac | OTI-DC01-OBM1 | Ethernet3 | SERVER_DC01-0601-ESX03_idrac | False | access | 3545 | - | Access |
| DC01-0601-ESX04 | idrac | OTI-DC01-OBM1 | Ethernet4 | SERVER_DC01-0601-ESX04_idrac | False | access | 3545 | - | Access |
| DC01-0601-ESX05 | idrac | OTI-DC01-OBM1 | Ethernet5 | SERVER_DC01-0601-ESX05_idrac | False | access | 3545 | - | Access |
| DC01-0601-ESX06 | idrac | OTI-DC01-OBM1 | Ethernet6 | SERVER_DC01-0601-ESX06_idrac | False | access | 3545 | - | Access |
| DC01-0601-SRVA | iLo | OTI-DC01-OBM1 | Ethernet7 | SERVER_DC01-0601-SRVA_iLo | False | access | 3545 | - | Access |
| DC01-0601-SRVB | iLo | OTI-DC01-OBM1 | Ethernet8 | SERVER_DC01-0601-SRVB_iLo | False | access | 3545 | - | Access |
| DC01-0601-SRVC | iLo | OTI-DC01-OBM1 | Ethernet9 | SERVER_DC01-0601-SRVC_iLo | False | access | 3545 | - | Access |
| DC01-0601-SRVD | iLo | OTI-DC01-OBM1 | Ethernet10 | SERVER_DC01-0601-SRVD_iLo | False | access | 3545 | - | Access |

### Port Profiles

| Profile Name | Parent Profile |
| ------------ | -------------- |
| Access | - |
