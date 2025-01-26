from openai import OpenAI
client = OpenAI()

prompt = 'Hi'

response = client.images.generate(
    prompt=prompt,
    n=2,
    size="1024x1024"
)

print(response.data[0].url)
