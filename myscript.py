### path: /home/hacker/Bureau/python/myscripyt.py ###
### codage : "UTF-8" ###
### Coded BY : Z3RF-003 ###
### Script name : All_In_One ###

#import modules
import  urllib
from urllib import parse
import urllib.request
import socket
import pickle
import os 
import colorama
from colorama import init,Fore 
import sys 
import platform
from platform import system
import requests
from bs4 import  BeautifulSoup
import lxml.html
import json
import  time
import random
import re

#fonction to get website IP's
def MassIPScanner():
  
    #get the path from the user
    path = input(Fore.YELLOW+'[#] Enter the path of the file : '+ Fore.LIGHTWHITE_EX)
  
    #checking that is a correct path
    if os.path.exists(path):
        try:
            with open(path, "rb") as file:
                try:
                    if os.path.isfile(path):
                        my_pick = pickle.Unpickler(file)
                        loading = my_pick.load()
                except KeyError:
                    pass
        except pickle.UnpicklingError:
            pass
        #if it's  directory we output an error msg and try again
        except IsADirectoryError:
            print(Fore.RED+"[-] It's a directory, enter a path of a file")
            error = input(Fore.YELLOW+'[#] Please, rerun the option by typing (r/R): '+Fore.LIGHTWHITE_EX )
            while True:
                if error == "r" or error == "R":
                    return MassIPScanner()
                if error != "r" or error != "R":
                    print(Fore.RED+'[-] Error, enter (r) Or (R)')
                    error = input(Fore.YELLOW+'[#] Please, rerun the option by typing (r/R): '+Fore.LIGHTWHITE_EX )
                    continue
  
   #if the path is wrong we output an error msg than try again             
    else:
        print(Fore.RED+"[-] Error, can't find path")
        error = input(Fore.YELLOW+"[#] Please, rerun the options by typing (r/R):"+Fore.LIGHTWHITE_EX)
        while True:
            if error == "r" or error == "R":
                return MassIPScanner()
            if error != "r" or error != "R":
                print(Fore.RED+"[-] Error, enter (r) Or (R)") 
                error = input(Fore.YELLOW+"[#] Please, rerun the option by typing (r/R):"+Fore.LIGHTWHITE_EX)
                continue
  
   #get the ip of the servers in thefile inputed
    file = open(path, "rb")
   #split lines in the file 
    lines = file.read().splitlines()
    count = 0 
    print(Fore.RED +"\n------------"+ Fore.CYAN +"[SCANNING FOR IP\'S, PLEASE WAIT]"+Fore.RED+"------------")
    time.sleep(1.5)
 
    for i in lines:
        i = i.decode("utf-8")
        if i.startswith('http'):
            try:
                req = requests.get(i)
                if req.status_code == 200:
                    split_url = parse.urlsplit(i)
                    ip_addr = socket.gethostbyname(split_url.netloc)
                    with open('HostsIP.txt', "a") as file:
                        file.write(ip_addr + "\n")  
                    #a = i.decode('utf-8')
                    ip_addr = Fore.CYAN + ip_addr
                    i = Fore.CYAN + i
                    arrow =Fore.RED + '====>'
                    string = Fore.GREEN + "[IP FOUND]"+" "+ i+" "+ arrow+" "+ip_addr
                    if ip_addr == '0.0.0.0':  
                        time.sleep(0.05)
                        print(Fore.GREEN+'[IP NOT FOUND]'+' '+ Fore.RED + string)
                    else:
                        time.sleep(0.05)
                        print(string)                
            except requests.exceptions.ConnectionError:
                i  = Fore.LIGHTWHITE_EX + i
                err = Fore.RED + '[HOST DOWN, CAN\'T FIND IP]'
                arrow = Fore.RED + "====>"
                x = Fore.CYAN + "[x]"
                string= err + " " + arrow + " " + x + " " + i + " " + x
                print(string)
        #if not i.startswith('http'): 
        else: 
            i = "http://" + i      
            try:
                req = requests.get(i)
                if req.status_code == 200:
                    split_url = parse.urlsplit(i)
                    ip_addr = socket.gethostbyname(split_url.netloc)
                    with open('HostsIP.txt', "a") as file:
                        file.write(ip_addr + "\n") 
                    #a = i.decode('utf-8')
                    ip_addr = Fore.CYAN + ip_addr
                    i = Fore.CYAN + i
                    arrow =Fore.RED + '====>'
                    string = Fore.GREEN + "[*]IP FOUND"+" "+ i+" "+ arrow+" "+ip_addr
                    if ip_addr == '0.0.0.0':  
                        time.sleep(0.05)
                        print(Fore.GREEN+'[CANT\'T FIND IP]'+' '+  string)
                    else:
                        time.sleep(0.05)
                        print(string)
            except requests.exceptions.ConnectionError:
                i  = Fore.LIGHTWHITE_EX + i
                err = Fore.RED + '[HOST DOWN, CAN\'T FIND IP]'
                arrow = Fore.RED + "====>"
                x = Fore.CYAN + "[x]"
                string= err + " " + arrow + " " + x+ i+ x
                print(string)                
        count += 1
        
    print(Fore.MAGENTA +'[x] Saved results in HostsIP.txt')
#Fonction to get Hosts inside a specific server
def RevereseIP_Domain():
 
    url = "https://domains.yougetsignal.com/domains.php"
    ip = input(Fore.YELLOW+ "[#] Enter an IP to grab website from server (or use the previous tool to get IP's): "+ Fore.LIGHTWHITE_EX)
    print(Fore.RED +"\n------------"+ Fore.CYAN +"[SCANNING FOR HOSTS ON SERVER, PLEASE WAIT]"+Fore.RED+"------------")
 
    #using youGetSignal API
    payload = {
        "remoteAddress": ip,
		"key": "",
		"_": ""
    }   

    res = requests.post(url, data=payload, headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
    data = res.json()

    #display the results
    for values in data.values():     
        try:
            with open('GrabbedHostsByIP.txt', "w")as file:
                for i in data['domainArray']:
                    var = "\n".join(i) 
                    file.write(var)    
                    var = "".join(i)
                    time.sleep(0.05) 
                    print(Fore.RED + '[HOST FOUND]:'+ " "+ Fore.GREEN+var)
                print(Fore.MAGENTA +'[x] Saved results in GrabbedHostsByIP.txt')
                break                
        except KeyError:
            if data['message'] == "No web sites found.":
                print(Fore.RED+'[-] No website found on these IP server')
                break
            if "Daily reverse IP check limit reached" in data['message']:
            #if data['status'] == "Fail":
                print(Fore.RED + '[-] You reach the limit, change your IP or retry later')
                break

# Find admin panels       
def FindAdmin_panel():
 
    possiblity = (
        'admin',
        'admin.php',
        "admin/index.php",
        "login/index.php",
        "login.php","administrator",
        "administrator.php",
        "login/admin.php",
        "login/administrator.php",
        "members",
        "login/members",
        "administration",
        "administration/login.html",
        "webadmin/login",
        'moderator/login.html',
        'moderator/admin.html',
        'account.html',
        'controlpanel.html',
        'admincontrol.html',
        'admin_login.html',
        'panel-administracion/login.html',
        'admin/home.asp',
        'admin/controlpanel.asp',
        'admin.asp',
        'pages/admin/admin-login.asp',
        'admin/admin-login.asp',
        'admin-login.asp',
        'admin/cp.asp',
        'cp.asp',
        'administrator/account.asp',
        'administrator.asp',
        'acceso.asp',
        'login.asp',
        'modelsearch/login.asp',
        'moderator.asp',
        'moderator/login.asp',
        'administrator/login.asp',
        'moderator/admin.asp',
        'controlpanel.asp',
        'admin/account.html',
        'adminpanel.html',
        'webadmin.html',
        'administration',
        'pages/admin/admin-login.html',
        'admin/admin-login.html',
        'webadmin/index.html',
        'webadmin/admin.html',
        'webadmin/login.html',
        'user.asp','user.html',
        'admincp/index.asp',
        'admincp/login.asp',
        'admincp/index.html',
        'admin/adminLogin.html',
        'adminLogin.html',
        'admin/adminLogin.html'
    )
 
    typing(Fore.GREEN +"[!] To get  results enter websites with a slash \'/\' at the end\n")
    time.sleep(1.5)
    admin_list = input(Fore.YELLOW + '[#] Enter a path of a websites lists :' + Fore.LIGHTWHITE_EX)
 
    #checking that the path exsits
    if os.path.exists(admin_list):
        try:
            with open(admin_list, 'rb') as file:
                try:
                    if os.path.isfile(admin_list):
                        my_pickler = pickle.Unpickler(file)
                        loadingg = my_pickler.load()
                except KeyError:
                    pass
        except pickle.UnpicklingError:
            pass
        except IsADirectoryError:
            print(Fore.RED+"[-] It's a directory, enter a path of a file")
            error = input(Fore.YELLOW+'[#] Please, rerun the option by typing (r/R): '+Fore.LIGHTWHITE_EX )
            while True:
                if error == "r" or error == "R":
                    return FindAdmin_panel()
                if error != "r" or error != "R":
                    print(Fore.RED+'[-] Error, enter (r) Or (R)')
                    error = input(Fore.YELLOW+'[#] Please, rerun the option by typing (r/R): '+Fore.LIGHTWHITE_EX )
 
    else:
        error = input(Fore.RED +'[-] Error, can\'t find path, enter (r/R) to use these options:' + Fore.LIGHTWHITE_EX)
        while True:
            if error == "r" or error == "R":
                return FindAdmin_panel()
            if error!= "r" or error != "R":
                print(Fore.RED +'[-] Error, enter (r) Or (r)')
                error = input(Fore.RED +'[-] Error, can\'t find path, enter (r/R) to use these options:' +Fore.LIGHTWHITE_EX)
                continue
 
    file = open(admin_list, 'rb')
    line = file.read().splitlines()
    count = 0
    print(Fore.RED +"\n------------"+ Fore.CYAN +"[SCANNING FOR ADMIN PANELS, PLEASE WAIT]"+Fore.RED+"------------")
    time.sleep(1.5)
 
    for i in line:
        #decoding bytes
        i = i.decode('utf-8')
        i = str(i)                    
        if not i.startswith('http'):
            print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")
            i = 'http://'+ i 
            for j in possiblity: 
                tout = i + j
                qq = tout.replace('\'', "")
                try:
                    req = requests.get(qq)
                    if req.status_code == 200:
                        print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+qq)
                    else:
                        print(Fore.LIGHTRED_EX + '[ADMIN PANEL NOT FOUND]' +" "+ Fore.RED + qq)             
                except requests.exceptions.ConnectionError:
                    print(Fore.RED + "[HOST DOWN]")                             
 
        elif i.startswith('http'):
            print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")  
            for j in possiblity:
                tout = i + j
                della3 = tout.replace("\'","")
                try:
                    req = requests.get(della3)
                    if req.status_code == 200:
                        print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+della3)
                    else:
                        print(Fore.LIGHTRED_EX + '[ADMIN PANEL NOT FOUND]' +" "+ Fore.RED + della3)                     
                except requests.exceptions.ConnectionError:
                    break
                    print(Fore.RED +"[HOST DOWN]")                   
    count += 1


def Grab_with_queries():
    headers = {
        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    querie = input(Fore.YELLOW +'[#] Enter a querie to grab websites : '+ Fore.LIGHTWHITE_EX)
    count = 0
    p = 0
    b = 0  
    while count  < 1000:  
        url = "https://www.bing.com/search?q="+str(querie)+"&first={}&FORM=PERE{}".format(p, b)
        req = requests.get(url, headers = headers)
        page_content = req.content
        web_page = re.findall('<h2><a href="(.*?)"', str(page_content))   
        for i in web_page:
            time.sleep(0.05)
            typing("\033[0;31m[\033[0;32m\033[5m+\033[0;31m]" + " " + "\033[0;36m"+i+ "\n")
            with open ("GrabbedHostsByDorks.txt", "a") as file:
               file.write(i + "\n") 
        count += 15
        p += 10
        b += 5
    print(Fore.MAGENTA +'[x] Saved results in GrabbedHostsByIP.txt')
    continueer = input(Fore.LIGHTRED_EX+'\n[*]Do you want to continue (y/n): ')
    if continueer == "y" or continueer == "Y":
        choices()
    else:
        exit()
       
def Grab_Bing():
    headers = {
        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    
        
      
def network_scanner():
    pass
    

def add_slash():
    nmi = input("enter the path of the file to add the slash : ")

def clean_scren():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

def typing(string):
    for words in string: 
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.001)

def local_IP():
    my_hostName = platform.node()
    my_ip = socket.gethostbyname(my_hostName)

def Public_Ip():
    url_publicIp =  "http://api.ipify.org/"
    req = requests.get(url_publicIp)
    html_page = req.content
    soup = BeautifulSoup(html_page,"html.parser")
    text= soup.find_all(text=True)
    output =""
    blacklist = [
        'html',
        'head',
        'body'
    ]
    for t in text:
        if t.parent.name not in blacklist:
            output +='{}'.format(t)

#get user choices     
def choices():    
    choice = input(Fore.LIGHTCYAN_EX +" \n[x] Choose options:  "+ Fore.LIGHTWHITE_EX)
    if choice == "1":
        MassIPScanner()
    if choice == "2":
        RevereseIP_Domain()
    if choice == "3":
        FindAdmin_panel()
    if choice == "4":
        return Grab_with_queries()
    if choice == "5":
        pass
    continueer = input(Fore.LIGHTRED_EX+'\n[*]Do you want to continue (y/n): ')
    if continueer == "y" or continueer == "Y":
        choices()
    else:
        print("[!] BYE, SEE YOU SOON")
        exit()

#main fonction
def all_in_one():
    clean_scren()
    typing("""
  
           \033[0;31m _______  .____  .___  .____         ___/   ___/  ___  
           \033[0;31m'      /  /      /   \ /           .'  /\ .'  /\ /   \ 
           \033[0;31m   .--'   |__.   |__-' |__.  .---' |  / | |  / |   _-'  
            \033[0;31m /       |      |  \  |           |,'  | |,'  |    \ 
           \033[0;31m,'______/ /----/ /   \ /           /`---' /`---' \___) 
                                                  
                            """)
    typing(Fore.LIGHTGREEN_EX+"""
                        [@]Script Name: HackThisShit
                        [@]Coded By: B1LLAl """)
    typing("""
    \033[0;31m[\033[0;32m\033[5mOPTIONS\033[0m\033[0;31m]:                                                          
            \033[0;37m---------[\033[0;36m\033[5mWEB-APP HACKING\033[0m\033[0;37m]---------                 
               \033[9m\033[0;31m[\033[0;32m\033[5m1\033[0;31m]\033[0m: Mass Websites IP Scanner               
               \033[0;31m[\033[0;32m\033[5m2\033[0;31m]\033[0m: Grab Websites from a spesific server [Reverse IP Domain]
               \033[0;31m[\033[0;32m\033[5m3\033[0;31m]\033[0m: Find Admin panels                       
               \033[0;31m[\033[0;32m\033[5m4\033[0;31m]\033[0m: Grab Websites with Dorks                
               \033[0;31m[\033[0;32m\033[5m5\033[0;31m]\033[0m: Grab Sites from Bing                   
                                                                                                       
                                                                                                                  
               """)
    
    choices() 

all_in_one()  
##coded By : ZERF ##
##All in one ##


