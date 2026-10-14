from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL = "claude-sonnet-5-5"
SYSTEM = (
    "You are ShopAssistant, an online store's support assistant. "
    "Returns are accepted withing 30 days of delivery. "
    "Answer in or two sentences."
)


def ask(messages):
    response = client.messages.create(
        model=MODEL,
        max_tokens=200,
        output_config={"effort": "low"},
        system=SYSTEM,
        messages=messages,
    )

    for block in response.content:
        if block.type == "text":
            reply = block.text
    print(reply)
    print("input tokens:", response.usage.input_tokens)
    return reply


history = []


def say(message):
    history.append({"role": "user", "content": message})
    reply = ask(history)
    history.append({"role": "user", "content": reply})


say("I bought a jacket 20 days ago.")
say("Can I still return it?")
