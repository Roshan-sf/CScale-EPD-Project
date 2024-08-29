import os
import requests


def find_value(d, value, path=""):
    found = []

    if isinstance(d, dict):
        for key, dvalue in d.items():
            new_path = f"{path}.{key}" if path else key
            
            if isinstance(dvalue, str) and value in dvalue: #added for partial match
                found.append(new_path)
            elif isinstance(dvalue, (dict, list)):
                found.extend(find_value(dvalue, value, new_path))

    elif isinstance(d, list):
        for index, item in enumerate(d):
            new_path = f"{path}[{index}]"

            if isinstance(item, str) and value in item:
                found.append(new_path)  #partial
            elif isinstance(item, (dict, list)):
                found.extend(find_value(item, value, new_path))

    return found

################################# ACCESSING API ######################################

header = {"Authorization": "Bearer "+os.getenv("ECOPORTAL_TOKEN"),
          "Content-Type": "application/json"}

api_url = ' https://data.eco-platform.org/resource/processes?search=true&distributed=true&virtual=true&metaDataOnly=false&validUntil=2022&format=JSON'

response = requests.get(url=api_url, headers=header)
main = response.json()

################################# creating data structure ######################################

EPDs = []

for x in range(2,5):
    num = x
    baseURL = 'https://epdnorway.lca-data.com/resource/datastocks/91413340-7bf0-4f88-a952-0f91cba685df/processes/'
    uuid = main['data'][num]['uuid']
    version = main['data'][num]['version']
    api_url = f'{baseURL}{uuid}?version={version}&format=JSON'

    response = requests.get(url=api_url, headers=header)
    results = response.json()

    name = results['processInformation']['dataSetInformation']['name']['baseName'][0]['value']
    
    material_data = {
        "material_id": uuid,
        "display_name": name,
        "source": "source_placeholder",  # Replace with actual source
        "description": "description_placeholder",  # Replace with actual description
        "validity_ends": "datetime_placeholder",  # Replace with actual datetime
        "thickness": {
            "qty": 0.0,  # Replace with actual thickness quantity
            "unit": "unit_placeholder"  # Replace with actual unit
        },
        "service_life": 0,  # Replace with actual service life
        "waste_rate": 0.0,  # Replace with actual waste rate
        "transportation": {
            "mode": "mode_placeholder",  # Replace with actual transportation mode
            "distance": {
                "qty": 0.0,  # Replace with actual distance quantity
                "unit": "unit_placeholder"  # Replace with actual unit
            }
        },
        "density": {
            "qty": 0.0,  # Replace with actual density quantity
            "unit": "unit_placeholder"  # Replace with actual unit
        },
        "linear_density": {
            "qty": 0.0,  # Replace with actual linear density quantity
            "unit": "unit_placeholder"  # Replace with actual unit
        },
        "declared_unit": "unit_placeholder",  # Replace with actual declared unit
        "lcia_method": "method_placeholder",  # Replace with actual LCIA method
        "background_database": "database_placeholder",  # Replace with actual background database
        "impacts": {
            "gwp_total": {
                "A1_A3": 0.0, "A4": 0.0, "A5": 0.0, "C1": 0.0,
                "C2": 0.0, "C3": 0.0, "C4": 0.0, "D1": 0.0, "D2": 0.0
            },
            "gwp_biogenic": {
                "A1_A3": 0.0, "A4": 0.0, "A5": 0.0, "C1": 0.0,
                "C2": 0.0, "C3": 0.0, "C4": 0.0, "D1": 0.0, "D2": 0.0
            },
            "gwp_fossil": {
                "A1_A3": 0.0, "A4": 0.0, "A5": 0.0, "C1": 0.0,
                "C2": 0.0, "C3": 0.0, "C4": 0.0, "D1": 0.0, "D2": 0.0
            },
            "gwp_iobc": {
                "A1_A3": 0.0, "A4": 0.0, "A5": 0.0, "C1": 0.0,
                "C2": 0.0, "C3": 0.0, "C4": 0.0, "D1": 0.0, "D2": 0.0
            }
        },
        "characteristics": {}  # Replace with actual characteristics
    }
    
    EPDs.append(material_data)

