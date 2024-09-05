

async def find_value(d, value, path=""):
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