import random

def choose_random_name():
    name_list = ["Gavin", "Alyssa", "Mary", "Ebenezer", "Bridgette", "Tobias", "Leona", "Franklin", "Annie", "Blake", "Beth", "Barnaby", "Brie", "Elijah", "Aubrey"]
    return(random.choice(name_list))
    
def choose_random_job():
    job_list = ["Librarian", "Farmer", "Fisherman", "Banker", "Artist", "Mayor", "Doctor", "Maid", "Miner", "Hunter", "Barber", "Carpenter", "Mailman", "Baker", "Trader"]
    return(random.choice(job_list))

def choose_random_traits():
    trait_list = ["Kind", "Arrogant", "Friendly", "Smart", "Confident", "Loyal", "Strong", "Mad", "Sad", "Decisive"]
    return(random.choice(trait_list))

def choose_motive():
    motive_list = ["I loved them but they didn't love me back", "I wanted their land", "they were blackmailing me", "they saw me stealing bread", "they dated the person I love", "I got paid to do it", "they creeped me out", "they wouldn't stop bothering me for the debt I owed", "I wanted to be noticed", "I discovered they caused the accident that killed my father"]
    return(random.choice(motive_list))

def choose_relation():
    relation_list = ["Lover", "Friend", "Sibling", "Neighbor", "Renter", "Employee"]
    return(random.choice(relation_list))

def get_murder_status(mrdrordr):
    i = 3
    if i == mrdrordr:#i will be the i in the for loop that controls the number of people talked to
        return "the murderer"
    return "not the murderer"

def construct_gpt_prompt(name, job, traits, motive, relation, murder_status):
    print(f"Respond as {name} who works as a {job} and is {traits}. They are the victim's {relation}. They are {murder_status} and their motive was {motive}.")
    
def construct_user_prompt(name, job, relation):
    print(f"My name is {name} and I work as a {job}. I was the victim's {relation}.")

def get_user_guess():
    print("Enter the name of who you think the murderer is: ")
    user_guess = input()
    return user_guess



def main():
    character_list = []
    name = choose_random_name()
    character_list.append(name)#need a list of who user has talked to to check user guess
    job = choose_random_job()
    traits = choose_random_traits()
    motive = choose_motive()
    relation = choose_relation()
    murder_status = get_murder_status(3)
    construct_gpt_prompt(name, job, traits, motive, relation, murder_status)
    construct_user_prompt(name, job, relation)
    user_guess = get_user_guess()

main()