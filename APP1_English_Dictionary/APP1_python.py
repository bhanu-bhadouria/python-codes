import jsonpickle
import difflib
import sqlite3

dictionary={}
with open("data.json","r") as file:
    data=file.read()
    dictionary=jsonpickle.decode(data)

def get_meaning(word):
    for result in dictionary[word]:
        print(result)

def check_word(word,keys):
    if word in keys:
        get_meaning(word)
        return 1
    elif word.title() in keys:
        get_meaning(word.title())
        return 1
    elif word.upper() in keys:
        get_meaning(word.upper())
        return 1
    else:
        if(len(difflib.get_close_matches(word,keys))> 0):
            word=difflib.get_close_matches(word,keys)[0]
            ch=input(f"did you mean {word} (y/n): ")
            if ch=='y':
                check_word(word,list_keys)
            else:
                print("the word does not exist")
                return 1
        else:
            print("word not found")

def create_database():
    con=sqlite3.connect("dictionary_db.db")
    c=con.cursor()
    c.execute("create table dictionary(word text,meaning text);")
    for a in list_keys:
        for result in dictionary[a]:
            d=(a,result)
            c.execute("insert into dictionary values(?,?);",d)
    con.commit()
    con.close()
    print("succesfully entered data into database")
            

choice='y'
list_keys=[a for a in dictionary.keys()]
while(choice=='y'):
    create_database()
    word=input("pls enter a word: ")
    word=word.lower()
    check_word(word,list_keys)
    choice=input("do you wish to continue (y/n): ")
