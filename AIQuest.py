import time
import random
from openai import OpenAI

## Setup ChatGPT
f = open("API_KEY.txt","r")
API_KEY = f.read()
f.close()

client = OpenAI(api_key = API_KEY)

## Functions
def intro():
    print(f'''
    \\-------|                                                       |--------/
     \\____  |-------------------------------------------------------|  ____ /
     /      | T H E   S E C R E T S   O F     P E B B L E B R O O K |       \\
    /—------|_______________________________________________________|--------\\''')
    time.sleep(1)
    print('''
                                                           |>>>
                   _                      _                |
    ____________ .' '.    _____/----/-\\ .' './========\\   / \\
   //// ////// /V_.-._\\  |.-.-.|===| _ |-----| u    u |  /___\\
  // /// // ///==\\ u |.  || | ||===||||| |T| |   ||   | .| u |_ _ _ _ _ _
 ///////-\\////====\\==|:::::::::::::::::::::::::::::::::::|u u| U U U U U
 |----/\\u |--|++++|..|""""""""""""::::::::::::::"""""|+++|+-+-+-+-+-+
 |u u|u | |u ||||||..|              '::::::::'           |===|>=== _ _ ==
 |===|  |u|==|++++|==|              .::::::::.           | T |....| V |..
 |u u|u | |u ||HH||         \|/    .::::::::::.
 |===|_.|u|_.|+HH+|_              .::::::::::::.              _
                __(_)___         .::::::::::::::.         ___(_)__
---------------/  / \  /|       .:::::;;;:::;;:::.       |\  / \  \-------
______________/_______/ |      .::::::;;:::::;;:::.      | \_______\________
|       |     [===  =] /|     .:::::;;;::::::;;;:::.     |\ [==  = ]   |
|_______|_____[ = == ]/ |    .:::::;;;:::::::;;;::::.    | \[ ===  ]___|____
     |       |[  === ] /|   .:::::;;;::::::::;;;:::::.   |\ [=  ===] |
_____|_______|[== = =]/ |  .:::::;;;::::::::::;;;:::::.  | \[ ==  =]_|______
 |       |    [ == = ] /| .::::::;;:::::::::::;;;::::::. |\ [== == ]      |
_|_______|____[=  == ]/ |.::::::;;:::::::::::::;;;::::::.| \[  === ]______|_
   |       |  [ === =] /.::::::;;::::::::::::::;;;:::::::.\ [===  =]   |
___|_______|__[ == ==]/.::::::;;;:::::::::::::::;;;:::::::.\[=  == ]___|_____''')
    time.sleep(1)
    print('''
  ··········································································
  : __  __               _             __  __           _                  :
  :|  \/  |_   _ _ __ __| | ___ _ __  |  \/  |_   _ ___| |_ ___ _ __ _   _ :
  :| |\/| | | | | '__/ _` |/ _ \ '__| | |\/| | | | / __| __/ _ \ '__| | | |:
  :| |  | | |_| | | | (_| |  __/ |    | |  | | |_| \__ \ ||  __/ |  | |_| |:
  :|_|  |_|\__,_|_|  \__,_|\___|_|    |_|  |_|\__, |___/\__\___|_|   \__, |:
  :                                           |___/                  |___/ :
  :	              (An AI-Generated Murder Mystery Game)                    :
  ··········································································
________________________  ''')
    enter = input("Press 'Enter' to Begin:")
    if(enter == ''):
        murder_method, murderer_order, murder_location = game_setup()
        print_intro_message(murder_method, murder_location)
    
def print_intro_message(murder_method, murder_location):
    time.sleep(1)
    print("""
~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. ' """)
    print("You, dear player, are an esteemed detective living in the sleepy town of Pebblebrook.")
    time.sleep(2)
    print("Recently, a tragedy has afflicted Pebblebrook, as <INSERTNAME>, an esteemed member of the community, was found murdered this morning.")
    time.sleep(3)
    print(f"Found dead due to {murder_method} {murder_location}, you are tasked with uncovering the perpretrator in this case and giving closure to the beloved <INSERTNAME>'s family.")
    time.sleep(3)
    print('''
         ____                 ____                 ____                 ____                 ____      
       /@ ...@\\             /@ ...@\\             /@ ...@\\             /@ ...@\\              /@ ...@\\
       @/////.%             @/////.%             @/////.%             @/////.%             @/////.%
       @@@//@@@             @@@//@@@             @@@//@@@             @@@//@@@             @@@//@@@
        @@  @@               @@  @@               @@  @@               @@  @@               @@  @@ 
         @##@                 @##@                 @##@                 @##@                 @##@
        @%++#@               @%++#@               @%++#@               @%++#@               @%++#@
   @@@@@#++++#@@@@@     @@@@@#++++#@@@@@     @@@@@#++++#@@@@@     @@@@@#++++#@@@@@     @@@@@#++++#@@@@@
  @@#++++++++++++#@@   @@#++++++++++++#@@   @@#++++++++++++#@@   @@#++++++++++++#@@   @@#++++++++++++#@@
  @@??????????????@@   @@??????????????@@   @@??????????????@@   @@??????????????@@   @@??????????????@@
                      
''')
    time.sleep(1)
    print("You have narrowed down your suspect list down to five individuals who were in contact with <INSERTNAME> within the 24-hour period before he died.")
    time.sleep(2)
    print("You have interviews set up with each suspect. For each interview, you may only ask ONE question, so ask WISELY.")
    time.sleep(2)
    ready = input("Dear player, are you ready to start the case? ['Yes'/'No'] ")
    while ready != 'Yes':
        print("That's not the spirit! Try again")
        ready = input("Dear player, are you ready to start the case? ['Yes'/'No'] ")
    time.sleep(2)
    for i in range(3):
        dist = "_______" * i
        dists = "       " * i

        print(f'''Off you go...
        `'::.
    _________H ,/%&%,
   /\     _   \%&&%&%
  /  \___/^\___\%&%&&
  |  | []   [] |%\Y&%'   {dists}     o
  |  |   .-.   | ||      {dists}     [
~~@._|@@_|||_@@|~||_____{dist}______/\_____ --->
     `""") )"""`
 ''')
        time.sleep(0.75)
        

def game_setup():
    murder_method, murder_location = choose_murder_situation()
    murderer_order = choose_random_killer()
    return murder_method, murderer_order, murder_location

def choose_murder_situation():
    murder_methods = [
        "poisoning", 
        "strangulation", 
        "stabbing", 
        "blunt force trauma", 
        "electrocution", 
        "drowning", 
        "arson", 
        "a fall from a high place", 
        "shooting", 
        "suffocation", 
        "a disguised accident", 
        "a ritualistic killing", 
        "asphyxiation", 
        "a cursed artifact", 
        "an unwanted exotic animal encounter",
        "a falling piano incident"]
    method = random.choice(murder_methods)

    murder_locations = murder_locations = [
    "at the abandoned warehouse",
    "in the old library",
    "at the city park",
    "at the local diner",
    "in the quaint inn",
    "at the cemetery",
    "at the train station",
    "by the riverbank",
    "in the historic mansion",
    "in the town square",
    "in the local art gallery",
    "at the community center",
    "in their own home"
    "washed up on the shore"]
    location = random.choice(murder_locations)
    return method, location

def choose_random_killer():
    return random.randint(1,5)
  
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