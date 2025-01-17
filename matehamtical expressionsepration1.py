import re
input_str ="def"
pattern = r'[+\-*/^%()]'
parts = re.split(pattern, input_str)
parts = [part for part in parts if part]
print(parts)