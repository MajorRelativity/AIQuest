from openai import OpenAI

# Setup ChatGPT
f = open("API_KEY.txt","r")
API_KEY = f.read()
f.close()

client = OpenAI(api_key = API_KEY)

def call_chatGPT_example():
    '''Example API call where the user is asking ChatGPT what their favorite color is and the response is printed'''
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You love the color green"},
            {"role": "user", "content": "What is your favorite color?"}
        ]
    )

    print(response.choices[0].message.content)

def prompt_gpt(gpt_role, user_question):
    '''
     Sends the user question to ChatGPT and returns the response
     Takes: 
        - gpt_role (str): Promt string that tells ChatGPT how it should respond to the user prompt
        - user_question (str): The question that the user intends to ask ChatGPT
        
     Returns:
        - response (str): Response ChatGPT gives the user
        
    '''
    gpt_steam = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": gpt_role},
            {"role": "user", "content": user_question}
        ]
    )
    response = gpt_steam.choices[0].message.content
    return response

def main():
     print(prompt_gpt("Your favorite color is blue","What is your favorite color?"))

main()