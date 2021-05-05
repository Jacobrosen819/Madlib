import random
import sqlite3
import random_words
import os
import time

#creating table/ databse
conn = sqlite3.connect("Madlibs.db")

cursor = conn.cursor() #create  CURSOR

#CREATe a table
cursor.execute ("""CREATE TABLE madlibs (
    title text,
    print_madlib text,
    date text
    )""")
#commit to database
conn.commit()

#conn close

conn.close()




#random_words.py varibales
ran_past_tense_verbs = random_words.ran_past_tense_verbs
ran_present_tense_verbs = random_words.ran_present_tense_verbs
ran_future_tense_verbs = random_words.ran_future_tense_verbs
ran_adjectives = random_words.ran_adjectives
ran_nouns = random_words.ran_nouns
ran_proper_nouns = random_words.ran_proper_nouns
ran_adverbs  = random_words.ran_adverbs
ran_pronouns = random_words.ran_pronouns
#print(random.choice())

class Madlibs:
  def __init__(self, how_it_works, madlib_1, madlib_2, madlib_3):
    self.how_it_works = how_it_works
    self.madlib_1= madlib_1
    self.madlib_2 = madlib_2
    self.madlib_3 = madlib_3
  def how_it_works():
    game = str(input ("We have prepared for you 3 madlibs. Please do all 3 madlibs, we have included features such as random choice where it will fill out the madlibs for you from a random set of words. You can also save any madlibs into a sql database and retrive them at anytime. To leave the game just type 'leave' here to quit the game. Which mad lib would you like to play 1, 2, or 3? "))
    if game == "1":
      Madlibs.madlib_1()
    elif game == "2":
      Madlibs.madlib_2()
    elif game == "3":
      Madlibs.madlib_3()
    elif game == "leave":
      # for windows
      # os.system('cls')
      os.system("ls")
      time.sleep(2)
      # Ubuntu version 10.10
      os.system('clear')
      
    

  def madlib_1 ():
    # Here the user inputs thier words
    random_word_filler = input("Do you want to fill in your own words, type yes (if you dont want to type any charecter and we will return a randomly genrated madlib)? ")
    if random_word_filler == "yes":
      adjective1 = input("Adjective: ")
      noun1 = input("Noun: ")
      verb1_past = input("A past tense verb: ")
      adverb1 = input("Adverb: ")
      adjective2 = input("Adjective: ")
      noun2 = input("Noun: ")
      noun3 = input("Noun: ")
      adjective3 = input("Adjective: ")
      verb2 = input("A present tense verb: ")
      adverb2 = input("Adverb: ")
      verb3_past = input("A past tense verb: ")
      adjective4 = input("Adjective: ")
      # we determine id it is a or an before teh adjectives
      if adjective1.startswith("a") or adjective1.startswith("e") or adjective1.startswith("i") or adjective1.startswith("o") or adjective1.startswith("U"):
        a_an1 = "an"
      else:
        a_an1 = "a"
      if adjective3.startswith("a") or adjective3.startswith("e") or adjective3.startswith("i") or adjective3.startswith("o") or adjective3.startswith("U"):
        a_an2 = "an"
      else:
        a_an2 = "a"
      print_madlib = "Today I went to the zoo. I saw" + " " + a_an1 +" "+ adjective1 + " " + noun1 + " jumping up and down in its tree. He " + verb1_past + " " + adverb1 +  " through the large tunnel that led to its " + adjective2 + " " + noun2 + " . I got some peanuts and passed them through the cage to a gigantic gray " + noun3 + " towering above my head. Feeding that animal made me hungry. I went to get " + a_an2 + " " + adjective3 + " scoop of ice cream. It filled my stomach. Afterwards I had to "+ verb2 + " " + adverb2 + " to catch our bus. When I got home I " + verb3_past + " my mom for a " + adjective4 + " day at the zoo."
      title = "A day at the zoo!!!"
      print(title)
      print("\n")
      print(print_madlib)
      play_again = input("would you like to play again, yes, or no?")
      if play_again == "y" or play_again == "yes":
        print("\n")
        return Madlibs.how_it_works()
      else:
        # for windows
        # os.system('cls')
        os.system("ls")
        time.sleep(2)
        # Ubuntu version 10.10
        os.system('clear')
    else:
      adjective1 = random.choice(ran_adjectives)
      noun1 = random.choice(ran_nouns)
      verb1_past = random.choice(ran_past_tense_verbs)
      adverb1 = random.choice(ran_adverbs)
      adjective2 = random.choice(ran_adjectives)
      noun2 = random.choice(ran_nouns)
      noun3 = random.choice(ran_nouns)
      adjective3 = random.choice(ran_adjectives)
      verb2 = random.choice(ran_present_tense_verbs)
      adverb2 = random.choice(ran_adverbs)
      verb3_past = random.choice(ran_past_tense_verbs)
      adjective4 = random.choice(ran_adjectives)
      # we determine id it is a or an before teh adjectives
      if adjective1.startswith("a") or adjective1.startswith("e") or adjective1.startswith("i") or adjective1.startswith("o") or adjective1.startswith("U"):
        a_an1 = "an"
      else:
        a_an1 = "a"
      if adjective3.startswith("a") or adjective3.startswith("e") or adjective3.startswith("i") or adjective3.startswith("o") or adjective3.startswith("U"):
        a_an2 = "an"
      else:
        a_an2 = "a"
      print_madlib = "Today I went to the zoo. I saw" + " " + a_an1 +" "+ adjective1 + " " + noun1 + " jumping up and down in its tree. He " + verb1_past + " " + adverb1 +  " through the large tunnel that led to its " + adjective2 + " " + noun2 + " . I got some peanuts and passed them through the cage to a gigantic gray " + noun3 + " towering above my head. Feeding that animal made me hungry. I went to get " + a_an2 + " " + adjective3 + " scoop of ice cream. It filled my stomach. Afterwards I had to"+ verb2 + " " + adverb2 + " to catch our bus. When I got home I " + verb3_past + " my mom for a " + adjective4 + " day at the zoo."
      title = "A day at the zoo!!!"
      print(title)
      print("\n")
      print(print_madlib)
      play_again = input("would you like to play again, yes, or no?")
      if play_again == "y" or play_again == "yes":
        print("\n")
        return Madlibs.how_it_works()
      else:
        # for windows
        # os.system('cls')
        os.system("ls")
        time.sleep(2)
        # Ubuntu version 10.10
        os.system('clear')

  def madlib_2 ():
    # Here the user inputs thier words
    random_word_filler = input("Do you want to fill in your own words, type yes (if you dont want to type any charecter and we will return a randomly genrated madlib)? ")
    if random_word_filler == "yes":
      adjective1 = input("ADjective: ")
      plural_noun1 = input("Plural noun: ")
      noun2 = input("Noun: ")
      adverb1 = input("Adverb: ")
      number1 = input("Number: ")
      past_tense_verb1 = input("Past tense verb: ")
      est_adjective = input("Est adjective: ")
      past_tense_verb2 = input("Past tense verb: ")
      adverb2 = input("Adverb: ")
      adjective2 = input("Adjective: ")

      if adjective1.startswith("a") or adjective1.startswith("e") or adjective1.startswith("i") or adjective1.startswith("o") or adjective1.startswith("U"):
        a_an1 = "an"
      else:
        a_an1 = "a"
      if adjective2.startswith("a") or adjective2.startswith("e") or adjective2.startswith("i") or adjective2.startswith("o") or adjective2.startswith("U"):
        a_an2 = "an"
      else:
        a_an2 = "a"
      print_madlib = "Today, my fabulous camp group went to a " + a_an1 + adjective1 + " amusement park. It was a fun park with lots of cool " + plural_noun1 + " and enjoyable play structures. When we got there, my kind counselor shouted loudly, \"Everybody off the " + noun2 + " \" We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I " + adverb1 + " ran over to get in the long line that had about" + number1 + " people in it. When I finally got on the roller coaster I was" + past_tense_verb1 + ". In fact I was so nervous my two knees were knocking together. This was them " + est_adjective + " ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little " + past_tense_verb2 + " but I was proud of myself. The rest of the day went "  + adverb2 + ". It was " + a_an2 + " " + adjective2 +" day at the fun park."
      print(print_madlib)
      play_again = input("would you like to play again, yes, or no?")
      if play_again == "y" or play_again == "yes":
        print("\n")
        return Madlibs.how_it_works()
      else:
        # for windows
        # os.system('cls')
        os.system("ls")
        time.sleep(2)
        # Ubuntu version 10.10
        os.system('clear')
    else:
        adjective1 = random.choice(ran_adjectives)
        plural_noun1 = random.choice(ran_nouns) + "s"
        noun2 = random.choice(ran_nouns)
        adverb1 = random.choice(ran_adverbs)
        number1 = str(random.randint)
        past_tense_verb1 = random.choice(ran_past_tense_verbs)
        est_adjective = random.choice(ran_adjectives) + "est"
        past_tense_verb2 = random.choice(ran_past_tense_verbs)
        adverb2 = random.choice(ran_adverbs)
        adjective2 = random.choice(ran_adjectives)
        if adjective1.startswith("a") or adjective1.startswith("e") or adjective1.startswith("i") or adjective1.startswith("o") or adjective1.startswith("U"):
            a_an1 = "an"
        else:
            a_an1 = "a"
        if adjective2.startswith("a") or adjective2.startswith("e") or adjective2.startswith("i") or adjective2.startswith("o") or adjective2.startswith("U"):
            a_an2 = "an"
        else:
            a_an2 = "a"
            print_madlib = "Today, my fabulous camp group went to a " + a_an1 + adjective1 + " amusement park. It was a fun park with lots of cool " + plural_noun1 + " and enjoyable play structures. When we got there, my kind counselor shouted loudly, \"Everybody off the " + noun2 + " \" We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I " + adverb1 + " ran over to get in the long line that had about" + number1 + " people in it. When I finally got on the roller coaster I was" + past_tense_verb1 + ". In fact I was so nervous my two knees were knocking together. This was them " + est_adjective + " ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little " + past_tense_verb2 + " but I was proud of myself. The rest of the day went "  + adverb2 + ". It was " + a_an2 + " " + adjective2 +" day at the fun park."
            print(print_madlib)
        play_again = input("would you like to play again, yes, or no?")
        if play_again == "y" or play_again == "yes":
            print("\n")
            return Madlibs.how_it_works()
        else:
            #for windows
            # # os.system('cls')
            os.system("ls")
            time.sleep(2)
            # Ubuntu version 10.10
            os.system('clear')
  def madlib_3 ():
        random_word_filler = input("Do you want to fill in your own words, type yes (if you dont want to type any charecter and we will return a randomly genrated madlib)? ")
        if random_word_filler == "yes":
            plur_noun1 = input("Plural Noun: ")
            plur_noun2 = input("Plural Noun: ")
            verb1 = input("Verb: ")
            noun3 = input("Noun: ")
            verb_ing_2 = input("Ing verb: ")
            plur_noun3 = input("Plural Noun: ")
            noun4 = input("Noun: ")
            plur_noun4 = input("Plural Noun: ")
            print_madlib = "When I go to the arcade with my " + plur_noun1 + " there are lots of games to play. I spend lots of time there with my friends. In the game X-Men you can be different " + plur_noun2 + ". The point of the game is to " + verb1 + " every robot. You also need to save people. Then you can go to the next level. \nIn the game Star Wars you are Luke Skywalker and you try to destroy every " + noun3 + ". In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are " + verb_ing_2 + " against. \nThere are a whole lot of other cool games. When you play some games you win " + plur_noun3 + " for certain scores. Once you're done you can cash in your tickets to get a big " + noun4 + ". You can save your " + plur_noun4 +  " for another time. When I went to this arcade I didn\'t believe how much fun it would be. So far I have had a lot of fun every time I've been to this great arcade!"
            print(print_madlib)
            play_again = input("would you like to play again, yes, or no?")
            if play_again == "y" or play_again == "yes":
                print("\n")
                return Madlibs.how_it_works()
            else:
                #for windows
                # # os.system('cls')
                os.system("ls")
                time.sleep(2)
                # Ubuntu version 10.10
                os.system('clear')
        else:
            plur_noun1 = random.choice(ran_nouns) + "s"
            plur_noun2 = random.choice(ran_nouns) + "s"
            verb1 = random.choice(ran_present_tense_verbs)
            noun3 = andom.choice(ran_nouns)
            verb_ing_2 = random.choice(ran_present_tense_verbs) + "ing"
            plur_noun3 = random.choice(ran_nouns) + "s"
            noun4 = andom.choice(ran_nouns)
            plur_noun4 = random.choice(ran_nouns) + "s"
            print_madlib = "When I go to the arcade with my " + plur_noun1 + " there are lots of games to play. I spend lots of time there with my friends. In the game X-Men you can be different " + plur_noun2 + ". The point of the game is to " + verb1 + " every robot. You also need to save people. Then you can go to the next level. \nIn the game Star Wars you are Luke Skywalker and you try to destroy every " + noun3 + ". In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are " + verb_ing_2 + " against. \nThere are a whole lot of other cool games. When you play some games you win " + plur_noun3 + " for certain scores. Once you're done you can cash in your tickets to get a big " + noun4 + ". You can save your " + plur_noun4 +  " for another time. When I went to this arcade I didn\'t believe how much fun it would be. So far I have had a lot of fun every time I've been to this great arcade!"
            print(print_madlib)
            play_again = input("would you like to play again, yes, or no?")
            if play_again == "y" or play_again == "yes":
                print("\n")
                return Madlibs.how_it_works()
            else:
                # for windows
                # # os.system('cls')
                os.system("ls")
                time.sleep(2)
                # Ubuntu version 10.10
                os.system('clear')






Madlibs.how_it_works()