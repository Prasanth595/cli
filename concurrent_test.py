import subprocess
import json
import sys

file = 'meta.json'
subprocess.run(f'del {file}', shell=True, capture_output=True)

# 并发执行 10 次
processes = []
for _ in range(10):
    p = subprocess.Popen(f'http --save-meta {file} GET http://httpbin.org/get', shell=True)
    processes.append(p)

for p in processes:
    p.wait()

# 验证 JSON 完整性
with open(file, 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f"成功读取 JSON，共 {len(data)} 条记录")
    assert len(data) == 10, f"预期 10 条，实际 {len(data)} 条"
print("并发测试通过")