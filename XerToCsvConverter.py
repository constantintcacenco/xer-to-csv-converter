import os
import pandas as pd 


class XerToCsvConverter:

    def __init__(self):
        self.tables = []

    def read_xer(self, file_path):
        with open(file_path) as f:
            content = f.read()
            tables = content.split('%T')
            self.tables = tables[1:]
    
    def check_output_dir(self, output_location):
        if not os.path.exists(output_location):
            os.makedirs(output_location)

    def check_missing_values(self, columns, rows_list):
        for row in rows_list:
            if len(columns) > len(row):
                row[len(columns):len(row)] = [None]*(len(columns) - len(row))
        return rows_list   

    def convert_to_csv(self, output_path):
        for table in self.tables:
            table_name = table.split()[0]
            fields = table.split(r'%F')[1].split('\n')[0].split()
            rows = table.split('%R')[1:]
            rows_list = [r.strip().split('\t') for r in rows]
            
            checked_rows_list = self.check_missing_values(fields,rows_list)

            df = pd.DataFrame(checked_rows_list, columns=fields, index=None)
            self.check_output_dir(output_path)
            csv_file_path = os.path.join(output_path,table_name + '.csv')
            df.to_csv(csv_file_path)
