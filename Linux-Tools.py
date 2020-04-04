import os
import time

def Menu():
    print("""\033[31m
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      \033[92mCoded By Toxic - Omega

\033[37m[\033[31m1\033[37m] Install Metasploit
\033[37m[\033[31m2\033[37m] Install
\033[37m[\033[31m3\033[37m] Install
\033[37m[\033[31mx\033[37m] Exit
""")
loop = True
while loop:
    Menu()
    what = input(">> ")
#------------------------------------------------------------------------------
    if what == "x":
        os.system("ls")
        os.system("clear")
        exit
        break
#------------------------------------------------------------------------------
    elif what == "1":
          os.system("clear")
          print("""
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      Coded By Toxic - Omega

[~] Installing...
""")
          os.system("sudo apt-get install metasploit-framework postgresql")
          print(" ")
          print("[~] To Start Metasploit Type metasplot In Terminal")
          Menu()