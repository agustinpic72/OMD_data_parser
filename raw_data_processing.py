import re
import json
import pandas as pd
from excel_to_raw import xlsx_to_raw

def get_data_from_file(raw_file_path):
    with open(raw_file_path, 'r') as f:
        data = f.read()
    return data

def get_matches_from_data(data, pattern):
    matches = re.finditer(pattern, data, re.DOTALL)
    return matches


def matches_to_list(matches):
    official_keys = ['host_name','alias','parents','use','address','contact_groups','icon_image']
    official_images = {
                       'SWC':'swc.png',
                       'SWM':'swm.png',
                       'SWT':'swt.png',
                       'MNG':'majornet.png',
                       'MNM':'majornet.png',
                       'MNT':'majornet.png',
                       'MNF':'majornet.png',
                       'PAM':'pam.png',
                       'PAC':'pac.png',
                       'APM':'apm.png',
                       'APT':'apt.png',
                       'SVV':'svv.png',
                       'SVL':'svv.png',
                       'SVH':'svv.png',
                       'NAS':'nas.png',
                       'NVR':'nvr.png',
                       'RIF':'rif.png',
                       'RIR':'rif.png',
                       'RIW':'rif.png',
                       'Internet':'int.png',
                       'UPS':'ups.png',
                       }
    parsed_data_list = []
    for match in matches:
        block_data = match.group(1)
        key_value_pairs = re.findall(r'(\S+)\s+([^\n]*)(?=\n\s+\S+|\n})', block_data, re.DOTALL)
        parsed_data = {}
        for key, value in key_value_pairs:
            if value.split(' ')[0] in official_keys:
                parsed_data[key] = ""
                parsed_data[value.split(' ')[0]] = value.split(' ')[-1]
                continue
            parsed_data[key] = value.strip()
        
        # Adds icon image to parsed_data
        if not parsed_data.get('icon_image'):
            if len(parsed_data['host_name'].split('-')) > 1:
                parsed_data['icon_image'] = official_images[parsed_data['host_name'].split('-')[3]]
            else:
                parsed_data['icon_image'] = official_images[parsed_data['host_name']]
        parsed_data_list.append(parsed_data)
    return parsed_data_list

def json_to_xlsx(json_file_path,xlsx_file_path):
    json_df = pd.read_json(json_file_path)
    json_df.to_excel(xlsx_file_path,sheet_name='raw_hosts', index=False)

def run():
    raw_file_path = 'raw.txt'
    json_file_path = 'parsed.json'
    xlsx_file_path = 'data.xlsx'
    updated_data_path = 'updated_data.txt'
    data = get_data_from_file(raw_file_path)
    pattern = r'define host\s*{([^}]+)}'
    matches = get_matches_from_data(data, pattern)
    parsed_data_list = matches_to_list(matches)
    json_data = json.dumps(parsed_data_list, indent=2)
    with open(json_file_path, 'w') as f:
        f.write(json_data)
    json_to_xlsx(json_file_path,xlsx_file_path)
    xlsx_to_raw(xlsx_file_path,updated_data_path)

if __name__ == '__main__':
    run()




