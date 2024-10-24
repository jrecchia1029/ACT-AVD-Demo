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
| 474 | 431 | 7 | 36 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| OTI-DC01-Leaf1 | 79 | 74 | 1 | 4 | System | Hardware |
| OTI-DC01-Leaf2 | 79 | 74 | 1 | 4 | System | Hardware |
| OTI-DC01-Leaf3 | 44 | 38 | 2 | 4 | Interfaces, System | Hardware |
| OTI-DC01-Leaf4 | 44 | 39 | 1 | 4 | Interfaces | Hardware |
| OTI-DC01-Leaf5A | 68 | 63 | 1 | 4 | System | Hardware |
| OTI-DC01-Leaf5B | 68 | 64 | 0 | 4 | - | Hardware |
| OTI-DC01-OBM1 | 10 | 6 | 0 | 4 | - | Hardware |
| OTI-DC01-Spine1 | 41 | 36 | 1 | 4 | System | Hardware |
| OTI-DC01-Spine2 | 41 | 37 | 0 | 4 | - | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 60 | 60 | 0 | 0 |
| Connectivity | 102 | 102 | 0 | 0 |
| Hardware | 36 | 0 | 0 | 36 |
| Interfaces | 143 | 141 | 2 | 0 |
| MLAG | 2 | 2 | 0 | 0 |
| Routing | 86 | 86 | 0 | 0 |
| System | 45 | 40 | 5 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 75 | OTI-DC01-Leaf1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.1% |
| 154 | OTI-DC01-Leaf2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 90.6% |
| 183 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 198 | OTI-DC01-Leaf3 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.8% |
| 227 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 310 | OTI-DC01-Leaf5A | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 93.9% |
| 429 | OTI-DC01-Spine1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 94.3% |

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
| 21 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC01-0601-ESX01_Onboard_NIC_1 = 'up' | PASS | - |
| 22 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - SERVER_DC01-0601-ESX01_Onboard_NIC_2 = 'up' | PASS | - |
| 23 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC01-Spine1_Ethernet1/1 = 'up' | PASS | - |
| 24 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC01-Spine2_Ethernet1/1 = 'up' | PASS | - |
| 25 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 26 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 27 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 28 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 29 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC01-0601-ESX01 = 'up' | PASS | - |
| 30 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC01-0601-ESX01 = 'up' | PASS | - |
| 31 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 32 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 33 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 34 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 35 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 36 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 37 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 38 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 39 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 40 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 41 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 42 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 43 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 44 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 45 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 46 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 47 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 48 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 49 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 50 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 51 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 52 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 53 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 54 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 55 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 56 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 57 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 58 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 59 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 60 | OTI-DC01-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 61 | OTI-DC01-Leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 62 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 63 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 64 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 65 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 66 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 67 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 68 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 69 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 70 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 71 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 72 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 73 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 74 | OTI-DC01-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 75 | OTI-DC01-Leaf1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.1% |
| 76 | OTI-DC01-Leaf1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 77 | OTI-DC01-Leaf1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 78 | OTI-DC01-Leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 79 | OTI-DC01-Leaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 80 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 81 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 82 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.4) | PASS | - |
| 83 | OTI-DC01-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.6) | PASS | - |
| 84 | OTI-DC01-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet2/1 | PASS | - |
| 85 | OTI-DC01-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet2/1 | PASS | - |
| 86 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 87 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 88 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 89 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 90 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 91 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 92 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 93 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.4) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 94 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.5) - Destination: OTI-DC01-Spine1 Ethernet2/1 (IP: 192.168.11.4) | PASS | - |
| 95 | OTI-DC01-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.7) - Destination: OTI-DC01-Spine2 Ethernet2/1 (IP: 192.168.11.6) | PASS | - |
| 96 | OTI-DC01-Leaf2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 97 | OTI-DC01-Leaf2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 98 | OTI-DC01-Leaf2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 99 | OTI-DC01-Leaf2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 100 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC01-0601-ESX01_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 101 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - SERVER_DC01-0601-ESX01_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 102 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC01-Spine1_Ethernet2/1 = 'up' | PASS | - |
| 103 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC01-Spine2_Ethernet2/1 = 'up' | PASS | - |
| 104 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 105 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 106 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 107 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 108 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC01-0601-ESX01 = 'up' | PASS | - |
| 109 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC01-0601-ESX01 = 'up' | PASS | - |
| 110 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 111 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 112 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 113 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 114 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 115 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 116 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 117 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 118 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 119 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 120 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 121 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 122 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 123 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 124 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 125 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 126 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 127 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 128 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 129 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 130 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 131 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 132 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 133 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 134 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 135 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 136 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 137 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 138 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 139 | OTI-DC01-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 140 | OTI-DC01-Leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 141 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 142 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 143 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 144 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 145 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 146 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 147 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 148 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 149 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 150 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 151 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 152 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 153 | OTI-DC01-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 154 | OTI-DC01-Leaf2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 90.6% |
| 155 | OTI-DC01-Leaf2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 156 | OTI-DC01-Leaf2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 157 | OTI-DC01-Leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 158 | OTI-DC01-Leaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 159 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 160 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 161 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.8) | PASS | - |
| 162 | OTI-DC01-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.10) | PASS | - |
| 163 | OTI-DC01-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet3/1 | PASS | - |
| 164 | OTI-DC01-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet3/1 | PASS | - |
| 165 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 166 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 167 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 168 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 169 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 170 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 171 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 172 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.5) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 173 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.9) - Destination: OTI-DC01-Spine1 Ethernet3/1 (IP: 192.168.11.8) | PASS | - |
| 174 | OTI-DC01-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.11) - Destination: OTI-DC01-Spine2 Ethernet3/1 (IP: 192.168.11.10) | PASS | - |
| 175 | OTI-DC01-Leaf3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 176 | OTI-DC01-Leaf3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 177 | OTI-DC01-Leaf3 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 178 | OTI-DC01-Leaf3 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 179 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC01-Spine1_Ethernet3/1 = 'up' | PASS | - |
| 180 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC01-Spine2_Ethernet3/1 = 'up' | PASS | - |
| 181 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 182 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 183 | OTI-DC01-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 184 | OTI-DC01-Leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 185 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 186 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 187 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 188 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 189 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 190 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 191 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 192 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 193 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 194 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 195 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 196 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 197 | OTI-DC01-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 198 | OTI-DC01-Leaf3 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.8% |
| 199 | OTI-DC01-Leaf3 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 200 | OTI-DC01-Leaf3 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 201 | OTI-DC01-Leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 202 | OTI-DC01-Leaf3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 203 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 204 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 205 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.12) | PASS | - |
| 206 | OTI-DC01-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.14) | PASS | - |
| 207 | OTI-DC01-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet4/1 | PASS | - |
| 208 | OTI-DC01-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet4/1 | PASS | - |
| 209 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 210 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 211 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 212 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 213 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 214 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 215 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 216 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.6) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 217 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.13) - Destination: OTI-DC01-Spine1 Ethernet4/1 (IP: 192.168.11.12) | PASS | - |
| 218 | OTI-DC01-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.15) - Destination: OTI-DC01-Spine2 Ethernet4/1 (IP: 192.168.11.14) | PASS | - |
| 219 | OTI-DC01-Leaf4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 220 | OTI-DC01-Leaf4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 221 | OTI-DC01-Leaf4 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 222 | OTI-DC01-Leaf4 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 223 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC01-Spine1_Ethernet4/1 = 'up' | PASS | - |
| 224 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC01-Spine2_Ethernet4/1 = 'up' | PASS | - |
| 225 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 226 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 227 | OTI-DC01-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 228 | OTI-DC01-Leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 229 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 230 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 231 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 232 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 233 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 234 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 235 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 236 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 237 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 238 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 239 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 240 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 241 | OTI-DC01-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 242 | OTI-DC01-Leaf4 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 243 | OTI-DC01-Leaf4 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 244 | OTI-DC01-Leaf4 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 245 | OTI-DC01-Leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 246 | OTI-DC01-Leaf4 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 247 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.7 | PASS | - |
| 248 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.8 | PASS | - |
| 249 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 250 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 251 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.7 | PASS | - |
| 252 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.8 | PASS | - |
| 253 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.13.73) | PASS | - |
| 254 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.16) | PASS | - |
| 255 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.18) | PASS | - |
| 256 | OTI-DC01-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.10.248) | PASS | - |
| 257 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC02-Leaf5A Ethernet52/1 | PASS | - |
| 258 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC01-Leaf5B Ethernet53/1 | PASS | - |
| 259 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC01-Leaf5B Ethernet54/1 | PASS | - |
| 260 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet5/1 | PASS | - |
| 261 | OTI-DC01-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet5/1 | PASS | - |
| 262 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 263 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 264 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 265 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 266 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 267 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 268 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 269 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.7) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 270 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.17) - Destination: OTI-DC01-Spine1 Ethernet5/1 (IP: 192.168.11.16) | PASS | - |
| 271 | OTI-DC01-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.19) - Destination: OTI-DC01-Spine2 Ethernet5/1 (IP: 192.168.11.18) | PASS | - |
| 272 | OTI-DC01-Leaf5A | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 273 | OTI-DC01-Leaf5A | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 274 | OTI-DC01-Leaf5A | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 275 | OTI-DC01-Leaf5A | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 276 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC01-0601-ESX01_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 277 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_OTI-DC02-Leaf5A_Ethernet52/1 = 'up' | PASS | - |
| 278 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_OTI-DC01-Leaf5B_Ethernet53/1 = 'up' | PASS | - |
| 279 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_OTI-DC01-Leaf5B_Ethernet54/1 = 'up' | PASS | - |
| 280 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC01-Spine1_Ethernet5/1 = 'up' | PASS | - |
| 281 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC01-Spine2_Ethernet5/1 = 'up' | PASS | - |
| 282 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 283 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 284 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 285 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC01-0601-ESX01 = 'up' | PASS | - |
| 286 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_OTI-DC01-Leaf5B_Port-Channel531 = 'up' | PASS | - |
| 287 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 288 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 289 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 290 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 291 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_Development = 'up' | PASS | - |
| 292 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 293 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 294 | OTI-DC01-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 295 | OTI-DC01-Leaf5A | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 296 | OTI-DC01-Leaf5A | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 297 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 298 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 299 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 300 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 301 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 302 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 303 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 304 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 305 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 306 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 307 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 308 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 309 | OTI-DC01-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 310 | OTI-DC01-Leaf5A | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 93.9% |
| 311 | OTI-DC01-Leaf5A | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 312 | OTI-DC01-Leaf5A | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 313 | OTI-DC01-Leaf5A | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 314 | OTI-DC01-Leaf5A | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 315 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.7 | PASS | - |
| 316 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.218.8 | PASS | - |
| 317 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine1 (IP: 10.245.217.1) | PASS | - |
| 318 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Spine2 (IP: 10.245.217.2) | PASS | - |
| 319 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.7 | PASS | - |
| 320 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.218.8 | PASS | - |
| 321 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.13.72) | PASS | - |
| 322 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine1 (IP: 192.168.11.20) | PASS | - |
| 323 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Spine2 (IP: 192.168.11.22) | PASS | - |
| 324 | OTI-DC01-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.10.251) | PASS | - |
| 325 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC02-Leaf5B Ethernet52/1 | PASS | - |
| 326 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC01-Leaf5A Ethernet53/1 | PASS | - |
| 327 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC01-Leaf5A Ethernet54/1 | PASS | - |
| 328 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC01-Spine1 Ethernet6/1 | PASS | - |
| 329 | OTI-DC01-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC01-Spine2 Ethernet6/1 | PASS | - |
| 330 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 331 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 332 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 333 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 334 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 335 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 336 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 337 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.217.8) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 338 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.11.21) - Destination: OTI-DC01-Spine1 Ethernet6/1 (IP: 192.168.11.20) | PASS | - |
| 339 | OTI-DC01-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.11.23) - Destination: OTI-DC01-Spine2 Ethernet6/1 (IP: 192.168.11.22) | PASS | - |
| 340 | OTI-DC01-Leaf5B | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 341 | OTI-DC01-Leaf5B | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 342 | OTI-DC01-Leaf5B | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 343 | OTI-DC01-Leaf5B | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 344 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC01-0601-ESX01_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 345 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_OTI-DC02-Leaf5B_Ethernet52/1 = 'up' | PASS | - |
| 346 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_OTI-DC01-Leaf5A_Ethernet53/1 = 'up' | PASS | - |
| 347 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_OTI-DC01-Leaf5A_Ethernet54/1 = 'up' | PASS | - |
| 348 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC01-Spine1_Ethernet6/1 = 'up' | PASS | - |
| 349 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC01-Spine2_Ethernet6/1 = 'up' | PASS | - |
| 350 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 351 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 352 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 353 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC01-0601-ESX01 = 'up' | PASS | - |
| 354 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_OTI-DC01-Leaf5A_Port-Channel531 = 'up' | PASS | - |
| 355 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 356 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 357 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 358 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 359 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_Development = 'up' | PASS | - |
| 360 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 361 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 362 | OTI-DC01-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 363 | OTI-DC01-Leaf5B | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 364 | OTI-DC01-Leaf5B | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 365 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 366 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 367 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 368 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 369 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 370 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 371 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 372 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 373 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 374 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 375 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 376 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 377 | OTI-DC01-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 378 | OTI-DC01-Leaf5B | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 379 | OTI-DC01-Leaf5B | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 380 | OTI-DC01-Leaf5B | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 381 | OTI-DC01-Leaf5B | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 382 | OTI-DC01-Leaf5B | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 383 | OTI-DC01-OBM1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 384 | OTI-DC01-OBM1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 385 | OTI-DC01-OBM1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 386 | OTI-DC01-OBM1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 387 | OTI-DC01-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC01-0601-ESX01_idrac = 'up' | PASS | - |
| 388 | OTI-DC01-OBM1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 389 | OTI-DC01-OBM1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 390 | OTI-DC01-OBM1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 391 | OTI-DC01-OBM1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 392 | OTI-DC01-OBM1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 393 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf1 (IP: 10.245.217.3) | PASS | - |
| 394 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf2 (IP: 10.245.217.4) | PASS | - |
| 395 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf3 (IP: 10.245.217.5) | PASS | - |
| 396 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf4 (IP: 10.245.217.6) | PASS | - |
| 397 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5A (IP: 10.245.217.7) | PASS | - |
| 398 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5B (IP: 10.245.217.8) | PASS | - |
| 399 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf1 (IP: 192.168.11.1) | PASS | - |
| 400 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf2 (IP: 192.168.11.5) | PASS | - |
| 401 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf3 (IP: 192.168.11.9) | PASS | - |
| 402 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf4 (IP: 192.168.11.13) | PASS | - |
| 403 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.11.17) | PASS | - |
| 404 | OTI-DC01-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.11.21) | PASS | - |
| 405 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC01-Leaf1 Ethernet55/1 | PASS | - |
| 406 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC01-Leaf2 Ethernet55/1 | PASS | - |
| 407 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC01-Leaf3 Ethernet55/1 | PASS | - |
| 408 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC01-Leaf4 Ethernet55/1 | PASS | - |
| 409 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC01-Leaf5A Ethernet55/1 | PASS | - |
| 410 | OTI-DC01-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC01-Leaf5B Ethernet55/1 | PASS | - |
| 411 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.11.0) - Destination: OTI-DC01-Leaf1 Ethernet55/1 (IP: 192.168.11.1) | PASS | - |
| 412 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.11.4) - Destination: OTI-DC01-Leaf2 Ethernet55/1 (IP: 192.168.11.5) | PASS | - |
| 413 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.11.8) - Destination: OTI-DC01-Leaf3 Ethernet55/1 (IP: 192.168.11.9) | PASS | - |
| 414 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.11.12) - Destination: OTI-DC01-Leaf4 Ethernet55/1 (IP: 192.168.11.13) | PASS | - |
| 415 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.11.16) - Destination: OTI-DC01-Leaf5A Ethernet55/1 (IP: 192.168.11.17) | PASS | - |
| 416 | OTI-DC01-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.11.20) - Destination: OTI-DC01-Leaf5B Ethernet55/1 (IP: 192.168.11.21) | PASS | - |
| 417 | OTI-DC01-Spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 418 | OTI-DC01-Spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 419 | OTI-DC01-Spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 420 | OTI-DC01-Spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 421 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_OTI-DC01-Leaf1_Ethernet55/1 = 'up' | PASS | - |
| 422 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_OTI-DC01-Leaf2_Ethernet55/1 = 'up' | PASS | - |
| 423 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_OTI-DC01-Leaf3_Ethernet55/1 = 'up' | PASS | - |
| 424 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_OTI-DC01-Leaf4_Ethernet55/1 = 'up' | PASS | - |
| 425 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_OTI-DC01-Leaf5A_Ethernet55/1 = 'up' | PASS | - |
| 426 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_OTI-DC01-Leaf5B_Ethernet55/1 = 'up' | PASS | - |
| 427 | OTI-DC01-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 428 | OTI-DC01-Spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 429 | OTI-DC01-Spine1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 94.3% |
| 430 | OTI-DC01-Spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 431 | OTI-DC01-Spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 432 | OTI-DC01-Spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 433 | OTI-DC01-Spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 434 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf1 (IP: 10.245.217.3) | PASS | - |
| 435 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf2 (IP: 10.245.217.4) | PASS | - |
| 436 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf3 (IP: 10.245.217.5) | PASS | - |
| 437 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf4 (IP: 10.245.217.6) | PASS | - |
| 438 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5A (IP: 10.245.217.7) | PASS | - |
| 439 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC01-Leaf5B (IP: 10.245.217.8) | PASS | - |
| 440 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf1 (IP: 192.168.11.3) | PASS | - |
| 441 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf2 (IP: 192.168.11.7) | PASS | - |
| 442 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf3 (IP: 192.168.11.11) | PASS | - |
| 443 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf4 (IP: 192.168.11.15) | PASS | - |
| 444 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.11.19) | PASS | - |
| 445 | OTI-DC01-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.11.23) | PASS | - |
| 446 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC01-Leaf1 Ethernet56/1 | PASS | - |
| 447 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC01-Leaf2 Ethernet56/1 | PASS | - |
| 448 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC01-Leaf3 Ethernet56/1 | PASS | - |
| 449 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC01-Leaf4 Ethernet56/1 | PASS | - |
| 450 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC01-Leaf5A Ethernet56/1 | PASS | - |
| 451 | OTI-DC01-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC01-Leaf5B Ethernet56/1 | PASS | - |
| 452 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.11.2) - Destination: OTI-DC01-Leaf1 Ethernet56/1 (IP: 192.168.11.3) | PASS | - |
| 453 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.11.6) - Destination: OTI-DC01-Leaf2 Ethernet56/1 (IP: 192.168.11.7) | PASS | - |
| 454 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.11.10) - Destination: OTI-DC01-Leaf3 Ethernet56/1 (IP: 192.168.11.11) | PASS | - |
| 455 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.11.14) - Destination: OTI-DC01-Leaf4 Ethernet56/1 (IP: 192.168.11.15) | PASS | - |
| 456 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.11.18) - Destination: OTI-DC01-Leaf5A Ethernet56/1 (IP: 192.168.11.19) | PASS | - |
| 457 | OTI-DC01-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.11.22) - Destination: OTI-DC01-Leaf5B Ethernet56/1 (IP: 192.168.11.23) | PASS | - |
| 458 | OTI-DC01-Spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 459 | OTI-DC01-Spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 460 | OTI-DC01-Spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 461 | OTI-DC01-Spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 462 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_OTI-DC01-Leaf1_Ethernet56/1 = 'up' | PASS | - |
| 463 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_OTI-DC01-Leaf2_Ethernet56/1 = 'up' | PASS | - |
| 464 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_OTI-DC01-Leaf3_Ethernet56/1 = 'up' | PASS | - |
| 465 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_OTI-DC01-Leaf4_Ethernet56/1 = 'up' | PASS | - |
| 466 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_OTI-DC01-Leaf5A_Ethernet56/1 = 'up' | PASS | - |
| 467 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_OTI-DC01-Leaf5B_Ethernet56/1 = 'up' | PASS | - |
| 468 | OTI-DC01-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 469 | OTI-DC01-Spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 470 | OTI-DC01-Spine2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 471 | OTI-DC01-Spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 472 | OTI-DC01-Spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 473 | OTI-DC01-Spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 474 | OTI-DC01-Spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
