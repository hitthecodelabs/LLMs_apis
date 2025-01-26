from openai import OpenAI
client = OpenAI()

prompt = 'Hi'

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            # "content": "Write a haiku about recursion in programming."
            'content' : prompt
        }
    ]
)

print(completion.choices[0].message)
