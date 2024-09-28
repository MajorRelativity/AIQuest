from openai import OpenAI

# Setup ChatGPT
f = open("API_KEY.txt","r")
API_KEY = f.read()
f.close()

client = OpenAI(api_key = API_KEY)

def call_chatGPT_example():

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": "What is your favorite color?"}
        ]
    )

    print(response.choices[0].message.content)

def main():
     call_chatGPT_example()

main()