from imdb import imdb
import shelve
import random 

actors = list()

def create_entry(actor, date, title, role):
    # create a dictionary for each row in imdb file
    entry = {'actor':str(actor),'title':title,'data':date,'role':role}
    # append this dictionary to our list
    actors.append(entry)

# call create_entry for every row in imdb file
imdb.process_file('data/actors.list.gz', create_entry)

# create a new shelve 
s = shelve.open('data/actors.db')

# pick 15 random entries from the imdb data
indexes_to_save = random.sample(range(0,len(actors)-1), 15)

# save these picked entries to the database
try:
    for i in indexes_to_save:
        s[str(i)] = actors[i]
finally:
    s.close()