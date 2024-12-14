d = {"name": "혼자 곤부하는 데이터 분석"}
print(d["name"])

import json

d_str = json.dumps(d, ensure_ascii=False)
print(d_str)

print(type(d_str))

d2 = json.loads(d_str)
print(d2["name"])

print(type(d2))

d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", " author": ["박해선","홍길동"]:, "year": 2022}')

print(d3["name"])
print(d3['author'])
print(d3['year'])

print(d3['author'][1])

d4_str = """
[
  {"name":"헌자 공부하는 데이터 분석", "author": "박해선", "year": 2022},
  {"name":"헌자 공부하는 머신러닝+딥러닝", "author": "박해선", "year": 2020}
]
"""

d4 = json.loads(d4_str)
print(d4[0]['name'])

import pandas as pd
pd.read_json(d4_str)

pd.DataFrame(d4)