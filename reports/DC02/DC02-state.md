# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |
| ----------- | ------------------ | ------------------ | ------------------- |
| 706 | 662 | 8 | 36 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| OTI-DC02-Leaf1 | 110 | 105 | 1 | 4 | Interfaces | Hardware |
| OTI-DC02-Leaf2 | 110 | 105 | 1 | 4 | Interfaces | Hardware |
| OTI-DC02-Leaf3 | 104 | 97 | 3 | 4 | Interfaces | Hardware |
| OTI-DC02-Leaf4 | 104 | 97 | 3 | 4 | Interfaces | Hardware |
| OTI-DC02-Leaf5A | 95 | 91 | 0 | 4 | - | Hardware |
| OTI-DC02-Leaf5B | 95 | 91 | 0 | 4 | - | Hardware |
| OTI-DC02-OBM1 | 14 | 10 | 0 | 4 | - | Hardware |
| OTI-DC02-Spine1 | 37 | 33 | 0 | 4 | - | Hardware |
| OTI-DC02-Spine2 | 37 | 33 | 0 | 4 | - | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 60 | 60 | 0 | 0 |
| Connectivity | 152 | 152 | 0 | 0 |
| Hardware | 36 | 0 | 0 | 36 |
| Interfaces | 283 | 275 | 8 | 0 |
| MLAG | 2 | 2 | 0 | 0 |
| Routing | 164 | 164 | 0 | 0 |
| System | 9 | 9 | 0 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 46 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 156 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 261 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 262 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 265 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |
| 365 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 366 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 369 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |

## All Test Results

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 1 | OTI-DC02-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 2 | OTI-DC02-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 3 | OTI-DC02-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.0) | PASS | - |
| 4 | OTI-DC02-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.2) | PASS | - |
| 5 | OTI-DC02-Leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet1/1 | PASS | - |
| 6 | OTI-DC02-Leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet1/1 | PASS | - |
| 7 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 8 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 9 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 10 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 11 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 12 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 13 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 14 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 15 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 16 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 17 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 18 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 19 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 20 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 21 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 22 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.3) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 23 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.1) - Destination: OTI-DC02-Spine1 Ethernet1/1 (IP: 192.168.12.0) | PASS | - |
| 24 | OTI-DC02-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.3) - Destination: OTI-DC02-Spine2 Ethernet1/1 (IP: 192.168.12.2) | PASS | - |
| 25 | OTI-DC02-Leaf1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 26 | OTI-DC02-Leaf1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 27 | OTI-DC02-Leaf1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 28 | OTI-DC02-Leaf1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 29 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC02-0901-ESX01_Onboard_NIC_1 = 'up' | PASS | - |
| 30 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC02-0901-ESX02_Onboard_NIC_1 = 'up' | PASS | - |
| 31 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC02-0901-SRVA_Port_0 = 'up' | PASS | - |
| 32 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC02-0901-ESX03_Onboard_NIC_1 = 'up' | PASS | - |
| 33 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC02-0901-ESX04_Onboard_NIC_1 = 'up' | PASS | - |
| 34 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet47 - DC02-0901-ESX02_Onboard_NIC_2 = 'up' | PASS | - |
| 35 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet48 - DC02-0901-ESX01_Onboard_NIC_2 = 'up' | PASS | - |
| 36 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC02-0901-ESX05_Onboard_NIC_1 = 'up' | PASS | - |
| 37 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet1/1 = 'up' | PASS | - |
| 38 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet1/1 = 'up' | PASS | - |
| 39 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - DC02-0901-ESX06_Onboard_NIC_1 = 'up' | PASS | - |
| 40 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 41 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 42 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 43 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 44 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC02-0901-ESX01 = 'up' | PASS | - |
| 45 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC02-0901-ESX02 = 'up' | PASS | - |
| 46 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 47 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - DC02-0901-ESX03 = 'up' | PASS | - |
| 48 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC02-0901-ESX04 = 'up' | PASS | - |
| 49 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel47 - DC02-0901-ESX02 = 'up' | PASS | - |
| 50 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel48 - DC02-0901-ESX01 = 'up' | PASS | - |
| 51 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC02-0901-ESX05 = 'up' | PASS | - |
| 52 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel6 - DC02-0901-ESX06 = 'up' | PASS | - |
| 53 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 54 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 55 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 56 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 57 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 58 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 59 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 60 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 61 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 62 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 63 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 64 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 65 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 66 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 67 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 68 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 69 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 70 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 71 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 72 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 73 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 74 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 75 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 76 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 77 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 78 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 79 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 80 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 81 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 82 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 83 | OTI-DC02-Leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 84 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 85 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 86 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 87 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 88 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 89 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 90 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 91 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 92 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 93 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 94 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 95 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 96 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 97 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 98 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 99 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 100 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 101 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 102 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 103 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 104 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 105 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 106 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 107 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 108 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 109 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 110 | OTI-DC02-Leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 111 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 112 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 113 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.4) | PASS | - |
| 114 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.6) | PASS | - |
| 115 | OTI-DC02-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet2/1 | PASS | - |
| 116 | OTI-DC02-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet2/1 | PASS | - |
| 117 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 118 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 119 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 120 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 121 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 122 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 123 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 124 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 125 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 126 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 127 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 128 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 129 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 130 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 131 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 132 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 133 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.5) - Destination: OTI-DC02-Spine1 Ethernet2/1 (IP: 192.168.12.4) | PASS | - |
| 134 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.7) - Destination: OTI-DC02-Spine2 Ethernet2/1 (IP: 192.168.12.6) | PASS | - |
| 135 | OTI-DC02-Leaf2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 136 | OTI-DC02-Leaf2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 137 | OTI-DC02-Leaf2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 138 | OTI-DC02-Leaf2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 139 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC02-0901-ESX01_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 140 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC02-0901-ESX02_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 141 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC02-0901-SRVA_Port_1 = 'up' | PASS | - |
| 142 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC02-0901-ESX03_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 143 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC02-0901-ESX04_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 144 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet47 - DC02-0901-ESX02_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 145 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet48 - DC02-0901-ESX01_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 146 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC02-0901-ESX05_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 147 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet2/1 = 'up' | PASS | - |
| 148 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet2/1 = 'up' | PASS | - |
| 149 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - DC02-0901-ESX06_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 150 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 151 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 152 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 153 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 154 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC02-0901-ESX01 = 'up' | PASS | - |
| 155 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC02-0901-ESX02 = 'up' | PASS | - |
| 156 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 157 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - DC02-0901-ESX03 = 'up' | PASS | - |
| 158 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC02-0901-ESX04 = 'up' | PASS | - |
| 159 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel47 - DC02-0901-ESX02 = 'up' | PASS | - |
| 160 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel48 - DC02-0901-ESX01 = 'up' | PASS | - |
| 161 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC02-0901-ESX05 = 'up' | PASS | - |
| 162 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel6 - DC02-0901-ESX06 = 'up' | PASS | - |
| 163 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 164 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 165 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 166 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 167 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 168 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 169 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 170 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 171 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 172 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 173 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 174 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 175 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 176 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 177 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 178 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 179 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 180 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 181 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 182 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 183 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 184 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 185 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 186 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 187 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 188 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 189 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 190 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 191 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 192 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 193 | OTI-DC02-Leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 194 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 195 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 196 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 197 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 198 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 199 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 200 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 201 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 202 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 203 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 204 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 205 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 206 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 207 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 208 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 209 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 210 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 211 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 212 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 213 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 214 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 215 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 216 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 217 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 218 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 219 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 220 | OTI-DC02-Leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 221 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 222 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 223 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.8) | PASS | - |
| 224 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.10) | PASS | - |
| 225 | OTI-DC02-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet3/1 | PASS | - |
| 226 | OTI-DC02-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet3/1 | PASS | - |
| 227 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 228 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 229 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 230 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 231 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 232 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 233 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 234 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 235 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 236 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 237 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 238 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 239 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 240 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 241 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 242 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 243 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.9) - Destination: OTI-DC02-Spine1 Ethernet3/1 (IP: 192.168.12.8) | PASS | - |
| 244 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.11) - Destination: OTI-DC02-Spine2 Ethernet3/1 (IP: 192.168.12.10) | PASS | - |
| 245 | OTI-DC02-Leaf3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 246 | OTI-DC02-Leaf3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 247 | OTI-DC02-Leaf3 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 248 | OTI-DC02-Leaf3 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 249 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC02-0901-SRVB_Port_0 = 'up' | PASS | - |
| 250 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet26 - DC02-0901-SRVC_Port_0 = 'up' | PASS | - |
| 251 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC02-0901-ESX05_Onboard_NIC_2 = 'up' | PASS | - |
| 252 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - DC02-0901-ESX03_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 253 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC02-0901-SRVA_Port_2 = 'up' | PASS | - |
| 254 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - DC02-0901-ESX04_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 255 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet3/1 = 'up' | PASS | - |
| 256 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet3/1 = 'up' | PASS | - |
| 257 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 258 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 259 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 260 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 261 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 262 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 263 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC02-0901-ESX05 = 'up' | PASS | - |
| 264 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - DC02-0901-ESX03 = 'up' | PASS | - |
| 265 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |
| 266 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - DC02-0901-ESX04 = 'up' | PASS | - |
| 267 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 268 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 269 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 270 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 271 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 272 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 273 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 274 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 275 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 276 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 277 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 278 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 279 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 280 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 281 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 282 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 283 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 284 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 285 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 286 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 287 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 288 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 289 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 290 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 291 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 292 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 293 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 294 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 295 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 296 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 297 | OTI-DC02-Leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 298 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 299 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 300 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 301 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 302 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 303 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 304 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 305 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 306 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 307 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 308 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 309 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 310 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 311 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 312 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 313 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 314 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 315 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 316 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 317 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 318 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 319 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 320 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 321 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 322 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 323 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 324 | OTI-DC02-Leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 325 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 326 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 327 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.12) | PASS | - |
| 328 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.14) | PASS | - |
| 329 | OTI-DC02-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet4/1 | PASS | - |
| 330 | OTI-DC02-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet4/1 | PASS | - |
| 331 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 332 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 333 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 334 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 335 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 336 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 337 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 338 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 339 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 340 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 341 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 342 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 343 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 344 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 345 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 346 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 347 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.13) - Destination: OTI-DC02-Spine1 Ethernet4/1 (IP: 192.168.12.12) | PASS | - |
| 348 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.15) - Destination: OTI-DC02-Spine2 Ethernet4/1 (IP: 192.168.12.14) | PASS | - |
| 349 | OTI-DC02-Leaf4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 350 | OTI-DC02-Leaf4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 351 | OTI-DC02-Leaf4 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 352 | OTI-DC02-Leaf4 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 353 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC02-0901-SRVB_Port_1 = 'up' | PASS | - |
| 354 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet26 - DC02-0901-SRVC_Port_1 = 'up' | PASS | - |
| 355 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC02-0901-ESX05_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 356 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - DC02-0901-ESX03_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 357 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC02-0901-SRVA_Port_3 = 'up' | PASS | - |
| 358 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - DC02-0901-ESX04_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 359 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet4/1 = 'up' | PASS | - |
| 360 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet4/1 = 'up' | PASS | - |
| 361 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 362 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 363 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 364 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 365 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 366 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 367 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC02-0901-ESX05 = 'up' | PASS | - |
| 368 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - DC02-0901-ESX03 = 'up' | PASS | - |
| 369 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |
| 370 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - DC02-0901-ESX04 = 'up' | PASS | - |
| 371 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 372 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 373 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 374 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 375 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 376 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 377 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 378 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 379 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 380 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 381 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 382 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 383 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 384 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 385 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 386 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 387 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 388 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 389 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 390 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 391 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 392 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 393 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 394 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 395 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 396 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 397 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 398 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 399 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 400 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 401 | OTI-DC02-Leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 402 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 403 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 404 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 405 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 406 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 407 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 408 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 409 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 410 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 411 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 412 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 413 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 414 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 415 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 416 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 417 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 418 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 419 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 420 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 421 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 422 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 423 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 424 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 425 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 426 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 427 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 428 | OTI-DC02-Leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 429 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.7 | PASS | - |
| 430 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.8 | PASS | - |
| 431 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 432 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 433 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.7 | PASS | - |
| 434 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.8 | PASS | - |
| 435 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.10.249) | PASS | - |
| 436 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.14.73) | PASS | - |
| 437 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.16) | PASS | - |
| 438 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.18) | PASS | - |
| 439 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC01-Leaf5A Ethernet52/1 | PASS | - |
| 440 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC02-Leaf5B Ethernet53/1 | PASS | - |
| 441 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC02-Leaf5B Ethernet54/1 | PASS | - |
| 442 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet5/1 | PASS | - |
| 443 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet5/1 | PASS | - |
| 444 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 445 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 446 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 447 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 448 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 449 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 450 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 451 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 452 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 453 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 454 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 455 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 456 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 457 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 458 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 459 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 460 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet52/1 (IP: 192.168.10.248) - Destination: OTI-DC01-Leaf5A Ethernet52/1 (IP: 192.168.10.249) | PASS | - |
| 461 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.17) - Destination: OTI-DC02-Spine1 Ethernet5/1 (IP: 192.168.12.16) | PASS | - |
| 462 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.19) - Destination: OTI-DC02-Spine2 Ethernet5/1 (IP: 192.168.12.18) | PASS | - |
| 463 | OTI-DC02-Leaf5A | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 464 | OTI-DC02-Leaf5A | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 465 | OTI-DC02-Leaf5A | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 466 | OTI-DC02-Leaf5A | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 467 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC02-0901-ESX04_Onboard_NIC_2 = 'up' | PASS | - |
| 468 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC02-0901-ESX06_Onboard_NIC_2 = 'up' | PASS | - |
| 469 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - DC02-0901-ESX05_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 470 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - DC02-0901-ESX06_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 471 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_LINK_TO_OTI-DC01-Leaf5A_Ethernet52/1 = 'up' | PASS | - |
| 472 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_PEER_OTI-DC02-Leaf5B_Ethernet53/1 = 'up' | PASS | - |
| 473 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_PEER_OTI-DC02-Leaf5B_Ethernet54/1 = 'up' | PASS | - |
| 474 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet5/1 = 'up' | PASS | - |
| 475 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet5/1 = 'up' | PASS | - |
| 476 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 477 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 478 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 479 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC02-0901-ESX04 = 'up' | PASS | - |
| 480 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC02-0901-ESX06 = 'up' | PASS | - |
| 481 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - DC02-0901-ESX05 = 'up' | PASS | - |
| 482 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - DC02-0901-ESX06 = 'up' | PASS | - |
| 483 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_PEER_OTI-DC02-Leaf5B_Po531 = 'up' | PASS | - |
| 484 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 485 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 486 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 487 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_PEER_L3_iBGP: vrf Production = 'up' | PASS | - |
| 488 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_PEER_L3_PEERING = 'up' | PASS | - |
| 489 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG_PEER = 'up' | PASS | - |
| 490 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 491 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 492 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 493 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 494 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 495 | OTI-DC02-Leaf5A | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 496 | OTI-DC02-Leaf5A | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 497 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 498 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 499 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 500 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 501 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 502 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 503 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 504 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 505 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 506 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 507 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 508 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 509 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 510 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 511 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 512 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 513 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 514 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 515 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 516 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 517 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 518 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 519 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 520 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 521 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 522 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 523 | OTI-DC02-Leaf5A | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 524 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.7 | PASS | - |
| 525 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.8 | PASS | - |
| 526 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 527 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 528 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.7 | PASS | - |
| 529 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.8 | PASS | - |
| 530 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.10.250) | PASS | - |
| 531 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.14.72) | PASS | - |
| 532 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.20) | PASS | - |
| 533 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.22) | PASS | - |
| 534 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC01-Leaf5B Ethernet52/1 | PASS | - |
| 535 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC02-Leaf5A Ethernet53/1 | PASS | - |
| 536 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC02-Leaf5A Ethernet54/1 | PASS | - |
| 537 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet6/1 | PASS | - |
| 538 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet6/1 | PASS | - |
| 539 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 540 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 541 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 542 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 543 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 544 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 545 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 546 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 547 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 548 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 549 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 550 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 551 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 552 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 553 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 554 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 555 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet52/1 (IP: 192.168.10.251) - Destination: OTI-DC01-Leaf5B Ethernet52/1 (IP: 192.168.10.250) | PASS | - |
| 556 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.21) - Destination: OTI-DC02-Spine1 Ethernet6/1 (IP: 192.168.12.20) | PASS | - |
| 557 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.23) - Destination: OTI-DC02-Spine2 Ethernet6/1 (IP: 192.168.12.22) | PASS | - |
| 558 | OTI-DC02-Leaf5B | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 559 | OTI-DC02-Leaf5B | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 560 | OTI-DC02-Leaf5B | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 561 | OTI-DC02-Leaf5B | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 562 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC02-0901-ESX04_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 563 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC02-0901-ESX06_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 564 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - DC02-0901-ESX05_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 565 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - DC02-0901-ESX06_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 566 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_LINK_TO_OTI-DC01-Leaf5B_Ethernet52/1 = 'up' | PASS | - |
| 567 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_PEER_OTI-DC02-Leaf5A_Ethernet53/1 = 'up' | PASS | - |
| 568 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_PEER_OTI-DC02-Leaf5A_Ethernet54/1 = 'up' | PASS | - |
| 569 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet6/1 = 'up' | PASS | - |
| 570 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet6/1 = 'up' | PASS | - |
| 571 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 572 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 573 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 574 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC02-0901-ESX04 = 'up' | PASS | - |
| 575 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC02-0901-ESX06 = 'up' | PASS | - |
| 576 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - DC02-0901-ESX05 = 'up' | PASS | - |
| 577 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - DC02-0901-ESX06 = 'up' | PASS | - |
| 578 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_PEER_OTI-DC02-Leaf5A_Po531 = 'up' | PASS | - |
| 579 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 580 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 581 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 582 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_PEER_L3_iBGP: vrf Production = 'up' | PASS | - |
| 583 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_PEER_L3_PEERING = 'up' | PASS | - |
| 584 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG_PEER = 'up' | PASS | - |
| 585 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 586 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 587 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 588 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 589 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 590 | OTI-DC02-Leaf5B | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 591 | OTI-DC02-Leaf5B | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 592 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 593 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 594 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 595 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 596 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 597 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 598 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 599 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 600 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 601 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 602 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 603 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 604 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 605 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 606 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 607 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 608 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 609 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 610 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 611 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 612 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 613 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 614 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 615 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 616 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 617 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 618 | OTI-DC02-Leaf5B | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 619 | OTI-DC02-OBM1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 620 | OTI-DC02-OBM1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 621 | OTI-DC02-OBM1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 622 | OTI-DC02-OBM1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 623 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC02-0901-ESX01_idrac = 'up' | PASS | - |
| 624 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC02-0901-ESX02_idrac = 'up' | PASS | - |
| 625 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC02-0901-ESX03_idrac = 'up' | PASS | - |
| 626 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC02-0901-ESX04_idrac = 'up' | PASS | - |
| 627 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC02-0901-ESX05_idrac = 'up' | PASS | - |
| 628 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - DC02-0901-ESX06_idrac = 'up' | PASS | - |
| 629 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet7 - DC02-0901-SRVA_iLo = 'up' | PASS | - |
| 630 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC02-0901-SRVB_iLo = 'up' | PASS | - |
| 631 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet9 - DC02-0901-SRVC_iLo = 'up' | PASS | - |
| 632 | OTI-DC02-OBM1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 633 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf1 (IP: 10.245.218.3) | PASS | - |
| 634 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf2 (IP: 10.245.218.4) | PASS | - |
| 635 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf3 (IP: 10.245.218.5) | PASS | - |
| 636 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf4 (IP: 10.245.218.6) | PASS | - |
| 637 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5A (IP: 10.245.218.7) | PASS | - |
| 638 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5B (IP: 10.245.218.8) | PASS | - |
| 639 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf1 (IP: 192.168.12.1) | PASS | - |
| 640 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf2 (IP: 192.168.12.5) | PASS | - |
| 641 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf3 (IP: 192.168.12.9) | PASS | - |
| 642 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf4 (IP: 192.168.12.13) | PASS | - |
| 643 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.12.17) | PASS | - |
| 644 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.12.21) | PASS | - |
| 645 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC02-Leaf1 Ethernet55/1 | PASS | - |
| 646 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC02-Leaf2 Ethernet55/1 | PASS | - |
| 647 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC02-Leaf3 Ethernet55/1 | PASS | - |
| 648 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC02-Leaf4 Ethernet55/1 | PASS | - |
| 649 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC02-Leaf5A Ethernet55/1 | PASS | - |
| 650 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC02-Leaf5B Ethernet55/1 | PASS | - |
| 651 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.12.0) - Destination: OTI-DC02-Leaf1 Ethernet55/1 (IP: 192.168.12.1) | PASS | - |
| 652 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.12.4) - Destination: OTI-DC02-Leaf2 Ethernet55/1 (IP: 192.168.12.5) | PASS | - |
| 653 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.12.8) - Destination: OTI-DC02-Leaf3 Ethernet55/1 (IP: 192.168.12.9) | PASS | - |
| 654 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.12.12) - Destination: OTI-DC02-Leaf4 Ethernet55/1 (IP: 192.168.12.13) | PASS | - |
| 655 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.12.16) - Destination: OTI-DC02-Leaf5A Ethernet55/1 (IP: 192.168.12.17) | PASS | - |
| 656 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.12.20) - Destination: OTI-DC02-Leaf5B Ethernet55/1 (IP: 192.168.12.21) | PASS | - |
| 657 | OTI-DC02-Spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 658 | OTI-DC02-Spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 659 | OTI-DC02-Spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 660 | OTI-DC02-Spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 661 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_LINK_TO_OTI-DC02-LEAF1_Ethernet55/1 = 'up' | PASS | - |
| 662 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_LINK_TO_OTI-DC02-LEAF2_Ethernet55/1 = 'up' | PASS | - |
| 663 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_LINK_TO_OTI-DC02-LEAF3_Ethernet55/1 = 'up' | PASS | - |
| 664 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_LINK_TO_OTI-DC02-LEAF4_Ethernet55/1 = 'up' | PASS | - |
| 665 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_LINK_TO_OTI-DC02-LEAF5A_Ethernet55/1 = 'up' | PASS | - |
| 666 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_LINK_TO_OTI-DC02-LEAF5B_Ethernet55/1 = 'up' | PASS | - |
| 667 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 668 | OTI-DC02-Spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 669 | OTI-DC02-Spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 670 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf1 (IP: 10.245.218.3) | PASS | - |
| 671 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf2 (IP: 10.245.218.4) | PASS | - |
| 672 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf3 (IP: 10.245.218.5) | PASS | - |
| 673 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf4 (IP: 10.245.218.6) | PASS | - |
| 674 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5A (IP: 10.245.218.7) | PASS | - |
| 675 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5B (IP: 10.245.218.8) | PASS | - |
| 676 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf1 (IP: 192.168.12.3) | PASS | - |
| 677 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf2 (IP: 192.168.12.7) | PASS | - |
| 678 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf3 (IP: 192.168.12.11) | PASS | - |
| 679 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf4 (IP: 192.168.12.15) | PASS | - |
| 680 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.12.19) | PASS | - |
| 681 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.12.23) | PASS | - |
| 682 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC02-Leaf1 Ethernet56/1 | PASS | - |
| 683 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC02-Leaf2 Ethernet56/1 | PASS | - |
| 684 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC02-Leaf3 Ethernet56/1 | PASS | - |
| 685 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC02-Leaf4 Ethernet56/1 | PASS | - |
| 686 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC02-Leaf5A Ethernet56/1 | PASS | - |
| 687 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC02-Leaf5B Ethernet56/1 | PASS | - |
| 688 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.12.2) - Destination: OTI-DC02-Leaf1 Ethernet56/1 (IP: 192.168.12.3) | PASS | - |
| 689 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.12.6) - Destination: OTI-DC02-Leaf2 Ethernet56/1 (IP: 192.168.12.7) | PASS | - |
| 690 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.12.10) - Destination: OTI-DC02-Leaf3 Ethernet56/1 (IP: 192.168.12.11) | PASS | - |
| 691 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.12.14) - Destination: OTI-DC02-Leaf4 Ethernet56/1 (IP: 192.168.12.15) | PASS | - |
| 692 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.12.18) - Destination: OTI-DC02-Leaf5A Ethernet56/1 (IP: 192.168.12.19) | PASS | - |
| 693 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.12.22) - Destination: OTI-DC02-Leaf5B Ethernet56/1 (IP: 192.168.12.23) | PASS | - |
| 694 | OTI-DC02-Spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 695 | OTI-DC02-Spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 696 | OTI-DC02-Spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 697 | OTI-DC02-Spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 698 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_LINK_TO_OTI-DC02-LEAF1_Ethernet56/1 = 'up' | PASS | - |
| 699 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_LINK_TO_OTI-DC02-LEAF2_Ethernet56/1 = 'up' | PASS | - |
| 700 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_LINK_TO_OTI-DC02-LEAF3_Ethernet56/1 = 'up' | PASS | - |
| 701 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_LINK_TO_OTI-DC02-LEAF4_Ethernet56/1 = 'up' | PASS | - |
| 702 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_LINK_TO_OTI-DC02-LEAF5A_Ethernet56/1 = 'up' | PASS | - |
| 703 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_LINK_TO_OTI-DC02-LEAF5B_Ethernet56/1 = 'up' | PASS | - |
| 704 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 705 | OTI-DC02-Spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 706 | OTI-DC02-Spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
