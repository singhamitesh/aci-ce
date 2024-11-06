import csv
import logging
from tabulate import tabulate

# configure logging
logging.basicConfig(filename='allconfigurationlog.log', level=logging.INFO, format='%(message)s')

# load bd.csv data
with open("BD.csv") as bd_file:
    bd_reader = csv.DictReader(bd_file)
    bd_data = {row["VLAN"]: row for row in bd_reader}

# load epg.csv data
with open("EPG.csv") as epg_file:
    epg_reader = csv.DictReader(epg_file)
    epg_data = {row["VLAN"]: row for row in epg_reader}

# load interface.csv data
with open("interface.csv") as interface_file:
    interface_reader = csv.DictReader(interface_file)
    interface_data = [row for row in interface_reader]

# merge data based on VLAN
merged_data = []
for interface_row in interface_data:
    vlan = interface_row["VLAN"]
    bd_row = bd_data.get(vlan, {})
    epg_row = epg_data.get(vlan, {})

    merged_row = {
        "VLAN": vlan,
        "NODE": interface_row.get("NODE", ""),
        "Int": interface_row.get("Int", ""),
        "Path": interface_row.get("PATH", ""),
        "tn": interface_row.get("tn", ""),
        "AP": interface_row.get("AP", ""),
        "Dom": epg_row.get("Dom", ""),
        "Alias": epg_row.get("Alias", ""),
        "SUBNET": bd_row.get("SUBNET", ""),
        "VRF": bd_row.get("VRF", ""),
        "L3OUT": bd_row.get("L3Out", "")
    }

    merged_data.append(merged_row)

# define the header
header = ["VLAN", "NODE", "Int", "Path", "tn", "AP", "Dom", "Alias", "SUBNET", "VRF", "L3OUT"]

# generate output tabular format 
output = tabulate(merged_data, headers="keys", tablefmt="plain", stralign="left", numalign="left")

print(output)

# log the output to the log file
logging.info(f"PRINTING INFO LOG - \n{output}")

