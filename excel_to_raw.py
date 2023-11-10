import pandas as pd
import json

def xlsx_to_raw(xlsx_file_path,updated_data_path):
    df = pd.read_excel(xlsx_file_path).to_json(orient='records')
    json_data = json.loads(df)
    with open(updated_data_path,'w') as f:
        for host in json_data:
            f.write('define host {\n')
            for key,value in host.items():
                value = value if value else ''
                f.write('\t'+key+'\t'+value+'\n')
            f.write('}\n')

def run():
    xlsx_file_path = 'data.xlsx'
    updated_data_path = 'updated_data.txt'
    xlsx_to_raw(xlsx_file_path,updated_data_path)

if __name__ == '__main__':
    run()