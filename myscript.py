##coded By : ZERF ##
##All in one ##


#import modules
import  urllib
from urllib import parse
import urllib.request
import validators
#import urllib2
#from url.parse import urljoin
import socket
import pickle
import os 
import colorama
from colorama import init,Fore
from termcolor import cprint, colored 
import sys 
import platform
from platform import system
import requests
from bs4 import  BeautifulSoup
import mechanize
import json
import  time

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
        #if it's  directory we iutout an error msg and try again
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
   #if the path it's wrong we outout an error msg thn try again             
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
        split_url = parse.urlsplit(i)
        ip_addr = socket.gethostbyname(split_url.netloc)
        a = i.decode('utf-8')
        string = "[{}] === > [{}]".format(a, ip_addr)
        if ip_addr == '0.0.0.0':  
            time.sleep(0.05)
            print(Fore.RED+'[IP NOT FOUND]'+' '+ Fore.LIGHTGREEN_EX + string)
        else:
            time.sleep(0.05)
            print(Fore.RED+'[IP FOUND]'+' '+ Fore.LIGHTGREEN_EX+string)
    count += 1
#Fonction to get Hosts inside a specific server
def RevereseIP_Domain():
    url = "https://domains.yougetsignal.com/domains.php"
    ip = input(Fore.YELLOW+ "[#] Enter an IP to grab website from server (or use the previous tool to get IP's): "+ Fore.LIGHTWHITE_EX)
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
        "admin/index.php"
        "login/index.php",
        "login.php",
        "administrator", 
        "administrator.php",
        "login/admin.php"
        "login/administrator.php"
        "members",
        "login/members"
    )
  
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
        error = input('[-] Error, can\'t find path, enter (r/R) to use these options:')
        while True:
            if error == "r" or error == "R":
                return FindAdmin_panel()
            if error!= "r" or error != "R":
                print('[-] Error, enter (r) Or (r)')
                error = input('[-] Error, can\'t find path, enter (r/R) to use these options:')
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
        '''if i.endswith("/"):
            if i.startswith("http"):
                    j = str(possibility2[0])
                    tout = i + j
                    zbi = tout.replace("\'","")
                    try:
                        req = requests.get(zbi)
                        if req.status_code == 200:
                            print(Fore.LIGHTCYAN_EX+"--------------["+i+"]--------------")
                            print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+zbi)
                        else:
                            print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                            print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ zbi)
                    except requests.exceptions.ConnectionError:
                        print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                        print(Fore.LIGHTRED_EX+'[HOST DOWN]')
            ''''''elif not i.startswith('http'):
                i = "http://" + i
                j = str(possibility2[0])
                tout = i + j
                shit = tout.replace("\'","")
                try:
                    req = requests.get(shit)
                    if req.status_code == 200:
                        print(Fore.LIGHTCYAN_EX+ '--------------['+i+']--------------')
                        print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+shit)
                    else:
                        print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                        print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ shit)
                except requests.exceptions.ConnectionError:
                    print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                    print(Fore.LIGHTRED_EX+'[HOST DOWN]')'''                     
        if not i.startswith('http'):
            print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")
            i = 'http://'+ i 
            for j in possiblity:
                #i = 'http://'+ i  
                tout = i + j
                qq = tout.replace('\'', "")
                try:
                    #req = requests.get(qq)
                    openurl = urllib.request.urlopen(qq)
                    #f req.status_code == 200:
                   # print(Fore.LIGHTCYAN_EX+"--------------["+i+"]--------------")
                    print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+qq)
                    #else:
                     #   print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                      #  print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ qq)
                except urllib.error.URLError as msg_error:
                    print('cant found panel')      
               # except requests.exceptions.ConnectionError:
                #    print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                 #   print(Fore.LIGHTRED_EX + '[HOST DOWN]') 
                #plus += 1
                
        elif i.startswith('http'):
            print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")
        
            for j in possiblity:
            #j = possiblity
                tout = i + j
                della3 = tout.replace("\'","")
                try:                   
                    openurl = urllib.request.urlopen(della3) 
                #req = requests.get(della3)
                # req.status_code == 200:
                   # print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")
                    print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+della3)
                #else:
                 #   print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                  #  print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ della3)
           # except requests.exceptions.ConnectionError:
            #    print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
             #   print(Fore.LIGHTRED_EX+'[HOST DOWN]')"""
                except urllib.error.URLError as msg:
                    print("cant find admin panel")
                
    count += 1
def Grab_with_queries():
    querie = input(Fore.YELLOW +'[#] Enter a querie to grab websites : '+ Fore.LIGHTWHITE_EX)
   # page = urllib.urlopen(querie)

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
#local ip
my_hostName = platform.node()
my_ip = socket.gethostbyname(my_hostName)
#public ip 
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
    continueer = input(Fore.LIGHTRED_EX+'\n[*]Do you want to continue (y/n): ')
    if continueer == "y" or continueer == "Y":
        choices()
    else:
        exit()
#main fonction
def all_in_one():
    clean_scren()
    typing(Fore.LIGHTRED_EX +"""
  
      \033[0;31m      _______  .____  .___  .____         ___/   ___/  ___  \033[0;31m
      \033[0;31m     '      /  /      /   \ /           .'  /\ .'  /\ /   \ \033[0;31m
        \033[0;31m      .--'   |__.   |__-' |__.  .---' |  / | |  / |   _-'  \033[0;31m
        \033[0;31m     /       |      |  \  |           |,'  | |,'  |    \ \033[0;31m
        \033[0;31m   ,'______/ /----/ /   \ /           /`---' /`---' \___) \033[0;31m
                                                  
                            """)
    typing(Fore.LIGHTGREEN_EX+"""
                        [@]Your Local IP: {}
                        [@]Your Public IP: {} \n""".format(my_ip,output))
    typing(Fore.LIGHTYELLOW_EX+"""
                    [OPTIONS]:
                             [1]: Mass_WebSite_IP_scanner
                             [2]: Grab sites from a spesific server
                             [3]: Find Admin panels
                             [4]: Grab Websites with Dorks \n""")
    choices() 

all_in_one()    
##coded By : ZERF ##
##All in one ##


#import modules
import  urllib
from urllib import parse
import urllib.request
import validators
#import urllib2
#from url.parse import urljoin
import socket
import pickle
import os 
import colorama
from colorama import init,Fore
from termcolor import cprint, colored 
import sys 
import platform
from platform import system
import requests
from bs4 import  BeautifulSoup
import mechanize
import json
import  time

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
        #if it's  directory we iutout an error msg and try again
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
   #if the path it's wrong we outout an error msg thn try again             
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
        split_url = parse.urlsplit(i)
        ip_addr = socket.gethostbyname(split_url.netloc)
        a = i.decode('utf-8')
        string = "[{}] === > [{}]".format(a, ip_addr)
        if ip_addr == '0.0.0.0':  
            time.sleep(0.05)
            print(Fore.RED+'[IP NOT FOUND]'+' '+ Fore.LIGHTGREEN_EX + string)
        else:
            time.sleep(0.05)
            print(Fore.RED+'[IP FOUND]'+' '+ Fore.LIGHTGREEN_EX+string)
    count += 1
#Fonction to get Hosts inside a specific server
def RevereseIP_Domain():
    url = "https://domains.yougetsignal.com/domains.php"
    ip = input(Fore.YELLOW+ "[#] Enter an IP to grab website from server (or use the previous tool to get IP's): "+ Fore.LIGHTWHITE_EX)
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
        "admin/index.php"
        "login/index.php",
        "login.php",
        "administrator", 
        "administrator.php",
        "login/admin.php"
        "login/administrator.php"
        "members",
        "login/members"
    )
  
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
        error = input('[-] Error, can\'t find path, enter (r/R) to use these options:')
        while True:
            if error == "r" or error == "R":
                return FindAdmin_panel()
            if error!= "r" or error != "R":
                print('[-] Error, enter (r) Or (r)')
                error = input('[-] Error, can\'t find path, enter (r/R) to use these options:')
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
        '''if i.endswith("/"):
            if i.startswith("http"):
                    j = str(possibility2[0])
                    tout = i + j
                    zbi = tout.replace("\'","")
                    try:
                        req = requests.get(zbi)
                        if req.status_code == 200:
                            print(Fore.LIGHTCYAN_EX+"--------------["+i+"]--------------")
                            print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+zbi)
                        else:
                            print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                            print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ zbi)
                    except requests.exceptions.ConnectionError:
                        print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                        print(Fore.LIGHTRED_EX+'[HOST DOWN]')
            ''''''elif not i.startswith('http'):
                i = "http://" + i
                j = str(possibility2[0])
                tout = i + j
                shit = tout.replace("\'","")
                try:
                    req = requests.get(shit)
                    if req.status_code == 200:
                        print(Fore.LIGHTCYAN_EX+ '--------------['+i+']--------------')
                        print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+shit)
                    else:
                        print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                        print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ shit)
                except requests.exceptions.ConnectionError:
                    print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                    print(Fore.LIGHTRED_EX+'[HOST DOWN]')'''                     
        if not i.startswith('http'):
            print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")
            i = 'http://'+ i 
            for j in possiblity:
                #i = 'http://'+ i  
                tout = i + j
                qq = tout.replace('\'', "")
                try:
                    #req = requests.get(qq)
                    openurl = urllib.request.urlopen(qq)
                    #f req.status_code == 200:
                   # print(Fore.LIGHTCYAN_EX+"--------------["+i+"]--------------")
                    print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+qq)
                    #else:
                     #   print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                      #  print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ qq)
                except urllib.error.URLError as msg_error:
                    print('cant found panel')      
               # except requests.exceptions.ConnectionError:
                #    print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                 #   print(Fore.LIGHTRED_EX + '[HOST DOWN]') 
                #plus += 1
                
        elif i.startswith('http'):
            print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")
        
            for j in possiblity:
            #j = possiblity
                tout = i + j
                della3 = tout.replace("\'","")
                try:                   
                    openurl = urllib.request.urlopen(della3) 
                #req = requests.get(della3)
                # req.status_code == 200:
                   # print(Fore.LIGHTCYAN_EX+ "--------------["+i+"]--------------")
                    print(Fore.RED + '[ADMIN PANEL FOUND]:'+ " "+ Fore.GREEN+della3)
                #else:
                 #   print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
                  #  print(Fore.RED +"[ADMIN PANEL NOT FOUND]" + " "+ Fore.LIGHTRED_EX+ della3)
           # except requests.exceptions.ConnectionError:
            #    print(Fore.LIGHTCYAN_EX + "--------------["+i+"]--------------")
             #   print(Fore.LIGHTRED_EX+'[HOST DOWN]')"""
                except urllib.error.URLError as msg:
                    print("cant find admin panel")
                
    count += 1
def Grab_with_queries():
    querie = input(Fore.YELLOW +'[#] Enter a querie to grab websites : '+ Fore.LIGHTWHITE_EX)
   # page = urllib.urlopen(querie)

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
#local ip
my_hostName = platform.node()
my_ip = socket.gethostbyname(my_hostName)
#public ip 
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
    continueer = input(Fore.LIGHTRED_EX+'\n[*]Do you want to continue (y/n): ')
    if continueer == "y" or continueer == "Y":
        choices()
    else:
        exit()
#main fonction
def all_in_one():
    clean_scren()
    typing(Fore.LIGHTRED_EX +"""
  
      \033[0;31m      _______  .____  .___  .____         ___/   ___/  ___  \033[0;31m
      \033[0;31m     '      /  /      /   \ /           .'  /\ .'  /\ /   \ \033[0;31m
        \033[0;31m      .--'   |__.   |__-' |__.  .---' |  / | |  / |   _-'  \033[0;31m
        \033[0;31m     /       |      |  \  |           |,'  | |,'  |    \ \033[0;31m
        \033[0;31m   ,'______/ /----/ /   \ /           /`---' /`---' \___) \033[0;31m
                                                  
                            """)
    typing(Fore.LIGHTGREEN_EX+"""
                        [@]Your Local IP: {}
                        [@]Your Public IP: {} \n""".format(my_ip,output))
    typing(Fore.LIGHTYELLOW_EX+"""
                    [OPTIONS]:
                             [1]: Mass_WebSite_IP_scanner
                             [2]: Grab sites from a spesific server
                             [3]: Find Admin panels
                             [4]: Grab Websites with Dorks \n""")
    choices() 

all_in_one()    
