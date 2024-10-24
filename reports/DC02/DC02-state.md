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
| 754 | 706 | 12 | 36 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| OTI-DC02-Leaf1 | 114 | 109 | 1 | 4 | Interfaces | Hardware |
| OTI-DC02-Leaf2 | 114 | 108 | 2 | 4 | Interfaces, System | Hardware |
| OTI-DC02-Leaf3 | 114 | 107 | 3 | 4 | Interfaces | Hardware |
| OTI-DC02-Leaf4 | 114 | 106 | 4 | 4 | Interfaces, System | Hardware |
| OTI-DC02-Leaf5A | 99 | 94 | 1 | 4 | System | Hardware |
| OTI-DC02-Leaf5B | 99 | 95 | 0 | 4 | - | Hardware |
| OTI-DC02-OBM1 | 18 | 14 | 0 | 4 | - | Hardware |
| OTI-DC02-Spine1 | 41 | 36 | 1 | 4 | System | Hardware |
| OTI-DC02-Spine2 | 41 | 37 | 0 | 4 | - | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 60 | 60 | 0 | 0 |
| Connectivity | 152 | 152 | 0 | 0 |
| Hardware | 36 | 0 | 0 | 36 |
| Interfaces | 295 | 287 | 8 | 0 |
| MLAG | 2 | 2 | 0 | 0 |
| Routing | 164 | 164 | 0 | 0 |
| System | 45 | 41 | 4 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 46 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 160 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 224 | OTI-DC02-Leaf2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.1% |
| 274 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 275 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - SERVER_DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 279 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |
| 388 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 389 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - SERVER_DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 393 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |
| 452 | OTI-DC02-Leaf4 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 94.1% |
| 551 | OTI-DC02-Leaf5A | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 96.9% |
| 709 | OTI-DC02-Spine1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 80.0% |

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
| 29 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC02-0901-ESX01_Onboard_NIC_1 = 'up' | PASS | - |
| 30 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - SERVER_DC02-0901-ESX02_Onboard_NIC_1 = 'up' | PASS | - |
| 31 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - SERVER_DC02-0901-SRVA_Port_0 = 'up' | PASS | - |
| 32 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - SERVER_DC02-0901-ESX03_Onboard_NIC_1 = 'up' | PASS | - |
| 33 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - SERVER_DC02-0901-ESX04_Onboard_NIC_1 = 'up' | PASS | - |
| 34 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet47 - SERVER_DC02-0901-ESX02_Onboard_NIC_2 = 'up' | PASS | - |
| 35 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet48 - SERVER_DC02-0901-ESX01_Onboard_NIC_2 = 'up' | PASS | - |
| 36 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_DC02-0901-ESX05_Onboard_NIC_1 = 'up' | PASS | - |
| 37 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC02-Spine1_Ethernet1/1 = 'up' | PASS | - |
| 38 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC02-Spine2_Ethernet1/1 = 'up' | PASS | - |
| 39 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - SERVER_DC02-0901-ESX06_Onboard_NIC_1 = 'up' | PASS | - |
| 40 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 41 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 42 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 43 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 44 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC02-0901-ESX01 = 'up' | PASS | - |
| 45 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - SERVER_DC02-0901-ESX02 = 'up' | PASS | - |
| 46 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 47 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - SERVER_DC02-0901-ESX03 = 'up' | PASS | - |
| 48 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - SERVER_DC02-0901-ESX04 = 'up' | PASS | - |
| 49 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel47 - SERVER_DC02-0901-ESX02 = 'up' | PASS | - |
| 50 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel48 - SERVER_DC02-0901-ESX01 = 'up' | PASS | - |
| 51 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_DC02-0901-ESX05 = 'up' | PASS | - |
| 52 | OTI-DC02-Leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel6 - SERVER_DC02-0901-ESX06 = 'up' | PASS | - |
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
| 110 | OTI-DC02-Leaf1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 111 | OTI-DC02-Leaf1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 112 | OTI-DC02-Leaf1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 113 | OTI-DC02-Leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 114 | OTI-DC02-Leaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 115 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 116 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 117 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.4) | PASS | - |
| 118 | OTI-DC02-Leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.6) | PASS | - |
| 119 | OTI-DC02-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet2/1 | PASS | - |
| 120 | OTI-DC02-Leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet2/1 | PASS | - |
| 121 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 122 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 123 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 124 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 125 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 126 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 127 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 128 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 129 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 130 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 131 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 132 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 133 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 134 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 135 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 136 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.4) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 137 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.5) - Destination: OTI-DC02-Spine1 Ethernet2/1 (IP: 192.168.12.4) | PASS | - |
| 138 | OTI-DC02-Leaf2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.7) - Destination: OTI-DC02-Spine2 Ethernet2/1 (IP: 192.168.12.6) | PASS | - |
| 139 | OTI-DC02-Leaf2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 140 | OTI-DC02-Leaf2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 141 | OTI-DC02-Leaf2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 142 | OTI-DC02-Leaf2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 143 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC02-0901-ESX01_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 144 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - SERVER_DC02-0901-ESX02_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 145 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - SERVER_DC02-0901-SRVA_Port_1 = 'up' | PASS | - |
| 146 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - SERVER_DC02-0901-ESX03_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 147 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - SERVER_DC02-0901-ESX04_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 148 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet47 - SERVER_DC02-0901-ESX02_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 149 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet48 - SERVER_DC02-0901-ESX01_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 150 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_DC02-0901-ESX05_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 151 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC02-Spine1_Ethernet2/1 = 'up' | PASS | - |
| 152 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC02-Spine2_Ethernet2/1 = 'up' | PASS | - |
| 153 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - SERVER_DC02-0901-ESX06_PCI_slot_1_Port_1 = 'up' | PASS | - |
| 154 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 155 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 156 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 157 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 158 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC02-0901-ESX01 = 'up' | PASS | - |
| 159 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - SERVER_DC02-0901-ESX02 = 'up' | PASS | - |
| 160 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 161 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - SERVER_DC02-0901-ESX03 = 'up' | PASS | - |
| 162 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - SERVER_DC02-0901-ESX04 = 'up' | PASS | - |
| 163 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel47 - SERVER_DC02-0901-ESX02 = 'up' | PASS | - |
| 164 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel48 - SERVER_DC02-0901-ESX01 = 'up' | PASS | - |
| 165 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_DC02-0901-ESX05 = 'up' | PASS | - |
| 166 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel6 - SERVER_DC02-0901-ESX06 = 'up' | PASS | - |
| 167 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 168 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 169 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 170 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 171 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 172 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 173 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 174 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 175 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 176 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 177 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 178 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 179 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 180 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 181 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 182 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 183 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 184 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 185 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 186 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 187 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 188 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 189 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 190 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 191 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 192 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 193 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 194 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 195 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 196 | OTI-DC02-Leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 197 | OTI-DC02-Leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 198 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 199 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 200 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 201 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 202 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 203 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 204 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 205 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 206 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 207 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 208 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 209 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 210 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 211 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 212 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 213 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 214 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 215 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 216 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 217 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 218 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 219 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 220 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 221 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 222 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 223 | OTI-DC02-Leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 224 | OTI-DC02-Leaf2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 78.1% |
| 225 | OTI-DC02-Leaf2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 226 | OTI-DC02-Leaf2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 227 | OTI-DC02-Leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 228 | OTI-DC02-Leaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 229 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 230 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 231 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.8) | PASS | - |
| 232 | OTI-DC02-Leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.10) | PASS | - |
| 233 | OTI-DC02-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet3/1 | PASS | - |
| 234 | OTI-DC02-Leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet3/1 | PASS | - |
| 235 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 236 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 237 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 238 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 239 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 240 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 241 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 242 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 243 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 244 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 245 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 246 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 247 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 248 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 249 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 250 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.5) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 251 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.9) - Destination: OTI-DC02-Spine1 Ethernet3/1 (IP: 192.168.12.8) | PASS | - |
| 252 | OTI-DC02-Leaf3 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.11) - Destination: OTI-DC02-Spine2 Ethernet3/1 (IP: 192.168.12.10) | PASS | - |
| 253 | OTI-DC02-Leaf3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 254 | OTI-DC02-Leaf3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 255 | OTI-DC02-Leaf3 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 256 | OTI-DC02-Leaf3 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 257 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC02-0901-ESX01_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 258 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - SERVER_DC02-0901-ESX02_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 259 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - SERVER_DC02-0901-SRVB_Port_0 = 'up' | PASS | - |
| 260 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet26 - SERVER_DC02-0901-SRVC_Port_0 = 'up' | PASS | - |
| 261 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - SERVER_DC02-0901-ESX03_Onboard_NIC_2 = 'up' | PASS | - |
| 262 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - SERVER_DC02-0901-ESX05_Onboard_NIC_2 = 'up' | PASS | - |
| 263 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - SERVER_DC02-0901-ESX03_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 264 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_DC02-0901-SRVA_Port_2 = 'up' | PASS | - |
| 265 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - SERVER_DC02-0901-ESX04_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 266 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC02-Spine1_Ethernet3/1 = 'up' | PASS | - |
| 267 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC02-Spine2_Ethernet3/1 = 'up' | PASS | - |
| 268 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 269 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 270 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 271 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 272 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC02-0901-ESX01 = 'up' | PASS | - |
| 273 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - SERVER_DC02-0901-ESX02 = 'up' | PASS | - |
| 274 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 275 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - SERVER_DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 276 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - SERVER_DC02-0901-ESX03 = 'up' | PASS | - |
| 277 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - SERVER_DC02-0901-ESX05 = 'up' | PASS | - |
| 278 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - SERVER_DC02-0901-ESX03 = 'up' | PASS | - |
| 279 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |
| 280 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - SERVER_DC02-0901-ESX04 = 'up' | PASS | - |
| 281 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 282 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 283 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 284 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 285 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 286 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 287 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 288 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 289 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 290 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 291 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 292 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 293 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 294 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 295 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 296 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 297 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 298 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 299 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 300 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 301 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 302 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 303 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 304 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 305 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 306 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 307 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 308 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 309 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 310 | OTI-DC02-Leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 311 | OTI-DC02-Leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 312 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 313 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 314 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 315 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 316 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 317 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 318 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 319 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 320 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 321 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 322 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 323 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 324 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 325 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 326 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 327 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 328 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 329 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 330 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 331 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 332 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 333 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 334 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 335 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 336 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 337 | OTI-DC02-Leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 338 | OTI-DC02-Leaf3 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 339 | OTI-DC02-Leaf3 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 340 | OTI-DC02-Leaf3 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 341 | OTI-DC02-Leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 342 | OTI-DC02-Leaf3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 343 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 344 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 345 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.12) | PASS | - |
| 346 | OTI-DC02-Leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.14) | PASS | - |
| 347 | OTI-DC02-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet4/1 | PASS | - |
| 348 | OTI-DC02-Leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet4/1 | PASS | - |
| 349 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 350 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 351 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 352 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 353 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 354 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 355 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 356 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 357 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 358 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 359 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 360 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 361 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 362 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 363 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 364 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.6) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 365 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.13) - Destination: OTI-DC02-Spine1 Ethernet4/1 (IP: 192.168.12.12) | PASS | - |
| 366 | OTI-DC02-Leaf4 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.15) - Destination: OTI-DC02-Spine2 Ethernet4/1 (IP: 192.168.12.14) | PASS | - |
| 367 | OTI-DC02-Leaf4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 368 | OTI-DC02-Leaf4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 369 | OTI-DC02-Leaf4 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 370 | OTI-DC02-Leaf4 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 371 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC02-0901-ESX01_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 372 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - SERVER_DC02-0901-ESX02_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 373 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet25 - SERVER_DC02-0901-SRVB_Port_1 = 'up' | PASS | - |
| 374 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet26 - SERVER_DC02-0901-SRVC_Port_1 = 'up' | PASS | - |
| 375 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - SERVER_DC02-0901-ESX03_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 376 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - SERVER_DC02-0901-ESX05_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 377 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - SERVER_DC02-0901-ESX03_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 378 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_DC02-0901-SRVA_Port_3 = 'up' | PASS | - |
| 379 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - SERVER_DC02-0901-ESX04_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 380 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC02-Spine1_Ethernet4/1 = 'up' | PASS | - |
| 381 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC02-Spine2_Ethernet4/1 = 'up' | PASS | - |
| 382 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 383 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 384 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 385 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - DIAG_VRF_Development = 'up' | PASS | - |
| 386 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC02-0901-ESX01 = 'up' | PASS | - |
| 387 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - SERVER_DC02-0901-ESX02 = 'up' | PASS | - |
| 388 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel25 - SERVER_DC02-0901-SRVB = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel25 is down/lowerLayerDown'] |
| 389 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel26 - SERVER_DC02-0901-SRVC = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel26 is down/lowerLayerDown'] |
| 390 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - SERVER_DC02-0901-ESX03 = 'up' | PASS | - |
| 391 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel4 - SERVER_DC02-0901-ESX05 = 'up' | PASS | - |
| 392 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - SERVER_DC02-0901-ESX03 = 'up' | PASS | - |
| 393 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_DC02-0901-SRVA = 'up' | FAIL | The following interface(s) are not in the expected state: ['Port-Channel5 is down/lowerLayerDown'] |
| 394 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - SERVER_DC02-0901-ESX04 = 'up' | PASS | - |
| 395 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan100 - Compute = 'up' | PASS | - |
| 396 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1000 - SRVR_FARM_BLADE = 'up' | PASS | - |
| 397 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan101 - Data = 'up' | PASS | - |
| 398 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 399 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 400 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 401 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1201 - UCP_MGMT_1 = 'up' | PASS | - |
| 402 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1202 - UCP_MGMT_2 = 'up' | PASS | - |
| 403 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2000 - Data_Prod = 'up' | PASS | - |
| 404 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan201 - VMOTION_A = 'up' | PASS | - |
| 405 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan202 - VXRAIL = 'up' | PASS | - |
| 406 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | PASS | - |
| 407 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | PASS | - |
| 408 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2500 - Scada_Dev = 'up' | PASS | - |
| 409 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2821 - Users_Dev = 'up' | PASS | - |
| 410 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2822 - Voice_Dev = 'up' | PASS | - |
| 411 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2833 - Broadcast1 = 'up' | PASS | - |
| 412 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan2834 - Broadcast2 = 'up' | PASS | - |
| 413 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3434 - VM_Servers = 'up' | PASS | - |
| 414 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3911 - SCADA_PROD = 'up' | PASS | - |
| 415 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan400 - VMWARE_REPL = 'up' | PASS | - |
| 416 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan500 - Compute_Backup = 'up' | PASS | - |
| 417 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan501 - Data_Backup = 'up' | PASS | - |
| 418 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan55 - HYPER_PROD = 'up' | PASS | - |
| 419 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan821 - SAN_Disk = 'up' | PASS | - |
| 420 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 421 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 422 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 423 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 424 | OTI-DC02-Leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 425 | OTI-DC02-Leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 426 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 427 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 428 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 429 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 430 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 431 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 432 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 433 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 434 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 435 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 436 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 437 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 438 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 439 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 440 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 441 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 442 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 443 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 444 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 445 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 446 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 447 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 448 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 449 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 450 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 451 | OTI-DC02-Leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 452 | OTI-DC02-Leaf4 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 94.1% |
| 453 | OTI-DC02-Leaf4 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 454 | OTI-DC02-Leaf4 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 455 | OTI-DC02-Leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 456 | OTI-DC02-Leaf4 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 457 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.7 | PASS | - |
| 458 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.8 | PASS | - |
| 459 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 460 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 461 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.7 | PASS | - |
| 462 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.8 | PASS | - |
| 463 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5A (IP: 192.168.10.248) | PASS | - |
| 464 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.14.73) | PASS | - |
| 465 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.16) | PASS | - |
| 466 | OTI-DC02-Leaf5A | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.18) | PASS | - |
| 467 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC01-Leaf5A Ethernet52/1 | PASS | - |
| 468 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC02-Leaf5B Ethernet53/1 | PASS | - |
| 469 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC02-Leaf5B Ethernet54/1 | PASS | - |
| 470 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet5/1 | PASS | - |
| 471 | OTI-DC02-Leaf5A | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet5/1 | PASS | - |
| 472 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 473 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 474 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 475 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 476 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 477 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 478 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 479 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 480 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 481 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 482 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 483 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 484 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 485 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 486 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 487 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.7) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 488 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet52/1 (IP: 192.168.10.249) - Destination: OTI-DC01-Leaf5A Ethernet52/1 (IP: 192.168.10.248) | PASS | - |
| 489 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.17) - Destination: OTI-DC02-Spine1 Ethernet5/1 (IP: 192.168.12.16) | PASS | - |
| 490 | OTI-DC02-Leaf5A | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.19) - Destination: OTI-DC02-Spine2 Ethernet5/1 (IP: 192.168.12.18) | PASS | - |
| 491 | OTI-DC02-Leaf5A | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 492 | OTI-DC02-Leaf5A | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 493 | OTI-DC02-Leaf5A | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 494 | OTI-DC02-Leaf5A | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 495 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC02-0901-ESX04_Onboard_NIC_2 = 'up' | PASS | - |
| 496 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - SERVER_DC02-0901-ESX06_Onboard_NIC_2 = 'up' | PASS | - |
| 497 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - SERVER_DC02-0901-ESX05_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 498 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - SERVER_DC02-0901-ESX06_PCI_slot_1_Port_2 = 'up' | PASS | - |
| 499 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_OTI-DC01-Leaf5A_Ethernet52/1 = 'up' | PASS | - |
| 500 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_OTI-DC02-Leaf5B_Ethernet53/1 = 'up' | PASS | - |
| 501 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_OTI-DC02-Leaf5B_Ethernet54/1 = 'up' | PASS | - |
| 502 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC02-Spine1_Ethernet5/1 = 'up' | PASS | - |
| 503 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC02-Spine2_Ethernet5/1 = 'up' | PASS | - |
| 504 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 505 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 506 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 507 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC02-0901-ESX04 = 'up' | PASS | - |
| 508 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - SERVER_DC02-0901-ESX06 = 'up' | PASS | - |
| 509 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - SERVER_DC02-0901-ESX05 = 'up' | PASS | - |
| 510 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - SERVER_DC02-0901-ESX06 = 'up' | PASS | - |
| 511 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_OTI-DC02-Leaf5B_Port-Channel531 = 'up' | PASS | - |
| 512 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 513 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 514 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 515 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_Production = 'up' | PASS | - |
| 516 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 517 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 518 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 519 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 520 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 521 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 522 | OTI-DC02-Leaf5A | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 523 | OTI-DC02-Leaf5A | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 524 | OTI-DC02-Leaf5A | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 525 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 526 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 527 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 528 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 529 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 530 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 531 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 532 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 533 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 534 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 535 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 536 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 537 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 538 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 539 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 540 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 541 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 542 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 543 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 544 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 545 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 546 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 547 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 548 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 549 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 550 | OTI-DC02-Leaf5A | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 551 | OTI-DC02-Leaf5A | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 96.9% |
| 552 | OTI-DC02-Leaf5A | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 553 | OTI-DC02-Leaf5A | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 554 | OTI-DC02-Leaf5A | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 555 | OTI-DC02-Leaf5A | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 556 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.7 | PASS | - |
| 557 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.245.217.8 | PASS | - |
| 558 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine1 (IP: 10.245.218.1) | PASS | - |
| 559 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Spine2 (IP: 10.245.218.2) | PASS | - |
| 560 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.7 | PASS | - |
| 561 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: 10.245.217.8 | PASS | - |
| 562 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC01-Leaf5B (IP: 192.168.10.250) | PASS | - |
| 563 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.14.72) | PASS | - |
| 564 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine1 (IP: 192.168.12.20) | PASS | - |
| 565 | OTI-DC02-Leaf5B | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Spine2 (IP: 192.168.12.22) | PASS | - |
| 566 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet52/1 - Remote: OTI-DC01-Leaf5B Ethernet52/1 | PASS | - |
| 567 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet53/1 - Remote: OTI-DC02-Leaf5A Ethernet53/1 | PASS | - |
| 568 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet54/1 - Remote: OTI-DC02-Leaf5A Ethernet54/1 | PASS | - |
| 569 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet55/1 - Remote: OTI-DC02-Spine1 Ethernet6/1 | PASS | - |
| 570 | OTI-DC02-Leaf5B | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet56/1 - Remote: OTI-DC02-Spine2 Ethernet6/1 | PASS | - |
| 571 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf1 Loopback0 (IP: 10.245.217.3) | PASS | - |
| 572 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf2 Loopback0 (IP: 10.245.217.4) | PASS | - |
| 573 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf3 Loopback0 (IP: 10.245.217.5) | PASS | - |
| 574 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf4 Loopback0 (IP: 10.245.217.6) | PASS | - |
| 575 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf5A Loopback0 (IP: 10.245.217.7) | PASS | - |
| 576 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Leaf5B Loopback0 (IP: 10.245.217.8) | PASS | - |
| 577 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Spine1 Loopback0 (IP: 10.245.217.1) | PASS | - |
| 578 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC01-Spine2 Loopback0 (IP: 10.245.217.2) | PASS | - |
| 579 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf1 Loopback0 (IP: 10.245.218.3) | PASS | - |
| 580 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf2 Loopback0 (IP: 10.245.218.4) | PASS | - |
| 581 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf3 Loopback0 (IP: 10.245.218.5) | PASS | - |
| 582 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf4 Loopback0 (IP: 10.245.218.6) | PASS | - |
| 583 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf5A Loopback0 (IP: 10.245.218.7) | PASS | - |
| 584 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Leaf5B Loopback0 (IP: 10.245.218.8) | PASS | - |
| 585 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Spine1 Loopback0 (IP: 10.245.218.1) | PASS | - |
| 586 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.245.218.8) - Destination: OTI-DC02-Spine2 Loopback0 (IP: 10.245.218.2) | PASS | - |
| 587 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet52/1 (IP: 192.168.10.251) - Destination: OTI-DC01-Leaf5B Ethernet52/1 (IP: 192.168.10.250) | PASS | - |
| 588 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet55/1 (IP: 192.168.12.21) - Destination: OTI-DC02-Spine1 Ethernet6/1 (IP: 192.168.12.20) | PASS | - |
| 589 | OTI-DC02-Leaf5B | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet56/1 (IP: 192.168.12.23) - Destination: OTI-DC02-Spine2 Ethernet6/1 (IP: 192.168.12.22) | PASS | - |
| 590 | OTI-DC02-Leaf5B | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 591 | OTI-DC02-Leaf5B | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 592 | OTI-DC02-Leaf5B | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 593 | OTI-DC02-Leaf5B | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 594 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC02-0901-ESX04_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 595 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - SERVER_DC02-0901-ESX06_PCI_slot_2_Port_2 = 'up' | PASS | - |
| 596 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet49/1 - SERVER_DC02-0901-ESX05_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 597 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet50/1 - SERVER_DC02-0901-ESX06_PCI_slot_2_Port_1 = 'up' | PASS | - |
| 598 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet52/1 - P2P_OTI-DC01-Leaf5B_Ethernet52/1 = 'up' | PASS | - |
| 599 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet53/1 - MLAG_OTI-DC02-Leaf5A_Ethernet53/1 = 'up' | PASS | - |
| 600 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet54/1 - MLAG_OTI-DC02-Leaf5A_Ethernet54/1 = 'up' | PASS | - |
| 601 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet55/1 - P2P_OTI-DC02-Spine1_Ethernet6/1 = 'up' | PASS | - |
| 602 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet56/1 - P2P_OTI-DC02-Spine2_Ethernet6/1 = 'up' | PASS | - |
| 603 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 604 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 605 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - DIAG_VRF_Production = 'up' | PASS | - |
| 606 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - SERVER_DC02-0901-ESX04 = 'up' | PASS | - |
| 607 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel2 - SERVER_DC02-0901-ESX06 = 'up' | PASS | - |
| 608 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel491 - SERVER_DC02-0901-ESX05 = 'up' | PASS | - |
| 609 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel501 - SERVER_DC02-0901-ESX06 = 'up' | PASS | - |
| 610 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel531 - MLAG_OTI-DC02-Leaf5A_Port-Channel531 = 'up' | PASS | - |
| 611 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1100 - SRVR_FARM_BLADE_0 = 'up' | PASS | - |
| 612 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1101 - SRVR_FARM_BLADE_1 = 'up' | PASS | - |
| 613 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan1102 - SRVR_FARM_BLADE_2 = 'up' | PASS | - |
| 614 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_Production = 'up' | PASS | - |
| 615 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 616 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 617 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan887 - NOCB_WORKLOAD1 = 'up' | PASS | - |
| 618 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan888 - NOCB_WORKLOAD2 = 'up' | PASS | - |
| 619 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan899 - NAS = 'up' | PASS | - |
| 620 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan999 - BWS = 'up' | PASS | - |
| 621 | OTI-DC02-Leaf5B | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | PASS | - |
| 622 | OTI-DC02-Leaf5B | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 623 | OTI-DC02-Leaf5B | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 624 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.1 - Peer: OTI-DC01-Spine1 | PASS | - |
| 625 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.2 - Peer: OTI-DC01-Spine2 | PASS | - |
| 626 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.3 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 627 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.35 - Peer: OTI-DC01-Leaf1 | PASS | - |
| 628 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.36 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 629 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.37 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 630 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.38 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 631 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.39 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 632 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.4 - Peer: OTI-DC01-Leaf2 | PASS | - |
| 633 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.5 - Peer: OTI-DC01-Leaf3 | PASS | - |
| 634 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.6 - Peer: OTI-DC01-Leaf4 | PASS | - |
| 635 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.7 - Peer: OTI-DC01-Leaf5A | PASS | - |
| 636 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.217.8 - Peer: OTI-DC01-Leaf5B | PASS | - |
| 637 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.1 - Peer: OTI-DC02-Spine1 | PASS | - |
| 638 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.2 - Peer: OTI-DC02-Spine2 | PASS | - |
| 639 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.3 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 640 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.35 - Peer: OTI-DC02-Leaf1 | PASS | - |
| 641 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.36 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 642 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.37 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 643 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.38 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 644 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.39 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 645 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.4 - Peer: OTI-DC02-Leaf2 | PASS | - |
| 646 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.5 - Peer: OTI-DC02-Leaf3 | PASS | - |
| 647 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.6 - Peer: OTI-DC02-Leaf4 | PASS | - |
| 648 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.7 - Peer: OTI-DC02-Leaf5A | PASS | - |
| 649 | OTI-DC02-Leaf5B | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.245.218.8 - Peer: OTI-DC02-Leaf5B | PASS | - |
| 650 | OTI-DC02-Leaf5B | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 651 | OTI-DC02-Leaf5B | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 652 | OTI-DC02-Leaf5B | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 653 | OTI-DC02-Leaf5B | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 654 | OTI-DC02-Leaf5B | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 655 | OTI-DC02-OBM1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 656 | OTI-DC02-OBM1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 657 | OTI-DC02-OBM1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 658 | OTI-DC02-OBM1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 659 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - SERVER_DC02-0901-ESX01_idrac = 'up' | PASS | - |
| 660 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - SERVER_DC02-0901-ESX02_idrac = 'up' | PASS | - |
| 661 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - SERVER_DC02-0901-ESX03_idrac = 'up' | PASS | - |
| 662 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - SERVER_DC02-0901-ESX04_idrac = 'up' | PASS | - |
| 663 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_DC02-0901-ESX05_idrac = 'up' | PASS | - |
| 664 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - SERVER_DC02-0901-ESX06_idrac = 'up' | PASS | - |
| 665 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet7 - SERVER_DC02-0901-SRVA_iLo = 'up' | PASS | - |
| 666 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - SERVER_DC02-0901-SRVB_iLo = 'up' | PASS | - |
| 667 | OTI-DC02-OBM1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet9 - SERVER_DC02-0901-SRVC_iLo = 'up' | PASS | - |
| 668 | OTI-DC02-OBM1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 669 | OTI-DC02-OBM1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 670 | OTI-DC02-OBM1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 671 | OTI-DC02-OBM1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 672 | OTI-DC02-OBM1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 673 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf1 (IP: 10.245.218.3) | PASS | - |
| 674 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf2 (IP: 10.245.218.4) | PASS | - |
| 675 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf3 (IP: 10.245.218.5) | PASS | - |
| 676 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf4 (IP: 10.245.218.6) | PASS | - |
| 677 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5A (IP: 10.245.218.7) | PASS | - |
| 678 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5B (IP: 10.245.218.8) | PASS | - |
| 679 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf1 (IP: 192.168.12.1) | PASS | - |
| 680 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf2 (IP: 192.168.12.5) | PASS | - |
| 681 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf3 (IP: 192.168.12.9) | PASS | - |
| 682 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf4 (IP: 192.168.12.13) | PASS | - |
| 683 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.12.17) | PASS | - |
| 684 | OTI-DC02-Spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.12.21) | PASS | - |
| 685 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC02-Leaf1 Ethernet55/1 | PASS | - |
| 686 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC02-Leaf2 Ethernet55/1 | PASS | - |
| 687 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC02-Leaf3 Ethernet55/1 | PASS | - |
| 688 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC02-Leaf4 Ethernet55/1 | PASS | - |
| 689 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC02-Leaf5A Ethernet55/1 | PASS | - |
| 690 | OTI-DC02-Spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC02-Leaf5B Ethernet55/1 | PASS | - |
| 691 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.12.0) - Destination: OTI-DC02-Leaf1 Ethernet55/1 (IP: 192.168.12.1) | PASS | - |
| 692 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.12.4) - Destination: OTI-DC02-Leaf2 Ethernet55/1 (IP: 192.168.12.5) | PASS | - |
| 693 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.12.8) - Destination: OTI-DC02-Leaf3 Ethernet55/1 (IP: 192.168.12.9) | PASS | - |
| 694 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.12.12) - Destination: OTI-DC02-Leaf4 Ethernet55/1 (IP: 192.168.12.13) | PASS | - |
| 695 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.12.16) - Destination: OTI-DC02-Leaf5A Ethernet55/1 (IP: 192.168.12.17) | PASS | - |
| 696 | OTI-DC02-Spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.12.20) - Destination: OTI-DC02-Leaf5B Ethernet55/1 (IP: 192.168.12.21) | PASS | - |
| 697 | OTI-DC02-Spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 698 | OTI-DC02-Spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 699 | OTI-DC02-Spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 700 | OTI-DC02-Spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 701 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_OTI-DC02-Leaf1_Ethernet55/1 = 'up' | PASS | - |
| 702 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_OTI-DC02-Leaf2_Ethernet55/1 = 'up' | PASS | - |
| 703 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_OTI-DC02-Leaf3_Ethernet55/1 = 'up' | PASS | - |
| 704 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_OTI-DC02-Leaf4_Ethernet55/1 = 'up' | PASS | - |
| 705 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_OTI-DC02-Leaf5A_Ethernet55/1 = 'up' | PASS | - |
| 706 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_OTI-DC02-Leaf5B_Ethernet55/1 = 'up' | PASS | - |
| 707 | OTI-DC02-Spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 708 | OTI-DC02-Spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 709 | OTI-DC02-Spine1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | FAIL | Device has reported a high CPU utilization: 80.0% |
| 710 | OTI-DC02-Spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 711 | OTI-DC02-Spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 712 | OTI-DC02-Spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 713 | OTI-DC02-Spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 714 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf1 (IP: 10.245.218.3) | PASS | - |
| 715 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf2 (IP: 10.245.218.4) | PASS | - |
| 716 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf3 (IP: 10.245.218.5) | PASS | - |
| 717 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf4 (IP: 10.245.218.6) | PASS | - |
| 718 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5A (IP: 10.245.218.7) | PASS | - |
| 719 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: OTI-DC02-Leaf5B (IP: 10.245.218.8) | PASS | - |
| 720 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf1 (IP: 192.168.12.3) | PASS | - |
| 721 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf2 (IP: 192.168.12.7) | PASS | - |
| 722 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf3 (IP: 192.168.12.11) | PASS | - |
| 723 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf4 (IP: 192.168.12.15) | PASS | - |
| 724 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5A (IP: 192.168.12.19) | PASS | - |
| 725 | OTI-DC02-Spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: OTI-DC02-Leaf5B (IP: 192.168.12.23) | PASS | - |
| 726 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1/1 - Remote: OTI-DC02-Leaf1 Ethernet56/1 | PASS | - |
| 727 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2/1 - Remote: OTI-DC02-Leaf2 Ethernet56/1 | PASS | - |
| 728 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3/1 - Remote: OTI-DC02-Leaf3 Ethernet56/1 | PASS | - |
| 729 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4/1 - Remote: OTI-DC02-Leaf4 Ethernet56/1 | PASS | - |
| 730 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5/1 - Remote: OTI-DC02-Leaf5A Ethernet56/1 | PASS | - |
| 731 | OTI-DC02-Spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6/1 - Remote: OTI-DC02-Leaf5B Ethernet56/1 | PASS | - |
| 732 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1/1 (IP: 192.168.12.2) - Destination: OTI-DC02-Leaf1 Ethernet56/1 (IP: 192.168.12.3) | PASS | - |
| 733 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2/1 (IP: 192.168.12.6) - Destination: OTI-DC02-Leaf2 Ethernet56/1 (IP: 192.168.12.7) | PASS | - |
| 734 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3/1 (IP: 192.168.12.10) - Destination: OTI-DC02-Leaf3 Ethernet56/1 (IP: 192.168.12.11) | PASS | - |
| 735 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4/1 (IP: 192.168.12.14) - Destination: OTI-DC02-Leaf4 Ethernet56/1 (IP: 192.168.12.15) | PASS | - |
| 736 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5/1 (IP: 192.168.12.18) - Destination: OTI-DC02-Leaf5A Ethernet56/1 (IP: 192.168.12.19) | PASS | - |
| 737 | OTI-DC02-Spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6/1 (IP: 192.168.12.22) - Destination: OTI-DC02-Leaf5B Ethernet56/1 (IP: 192.168.12.23) | PASS | - |
| 738 | OTI-DC02-Spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on vEOS-lab. |
| 739 | OTI-DC02-Spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on vEOS-lab. |
| 740 | OTI-DC02-Spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | SKIPPED | VerifyTemperature test is not supported on vEOS-lab. |
| 741 | OTI-DC02-Spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on vEOS-lab. |
| 742 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1/1 - P2P_OTI-DC02-Leaf1_Ethernet56/1 = 'up' | PASS | - |
| 743 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2/1 - P2P_OTI-DC02-Leaf2_Ethernet56/1 = 'up' | PASS | - |
| 744 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3/1 - P2P_OTI-DC02-Leaf3_Ethernet56/1 = 'up' | PASS | - |
| 745 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4/1 - P2P_OTI-DC02-Leaf4_Ethernet56/1 = 'up' | PASS | - |
| 746 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5/1 - P2P_OTI-DC02-Leaf5A_Ethernet56/1 = 'up' | PASS | - |
| 747 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6/1 - P2P_OTI-DC02-Leaf5B_Ethernet56/1 = 'up' | PASS | - |
| 748 | OTI-DC02-Spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 749 | OTI-DC02-Spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 750 | OTI-DC02-Spine2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | PASS | - |
| 751 | OTI-DC02-Spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | PASS | - |
| 752 | OTI-DC02-Spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | PASS | - |
| 753 | OTI-DC02-Spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 754 | OTI-DC02-Spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
