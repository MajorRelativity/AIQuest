from openai import OpenAI

f = open("API_KEY.txt","r")
API_KEY = f.read()
f.close()

client = OpenAI(api_key = API_KEY)

def initialize_chatGPT():

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": "What is your favorite color?"}
        ]
    )

    print(response)

def main():
    initialize_chatGPT()
    print("Hello World")

main()