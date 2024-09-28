from openai import OpenAI

## Setup ChatGPT
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

def prompt_gpt(gpt_role: str, user_question: str):
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

def get_user_question(name: str, user_prompt: str, suspect_number: int):
    ''' 
     Prompts the user for what question they want to ask the suspect.
     Takes:
        - name (str): Name of the suspect they are questioning
        - user_promt (str): What the suspect says to the user
        - suspect_numer (int): What order in the interview process the suspect is 
     Returns:
        - user_question (str): The question the user wants to ask the suspect
    
    '''
    if suspect_number == 1:
        print("You approach the first subject")
    else:
        print("You approach the next subject")

    print(f"[{name}]: {user_prompt}")
    user_question = input(f"What question would you like to ask {name}? ")
    return user_question



def main():
     user_question = get_user_question("Jacob","Hi I am Jacob",1)
     print(prompt_gpt("Your favorite color is blue", user_question))

main()