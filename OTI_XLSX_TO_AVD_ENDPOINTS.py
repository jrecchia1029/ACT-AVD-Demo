import json, csv, os, yaml, sys
import pandas as pd

import os
dirname = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(dirname, os.pardir))

# print(parent_directory)

# sys.exit(0)

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

if n > 1:
    port_profiles = bool(sys.argv[1])
else:
    port_profiles = True

print("port_profiles is %s!" % str(port_profiles))

XLSXName = os.path.join(dirname, "OtiNetworkConnectivitySpreadsheet.xlsx")

data_xls = pd.read_excel(XLSXName, 'Sheet1', index_col=None)
data_xls.to_csv('oti.csv', encoding='utf-8')


# PWD = os.path.dirname(os.path.realpath(__file__))
PWD = os.path.dirname(__file__)


# checkFor = "DC02-0901-ESX03"
checkFor = None
checkInts = 4



# 
# Assumptions
# MLAG or ESI are pairs that follow each other
# dual-homed are configured with the merge of both VLAN assignments
# 

portchannels = []
ESIs = []

def filterWhitespace(fieldIn):
    return str(fieldIn).replace(" ", '_')

# {'Status': 'CONNECTED', 'Wave': 'Wave 1', 'Equipment / Server': 'Server1', 'Server Port': 'port 3', 'Media': 'Fiber', 'Cabinet / Rack': '9323.01.3344', 'IP Address': '', ' Gateway IP': '', 'Speed': 'Auto (25GB)', 'VLAN': '3434\n3433\n2818', 'Switch / Router': 'Switch1', 'Switch / Router Rack': 'AR17', 'Network Port': '29', 'Trunked': 'YES', 'Jumbo Frames': '9216', 'DHCP': ''}
def rowToEndpoint(rowIn):
    endpointName = str("%s~%s" % (filterWhitespace(rowIn['Server']), filterWhitespace(rowIn['Server Port'])))
    rack = filterWhitespace(rowIn['Cabinet and Rack'])
    adapters = [dict(),]
    adapters[0]['endpoint_ports'] = [filterWhitespace(rowIn['Server Port']),]
    adapters[0]['switch_ports'] = [filterWhitespace(rowIn['Network Port']).replace("_",''),]
    adapters[0]['switches'] = [filterWhitespace(rowIn['Switch']),]
    
    adapters[0]['mode'] = None
    if filterWhitespace(rowIn['Trunk']).lower() in ["true","yes", "y"]:
        adapters[0]['mode'] = "trunk"
    else:
        adapters[0]['mode'] = "access"
    
    if filterWhitespace(rowIn['Jumbo Frames']) != "":
        # print(rowIn['Jumbo Frames'])
        # print(type(rowIn['Jumbo Frames']))
        adapters[0]['mtu'] = int(float(filterWhitespace(rowIn['Jumbo Frames'])))
    
    if rowIn['Vlan'][-1:] == "\n":
        rowIn['Vlan'] = rowIn['Vlan'][0:-1]
    
    adapters[0]['vlans'] = str(rowIn['Vlan']).replace('\n', ", ")
    
    if port_profiles:
        adapters[0]['profile'] = "Access"
    
    adapters[0]['mlag'] = None
    adapters[0]['esi'] = None
    if str(rowIn['Port-Channel']).lower() == "mlag":
        adapters[0]['mlag'] = True
    elif str(rowIn['Port-Channel']).lower() == "esi":
        adapters[0]['esi'] = True
    else:
        pass
    
    
    
    return {"name": endpointName, "rack": rack, "adapters": adapters}
    
def mergeOne(twoIN):
    shortList = [x["adapters"][0] for x in twoIN]
    # print(twoIN)
    # print(shortList)
    def split(parameter):
        # print(str(type(shortList[0][parameter])))
        if type(shortList[0][parameter]) == type([]):
            return [shortList[0][parameter][0], shortList[1][parameter][0]]
        else:
            return [shortList[0][parameter], shortList[1][parameter]]

    def join(parameter):
        # print(parameter)
        # print(shortList[0])
        # some parameters like MTU attempt to be forced in the return from mergeOne
        # try and pass if the parameter is not set
        try:
            return shortList[0][parameter]
        except:
            pass

    def sortVLANs(strIN):

        # print([str(VLAN).strip() for VLAN in str(strIN).split(",")].sort())
        return [str(VLAN).strip() for VLAN in str(strIN).split(",")].sort()
    
        return ", ".join([str(VLAN).strip() for VLAN in str(strIN).split(",")].sort())[:-2]

    dataOut = None
    if join("esi"):
        # We are in a situation where we are AA with ESI and need to define those parameters
        dataOut = {
            "name":twoIN[0]["name"],
            "rack":twoIN[0]["rack"],
            "adapters":[{
                    "endpoint_ports":split("endpoint_ports"),
                    "switch_ports":split("switch_ports"),
                    "switches":split("switches"),
                    "mode":split("mode"),
                    "vlans":sortVLANs(join("vlans")),
                    "mtu":join("mtu"),
                    "mode":join("mode"),
                    "port_channel": {
                        "mode": "active"
                    },
                    "ethernet_segment": {
                        "short_esi": "auto"
                    }
                },]}
    else:
        # If we are not in ESI mode then we are an MLAG PO
        dataOut = {
            "name":twoIN[0]["name"],
            "rack":twoIN[0]["rack"],
            "adapters":[{
                    "endpoint_ports":split("endpoint_ports"),
                    "switch_ports":split("switch_ports"),
                    "switches":split("switches"),
                    "mode":split("mode"),
                    "vlans":join("vlans"),
                    "mtu":join("mtu"),
                    "mode":join("mode"),
                    "port_channel": {
                        "mode": "active"
                    }
                },]}
    
    if port_profiles:
        dataOut["adapters"][0]["profile"] = "Access"

    return dataOut 
    

def mergeAllRows(dataIn):
    output = {"servers":[]}
    for endpoint in range(len(dataIn["servers"])):
        
        endpoint1 = dataIn["servers"][endpoint]["adapters"][0]
        
        endpointName = dataIn["servers"][endpoint]["name"].split("~")
        
        if checkFor == endpointName[0]:
            print(endpointName[1])

        # if our endpoint has mlag or esi configured we move forward
        if endpoint1['esi'] or endpoint1['mlag']:
            # print(endpoint1)
            if endpoint1['mlag']:
                poSetting = "mlag"
            else:
                poSetting = "esi"

                        # for the index of the link in the list of links
            listoflinks = [dataIn["servers"][key] for key in range(len(dataIn["servers"])) \
                        # if the endpoint hostname matches the current 
                           if (str(dataIn["servers"][key]["name"])[:str(dataIn["servers"][key]["name"]).find("~")] == endpointName[0] and \
                        # and the mlag setting or the esi setting match
                           (endpoint1[poSetting]==dataIn["servers"][key]["adapters"][0][poSetting]) and \
                        # and the switch ports are the same
                            endpoint1["switch_ports"]==dataIn["servers"][key]["adapters"][0]["switch_ports"]) and \
                            endpoint1["vlans"]==dataIn["servers"][key]["adapters"][0]["vlans"]    ]
                        # Then we add it to the list in listoflinks for the agg


            # '3434, 1000, 2000, 500'

            # vs
            # 


            # for link in listoflinks:
            #     if "idrac" in link["adapters"][0]["endpoint_ports"]:
            #         print(link)
            # print(str(dataIn["servers"][0]["name"])[:str(dataIn["servers"][0]["name"]).find("~")])
            # print()
            # print(listoflinks)
            # print()
            # print(mergeOne(listoflinks))
            # verify this isnt the second link in the two that has already been added
            if not mergeOne(listoflinks) in output["servers"]:
                output["servers"].append(mergeOne(listoflinks))
        else:
            # print(en
            # dpoint)
            dataIn["servers"][endpoint]["profile"] = "Access"
            output["servers"].append(dataIn["servers"][endpoint])
        # print( mergeOne(listoflinks))
    return output

def splitName(nameIn):
    return nameIn[:nameIn.find("~")]

# Merge all single and po interfaces into one endpoint
def mergePos(dataIn):
    output = []
    completedDevices = []
    for link in dataIn["servers"]:
        # There are entries in servers for each single link or po
        # merge those links into one endpoint with multiple adapters
        endpointName = splitName(link["name"])

        if endpointName in completedDevices:
            continue
        else:
            completedDevices.append(endpointName)
        
        if endpointName == checkFor:
            print(endpointName)
        
        count = 0
        # If we are here we have a new device to process
        # prep new server to be added
        newServer = {}
        newServer["name"] = endpointName
        newServer["rack"] = link["rack"]
        newServer["adapters"] = []

        for newLink in dataIn["servers"]:
            if newServer["name"] == splitName(newLink["name"]):

                for adapter in newLink["adapters"]:
                    # filter all elements like MLAG or ESI that are None or (null)!
                    newServer["adapters"].append({k: v for k, v in adapter.items() if v is not None})
                    # count += 1
                    # print(count)


        output.append(newServer)
    return {"servers": output}
     

if __name__ == "__main__":
    print("Starting in %s!" % (PWD))
    data = {"servers": []}
    with open(os.path.join(PWD,"oti.csv")) as openFile:
        rawData = csv.DictReader(openFile)
        for row in rawData:
            data["servers"].append(rowToEndpoint(row))

    data["servers"] = [endpoint for endpoint in data["servers"] if endpoint["name"] != "~"]

    
    if checkFor:
        print("%s has %s links FYI!" % (checkFor, str(len(   [endpoint for endpoint in data["servers"] if endpoint['name'][:endpoint['name'].find("~")] == checkFor]))))

    data = mergeAllRows(data)
    
    if checkFor:
        print("%s has %s individual adapters FYI!" % (checkFor, str(len(   [endpoint for endpoint in data["servers"] if endpoint['name'][:endpoint['name'].find("~")] == checkFor]))))
    
    data = mergePos(data)
    if checkFor:
        print("%s has %s merged adapters FYI!" % (checkFor, str(len(   [endpoint["adapters"] for endpoint in data["servers"] if endpoint['name'] == checkFor][0]))))
    
        # Set port profile to add portfast after all is done!
    #  
    # port_profiles:
#    - profile: Access
#      spanning_tree_portfast: edge
    data["port_profiles"] = [ { "profile":"Access", \
                                "spanning_tree_portfast":"edge"},]

    endpoints_data = {
        "port_profiles": data.get("port_profiles", []),
        "servers": data.get("servers", [])
    }

    # with open('outputConfig.json', 'w') as json_file:
    #     json.dump(data, json_file)
    
    
    yaml.Dumper.ignore_aliases = lambda *args : True
    with open('group_vars/OTI_Endpoints.yml', 'w') as yaml_file:
        yaml.dump(endpoints_data, yaml_file, indent=3, sort_keys=False)
    
    if checkFor:
        assert(len([endpoint["adapters"] for endpoint in data["servers"] if endpoint['name'] == checkFor][0]) == checkInts)
    
    # print(data)
    print("Done!")