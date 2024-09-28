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

def main():
    choose_random_name()
    choose_random_job()
    choose_random_traits()
    choose_motive()

main()