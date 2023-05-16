import argparse
import json
import random

def merge_json_files(file1, file2, output_file):
    # 读取第一个 JSON 文件
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)

    # 读取第二个 JSON 文件
    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    # 合并两个 JSON 数据
    merged_data = data1 + data2

    # 写入合并后的数据到输出文件
    with open(output_file, 'w', encoding='utf-8') as f_out:
        json.dump(merged_data, f_out, ensure_ascii=False, indent=2)

def shuffle_json_file(input_file, output_file):
    # 读取 JSON 文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 打乱数据
    random.shuffle(data)

    # 写入打乱后的数据到输出文件
    with open(output_file, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, ensure_ascii=False, indent=2)

def calculate_max_lengths(json_file):
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    input_max_length = max(len(record.get('content', '')) for record in data)
    output_max_length = max(len(record.get('summary', '')) for record in data)

    return input_max_length, output_max_length

# 解析命令行参数
parser = argparse.ArgumentParser(description='JSON File Processing')
parser.add_argument('--merge', nargs=3, metavar=('file1', 'file2', 'output'), help='Merge two JSON files')
parser.add_argument('--shuffle', nargs=2, metavar=('file_input', 'file_output'), help='Shuffle JSON file')
parser.add_argument('--statistic', metavar='file', help='Calculate max lengths of input and output fields')

args = parser.parse_args()

# 根据命令行参数选择执行相应的函数
if args.merge:
    file1, file2, output_file = args.merge
    merge_json_files(file1, file2, output_file)
elif args.shuffle:
    input_file, output_file = args.shuffle
    shuffle_json_file(input_file, output_file)
elif args.statistic:
    json_file = args.statistic
    input_max_len, output_max_len = calculate_max_lengths(json_file)
    print('Input Max Length:', input_max_len)
    print('Output Max Length:', output_max_len)
else:
    print('No valid command specified. Use --merge, --shuffle, or --statistic.')

