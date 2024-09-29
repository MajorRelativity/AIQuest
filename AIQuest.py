import time
import random
from openai import OpenAI

## Setup ChatGPT
f = open("API_KEY.txt","r")
API_KEY = f.read()
f.close()

client = OpenAI(api_key = API_KEY)

## Functions
def intro(victim):
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
        print_intro_message(murder_method, murder_location, victim)
        return murder_method, murderer_order, murder_location
    
def print_intro_message(murder_method, murder_location, victim):
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
  ..    ..-''    ;       ''. ' 
          """)
    print(" ")
    print("[Narrator]: You, dear player, are an esteemed detective living in the sleepy town of Pebblebrook.")
    time.sleep(2)
    print(f"[Narrator]: Recently, a tragedy has afflicted Pebblebrook, as {victim}, a valued member of the community, was found murdered this morning.")
    time.sleep(3)
    print(f"[Narrator]: Found dead due to {murder_method} {murder_location}, you are tasked with uncovering the perpretrator in this case and\ngiving closure to the beloved {victim}'s family.")
    time.sleep(3)
    print('''
         ____                 ____                 ____               
       /@ ...@\\             /@ ...@\\             /@ ...@\\         
       @/////.%             @/////.%             @/////.%             
       @@@//@@@             @@@//@@@             @@@//@@@            
        @@  @@               @@  @@               @@  @@              
         @##@                 @##@                 @##@              
        @%++#@               @%++#@               @%++#@              
   @@@@@#++++#@@@@@     @@@@@#++++#@@@@@     @@@@@#++++#@@@@@     
  @@#++++++++++++#@@   @@#++++++++++++#@@   @@#++++++++++++#@@   
  @@??????????????@@   @@??????????????@@   @@??????????????@@  
                      
''')
    time.sleep(1)
    print(f"[Narrator]: You have narrowed down your suspect list down to three individuals who were in contact with {victim} within the 24-hour period before he died.")
    time.sleep(2)
    print("[Narrator]: You have interviews set up with each suspect. For each interview, you may only ask ONE question, so ask WISELY.")
    time.sleep(2)
    print("[Narrator]: Dear player, are you ready to start the case? ['Yes'/'No'] ")
    ready = input("[You]: ")
    while ready.lower() != 'yes':
        print("[Narrator]: That's not the spirit! Try again")
        print("[Narrator]: Dear player, are you ready to start the case? ['Yes'/'No'] ")
        ready = input("[You]: ")
    time.sleep(2)
    for i in range(3):
        dist = "_______" * i
        dists = "       " * i

        print(f'''[Narrator]: Off you go...
        `'::.
    _________H ,/%&%,
   /\     _   \%&&%&%
  /  \___/^\___\%&%&&
  |  | []   [] |%\Y&%'   {dists}     o
  |  |   .-.   | ||      {dists}     [
~~@._|@@_|||_@@|~||_____{dist}_____ /\ ____ --->
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
    return random.randint(1,3)
  
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
        print("[Narrator]: You approach the first suspect")
    else:
        print("[Narrator]: You approach the next suspect")

    print(f"[{name}]: {user_prompt}")
    print(' ')
    print(f"[Narrator]: What question would you like to ask {name}?")
    user_question = input("[You]: ")
    print(' ')
    return user_question

def choose_random_name():
    name_list = ["Gavin", "Alyssa", "Mary", "Ebenezer", "Bridgette", "Tobias", "Leona", "Franklin", "Annie", "Blake", "Beth", "Barnaby", "Brie", "Elijah", "Aubrey"]
    return(random.choice(name_list))
    
def choose_random_job():
    job_list = ["librarian", "farmer", "fisherman", "banker", "artist", "mayor", "doctor", "maid", "miner", "hunter", "barber", "carpenter", "mailman", "baker", "trader"]
    return(random.choice(job_list))

def choose_random_traits():
    trait_list = ["Kind", "Arrogant", "Friendly", "Smart", "Confident", "Loyal", "Strong", "Sad", "Decisive"]
    return(random.choice(trait_list))

def choose_motive(victim):
    motive_list = [f"you loved {victim} but they didn't love me back", "you wanted their land", f"{victim} was blackmailing you", f"{victim} saw you stealing bread", f"{victim} dated the person you love", "you got paid to do it", f"{victim} creeped you out", f"{victim} wouldn't stop bothering you for the debt you owed", "you wanted to be noticed", f"you discovered {victim} caused the accident that killed your father"]
    return(random.choice(motive_list))

def choose_relation():
    relation_list = ["lover", "spouse", "friend", "sibling", "neighbor", "renter", "employee"]
    return(random.choice(relation_list))

def get_murder_status(i, mrdrordr, murder_method, murder_location, murder_motive):
    if i == mrdrordr - 1:#i will be the i in the for loop that controls the number of people talked to
        return f"the murderer. You murdered the victim with {murder_method} {murder_location} because {murder_motive}. Without revealing yourself as the murderer, in your response you accidentally give multiple clues that you are the murderer"
    return f"not the murderer. You are aware that the victim was murdered with {murder_method} {murder_location}"

def construct_gpt_prompt(name, job, traits, motive, relation, murder_status, victim):
    return(f"You are {name} and you work as a {job}. You are {traits}. You are currently being interrogated by a detective. You know the victim of the murder is {victim}. You are the {relation} of the victim. Your response should be at least 12 sentences. You are {murder_status}.")
    
def construct_user_prompt(name, job, relation, victim):
    return(f"My name is {name} and I work as a {job}. I was {victim}'s {relation}.")

def get_user_guess():
    print('')
    print("[Narrator]: Enter the name of who you think the murderer is: ")
    user_guess = input("[You]: ")
    print(' ')
    return user_guess

def check_user_guess(user_guess, character_list, mrdrorder):
    if user_guess.lower() == character_list[mrdrorder - 1].lower():
        #return "Congrats! You found the murderer!"
        return True
    #return "Sorry you accused an innocent person."
    return False

def print_outro(result, user_guess, victim, murderer):
    if result == True:
        print(f"[Narrator]: You methodically pieced together all the information. By focusing on the answer you were given you were able to correctly deduce who was the murderer. {user_guess} confesses that they killed {victim}. With the truth unveiled and justice served Pebblebrook can begin to heal again though it will never be the same.")
        print(" ")
        print("-- YOU WIN --")
    else:
        print(f"[Narrator]: You wrongly accused {user_guess} of being a murderer. {victim}'s murderer will run free and Pebblebrook will have to try to heal without closure.")
        print(" ")
        print("-- YOU LOSE -- ")
        print(f"The murderer was {murderer}")

def run_game():
    # Run the Introduction
    victim = choose_random_name()
    murder_method, murderer_order, murder_location = intro(victim)

    # Run Character Interview
    character_list = run_character_interview(murder_method, murderer_order, murder_location, victim)

    # Run Conclusion
    run_conclusion(character_list, victim, murderer_order)

def run_character_interview(murder_method, murderer_order, murder_location, victim):
    character_list = []

    for i in range(3):
        print(" ")
        print(f" -- INTERVIEW #{i + 1} ---")

        # Get Information About Character
        name = choose_random_name()
        character_list.append(name) # list of who user has talked to to check user guess
        job = choose_random_job()
        traits = choose_random_traits()
        motive = choose_motive(victim)

        relation = choose_relation()
        murder_status = get_murder_status(i, murderer_order, murder_method, murder_location, motive)
        
        # Construct Prompts
        gpt_prompt = construct_gpt_prompt(name, job, traits, motive, relation, murder_status, victim) # need murder_method from Emma
        user_prompt = construct_user_prompt(name, job, relation, victim)

        # Interaction
        print(' ')
        user_question = get_user_question(name, user_prompt, i + 1)
        suspect_response = prompt_gpt(gpt_prompt, user_question)
        print(f"[{name}]: {suspect_response}")

    return character_list

def run_conclusion(character_list, victim, murderer_order):
    user_guess = get_user_guess()
    result = check_user_guess(user_guess, character_list, murderer_order) #need murder order from Emma
    print_outro(result, user_guess, victim, character_list[murderer_order - 1])

def main():
    run_game()

    
main()