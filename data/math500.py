"""
Data Link: https://huggingface.co/datasets/HuggingFaceH4/MATH-500
"""
import csv
import json
from tqdm import tqdm

test_path = './MATH500/original_data/test.jsonl'
output_path = './MATH500/test.json'

data_list = []
with open(test_path, 'r') as file:
    for id, line in enumerate(file.readlines()):
        line = json.loads(line)
        data_list.append({
            'id': id, 
            'Question': line['problem'],
            'solution': line['solution'],
            'answer': line['answer'],
            'subject': line['subject'],
            'level': line['level'],
            'unique_id': line['unique_id'],
        })

# Write the updated data to JSON
with open(output_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)
