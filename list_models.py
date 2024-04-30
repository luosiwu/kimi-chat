import os
from openai import OpenAI
 
client = OpenAI(
    api_key="sk-v2Nkax4JXtnjf8NAV7m7jWbIyRD5ulnQnwTukxMbBtdGEfRo",
    base_url="https://api.moonshot.cn/v1",
)

'''
model[0]: moonshot-v1-8k
model[1]: moonshot-v1-32k
model[2]: moonshot-v1-128k
'''


model_list = client.models.list()
model_data = model_list.data
 
for i, model in enumerate(model_data):
    print(f"model[{i}]:", model.id)