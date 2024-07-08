#!/usr/bin/env python3
from tinydb import TinyDB, Query
import datetime
from os import system, name
from time import sleep

today = datetime.date.today()

db = TinyDB('db.json')

titleScreen = '''
 | \ | |     | |          | |
 |  \| | ___ | |_ ___  ___| |
 | . ` |/ _ \| __/ _ \/ __| |
 | |\  | (_) | ||  __/\__ \_|
 |_| \_|\___/ \__\___||___(_)
 - by woflmao
 =============================
 (n) to add a new entry
 (s) to search for an entry
 (d) to delete an entry
 (x) to delete all entries
 (q) to quit
'''
searchScreen = '''
      (t) to search by title
      (d) to search by date
      (l) to list all entries
      '''

def clear():
    """for removing the clutter from the screen when necessary"""
    system('cls' if name == 'nt' else 'clear')

clear()
choice = None
while choice != 'q':
  print(titleScreen)
  choice = input('Please choose from above options:')

  if choice == 'n':
    clear()
    print('Please enter the title of the entry:')
    title = input()
    print('Please enter the note:')
    entry = input()
    db.insert({'date': str(today), 'title': title, 'entry': entry, 'id': len(db)})
    print('Entry added!')
    sleep(1)
    clear()

  elif choice == 's':
    clear()
    print(searchScreen)
    searchChoice = input('Please choose from above options:')
    if searchChoice == 't':
      clear()
      res = db.search(Query().title == input('Please enter the title:'))
      print(str(res[0]['id']) + ' - ' + res[0]['date'] + ' - ' + res[0]['title'] + '\n' + res[0]['entry'])
    elif searchChoice == 'd':
      clear()
      res = db.search(Query().date == input('Please enter the date:'))
      print(str(res[0]['id']) + ' - ' +res[0]['date'] + ' - ' + res[0]['title'] + '\n' + res[0]['entry'])
    elif searchChoice == 'l':
      clear()
      for item in db:
        print(str(item['id']) + ' - ' + item['date'] + ' - ' + item['title'] + '\n' + item['entry'])
    
  elif choice == 'd':
    clear()
    print('Please enter the id of the entry to delete:')
    db.remove(Query().id == input())

  elif choice == 'x':
    clear()
    print('Are you sure you want to delete all entries? (y/n)')
    if input() == 'y':
      db.truncate()
      clear()
      print('All entries deleted!')
      sleep(1)
      clear()
    else:
      clear()
      print('All entries not deleted!')
      sleep(1)
      clear()

  elif choice == 'q':
    print('Goodbye!')
    sleep(1)
    clear()
    break
