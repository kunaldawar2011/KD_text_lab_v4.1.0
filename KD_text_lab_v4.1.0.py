import time 
import colorama
import random
from colorama import Fore, Back, Style
a = "KD TEXT LAB v4.1.0"
time1 = time.time()
print(Fore.BLUE + str(a.center(50, "-")))
ques1 = input("enter your name to continue: " + Fore.RESET)
print(Fore.CYAN + "welcome", ques1 + Fore.RESET)
print(Fore.RED + Back.WHITE  + "what you want to do \n1. edit text & experiment\n2. exit" + Fore.RESET + Back.RESET)
try:
  ques2 = int(input("enter only in numbers: "))
  if ques2 == 1:
    print(Fore.BLACK + Back.WHITE +  "Loading sys..." + Fore.RESET + Back.RESET)
    time.sleep(0.3)
    n = random.randint(1, 30)
    for i in range(1, n+1):
      time.sleep(0.23)
      print("#"*i)
    print("system loaded sucessfully")
    text = input(Fore.GREEN + "enter text to edit: ")
    print("text saved" + Fore.RESET)
    while True:
      print(Fore.RED + "1. count text" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.MAGENTA + "2. capital all text" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.BLUE + "3. uncapital all text" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.YELLOW + "4. reverse text" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.GREEN + "5. count words" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.RED + "6. test is the alphabet is in sentence it may write true or false weheter the condition..." + Fore.RESET)
      time.sleep(0.1)
      print(Fore.MAGENTA + "7. test the sentence is there is a number it may write true or false" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.CYAN + "8. split test" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.RED + "9. swap case it will convert capital to small and small to capital" + Fore.RESET)
      print(Fore.MAGENTA + "10. title it will captial the first letter of sentence")
      time.sleep(0.1)
      print(Fore.GREEN + "11. captilize it will capital  first letter of sentence" + Fore.RESET)
      time.sleep(0.1)
      print(Fore.BLUE + "12. Find a alphabet or number it will find alphabet and number symobol etc. " + Fore.RESET)
      time.sleep(0.1)
      print(Fore.WHITE + "13. time used this app? " + Fore.RESET)
      time.sleep(0.1)
      print(Fore.RED + Back.YELLOW + "14. Exit" + Fore.RESET + Back.RESET)
      try:
        ques3 = int(input(Fore.CYAN + "enter only in number: " + Fore.RESET))
        match ques3:
          case 1:
            print("text counted: ", len(text))
          case 2:
            print(text.upper())
          case 3:
            print(text.lower())
          case 4:
            print(text[::-1])
          case 5:
            print("text counted: ", len(text.split()))
          case 6:
            print(text.strip().isalpha())
          case 7:
                 print(text.strip().isdigit())
          case 8:
            print(text.split())
          case 9:
            print(text.swapcase())
          case 10:
            print(text.title())
          case 11:
            print(text.capitalize())
          case 12:
            f = input("enter text to find: ")
            if f in text:
              time.sleep(0.70)
              
              print("text founded: ", text.find(f))
            else:
              print("text not found")
          case 13:
            time2 = time.time()
            print(Fore.RED + f"you used this app in seconds {round(time2 - time1)}" + Fore.RESET)
          case 14:
            print("exiting")
            break
          case _:
            print("invalid input")
      except ValueError:
        print("you write wrong number")
  elif ques2 ==  2:
    time.sleep(0.25)
    
    print("exiting")
    exit()
except ValueError:
  print("you write alphabet or give space")            