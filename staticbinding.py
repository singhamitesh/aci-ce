import csv
import logging

# Configure logging
logging.basicConfig(filename='staticbindinglog.log', level=logging.INFO, format='%(message)s')

# Read the merged_output.csv file
with open('merged_output.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    # Print header
    print(f'{"AP":<10} {"tn":<10} {"VLAN":<10} {"PATH":<10} {"NODE":<10} {"Int":<10}')  # width for alignment
    logging.info(f'{"VLAN":<10} {"AP":<10} {"tn":<10} {"PATH":<10} {"NODE":<10} {"Int":<10}') # log the output

    # Iterate through each row in the CSV
    for row in reader:
        vlan = row['VLAN']
        ap = row['AP']
        tn = row['tn']
        path = row['PATH']
        node = row['NODE']
        value = row['Int']
        
        
        # Construct the API link
        api_link = f'This API has been called for BD-CONFIG -  https://localhost:10455//api/node/mo/uni/tn-{tn}/ap-{ap}/epg-VL-{vlan}-EPG/rspathAtt-[topology/pod-1/{path}-{node}/pathep-{value}.json'
        print(api_link)
        logging.info(api_link)
        
        print(f'{vlan:<10} {ap:<10} {tn:<10} {path:<10} {node:<10} {value:<10}')  # Adjust the width for alignment
        logging.info(f'{vlan:<10} {ap:<10} {tn:<10} {path:<10} {node:<10} {value:<10}')  # Log the output