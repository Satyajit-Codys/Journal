#!/usr/bin/env python 
import random
import time

print("Hi Satyajit!!\n")
print("Your journal is loading........\n")
time.sleep(1)

quotes = {
    0: "The only thing that will make you happy is being happy with who you are, and not who people think you are. — Goldie Hawn",
    1: "The talent for being happy is appreciating and liking what you have, instead of what you don’t have. — Woody Allen",
    2: "The art of being happy lies in the power of extracting happiness from common things. — Henry Ward Beecher",
    3: "Happiness cannot be traveled to, owned, earned, worn or consumed. Happiness is the spiritual experience of living every minute with love, grace, and gratitude. — Denis Waitley",
    4: "Happiness is not something you postpone for the future; it is something you design for the present. — Jim Rohn",
    5: "There is only one happiness in this life, to love and be loved. — George Sand",
    6: "Happiness is a choice. You can choose to be happy. There’s going to be stress in life, but it’s your choice whether you let it affect you or not. — Valerie Bertinelli",
    7: "Happiness radiates like the fragrance from a flower and draws all good things towards you. — Maharishi Mahesh Yogi",
    8: "Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared. — Buddha",
    9: "Happiness doesn’t depend on any external conditions, it is governed by our mental attitude. — Dale Carnegie"
}

time.sleep(5)
print(quotes[random.randint(0,9)])
date = input("\n Enter Today's Date to Continue: ")
f = open(date+".txt", "a")
f.write("\nWake up time: " + input("\nWhen you wake up today? "))

time.sleep(1)
havePlan = input("\nDid you have a plan for the day when you wake up? (yes/no) ")
f.write("\nHave plan for the day: " + havePlan)

if havePlan=="yes":
  print("\nGreat; Keep it up.")
else:
  reasonForNoPlan = input("\nWhat stopped you from doing that? ")
  f.write("\nReason for not having plan: " + reasonForNoPlan)

time.sleep(2)
learnToday = input("\n What did you learn today? ")
if "nothing" in learnToday:
  print("Buddy are you okay? I  just recognize you said nothing in your answer.  Everyday we learn something new, sometimes even we don't realize that we are learning; but learning.")
f.write("\nLearned Today: " + learnToday)

print("\nSpecial Question Coming Up...")
for i in range(5):
  print("................")
  time.sleep(1)
f.write("\nMoment of Happiness: " + input("\n What was the truest moment of happiness for you today? ") )

print("\nSaving your Happiness...")
for i in range(2):
  print("................")
  time.sleep(1)
f.write("\nMoment of sadness: " + input("\n What was the biggest moment of unhappiness for you today? ") )

print("\nConverting your unhappiness to happiness.....")
for i in range(3):
  print("........")
  time.sleep(1)
print("Done")

helpSomeone = input("\nDid you help someone in anyway? (yes/no)+answer")
if "yes" in helpSomeone:
  print("If someone deserves thanks!!  It's you Subha")
else:
  print("Always help someone. You might be the only one who does.")
f.write("\n Helped Someone: " + helpSomeone)

timelyEat = input("\n Did you eat on time throughout the day? (yes/no)")
f.write("\nEat on time: " + timelyEat)
if timelyEat == "no":
  f.write("\n Reason for not eating on time: " + input("\n Why not?"))
  print("\nUnderstanding Your reason.....")
  time.sleep(1)

thinkMost = input("\nWho did you think about most today? ")
f.write("\nMost thought person: " + thinkMost)
f.write("\n Reason for thinking: " + input("What about {} did you think?".format(thinkMost)))

isAngry =  input("Is there any situation when you got angry? (yeas/no) ")
f.write("\nAny situation of Anger: " + isAngry)
if isAngry == "yes":
  f.write("\n Reason for Anger: " + input("\n What made you angry? "))
  f.write("\n React to the anger: " + input("\nHow did you react to this situation? "))
  f.write("\n Able to Control Temper: " + input("\nWere you able to control your temper? "))

f.write("\nReading: " + input("\nWhat did you read today?"))
f.write("\n More about readings: " + input("\n Tell me more about your readings....."))

f.write("\nMusic: " + input("\nWhat music did you listen to? "))
print("\nThanks for sharing. One day you will pat on yourself for this.\nlike this .....")
for i in range(5):
  print("Sabbas.... ")
  time.sleep(1)

f.write("\nTomorrow's Plan: " + input("\n\n So What's your plan for tomorrow? "))
print("Great Plan. Keep up the fire.")
time.sleep(1)

print("\nNow the Great part coming in....\n\n“Gratitude is the healthiest of all human emotions. The more you express gratitude for what you have, the more likely you will have even more to express gratitude for.” —Zig Ziglar")
f.write("\nThankful: " + input("What are you thankful for ?"))
print("Take Care Satyajit....")

f.close()
