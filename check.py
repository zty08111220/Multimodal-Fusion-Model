import os
import chardet

# 存储所有不重复的编码方式
unique_encodings = set()

# 遍历 1.txt 到 5129.txt
for i in range(1, 5130):
    file_path = os.path.join('data', f'{i}.txt')
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    # 检测文件编码
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
        # 将编码方式添加到集合中
        unique_encodings.add(encoding)

# 打印所有不重复的编码方式
print("Unique encodings found:")
for encoding in unique_encodings:
    print(encoding)