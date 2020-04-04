import os
import time

os.system("clear")
def Menu():
    print("""\033[31m
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      \033[92mCoded By Toxic - Omega

\033[37m[\033[31m1\033[37m] Install Metasploit
\033[37m[\033[31m2\033[37m] Install Nmap
\033[37m[\033[31m3\033[37m] Install Websploit
\033[37m[\033[31m4\033[37m] Install Hydra
\033[37m[\033[31m5\033[37m] Install SqlMap
\033[37m[\033[31mx\033[37m] Exit
""")
loop = True
while loop:
    Menu()
    what = input(">> ")
    if what == "x":
        os.system("ls")
        os.system("clear")
        exit
        break
    elif what == "1":
          os.system("clear")
          print("""\033[31m
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      \033[92mCoded By Toxic - Omega

\033[37m[\033[31m~\033[37m] Installing...
""")
          os.system("sudo apt-get install metasploit-framework postgresql")
          print(" ")
          print("\033[37m[\033[31m~\033[37m] To Start Metasploit Type 'msfconsole' In Terminal")
          time.sleep(5)
          os.system("clear")
    elif what == "2":
          os.system("clear")
          print("""\033[31m
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      \033[92mCoded By Toxic - Omega

\033[37m[\033[31m~\033[37m] Installing...
""")
          os.system("sudo apt-get install nmap")
          print(" ")
          print("\033[37m[\033[31m~\033[37m] To Start Nmap Type 'nmap' In Terminal")
          time.sleep(5)
          os.system("clear")
    elif what == "3":
          os.system("clear")
          print("""\033[31m
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      \033[92mCoded By Toxic - Omega

\033[37m[\033[31m~\033[37m] Installing...
""")
          os.system("sudo apt-get install websploit")
          print(" ")
          print("\033[37m[\033[31m~\033[37m] To Start Websploit Type 'websploit' In Terminal")
          time.sleep(5)
          os.system("clear")
    elif what == "4":
          os.system("clear")
          print("""\033[31m
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      \033[92mCoded By Toxic - Omega

\033[37m[\033[31m~\033[37m] Installing...
""")
          os.system("sudo apt-get install hydra")
          print(" ")
          print("\033[37m[\033[31m~\033[37m] To Start Hydra Type 'hydra' In Terminal")
          time.sleep(5)
          os.system("clear")
    elif what == "5":
          os.system("clear")
          print("""\033[31m
╦  ┬┌┐┌┬ ┬─┐ ┬       ╔╦╗┌─┐┌─┐┬  ┌─┐
║  │││││ │┌┴┬┘  ───   ║ │ ││ ││  └─┐
╩═╝┴┘└┘└─┘┴ └─        ╩ └─┘└─┘┴─┘└─┘
      \033[92mCoded By Toxic - Omega

\033[37m[\033[31m~\033[37m] Installing...
""")
          os.system("sudo apt-get install sqlmap")
          print(" ")
          print("\033[37m[\033[31m~\033[37m] To Start Sqlmap Type 'sqlmap' In Terminal")
          time.sleep(5)
          os.system("clear")
          
