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
| 601 | 555 | 10 | 36 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| OTI-DC01-Leaf1 | 87 | 83 | 0 | 4 | - | Hardware |
| OTI-DC01-Leaf2 | 87 | 83 | 0 | 4 | - | Hardware |
| OTI-DC01-Leaf3 | 87 | 79 | 4 | 4 | Interfaces | Hardware |
| OTI-DC01-Leaf4 | 87 | 79 | 4 | 4 | Interfaces | Hardware |
| OTI-DC01-Leaf5A | 82 | 77 | 1 | 4 | Interfaces | Hardware |
| OTI-DC01-Leaf5B | 82 | 77 | 1 | 4 | Interfaces | Hardware |
| OTI-DC01-OBM1 | 15 | 11 | 0 | 4 | - | Hardware |
| OTI-DC01-Spine1 | 37 | 33 | 0 | 4 | - | Hardware |
| OTI-DC01-Spine2 | 37 | 33 | 0 | 4 | - | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 60 | 60 | 0 | 0 |
| Connectivity | 102 | 102 | 0 | 0 |
| Hardware | 36 | 0 | 0 | 36 |
| Interfaces | 306 | 296 | 10 | 0 |
| MLAG | 2 | 2 | 0 | 0 |
| Routing | 86 | 86 | 0 | 0 |
| System | 9 | 9 | 0 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 210 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - DC01-0601-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel11 is down/lowerLayerDown'] |
| 211 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel12 - DC01-0601-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel12 is down/lowerLayerDown'] |
| 212 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel13 - DC01-0601-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel13 is down/lowerLayerDown'] |
| 213 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel14 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel14 is down/lowerLayerDown'] |
| 297 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - DC01-0601-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel11 is down/lowerLayerDown'] |
| 298 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel12 - DC01-0601-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel12 is down/lowerLayerDown'] |
| 299 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel13 - DC01-0601-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel13 is down/lowerLayerDown'] |
| 300 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel14 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel14 is down/lowerLayerDown'] |
| 396 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 478 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |

## All Test Results

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 1 | OTI-DC01-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 2 | OTI-DC01-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 3 | OTI-DC01-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.0) | PASS | - |
| 4 | OTI-DC01-Leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.2) | PASS | - |
| 5 | OTI-DC01-Leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet1/1 | PASS | - |
| 6 | OTI-DC01-Leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet1/1 | PASS | - |
| 7 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 8 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 9 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 10 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 11 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 12 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 13 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 14 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.3) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 15 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.1) - Destination: OTI-DC01-Spine1 Ethernet1/1 (IP: 192.168.11.0) | PASS | - |
| 16 | OTI-DC01-Leaf1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.3) - Destination: OTI-DC01-Spine2 Ethernet1/1 (IP: 192.168.11.2) | PASS | - |
| 17 | OTI-DC01-Leaf1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 18 | OTI-DC01-Leaf1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 19 | OTI-DC01-Leaf1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 20 | OTI-DC01-Leaf1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 21 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC01-0601-ESX01_Onboard_NIC_1 = 'up' | PASS | - |
| 22 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet11 - DC01-0601-ESX03_Onboard_NIC_1 = 'up' | PASS | - |
| 23 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet12 - DC01-0601-ESX04_Onboard_NIC_1 = 'up' | PASS | - |
| 24 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC01-0601-ESX02_Onboard_NIC_1 = 'up' | PASS | - |
| 25 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC01-0601-ESX01_Onboard_NIC_2 = 'up' | PASS | - |
| 26 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet26 - DC01-0601-ESX02_Onboard_NIC_2 = 'up' | PASS | - |
| 27 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet30 - DC01-0601-ESX05_Onboard_NIC_1 = 'up' | PASS | - |
| 28 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet31 - DC01-0601-ESX06_Onboard_NIC_1 = 'up' | PASS | - |
| 29 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC01-SPINE1_Ethernet1/1 = 'up' | PASS | - |
| 30 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC01-SPINE2_Ethernet1/1 = 'up' | PASS | - |
| 31 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 32 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 33 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 34 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 35 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC01-0601-ESX01 = 'up' | PASS | - |
| 36 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - DC01-0601-ESX03 = 'up' | PASS | - |
| 37 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel12 - DC01-0601-ESX04 = 'up' | PASS | - |
| 38 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC01-0601-ESX02 = 'up' | PASS | - |
| 39 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC01-0601-ESX01 = 'up' | PASS | - |
| 40 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - DC01-0601-ESX02 = 'up' | PASS | - |
| 41 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel30 - DC01-0601-ESX05 = 'up' | PASS | - |
| 42 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel31 - DC01-0601-ESX06 = 'up' | PASS | - |
| 43 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 44 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 45 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 46 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 47 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 48 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 49 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 50 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 51 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 52 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 53 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 54 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 55 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 56 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 57 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 58 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 59 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 60 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 61 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 62 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 63 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 64 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 65 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 66 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 67 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 68 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 69 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 70 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 71 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 72 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 73 | OTI-DC01-Leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 74 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 75 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 76 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 77 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 78 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 79 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 80 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 81 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 82 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 83 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 84 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 85 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 86 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 87 | OTI-DC01-Leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 88 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 89 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 90 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.4) | PASS | - |
| 91 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.6) | PASS | - |
| 92 | OTI-DC01-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet2/1 | PASS | - |
| 93 | OTI-DC01-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet2/1 | PASS | - |
| 94 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 95 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 96 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 97 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 98 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 99 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 100 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 101 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 102 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.5) - Destination: OTI-DC01-Spine1 Ethernet2/1 (IP: 192.168.11.4) | PASS | - |
| 103 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.7) - Destination: OTI-DC01-Spine2 Ethernet2/1 (IP: 192.168.11.6) | PASS | - |
| 104 | OTI-DC01-Leaf2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 105 | OTI-DC01-Leaf2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 106 | OTI-DC01-Leaf2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 107 | OTI-DC01-Leaf2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 108 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC01-0601-ESX01_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 109 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet11 - DC01-0601-ESX03_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 110 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet12 - DC01-0601-ESX04_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 111 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC01-0601-ESX02_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 112 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC01-0601-ESX01_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 113 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet26 - DC01-0601-ESX02_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 114 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet30 - DC01-0601-ESX05_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 115 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet31 - DC01-0601-ESX06_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 116 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC01-SPINE1_Ethernet2/1 = 'up' | PASS | - |
| 117 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC01-SPINE2_Ethernet2/1 = 'up' | PASS | - |
| 118 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 119 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 120 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 121 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 122 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC01-0601-ESX01 = 'up' | PASS | - |
| 123 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - DC01-0601-ESX03 = 'up' | PASS | - |
| 124 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel12 - DC01-0601-ESX04 = 'up' | PASS | - |
| 125 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC01-0601-ESX02 = 'up' | PASS | - |
| 126 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC01-0601-ESX01 = 'up' | PASS | - |
| 127 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - DC01-0601-ESX02 = 'up' | PASS | - |
| 128 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel30 - DC01-0601-ESX05 = 'up' | PASS | - |
| 129 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel31 - DC01-0601-ESX06 = 'up' | PASS | - |
| 130 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 131 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 132 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 133 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 134 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 135 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 136 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 137 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 138 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 139 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 140 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 141 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 142 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 143 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 144 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 145 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 146 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 147 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 148 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 149 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 150 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 151 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 152 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 153 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 154 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 155 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 156 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 157 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 158 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 159 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 160 | OTI-DC01-Leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 161 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 162 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 163 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 164 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 165 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 166 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 167 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 168 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 169 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 170 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 171 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 172 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 173 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 174 | OTI-DC01-Leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 175 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 176 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 177 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.8) | PASS | - |
| 178 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.10) | PASS | - |
| 179 | OTI-DC01-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet3/1 | PASS | - |
| 180 | OTI-DC01-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet3/1 | PASS | - |
| 181 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 182 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 183 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 184 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 185 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 186 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 187 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 188 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 189 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.9) - Destination: OTI-DC01-Spine1 Ethernet3/1 (IP: 192.168.11.8) | PASS | - |
| 190 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.11) - Destination: OTI-DC01-Spine2 Ethernet3/1 (IP: 192.168.11.10) | PASS | - |
| 191 | OTI-DC01-Leaf3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 192 | OTI-DC01-Leaf3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 193 | OTI-DC01-Leaf3 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 194 | OTI-DC01-Leaf3 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 195 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC01-0601-ESX03_Onboard_NIC_2 = 'up' | PASS | - |
| 196 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet11 - DC01-0601-SRVA_Port_0 = 'up' | PASS | - |
| 197 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet12 - DC01-0601-SRVB_Port_0 = 'up' | PASS | - |
| 198 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet13 - DC01-0601-SRVC_Port_0 = 'up' | PASS | - |
| 199 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet14 - DC01-0601-SRVD_Port_0 = 'up' | PASS | - |
| 200 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC01-0601-ESX04_Onboard_NIC_2 = 'up' | PASS | - |
| 201 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC01-0601-ESX05_Onboard_NIC_2 = 'up' | PASS | - |
| 202 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC01-0601-ESX06_Onboard_NIC_2 = 'up' | PASS | - |
| 203 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC01-SPINE1_Ethernet3/1 = 'up' | PASS | - |
| 204 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC01-SPINE2_Ethernet3/1 = 'up' | PASS | - |
| 205 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 206 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 207 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 208 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 209 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC01-0601-ESX03 = 'up' | PASS | - |
| 210 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - DC01-0601-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel11 is down/lowerLayerDown'] |
| 211 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel12 - DC01-0601-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel12 is down/lowerLayerDown'] |
| 212 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel13 - DC01-0601-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel13 is down/lowerLayerDown'] |
| 213 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel14 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel14 is down/lowerLayerDown'] |
| 214 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC01-0601-ESX04 = 'up' | PASS | - |
| 215 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - DC01-0601-ESX05 = 'up' | PASS | - |
| 216 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC01-0601-ESX06 = 'up' | PASS | - |
| 217 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 218 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 219 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 220 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 221 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 222 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 223 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 224 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 225 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 226 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 227 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 228 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 229 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 230 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 231 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 232 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 233 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 234 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 235 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 236 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 237 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 238 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 239 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 240 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 241 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 242 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 243 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 244 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 245 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 246 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 247 | OTI-DC01-Leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 248 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 249 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 250 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 251 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 252 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 253 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 254 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 255 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 256 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 257 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 258 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 259 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 260 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 261 | OTI-DC01-Leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 262 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 263 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 264 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.12) | PASS | - |
| 265 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.14) | PASS | - |
| 266 | OTI-DC01-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet4/1 | PASS | - |
| 267 | OTI-DC01-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet4/1 | PASS | - |
| 268 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 269 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 270 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 271 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 272 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 273 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 274 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 275 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 276 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.13) - Destination: OTI-DC01-Spine1 Ethernet4/1 (IP: 192.168.11.12) | PASS | - |
| 277 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.15) - Destination: OTI-DC01-Spine2 Ethernet4/1 (IP: 192.168.11.14) | PASS | - |
| 278 | OTI-DC01-Leaf4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 279 | OTI-DC01-Leaf4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 280 | OTI-DC01-Leaf4 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 281 | OTI-DC01-Leaf4 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 282 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC01-0601-ESX03_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 283 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet11 - DC01-0601-SRVA_Port_1 = 'up' | PASS | - |
| 284 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet12 - DC01-0601-SRVB_Port_1 = 'up' | PASS | - |
| 285 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet13 - DC01-0601-SRVC_Port_1 = 'up' | PASS | - |
| 286 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet14 - DC01-0601-SRVD_Port_1 = 'up' | PASS | - |
| 287 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC01-0601-ESX04_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 288 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC01-0601-ESX05_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 289 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC01-0601-ESX06_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 290 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC01-SPINE1_Ethernet4/1 = 'up' | PASS | - |
| 291 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC01-SPINE2_Ethernet4/1 = 'up' | PASS | - |
| 292 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 293 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 294 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 295 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 296 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC01-0601-ESX03 = 'up' | PASS | - |
| 297 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - DC01-0601-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel11 is down/lowerLayerDown'] |
| 298 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel12 - DC01-0601-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel12 is down/lowerLayerDown'] |
| 299 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel13 - DC01-0601-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel13 is down/lowerLayerDown'] |
| 300 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel14 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel14 is down/lowerLayerDown'] |
| 301 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC01-0601-ESX04 = 'up' | PASS | - |
| 302 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - DC01-0601-ESX05 = 'up' | PASS | - |
| 303 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC01-0601-ESX06 = 'up' | PASS | - |
| 304 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 305 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 306 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 307 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 308 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 309 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 310 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 311 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 312 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 313 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 314 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 315 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 316 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 317 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 318 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 319 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 320 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 321 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 322 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 323 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 324 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 325 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 326 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 327 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 328 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 329 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 330 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 331 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 332 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 333 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 334 | OTI-DC01-Leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 335 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 336 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 337 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 338 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 339 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 340 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 341 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 342 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 343 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 344 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 345 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 346 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 347 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 348 | OTI-DC01-Leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 349 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.7 | PASS | - |
| 350 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.8 | PASS | - |
| 351 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 352 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 353 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.7 | PASS | - |
| 354 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.8 | PASS | - |
| 355 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.13.73) | PASS | - |
| 356 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.16) | PASS | - |
| 357 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.18) | PASS | - |
| 358 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.10.248) | PASS | - |
| 359 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC02-Leaf5A Ethernet52/1 | PASS | - |
| 360 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC01-Leaf5B Ethernet53/1 | PASS | - |
| 361 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC01-Leaf5B Ethernet54/1 | PASS | - |
| 362 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet5/1 | PASS | - |
| 363 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet5/1 | PASS | - |
| 364 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 365 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 366 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 367 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 368 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 369 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 370 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 371 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 372 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.17) - Destination: OTI-DC01-Spine1 Ethernet5/1 (IP: 192.168.11.16) | PASS | - |
| 373 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.19) - Destination: OTI-DC01-Spine2 Ethernet5/1 (IP: 192.168.11.18) | PASS | - |
| 374 | OTI-DC01-Leaf5A | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 375 | OTI-DC01-Leaf5A | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 376 | OTI-DC01-Leaf5A | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 377 | OTI-DC01-Leaf5A | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 378 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC01-0601-ESX01_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 379 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC01-0601-ESX02_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 380 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC01-0601-SRVD_Port_2 = 'up' | PASS | - |
| 381 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC01-0601-ESX03_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 382 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC01-0601-ESX04_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 383 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC01-0601-ESX05_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 384 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_LINK_TO_OTI-DC02-Leaf5A_Ethernet52/1 = 'up' | PASS | - |
| 385 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_PEER_OTI-DC01-Leaf5B_Ethernet53/1 = 'up' | PASS | - |
| 386 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_PEER_OTI-DC01-Leaf5B_Ethernet54/1 = 'up' | PASS | - |
| 387 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC01-SPINE1_Ethernet5/1 = 'up' | PASS | - |
| 388 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC01-SPINE2_Ethernet5/1 = 'up' | PASS | - |
| 389 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - DC01-0601-ESX06_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 390 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 391 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 392 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 393 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 394 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC01-0601-ESX01 = 'up' | PASS | - |
| 395 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC01-0601-ESX02 = 'up' | PASS | - |
| 396 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 397 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - DC01-0601-ESX03 = 'up' | PASS | - |
| 398 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC01-0601-ESX04 = 'up' | PASS | - |
| 399 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC01-0601-ESX05 = 'up' | PASS | - |
| 400 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_PEER_OTI-DC01-Leaf5B_Po531 = 'up' | PASS | - |
| 401 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel6 - DC01-0601-ESX06 = 'up' | PASS | - |
| 402 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 403 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 404 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 405 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 406 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 407 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_PEER_L3_iBGP: vrf Production = 'up' | PASS | - |
| 408 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_PEER_L3_iBGP: vrf Development = 'up' | PASS | - |
| 409 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 410 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_PEER_L3_PEERING = 'up' | PASS | - |
| 411 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG_PEER = 'up' | PASS | - |
| 412 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 413 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 414 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 415 | OTI-DC01-Leaf5A | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 416 | OTI-DC01-Leaf5A | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 417 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 418 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 419 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 420 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 421 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 422 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 423 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 424 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 425 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 426 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 427 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 428 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 429 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 430 | OTI-DC01-Leaf5A | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 431 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.7 | PASS | - |
| 432 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.8 | PASS | - |
| 433 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 434 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 435 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.7 | PASS | - |
| 436 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.8 | PASS | - |
| 437 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.13.72) | PASS | - |
| 438 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.20) | PASS | - |
| 439 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.22) | PASS | - |
| 440 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.10.251) | PASS | - |
| 441 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC02-Leaf5B Ethernet52/1 | PASS | - |
| 442 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC01-Leaf5A Ethernet53/1 | PASS | - |
| 443 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC01-Leaf5A Ethernet54/1 | PASS | - |
| 444 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet6/1 | PASS | - |
| 445 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet6/1 | PASS | - |
| 446 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 447 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 448 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 449 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 450 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 451 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 452 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 453 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 454 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.21) - Destination: OTI-DC01-Spine1 Ethernet6/1 (IP: 192.168.11.20) | PASS | - |
| 455 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.23) - Destination: OTI-DC01-Spine2 Ethernet6/1 (IP: 192.168.11.22) | PASS | - |
| 456 | OTI-DC01-Leaf5B | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 457 | OTI-DC01-Leaf5B | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 458 | OTI-DC01-Leaf5B | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 459 | OTI-DC01-Leaf5B | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 460 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC01-0601-ESX01_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 461 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC01-0601-ESX02_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 462 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - DC01-0601-SRVD_Port_3 = 'up' | PASS | - |
| 463 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC01-0601-ESX03_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 464 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC01-0601-ESX04_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 465 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC01-0601-ESX05_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 466 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_LINK_TO_OTI-DC02-Leaf5B_Ethernet52/1 = 'up' | PASS | - |
| 467 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_PEER_OTI-DC01-Leaf5A_Ethernet53/1 = 'up' | PASS | - |
| 468 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_PEER_OTI-DC01-Leaf5A_Ethernet54/1 = 'up' | PASS | - |
| 469 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC01-SPINE1_Ethernet6/1 = 'up' | PASS | - |
| 470 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC01-SPINE2_Ethernet6/1 = 'up' | PASS | - |
| 471 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - DC01-0601-ESX06_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 472 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 473 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 474 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - Production_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 475 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - Development_VTEP_DIAGNOSTICS = 'up' | PASS | - |
| 476 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC01-0601-ESX01 = 'up' | PASS | - |
| 477 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - DC01-0601-ESX02 = 'up' | PASS | - |
| 478 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - DC01-0601-SRVD = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 479 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - DC01-0601-ESX03 = 'up' | PASS | - |
| 480 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - DC01-0601-ESX04 = 'up' | PASS | - |
| 481 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - DC01-0601-ESX05 = 'up' | PASS | - |
| 482 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_PEER_OTI-DC01-Leaf5A_Po531 = 'up' | PASS | - |
| 483 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel6 - DC01-0601-ESX06 = 'up' | PASS | - |
| 484 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 485 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 486 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 487 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 488 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 489 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_PEER_L3_iBGP: vrf Production = 'up' | PASS | - |
| 490 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_PEER_L3_iBGP: vrf Development = 'up' | PASS | - |
| 491 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 492 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_PEER_L3_PEERING = 'up' | PASS | - |
| 493 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG_PEER = 'up' | PASS | - |
| 494 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 495 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 496 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 497 | OTI-DC01-Leaf5B | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 498 | OTI-DC01-Leaf5B | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 499 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 500 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 501 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 502 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 503 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 504 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 505 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 506 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 507 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 508 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 509 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 510 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 511 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 512 | OTI-DC01-Leaf5B | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 513 | OTI-DC01-OBM1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 514 | OTI-DC01-OBM1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 515 | OTI-DC01-OBM1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 516 | OTI-DC01-OBM1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 517 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC01-0601-ESX01_idrac = 'up' | PASS | - |
| 518 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet10 - DC01-0601-SRVD_iLo = 'up' | PASS | - |
| 519 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC01-0601-ESX02_idrac = 'up' | PASS | - |
| 520 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - DC01-0601-ESX03_idrac = 'up' | PASS | - |
| 521 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - DC01-0601-ESX04_idrac = 'up' | PASS | - |
| 522 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - DC01-0601-ESX05_idrac = 'up' | PASS | - |
| 523 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - DC01-0601-ESX06_idrac = 'up' | PASS | - |
| 524 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet7 - DC01-0601-SRVA_iLo = 'up' | PASS | - |
| 525 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC01-0601-SRVB_iLo = 'up' | PASS | - |
| 526 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet9 - DC01-0601-SRVC_iLo = 'up' | PASS | - |
| 527 | OTI-DC01-OBM1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 528 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf1 (IP: 10.245.217.3) | PASS | - |
| 529 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf2 (IP: 10.245.217.4) | PASS | - |
| 530 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf3 (IP: 10.245.217.5) | PASS | - |
| 531 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf4 (IP: 10.245.217.6) | PASS | - |
| 532 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5A (IP: 10.245.217.7) | PASS | - |
| 533 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5B (IP: 10.245.217.8) | PASS | - |
| 534 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf1 (IP: 192.168.11.1) | PASS | - |
| 535 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf2 (IP: 192.168.11.5) | PASS | - |
| 536 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf3 (IP: 192.168.11.9) | PASS | - |
| 537 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf4 (IP: 192.168.11.13) | PASS | - |
| 538 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.11.17) | PASS | - |
| 539 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.11.21) | PASS | - |
| 540 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC01-Leaf1 Ethernet55/1 | PASS | - |
| 541 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC01-Leaf2 Ethernet55/1 | PASS | - |
| 542 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC01-Leaf3 Ethernet55/1 | PASS | - |
| 543 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC01-Leaf4 Ethernet55/1 | PASS | - |
| 544 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC01-Leaf5A Ethernet55/1 | PASS | - |
| 545 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC01-Leaf5B Ethernet55/1 | PASS | - |
| 546 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.11.0) - Destination: OTI-DC01-Leaf1 Ethernet55/1 (IP: 192.168.11.1) | PASS | - |
| 547 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.11.4) - Destination: OTI-DC01-Leaf2 Ethernet55/1 (IP: 192.168.11.5) | PASS | - |
| 548 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.11.8) - Destination: OTI-DC01-Leaf3 Ethernet55/1 (IP: 192.168.11.9) | PASS | - |
| 549 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.11.12) - Destination: OTI-DC01-Leaf4 Ethernet55/1 (IP: 192.168.11.13) | PASS | - |
| 550 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.11.16) - Destination: OTI-DC01-Leaf5A Ethernet55/1 (IP: 192.168.11.17) | PASS | - |
| 551 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.11.20) - Destination: OTI-DC01-Leaf5B Ethernet55/1 (IP: 192.168.11.21) | PASS | - |
| 552 | OTI-DC01-Spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 553 | OTI-DC01-Spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 554 | OTI-DC01-Spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 555 | OTI-DC01-Spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 556 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_LINK_TO_OTI-DC01-LEAF1_Ethernet55/1 = 'up' | PASS | - |
| 557 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_LINK_TO_OTI-DC01-LEAF2_Ethernet55/1 = 'up' | PASS | - |
| 558 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_LINK_TO_OTI-DC01-LEAF3_Ethernet55/1 = 'up' | PASS | - |
| 559 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_LINK_TO_OTI-DC01-LEAF4_Ethernet55/1 = 'up' | PASS | - |
| 560 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_LINK_TO_OTI-DC01-LEAF5A_Ethernet55/1 = 'up' | PASS | - |
| 561 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_LINK_TO_OTI-DC01-LEAF5B_Ethernet55/1 = 'up' | PASS | - |
| 562 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 563 | OTI-DC01-Spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 564 | OTI-DC01-Spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 565 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf1 (IP: 10.245.217.3) | PASS | - |
| 566 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf2 (IP: 10.245.217.4) | PASS | - |
| 567 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf3 (IP: 10.245.217.5) | PASS | - |
| 568 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf4 (IP: 10.245.217.6) | PASS | - |
| 569 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5A (IP: 10.245.217.7) | PASS | - |
| 570 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5B (IP: 10.245.217.8) | PASS | - |
| 571 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf1 (IP: 192.168.11.3) | PASS | - |
| 572 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf2 (IP: 192.168.11.7) | PASS | - |
| 573 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf3 (IP: 192.168.11.11) | PASS | - |
| 574 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf4 (IP: 192.168.11.15) | PASS | - |
| 575 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.11.19) | PASS | - |
| 576 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.11.23) | PASS | - |
| 577 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC01-Leaf1 Ethernet56/1 | PASS | - |
| 578 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC01-Leaf2 Ethernet56/1 | PASS | - |
| 579 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC01-Leaf3 Ethernet56/1 | PASS | - |
| 580 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC01-Leaf4 Ethernet56/1 | PASS | - |
| 581 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC01-Leaf5A Ethernet56/1 | PASS | - |
| 582 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC01-Leaf5B Ethernet56/1 | PASS | - |
| 583 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.11.2) - Destination: OTI-DC01-Leaf1 Ethernet56/1 (IP: 192.168.11.3) | PASS | - |
| 584 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.11.6) - Destination: OTI-DC01-Leaf2 Ethernet56/1 (IP: 192.168.11.7) | PASS | - |
| 585 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.11.10) - Destination: OTI-DC01-Leaf3 Ethernet56/1 (IP: 192.168.11.11) | PASS | - |
| 586 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.11.14) - Destination: OTI-DC01-Leaf4 Ethernet56/1 (IP: 192.168.11.15) | PASS | - |
| 587 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.11.18) - Destination: OTI-DC01-Leaf5A Ethernet56/1 (IP: 192.168.11.19) | PASS | - |
| 588 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.11.22) - Destination: OTI-DC01-Leaf5B Ethernet56/1 (IP: 192.168.11.23) | PASS | - |
| 589 | OTI-DC01-Spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 590 | OTI-DC01-Spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 591 | OTI-DC01-Spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 592 | OTI-DC01-Spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 593 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_LINK_TO_OTI-DC01-LEAF1_Ethernet56/1 = 'up' | PASS | - |
| 594 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_LINK_TO_OTI-DC01-LEAF2_Ethernet56/1 = 'up' | PASS | - |
| 595 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_LINK_TO_OTI-DC01-LEAF3_Ethernet56/1 = 'up' | PASS | - |
| 596 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_LINK_TO_OTI-DC01-LEAF4_Ethernet56/1 = 'up' | PASS | - |
| 597 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_LINK_TO_OTI-DC01-LEAF5A_Ethernet56/1 = 'up' | PASS | - |
| 598 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_LINK_TO_OTI-DC01-LEAF5B_Ethernet56/1 = 'up' | PASS | - |
| 599 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 600 | OTI-DC01-Spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 601 | OTI-DC01-Spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
