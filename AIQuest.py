import random

def choose_random_name():
    name_list = ["Gavin", "Alyssa", "Mary", "Ebenezer", "Bridgette", "Tobias", "Leona", "Franklin", "Annie", "Blake", "Beth", "Barnaby", "Brie", "Elijah", "Aubrey"]
    print(random.choice(name_list))
    
def choose_random_job():
    job_list = ["Librarian", "Farmer", "Fisherman", "Banker", "Artist", "Mayor", "Doctor", "Maid", "Miner", "Hunter", "Barber", "Carpenter", "Mailman", "Baker", "Trader"]
    print(random.choice(job_list))

def choose_random_traits():
    trait_list = ["Kind", "Arrogant", "Friendly", "Smart", "Confident", "Loyal", "Strong", "Mad", "Sad", "Decisive"]
    print(random.choice(trait_list))

def choose_motive():
    motive_list = ["I loved them but they didn't love me back", "I wanted their land", "They were blackmailing me", "They saw me stealing bread", "They dated the person I love", "I got paid to do it", "They creeped me out", "They wouldn't stop bothering me for the debt I owed", "I wanted to be noticed", "I discovered they caused the accident that killed my father"]
    print(random.choice(motive_list))

def choose_relation():
    relation_list = ["Lover", "Friend", "Sibling", "Neighbor", "Renter", "Employee"]
    print(random.choice(relation_list))

def get_murder_status(mrdrordr):
    if i == mrdrordr:#i will be the i in the for loop that controls the number of people talked to
        return True
    return False

def construct_gpt_prompt(name, job, traits, motive, relation, murder_status):
    print(f"Respond as {name} who works as a {job} and is {traits}. They are the victim's {relation}. They are {murder_status} and their motive was {motive}.")

def main():
    name = choose_random_name()
    job = choose_random_job()
    traits = choose_random_traits()
    motive = choose_motive()
    relation = choose_relation()
    murder_status = get_murder_status()
    construct_gpt_prompt(name, job, traits, motive, relation, murder_status)
    construct_user_prompt(name, job, relation)

main()