import time
import random

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

def main():
    print("Hello World")
    intro()
    
main()