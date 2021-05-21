import sqlite3
import difflib


con=sqlite3.connect("dictionary_db.db")
c=con.cursor()
def getmeaning(res):
    for m in res:
        print(m[0])
def check_word(word):
    if word in list_keys:
        c.execute(f"select meaning from dictionary where word='{word}';")
        result=c.fetchall()
        getmeaning(result)
        return 1
    elif word.title() in list_keys:
        c.execute(f"select meaning from dictionary where word='{word.title()}';")
        result=c.fetchall()
        getmeaning(result)
        return 1
    elif word.upper() in list_keys:
        c.execute(f"select meaning from dictionary where word='{word.upper()}';")
        result=c.fetchall()
        getmeaning(result)
        return 1
    else:
        if(len(difflib.get_close_matches(word,list_keys))>0):
            word=difflib.get_close_matches(word,list_keys)[0]
            ch=input(f"did you mean {word} (y/n): ")
            if ch=='y':
                check_word(word)
            else:
                print("no such word found")
                return 1
        else:
            print("pls double check")
list_keys=[]  
choice='y'
while choice=='y':
    c.execute("select word from dictionary;")
    for a in c.fetchall():
        list_keys.append(a[0])
    word=input("pls enter the word : ")
    check_word(word)
    choice=input("do you wish to continue (y/n) : ")

con.commit()
con.close()