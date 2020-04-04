import os
import time

def Menu():
    print("""
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      Coded By Toxic - Omega

[1] Install Metasploit
[2] Install
[3] Install
[x] Exit
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
          Menu()