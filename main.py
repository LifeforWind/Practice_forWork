import argparse
import openpyxl
import json

def convert_excel_to_json(excel_file, sheet_name, json_file):
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook[sheet_name]

    data = []

    for row in worksheet.iter_rows(min_row=2, values_only=True):
        record = {
            'content': row[0].replace('\n', '\n'),
            'summary': row[1].replace('\n', '\n')
        }
        data.append(record)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 解析命令行参数
parser = argparse.ArgumentParser(description='Excel to JSON Converter')
parser.add_argument('excel_file', help='Excel file path')
parser.add_argument('json_file', help='Output JSON file path')

args = parser.parse_args()

# 调用转换函数
convert_excel_to_json(args.excel_file, "Sheet1", args.json_file)
