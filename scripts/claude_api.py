import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

prompt = 'Hi'

message = client.messages.create(
    # model="claude-3-5-sonnet-20240620",
    # model="claude-3-5-haiku-20241022",
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    temperature=0,
    messages=[prompt]
)
print(message.content)
