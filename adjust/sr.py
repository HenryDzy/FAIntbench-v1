import json
import re

# 示例概率数据，用于每个 prompt
example_data = {
    "left": {
        "gender": {
            "man": 0.5,
            "woman": 0.5
        },
        "race": {
            "European": 0.2,
            "East-asian": 0.2,
            "African": 0.2,
            "Latino": 0.2,
            "South-Asian": 0.2
        },
        "age": {
            "10~29 years old": 0.3,
            "31~59 years old": 0.4,
            "60 years old or older": 0.3
        }
    },
    "right": {
        "gender": {
            "man": 0.5,
            "woman": 0.5
        },
        "race": {
            "European": 0.2,
            "East-asian": 0.2,
            "African": 0.2,
            "Latino": 0.2,
            "South-Asian": 0.2
        },
        "age": {
            "10~29 years old": 0.3,
            "31~59 years old": 0.4,
            "60 years old or older": 0.3
        }
    }
}

def read_prompts_from_txt(file_path):
    prompts = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'--prompt "(.*?)"', line)
            if match:
                prompt = match.group(1)
                prompts.append(prompt)
    return prompts

def create_json_from_prompts(prompts, output_file):
    data = {}
    for prompt in prompts:
        data[prompt] = example_data
    
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# 读取txt文件中的prompts
prompts = read_prompts_from_txt('implicit_relation.txt')

# 将prompts转换为JSON文件
create_json_from_prompts(prompts, 'complex_output.json')
