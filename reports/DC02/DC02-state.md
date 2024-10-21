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
| 506 | 458 | 12 | 36 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| OTI-DC02-Leaf1 | 64 | 58 | 2 | 4 | Interfaces, System | Hardware |
| OTI-DC02-Leaf2 | 64 | 58 | 2 | 4 | Interfaces, System | Hardware |
| OTI-DC02-Leaf3 | 64 | 58 | 2 | 4 | Interfaces, System | Hardware |
| OTI-DC02-Leaf4 | 64 | 58 | 2 | 4 | Interfaces, System | Hardware |
| OTI-DC02-Leaf5A | 81 | 76 | 1 | 4 | Interfaces | Hardware |
| OTI-DC02-Leaf5B | 81 | 75 | 2 | 4 | Interfaces, System | Hardware |
| OTI-DC02-OBM1 | 8 | 4 | 0 | 4 | - | Hardware |
| OTI-DC02-Spine1 | 40 | 36 | 0 | 4 | - | Hardware |
| OTI-DC02-Spine2 | 40 | 35 | 1 | 4 | System | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 60 | 60 | 0 | 0 |
| Connectivity | 152 | 152 | 0 | 0 |
| Hardware | 36 | 0 | 0 | 36 |
| Interfaces | 56 | 50 | 6 | 0 |
| MLAG | 2 | 2 | 0 | 0 |
| Routing | 164 | 164 | 0 | 0 |
| System | 36 | 30 | 6 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 33 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 61 | OTI-DC02-Leaf1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 84.8% |
| 97 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 125 | OTI-DC02-Leaf2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 83.9% |
| 161 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 189 | OTI-DC02-Leaf3 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 87.5% |
| 225 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 253 | OTI-DC02-Leaf4 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 90.9% |
| 305 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 386 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 415 | OTI-DC02-Leaf5B | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.8% |
| 503 | OTI-DC02-Spine2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 85.7% |

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
| 29 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet1/1 = 'up' | PASS | - |
| 30 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet1/1 = 'up' | PASS | - |
| 31 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 32 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 33 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 34 | OTI-DC02-Leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 35 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 36 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 37 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 38 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 39 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 40 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 41 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 42 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 43 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 44 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 45 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 46 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 47 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 48 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 49 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 50 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 51 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 52 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 53 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 54 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 55 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 56 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 57 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 58 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 59 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 60 | OTI-DC02-Leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 61 | OTI-DC02-Leaf1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 84.8% |
| 62 | OTI-DC02-Leaf1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 63 | OTI-DC02-Leaf1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 64 | OTI-DC02-Leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 65 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 66 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 67 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.4) | PASS | - |
| 68 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.6) | PASS | - |
| 69 | OTI-DC02-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet2/1 | PASS | - |
| 70 | OTI-DC02-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet2/1 | PASS | - |
| 71 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 72 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 73 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 74 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 75 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 76 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 77 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 78 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 79 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 80 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 81 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 82 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 83 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 84 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 85 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 86 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 87 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.5) - Destination: OTI-DC02-Spine1 Ethernet2/1 (IP: 192.168.12.4) | PASS | - |
| 88 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.7) - Destination: OTI-DC02-Spine2 Ethernet2/1 (IP: 192.168.12.6) | PASS | - |
| 89 | OTI-DC02-Leaf2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 90 | OTI-DC02-Leaf2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 91 | OTI-DC02-Leaf2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 92 | OTI-DC02-Leaf2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 93 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet2/1 = 'up' | PASS | - |
| 94 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet2/1 = 'up' | PASS | - |
| 95 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 96 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 97 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 98 | OTI-DC02-Leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 99 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 100 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 101 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 102 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 103 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 104 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 105 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 106 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 107 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 108 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 109 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 110 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 111 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 112 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 113 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 114 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 115 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 116 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 117 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 118 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 119 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 120 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 121 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 122 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 123 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 124 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 125 | OTI-DC02-Leaf2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 83.9% |
| 126 | OTI-DC02-Leaf2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 127 | OTI-DC02-Leaf2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 128 | OTI-DC02-Leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 129 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 130 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 131 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.8) | PASS | - |
| 132 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.10) | PASS | - |
| 133 | OTI-DC02-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet3/1 | PASS | - |
| 134 | OTI-DC02-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet3/1 | PASS | - |
| 135 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 136 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 137 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 138 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 139 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 140 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 141 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 142 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 143 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 144 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 145 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 146 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 147 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 148 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 149 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 150 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 151 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.9) - Destination: OTI-DC02-Spine1 Ethernet3/1 (IP: 192.168.12.8) | PASS | - |
| 152 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.11) - Destination: OTI-DC02-Spine2 Ethernet3/1 (IP: 192.168.12.10) | PASS | - |
| 153 | OTI-DC02-Leaf3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 154 | OTI-DC02-Leaf3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 155 | OTI-DC02-Leaf3 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 156 | OTI-DC02-Leaf3 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 157 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet3/1 = 'up' | PASS | - |
| 158 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet3/1 = 'up' | PASS | - |
| 159 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 160 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 161 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 162 | OTI-DC02-Leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 163 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 164 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 165 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 166 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 167 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 168 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 169 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 170 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 171 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 172 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 173 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 174 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 175 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 176 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 177 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 178 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 179 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 180 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 181 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 182 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 183 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 184 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 185 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 186 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 187 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 188 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 189 | OTI-DC02-Leaf3 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 87.5% |
| 190 | OTI-DC02-Leaf3 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 191 | OTI-DC02-Leaf3 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 192 | OTI-DC02-Leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 193 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 194 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 195 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.12) | PASS | - |
| 196 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.14) | PASS | - |
| 197 | OTI-DC02-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet4/1 | PASS | - |
| 198 | OTI-DC02-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet4/1 | PASS | - |
| 199 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 200 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 201 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 202 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 203 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 204 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 205 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 206 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 207 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 208 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 209 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 210 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 211 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 212 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 213 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 214 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 215 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.13) - Destination: OTI-DC02-Spine1 Ethernet4/1 (IP: 192.168.12.12) | PASS | - |
| 216 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.15) - Destination: OTI-DC02-Spine2 Ethernet4/1 (IP: 192.168.12.14) | PASS | - |
| 217 | OTI-DC02-Leaf4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 218 | OTI-DC02-Leaf4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 219 | OTI-DC02-Leaf4 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 220 | OTI-DC02-Leaf4 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 221 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet4/1 = 'up' | PASS | - |
| 222 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet4/1 = 'up' | PASS | - |
| 223 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 224 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 225 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 226 | OTI-DC02-Leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 227 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 228 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 229 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 230 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 231 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 232 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 233 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 234 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 235 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 236 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 237 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 238 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 239 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 240 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 241 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 242 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 243 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 244 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 245 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 246 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 247 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 248 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 249 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 250 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 251 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 252 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 253 | OTI-DC02-Leaf4 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 90.9% |
| 254 | OTI-DC02-Leaf4 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 255 | OTI-DC02-Leaf4 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 256 | OTI-DC02-Leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 257 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.7 | PASS | - |
| 258 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.8 | PASS | - |
| 259 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 260 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 261 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.7 | PASS | - |
| 262 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.8 | PASS | - |
| 263 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.10.249) | PASS | - |
| 264 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.14.73) | PASS | - |
| 265 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.16) | PASS | - |
| 266 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.18) | PASS | - |
| 267 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC01-Leaf5A Ethernet52/1 | PASS | - |
| 268 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC02-Leaf5B Ethernet53/1 | PASS | - |
| 269 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC02-Leaf5B Ethernet54/1 | PASS | - |
| 270 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet5/1 | PASS | - |
| 271 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet5/1 | PASS | - |
| 272 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 273 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 274 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 275 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 276 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 277 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 278 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 279 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 280 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 281 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 282 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 283 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 284 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 285 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 286 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 287 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 288 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet52/1 (IP: 192.168.10.248) - Destination: OTI-DC01-Leaf5A Ethernet52/1 (IP: 192.168.10.249) | PASS | - |
| 289 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.17) - Destination: OTI-DC02-Spine1 Ethernet5/1 (IP: 192.168.12.16) | PASS | - |
| 290 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.19) - Destination: OTI-DC02-Spine2 Ethernet5/1 (IP: 192.168.12.18) | PASS | - |
| 291 | OTI-DC02-Leaf5A | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 292 | OTI-DC02-Leaf5A | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 293 | OTI-DC02-Leaf5A | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 294 | OTI-DC02-Leaf5A | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 295 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_LINK_TO_OTI-DC01-Leaf5A_Ethernet52/1 = 'up' | PASS | - |
| 296 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_PEER_OTI-DC02-Leaf5B_Ethernet53/1 = 'up' | PASS | - |
| 297 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_PEER_OTI-DC02-Leaf5B_Ethernet54/1 = 'up' | PASS | - |
| 298 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet5/1 = 'up' | PASS | - |
| 299 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet5/1 = 'up' | PASS | - |
| 300 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 301 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 302 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_PEER_OTI-DC02-Leaf5B_Po531 = 'up' | PASS | - |
| 303 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_PEER_L3_PEERING = 'up' | PASS | - |
| 304 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG_PEER = 'up' | PASS | - |
| 305 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 306 | OTI-DC02-Leaf5A | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 307 | OTI-DC02-Leaf5A | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 308 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 309 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 310 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 311 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 312 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 313 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 314 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 315 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 316 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 317 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 318 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 319 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 320 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 321 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 322 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 323 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 324 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 325 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 326 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 327 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 328 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 329 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 330 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 331 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 332 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 333 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 334 | OTI-DC02-Leaf5A | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 335 | OTI-DC02-Leaf5A | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 336 | OTI-DC02-Leaf5A | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 337 | OTI-DC02-Leaf5A | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 338 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.7 | PASS | - |
| 339 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.8 | PASS | - |
| 340 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 341 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 342 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.7 | PASS | - |
| 343 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.8 | PASS | - |
| 344 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.10.250) | PASS | - |
| 345 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.14.72) | PASS | - |
| 346 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.20) | PASS | - |
| 347 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.22) | PASS | - |
| 348 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC01-Leaf5B Ethernet52/1 | PASS | - |
| 349 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC02-Leaf5A Ethernet53/1 | PASS | - |
| 350 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC02-Leaf5A Ethernet54/1 | PASS | - |
| 351 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet6/1 | PASS | - |
| 352 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet6/1 | PASS | - |
| 353 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 354 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 355 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 356 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 357 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 358 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 359 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 360 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 361 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 362 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 363 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 364 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 365 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 366 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 367 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 368 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 369 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet52/1 (IP: 192.168.10.251) - Destination: OTI-DC01-Leaf5B Ethernet52/1 (IP: 192.168.10.250) | PASS | - |
| 370 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.21) - Destination: OTI-DC02-Spine1 Ethernet6/1 (IP: 192.168.12.20) | PASS | - |
| 371 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.23) - Destination: OTI-DC02-Spine2 Ethernet6/1 (IP: 192.168.12.22) | PASS | - |
| 372 | OTI-DC02-Leaf5B | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 373 | OTI-DC02-Leaf5B | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 374 | OTI-DC02-Leaf5B | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 375 | OTI-DC02-Leaf5B | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 376 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_LINK_TO_OTI-DC01-Leaf5B_Ethernet52/1 = 'up' | PASS | - |
| 377 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_PEER_OTI-DC02-Leaf5A_Ethernet53/1 = 'up' | PASS | - |
| 378 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_PEER_OTI-DC02-Leaf5A_Ethernet54/1 = 'up' | PASS | - |
| 379 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_LINK_TO_OTI-DC02-SPINE1_Ethernet6/1 = 'up' | PASS | - |
| 380 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_LINK_TO_OTI-DC02-SPINE2_Ethernet6/1 = 'up' | PASS | - |
| 381 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 382 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VTEP_VXLAN_Tunnel_Source = 'up' | PASS | - |
| 383 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_PEER_OTI-DC02-Leaf5A_Po531 = 'up' | PASS | - |
| 384 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_PEER_L3_PEERING = 'up' | PASS | - |
| 385 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG_PEER = 'up' | PASS | - |
| 386 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | FAIL | The following interface(s) are not in the expected state: ['Vxlan1 is down/down'] |
| 387 | OTI-DC02-Leaf5B | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 388 | OTI-DC02-Leaf5B | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 389 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 390 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 391 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 392 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 393 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 394 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 395 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 396 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 397 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 398 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 399 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 400 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 401 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 402 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 403 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 404 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 405 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 406 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 407 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 408 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 409 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 410 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 411 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 412 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 413 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 414 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 415 | OTI-DC02-Leaf5B | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.8% |
| 416 | OTI-DC02-Leaf5B | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 417 | OTI-DC02-Leaf5B | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 418 | OTI-DC02-Leaf5B | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 419 | OTI-DC02-OBM1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 420 | OTI-DC02-OBM1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 421 | OTI-DC02-OBM1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 422 | OTI-DC02-OBM1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 423 | OTI-DC02-OBM1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 424 | OTI-DC02-OBM1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 425 | OTI-DC02-OBM1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 426 | OTI-DC02-OBM1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 427 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf1 (IP: 10.245.218.3) | PASS | - |
| 428 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf2 (IP: 10.245.218.4) | PASS | - |
| 429 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf3 (IP: 10.245.218.5) | PASS | - |
| 430 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf4 (IP: 10.245.218.6) | PASS | - |
| 431 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5A (IP: 10.245.218.7) | PASS | - |
| 432 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5B (IP: 10.245.218.8) | PASS | - |
| 433 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf1 (IP: 192.168.12.1) | PASS | - |
| 434 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf2 (IP: 192.168.12.5) | PASS | - |
| 435 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf3 (IP: 192.168.12.9) | PASS | - |
| 436 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf4 (IP: 192.168.12.13) | PASS | - |
| 437 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.12.17) | PASS | - |
| 438 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.12.21) | PASS | - |
| 439 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC02-Leaf1 Ethernet55/1 | PASS | - |
| 440 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC02-Leaf2 Ethernet55/1 | PASS | - |
| 441 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC02-Leaf3 Ethernet55/1 | PASS | - |
| 442 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC02-Leaf4 Ethernet55/1 | PASS | - |
| 443 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC02-Leaf5A Ethernet55/1 | PASS | - |
| 444 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC02-Leaf5B Ethernet55/1 | PASS | - |
| 445 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.12.0) - Destination: OTI-DC02-Leaf1 Ethernet55/1 (IP: 192.168.12.1) | PASS | - |
| 446 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.12.4) - Destination: OTI-DC02-Leaf2 Ethernet55/1 (IP: 192.168.12.5) | PASS | - |
| 447 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.12.8) - Destination: OTI-DC02-Leaf3 Ethernet55/1 (IP: 192.168.12.9) | PASS | - |
| 448 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.12.12) - Destination: OTI-DC02-Leaf4 Ethernet55/1 (IP: 192.168.12.13) | PASS | - |
| 449 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.12.16) - Destination: OTI-DC02-Leaf5A Ethernet55/1 (IP: 192.168.12.17) | PASS | - |
| 450 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.12.20) - Destination: OTI-DC02-Leaf5B Ethernet55/1 (IP: 192.168.12.21) | PASS | - |
| 451 | OTI-DC02-Spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 452 | OTI-DC02-Spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 453 | OTI-DC02-Spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 454 | OTI-DC02-Spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 455 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_LINK_TO_OTI-DC02-LEAF1_Ethernet55/1 = 'up' | PASS | - |
| 456 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_LINK_TO_OTI-DC02-LEAF2_Ethernet55/1 = 'up' | PASS | - |
| 457 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_LINK_TO_OTI-DC02-LEAF3_Ethernet55/1 = 'up' | PASS | - |
| 458 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_LINK_TO_OTI-DC02-LEAF4_Ethernet55/1 = 'up' | PASS | - |
| 459 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_LINK_TO_OTI-DC02-LEAF5A_Ethernet55/1 = 'up' | PASS | - |
| 460 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_LINK_TO_OTI-DC02-LEAF5B_Ethernet55/1 = 'up' | PASS | - |
| 461 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 462 | OTI-DC02-Spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 463 | OTI-DC02-Spine1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 464 | OTI-DC02-Spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 465 | OTI-DC02-Spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 466 | OTI-DC02-Spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 467 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf1 (IP: 10.245.218.3) | PASS | - |
| 468 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf2 (IP: 10.245.218.4) | PASS | - |
| 469 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf3 (IP: 10.245.218.5) | PASS | - |
| 470 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf4 (IP: 10.245.218.6) | PASS | - |
| 471 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5A (IP: 10.245.218.7) | PASS | - |
| 472 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5B (IP: 10.245.218.8) | PASS | - |
| 473 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf1 (IP: 192.168.12.3) | PASS | - |
| 474 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf2 (IP: 192.168.12.7) | PASS | - |
| 475 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf3 (IP: 192.168.12.11) | PASS | - |
| 476 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf4 (IP: 192.168.12.15) | PASS | - |
| 477 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.12.19) | PASS | - |
| 478 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.12.23) | PASS | - |
| 479 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC02-Leaf1 Ethernet56/1 | PASS | - |
| 480 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC02-Leaf2 Ethernet56/1 | PASS | - |
| 481 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC02-Leaf3 Ethernet56/1 | PASS | - |
| 482 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC02-Leaf4 Ethernet56/1 | PASS | - |
| 483 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC02-Leaf5A Ethernet56/1 | PASS | - |
| 484 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC02-Leaf5B Ethernet56/1 | PASS | - |
| 485 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.12.2) - Destination: OTI-DC02-Leaf1 Ethernet56/1 (IP: 192.168.12.3) | PASS | - |
| 486 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.12.6) - Destination: OTI-DC02-Leaf2 Ethernet56/1 (IP: 192.168.12.7) | PASS | - |
| 487 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.12.10) - Destination: OTI-DC02-Leaf3 Ethernet56/1 (IP: 192.168.12.11) | PASS | - |
| 488 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.12.14) - Destination: OTI-DC02-Leaf4 Ethernet56/1 (IP: 192.168.12.15) | PASS | - |
| 489 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.12.18) - Destination: OTI-DC02-Leaf5A Ethernet56/1 (IP: 192.168.12.19) | PASS | - |
| 490 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.12.22) - Destination: OTI-DC02-Leaf5B Ethernet56/1 (IP: 192.168.12.23) | PASS | - |
| 491 | OTI-DC02-Spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 492 | OTI-DC02-Spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 493 | OTI-DC02-Spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 494 | OTI-DC02-Spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 495 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_LINK_TO_OTI-DC02-LEAF1_Ethernet56/1 = 'up' | PASS | - |
| 496 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_LINK_TO_OTI-DC02-LEAF2_Ethernet56/1 = 'up' | PASS | - |
| 497 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_LINK_TO_OTI-DC02-LEAF3_Ethernet56/1 = 'up' | PASS | - |
| 498 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_LINK_TO_OTI-DC02-LEAF4_Ethernet56/1 = 'up' | PASS | - |
| 499 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_LINK_TO_OTI-DC02-LEAF5A_Ethernet56/1 = 'up' | PASS | - |
| 500 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_LINK_TO_OTI-DC02-LEAF5B_Ethernet56/1 = 'up' | PASS | - |
| 501 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - EVPN_Overlay_Peering = 'up' | PASS | - |
| 502 | OTI-DC02-Spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 503 | OTI-DC02-Spine2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 85.7% |
| 504 | OTI-DC02-Spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 505 | OTI-DC02-Spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 506 | OTI-DC02-Spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
