from openai import OpenAI
 
client = OpenAI(
    api_key = "sk-v2Nkax4JXtnjf8NAV7m7jWbIyRD5ulnQnwTukxMbBtdGEfRo",
    base_url = "https://api.moonshot.cn/v1",
)
 
history = [
    {"role": "system", "content": "你是人工智能助手。"}
]
 
def chat(query, history):
    history.append({
        "role": "user", 
        "content": query
    })
    print(history)
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
        temperature=0.3,
    )
    result = completion.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": result
    })
    return result
 
print(chat("地球的自转周期是多少？", history))
print(chat("月球呢？", history))