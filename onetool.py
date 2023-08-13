#!bin/python3
# Code By : Cyb3rArjun
# Github  : https://github.com/Cyb3rArjun

import os
import sys
import subprocess

#color
red = "\033[31m"
green = "\033[32m"
orange = "\033[33m"
nc = "\033[36m"

#version
version = "0.1.0"
#editior
codeby="Cyb3rArjun"
opkg="x11-repo"

def cls():
  if sys.platform.startswith('win'):
      subprocess.run('cls', shell=True)
  else:
     subprocess.run('clear', shell=True)
     
def linux_pkg(lpkg):
  os.system("apt install {lpkg} -y")

def update():
   
    print(f"{orange}Update Tool")
    print("")
    print("This will update the tool from the git repo.")
    print("Any changes made to the tool will be overwritten.")
    os.system("sleep 2")
    print("")
    print("Are you sure you want to update the tool?")
    ans = input("[Y/N] ").lower()
    if ans == "y":
        subprocess.run(["git", "pull"])
        print("Tool updated successfully!")
        os.system("sleep 2")
    else:
        print("Update cancelled.")

def pkg_install(pkg):
  print(f"{green} {pkg} installing ....")
  os.system("apt install {pkg} -y ")
  os.system("sleep 2")
  os.system("clear")
  print(f"{green}Successfully Install !")
  print(f"{orange}Now Type {pkg} on your Terminal ")
     
def logo():
  print(f"""     
               █▀█ █▄░█ █▀▀ ▄▄ ▀█▀ █▀█ █▀█ █░░
               █▄█ █░▀█ ██▄ ░░ ░█░ █▄█ █▄█ █▄▄
                         {red}Version :{nc} {version} {nc}
                         {red}CodeBy  :{nc} {codeby} {nc}
                         {red}Github  :{nc} https://github.com/AlockDj{nc}             
                                                                    
                                                                    """)
def menu():
  print(f"""{nc}============Main Menu============{nc}""")
  print("")
  print(f"{nc}01) Fun Script ")
  print(f"{nc}02) Programming Language ")
  print(f"{nc}03) All Hacking Tools ")
  print(f"{nc}04) Update System ")
  print(f"{nc}05) Exit ")
  
  ent=input(">>>")
  if ent=="01" or ent=="1":
    cls()
    funscript()
   
  
  elif ent=="02" or ent=="2":
     cls()
     language()
     
  elif ent=="03" or ent=="3":
     cls()
     alltool()
     
  elif ent=="04" or ent=="4":
     cls()
     update()
     
  elif ent=="05" or ent=="5":
     exit()
              
  else:
     print("Wrong Enter Pleas input Available options !")
     cls()
     logo()
     menu()
  

def alltool_install(ati):
   print(f"{green} {ati} installing ....")
   os.system("apt update -y && apt upgrade -y")
   os.system("apt install {ati} -y ")
   os.system("sleep 2")
   os.system("clear")
   print(f"{green}Successfully Install !")
   print(f"{orange}Now Type {ati} on your Terminal ")
     
   
def funscript():
  print(f"""{nc}===========Fun Script==========""")
  print(f"{nc}01) sl {red}(Simulate Train)")
  print(f"{nc}02) fortune {red}(Random Quotes)")
  print(f"{nc}03) rev {red}(Reverse Every Text)")
  print(f"{nc}04) cowsay {red}(cow customizable message)")
  print(f"{nc}05) cmatrix {red} (Matrix in terminal)")
  print(f"{nc}06) oneko {red} (small animated cat ")
  print(f"{nc}07) aafire {red} (fire animation on terminal)")
  print(f"{nc}00) Back ")
    
  opt=input(">>>")
  if opt=="01" or opt=="1":
    cls()
    pkg="sl"
    pkg_install(pkg)
      
  elif opt=="02" or opt=="2":
      cls()
      pkg="fortune"
      pkg_install(pkg)
      
  elif opt=="03" or opt=="3":
      cls()
      pkg="rev"
      pkg_install(pkg)
      
  elif opt=="04" or opt=="4":
      cls()
      pkg="cowsay"
      pkg_install(pkg)
      
  elif opt=="05" or opt=="5":
      cls()
      pkg="cmatrix"
      pkg_install(pkg)
      
  elif opt=="06" or opt=="6":
      cls()
      lpkg=opkg
      pkg="oneko"
      linux_pkg(lpkg)
      pkg_install(pkg)

      
  elif opt=="07" or opt=="7":
     cls()
     lpkg=opkg
     pkg="aafire"
     linux_pkg(lpkg)
     pkg_install(pkg)
      
  elif opt=="00" or opt=="0":
      cls()
      menu()
    
  else:
      print("Wrong Enter! please input available option")   
      cls()
      os.system("sleep 1")
      funscript()
      

   
def language():
  print(f"""{nc}===========*Programming Language*==========""")
  print(f"{nc}01) Python 2 ")
  print(f"{nc}02) Python 3")
  print(f"{nc}03) C/C++       ")
  print(f"{nc}04) D ")
  print(f"{nc}05) Dart ")
  print(f"{nc}06) Elixir")
  print(f"{nc}07) Erlang")
  print(f"{nc}08) Forth")
  print(f"{nc}09) Go ")
  print(f"{nc}10) Groovy")
  print(f"{nc}11) OpenJDk")
  print(f"{nc}12) NodeJS")
  print(f"{nc}13) Kotlin")
  print(f"{nc}14) Lua")
  print(f"{nc}15) Perl")
  print(f"{nc}16) PHP")
  print(f"{nc}17) Racket ")
  print(f"{nc}18) Ruby")
  print(f"{nc}19) Rust")
  print(f"{nc}20) Scala")
  print(f"{nc}21) Swift")
  print(f"{nc}22) MariaDB")
  print(f"{nc}23) Postgresql")
  print(f"{nc}00) Back ")
    
  opt=input(">>>")
  if opt=="01" or opt=="1":
    cls()
    pkg="python 2"
    pkg_install(pkg)
      
  elif opt=="02" or opt=="2":
      cls()
      pkg="python"
      pkg_install(pkg)
      
  elif opt=="03" or opt=="3":
      cls()
      pkg="clang"
      pkg_install(pkg)
      
      
  elif opt=="04" or opt=="4":
      cls()
      pkg="ldc"
      pkg_install(pkg)
      
  elif opt=="05" or opt=="5":
      cls()
      pkg="dart"
      pkg_install(pkg)
      
  elif opt=="06" or opt=="6":
     cls()
     pkg="elixir"
     pkg_install(pkg)
      
  elif opt=="07" or opt=="7":
      cls()
      pkg="erlang"
      pkg_install(pkg)

  elif opt=="08" or opt=="8":
      cls()
      pkg="pforth"
      pkg_install(pkg)


  elif opt=="09" or opt=="9":
      cls()
      pkg="golang"
      pkg_install(pkg)


  elif opt=="10":
      cls()
      pkg="groovy"
      pkg_install(pkg)

  elif opt=="11":
      cls()
      pkg="openjdk"
      pkg_install(pkg)

  elif opt=="12":
      cls()
      lpkg=ppkg
      linux_pkg(lpkg)
      pkg="nodejs"
      pkg_install(pkg)

  elif opt=="13":
      cls()
      pkg="kotlin"
      pkg_install(pkg)

  elif opt=="14":
      cls()
      pkg="lua"
      pkg_install(pkg)

  elif opt=="15":
      cls()
      pkg="perl"
      pkg_install(pkg)

  elif opt=="16":
      cls()
      pkg="php"
      pkg_install(pkg)

  elif opt=="17":
      cls()
      pkg="racket"
      pkg_install(pkg)

  elif opt=="18":
      cls()
      pkg="ruby"
      pkg_install(pkg)

  elif opt=="19":
      cls()
      pkg="rust"
      pkg_install(pkg)

  elif opt=="20":
      cls()
      pkg="scala"
      pkg_install(pkg)

  elif opt=="21":
      cls()
      pkg="swift"
      pkg_install(pkg)

  elif opt=="22":
      cls()
      pkg="mariadb"
      pkg_install(pkg)

  elif opt=="23":
      cls()
      pkg="postgresql"
      pkg_install(pkg)

  elif opt=="00" or opt=="0":
      cls()
      menu()
    
  else:
      print("Wrong Enter! please input available option")  
      os.system("clear") 
      cls()
      os.system("sleep 1")
      language()
      

  
def language():
  print(f"""{nc}===========*All Hacking Tools*==========""")
  print(f"{nc}01) Nmap")
  print(f"{nc}02) Metasploit")
  print(f"{nc}03) SQLMap      ")
  print(f"{nc}04) Hydra")
  print(f"{nc}05) ngrok")
  print(f"{nc}06) kali Nethunter")
  print(f"{nc}07) Red Hawk")
  print(f"{nc}08) IpGeoLocation")
  print(f"{nc}09) Angry Fuzzer")
  print(f"{nc}10) Weeman")
  print(f"{nc}11) Cupp")
  print(f"{nc}12) Routersploit")
  print(f"{nc}13) Infoga")
  print(f"{nc}14) ReconDog")
  print(f"{nc}15) MapEye")
  print(f"{nc}16) Easymap")
  print(f"{nc}17)  Crips")
  print(f"{nc}18) EvilUrl")
  print(f"{nc}19) striker")
  print(f"{nc}20) zphisher")
  print(f"{nc}21) sherlock")
  print(f"{nc}22) userrecon")
  print(f"{nc}23) PhoneInfoga")
  print(f"{nc}24) ADB-Toolkit")
  print(f"{nc}25) EagleEye")
  print(f"{nc}26) InSpy")
  print(f"{nc}27) WebSploit")
  print(f"{nc}28) sqlmate")
  print(f"{nc}29) XSStrike")
  print(f"{nc}30) Sn1per")
  print(f"{nc}31) Instahack")
  print(f"{nc}32) Crunch")
  print(f"{nc}33) Gemail-Hack")
  print(f"{nc}34) BurteX")
  print(f"{nc}35) brutespray")
  print(f"{nc}36) elpscrk")
  print(f"{nc}37) fbht")
  print(f"{nc}38) Aircrack-ng")
  print(f"{nc}39) wifite")
  print(f"{nc}40) Wifiphisher")
  print(f"{nc}41) apktool")
  print(f"{nc}42) jadx")
  print(f"{nc}43) A-rat")
  print(f"{nc}44) Commix")
  print(f"{nc}45) zerodoor")
  print(f"{nc}46) knockMail")
  print(f"{nc}47) Ettercap")
  print(f"{nc}48) hping3")
  print(f"{nc}49) tshark")
  print(f"{nc}50) dos2unix")
  print(f"{nc}51) Pdfinfo")
  print(f"{nc}52) SocialFish")
  print(f"{nc}53) LiteOTP")
  print(f"{nc}54)F4K#")
  print(f"{nc}55) Cookie-stealer")
  print(f"{nc}56) zphisher")
  print(f"{nc}57) Evilginx")
  print(f"{nc}58) ghost-Phisher")
  print(f"{nc}00) Back ")
    
  opt=input(">>>")
  if opt=="01" or opt=="1":
    cls()
    print(f"{orange} Installing Nmap ")
    os.system("apt update && apt upgrade")
    os.system("apt install nmap")
    print(f"{green} Successfully Install Nmap")
      
  elif opt=="02" or opt=="2":
      cls()
      print(f"{orange}wait 15-20 Mintes")
      print(f"{orange}It take 2GB storage on your Mobile ")
      os.system("apt update && apt upgrade")
      os.system("apt install wget curl openssh git -y")
      os.system("apt install ncurses-utils")
      os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x metasploit.sh")
      os.system("./metasploit.sh")
      os.system("rm -rf metasploit.sh")
      cls()
      print(f"{green} Now Type metasploit on Terminal ")
      
  elif opt=="03" or opt=="3":
      cls()
      print(f"{orange} Installing Wait...")
      os.system("apt update && apt upgrade -y")
      os.system("apt install git python3 -y")
      os.system("git clone https://github.com/sqlmapproject/sqlmap.git && cd sqlmap ")
      print(f"{green} type `python3 sqlmap.py` in terminal !")
          
  elif opt=="04" or opt=="4":
   cls()
   print(f"{orange} Installing hydra wait minutes...")
   os.system("apt update && apt upgrade -y && apt install git -y")
   os.system(" cd && git clone https://github.com/vanhauser-thc/thc-hydra")
   os.system("cd $HOME/thc-hydra && ./configure make && make install")
   cls()
   print(f"{green} Now type ./hydra in your terminal !")
      
  elif opt=="05" or opt=="5":
      cls()
      print(f"{orange} Installing Ngrok")
      os.system("apt install zip wget -y")
      os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
      os.system("unzip ngrok-stable-linux-arm.zip && chmod +x ngrok")
      cls()
      print(f"{green} type in your terminal ./ngrok authtoken <YOUR_AUTH_TOKEN_HERE> ")


  elif opt=="06" or opt=="6":
     cls()
     print(f"{orange} Installing Kali Nethunter ")
     print(f"{orange} At least 2GB storage required , and wait 20 minutes")
     os.system("termux-setup-storage && apt update && apt upgrade -y")
     os.system("apt install wget -y")
     os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr && chmod +x install-nethunter-termux && ./install-nethunter-termux")
     cls()
     print(f"{green} successfully Install Kali Nethunter ")



  elif opt=="07" or opt=="7":
      cls()
      print(f"{orange} Installing Red Hawk")
      os.system("apt update && apt upgrade -y")
      os.system("apt install git php -y && cd && git clone https://github.com/Tuhinshubhra/RED_HAWK")
      cls()
      print(f"{green} Successfully Install Red Hawk")

  elif opt=="08" or opt=="8":
      cls()
      print(f" {orange} Installing IPGeoLocation")
      os.system("apt update && apt upgrade -y && apt install git -y ")
      os.system("apt install python -y ")
      os.system("apt install python3-setuptools")
      os.system("cd && git clone https://github.com/maldevel/IPGeoLocation.git")
      os.system("cd IPGeoLocation pip3 install -r requirements.txt --user && pip install -r requirements.txt --user")
      cls()
      print(f"{green} Type your terminal ./ip2geolocation.py ")

  elif opt=="09" or opt=="9":
      cls()
      print(f"{orange} Installing Angry Fuzzer ")
      os.system("apt update && apt upgrade -y")
      os.system("apt install git python2 -y")
      os.system("cd && git clone https://github.com/ihebski/angryFuzzer")
      os.system("cd angryFuzzer && pip2 install -r requirements.txt && pip install requests")
      cls()
      print(f"{green} type your terminal python2 angryFuzzer.py -h")

  elif opt=="10":
      cls()
      print(f"{orange} Installing Weeman ")
      os.system("apt update && apt upgrade -y")
      os.system("apt install git python2 -y")
      os.system("cd && git clone  https://github.com/evait-security/weeman.git")
      print(f"{green} Successfully Install Weeman")

  elif opt=="11":
      cls()
      print(f"{orange} Installing CUPP")
      os.system("apt update && apt upgrade -y")
      os.system("apt install git python -y && cd")
      os.system("git clone https://github.com/Mebus/cupp ")
      cls()
      print(f"{green} Successfully Install CUPP")
  
  elif opt=="12":
      cls()
      print(f" {orange} Installing RouterSploit ")
      os.system("apt update && apt upgrade -y")
      os.system("cd && apt install git python3 -y")
      os.system("git clone https://github.com/threat9/routersploit")
      os.system("c routersploit && python3 -m pip install -r requirements.txt")
      cls()
      print(f"{green} Successfully Install RouterSploit ")
      print(f"{green} type your terminal python3 rsf.py")

  elif opt=="13":
      cls()
      print(f"{orange} Installing Infoga")
      os.system("apt update && apt upgrade -y")
      os.system("cd && apt install git python -y")
      os.system("git clone https://github.com/m4ll0k/Infoga.git && cd Infoga ")
      os.system("python setup.py install")
      cls()
      print(f"{green} Successfully Install Infoga")
      print(f"{green} Type Your terminal python infoga.py ")
  
  elif opt=="14":
      cls()
      print(f"{orange} Installing ReconDog")
      os.system("apt install && apt upgrade -y")
      os.system("cd && apt install git python -y")
      os.system("git clone https://github.com/s0md3v/ReconDog && cd ReconDog")
      os.system("pip install -r requirements.txt")
      cls()
      print("")

  elif opt=="15":
      cls()
   

  elif opt=="16":
      cls()
      pkg="php"
      pkg_install(pkg)

  elif opt=="17":
      cls()
      pkg="racket"
      pkg_install(pkg)

  elif opt=="18":
      cls()
      pkg="ruby"
      pkg_install(pkg)

  elif opt=="19":
      cls()
      pkg="rust"
      pkg_install(pkg)

  elif opt=="20":
      cls()
      pkg="scala"
      pkg_install(pkg)

  elif opt=="21":
      cls()
      pkg="swift"
      pkg_install(pkg)

  elif opt=="22":
      cls()
      pkg="mariadb"
      pkg_install(pkg)

  elif opt=="23":
      cls()
      pkg="postgresql"
      pkg_install(pkg)

  elif opt=="00" or opt=="0":
      cls()
      menu()
    
  else:
      print("Wrong Enter! please input available option")  
      os.system("clear") 
      cls()
      os.system("sleep 1")
      language()
      

logo()
menu()
