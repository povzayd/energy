import pyfiglet
#import os
import colorama
import termcolor
import webbrowser
import math
from colorama import init, Fore
from termcolor import colored
banner=pyfiglet.figlet_format( "CALCULATE HOW MUCH ENERGY YOU ARE" )
print(Fore.CYAN + banner + Fore.RESET)
#example syntax
#print(colored('Hello, World!', 'green', 'on_red'))
#print(Fore.YOURCOLOR + "LOL" + Fore.RESET)
print(colored("HEYY! YOU FORGOT TO CHECK OUT MY OTHER SOCIALS! NO WORRIES HERE THEY ARE :-",'cyan','on_red'))
print(Fore.MAGENTA + "INSTAGRAM📱: https://instagram.com/povzayd" + Fore.RESET)
print(Fore.RED + "YOUTUBE▶️: https://YouTube.com/@povzayd" + Fore.RESET)
print(Fore.CYAN + "X𝕏: https://x.com/povzayd" + Fore.RESET)
print(Fore.BLUE + "GITHUB</>: https://github.com/povzayd" + Fore.RESET)
print(Fore.GREEN + "IMAGINE YOUR MASS IN pg,ng,µg,mg,g,kg,t,Mt,Gt FORMAT AND ENTER THE CORRESPONDING VALUES" + Fore.RESET)
print(Fore.WHITE + "DETAILED PDF ABOUT MASS IS AVAILABLE IN THIS DIRECTORY" + Fore.RESET)
print(Fore.YELLOW + "TO GET LATEST UPDATES JUST EXECUTE 'git pull' command" + Fore.RESET)
print(Fore.LIGHTGREEN_EX + "UNITS OF MASS\n pg=picogram \n ng=nanogram \n ug= microgram \n mg=milligram \n g=gram \n kg=kilogram \n t=ton \n Mt=Megaton \n Gt=Gigaton \n" + Fore.RESET)
unit=str(input(Fore.MAGENTA + "Enter The Unit Of Your Mass :-" + Fore.RESET))
c=float(299792458)
#def energy()
#url="https://youtu.be/uAJlg8MDAlU"


if unit=="pg":
  print("pg selected as your unit")
if unit=="ng":
  print("ng selected as your unit")
if unit=="ug":
  print("µg selected as your unit")
if unit=="mg":
  print("mg selected as your unit")
if unit=="g":
  print("g selected as your unit")
if unit=="kg":
  print("kg selected as your unit")
if unit=="t":
  print("t selected as your unit")
if unit=="Mt":
  print("Mt selected as your unit")
if unit=="Gt":
  print("Gt selected as your unit")
else:
  unit=="kg"
#a=float(input("Enter your mass",'unit',":"))
# print("You're supposed to enter a numerical value here!")
#b=a*9*10000000000000000
#print("You're ",b,"Joules of Energy i.e enough to destroy this universe")
while True:
    try:
        a = float(input(Fore.YELLOW + f"Enter your mass ({unit}) :" + Fore.RESET))
        if a<0:
          print("AB DEKH TU BETE AB DEKH TU AB TU GAYA")
          url="https://youtu.be/uAJlg8MDAlU"
          import os
          os.system(f"am start -a android.intent.action.VIEW -d {url} > /dev/null 2>&1")
          
 # webbrowser.open_new_tab("(https://youtu.be/uAJlg8MDAlU)")
        else:
          break
    except ValueError:
        print(Fore.BLUE + "Invalid input. Please enter a number." + Fore.RESET)
#defining E dont add return b or then call using b=E() then do  print("Blalalalal",b,"blaaaaaaa")
def E():
  if unit=='pg':
    b=float(c*c*a/1000000000000000)
  elif unit=='ng':
    b=float(c*c*a/1000000000000)
  elif unit=='ug':
    b=float(c*c*a/1000000000)
  elif unit=='mg':
    b=float(c*c*a/1000000)
  elif unit=='g':
    b=float(c*c*a/1000)
  elif unit=='kg':
    b=float(c*c*a/1*1)
  elif unit=='t':
    b=float(c*c*a*1000)
  elif unit=='Mt':
    b=float(c*c*a*1000000)
  elif unit=='Gt':
    b=float(c*c*a*1000000000000)
  print(Fore.RED + "You're ",b,"Joules of Energy, So never Underestimate Yourself :)" + Fore.RESET) 
E()
#calling E dont delete this line man.
#b=E()
#l=math.sqrt(b/a)
#print("You're",b,"Joules of energy,with this amount of energy you can travel",l,"meters")
#if b is not None:
#  l = math.sqrt(b/a)
#  print("You're",b,"Joules of energy,with this amount of energy you can travel",l,"meters")
#else:
#  print("Error: Unable to calculate energy")
#os.system(f"am start -a android.intent.action.VIEW -d {url}")

#social media promotion 😂😂😂😂
"""url1="https://Instagram.com/povzayd"
url2="https://youtube.com/@povzayd"
url3="https://github.com/povzayd"
url4="https://x.com/povzayd/"
ask = input(Fore.GREEN + "DO YOU WANT TO CHECK OUT MY SOCIALS? y/n: " + Fore.RESET)

while True:
    try:
        if ask == 'y':
            import os
            print(" Enter 1 For Instagram \n Enter 2 For YouTube \n Enter 3 For GitHub \n Enter 4 For 𝕏")
            print("Press Enter Or Any Other Key To Exit")
            option = input("Enter Your Choice :")

            if option == '1':
                os.system(f"am start -a android.intent.action.VIEW -d {url1} > /dev/null 2>&1")
            elif option == '2':
                os.system(f"am start -a android.intent.action.VIEW -d {url2} > /dev/null 2>&1")
            elif option == '3':
                os.system(f"am start -a android.intent.action.VIEW -d {url3} > /dev/null 2>&1")
            elif option == '4':  # Open All nrn
                #urls = [url1, url2, url3, url4]
                #for url in urls:
                os.system(f"am start -a android.intent.action.VIEW -d {url4} > /dev/null 2>&1 &")
            else:
                print(Fore.MAGENTA + "Thanks For Using This Tool. Have A Great Day :)" + Fore.RESET)
                break
        else:
            print(Fore.MAGENTA + "Thanks For Using This Tool. Have A Great Day :)" + Fore.RESET)
            break
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Fore.RESET)
"""
url1 = "https://Instagram.com/povzayd"
url2 = "https://youtube.com/@povzayd"
url3 = "https://github.com/povzayd"
url4 = "https://x.com/povzayd/"
ask = input("DO YOU WANT TO CHECK OUT MY SOCIALS? y/n: ")

# ANSI escape code for blue text
blue = "\033[34m"
reset = "\033[0m"

while True:
    try:
        if ask == 'y':
            import os
            print(f"{blue}Enter 1 For Instagram \nEnter 2 For YouTube \nEnter 3 For GitHub \nEnter 4 For 𝕏{reset}")
            print(f"{blue}Press Enter Or Any Other Key To Exit{reset}")
            option = input("Enter Your Choice :")

            if option == '1':
                os.system(f"am start -a android.intent.action.VIEW -d {url1} > /dev/null 2>&1")
            elif option == '2':
                os.system(f"am start -a android.intent.action.VIEW -d {url2} > /dev/null 2>&1")
            elif option == '3':
                os.system(f"am start -a android.intent.action.VIEW -d {url3} > /dev/null 2>&1")
            elif option == '4':
                os.system(f"am start -a android.intent.action.VIEW -d {url4} > /dev/null 2>&1 &")
            else:
                print(f"{blue}Thanks For Using This Tool. Have A Great Day :){reset}")
                break
        else:
            print(f"{blue}Thanks For Using This Tool. Have A Great Day :){reset}")
            break
    except Exception as e:
        print(f"{blue}An error occurred: {e}{reset}")
