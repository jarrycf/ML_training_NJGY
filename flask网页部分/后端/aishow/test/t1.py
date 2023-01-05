import openai
# Set the API key
openai.api_key = "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"
model_engine = "text-davinci-003"
# model_engine = "text-babbage-001"
prompt=f"回复朋友的消息:'如何用python写一个最简单的程序'"
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=30, n=1,stop=None,temperature=0.3)
response = completions.choices[0].text
print(response)
