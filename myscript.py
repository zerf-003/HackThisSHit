### path: /home/hacker/Bureau/python/myscripyt.py ###
### codage : "UTF-8" ###
### Coded BY : Z3RF-003 ###
### Script name : All_In_One ###

#import modules
import ipaddress
import http.client
from urllib import parse
import urllib.request
import socket
import os 
import colorama
from colorama import init,Fore 
from bs4 import BeautifulSoup
import sys 
import platform
from platform import system
import requests
import json
import  time
import random
import re
from scapy.all import *
import threading
from threading import Thread
import pandas



def MassIPScanner():
    try:
        path = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter a Hosts File : '+ Fore.LIGHTWHITE_EX)
        file = open(path, "rb")
        lines = file.read().splitlines()
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scanning For IP\'s, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        time.sleep(1.5)
        for i in lines:
            i = i.decode("utf-8")
            if i.startswith('http'):
                try:
                    req = requests.get(i,allow_redirects=True)
                    if req.status_code == 200:
                        split_url = parse.urlsplit(i)
                        ip_addr = socket.gethostbyname(split_url.netloc)
                        with open('HostsIP.txt', "a") as file:
                            file.write(ip_addr + "\n")  
                        ip_addr = Fore.WHITE + ip_addr
                        i = Fore.WHITE + i
                        arrow =Fore.RED + '====>'
                        string = "\033[0;31m[\033[0;32mIP Found\033[0;31m]"+" "+ i+" "+ arrow+" "+ip_addr
        
                        if ip_addr == '0.0.0.0':  
                            time.sleep(0.05)
                            print("\033[0;37m[\033[0;31m\033[5mCan\'t Find IP\033[0;37m]"+' ' + "\033[1;31m"+ string)
                        else:
                            time.sleep(0.05)
                            print(string) 
                except requests.exceptions.ConnectionError:
                    i  = Fore.WHITE + i
                    err = '\033[0;37m[\033[0;31m\033[5mCan\'t Find IP\033[0;37m]'
                    arrow = Fore.RED + "====>"
                    x =  "\033[0;37m[\033[0;31m\033[5m!\033[0;37m]"
                    string= err + " " + arrow + " " + x + " " + i + " " + x
                    print(string)
            else: 
                i = "http://" + i     
                try:
                    req = requests.get(i, allow_redirects=True)
                    if req.status_code == 200:
                        split_url = parse.urlsplit(i)
                        ip_addr = socket.gethostbyname(split_url.netloc)
                        with open('HostsIP.txt', "a") as file:
                            file.write(ip_addr + "\n") 
                        ip_addr = Fore.WHITE+ ip_addr
                        i = Fore.WHITE + i
                        arrow =Fore.RED + '====>'
                        string = "\033[0;31m[\033[0;32mIP Found\033[0;31m]"+" "+ i+" "+ arrow+" "+ "\033[1;37m"+ip_addr
                    
                        if ip_addr == '0.0.0.0':  
                            time.sleep(0.05)
                            print('\033[0;37m[\033[0;31m\033[5mCan\'t Find IP\033[0;37m]'+ ' '+ "\033[1;31m"+ string)
                        else:
                            time.sleep(0.05)
                            print(string)
                except requests.exceptions.ConnectionError:
                    i  = Fore.WHITE + i
                    err = "\033[0;37m[\033[0;31m\033[3m\033[5mCan\'t Find IP\033[0;37m]"
                    arrow = Fore.RED + "====>"
                    x =  "\033[0;37m[\033[0;31m\033[5m!\033[0;37m]"
                    string= err + " " + arrow + " " + x+ i+ x
                    print(string) 
        print(Fore.MAGENTA +'[x] Saved results in HostsIP.txt')                 
    except FileNotFoundError:
        print('cant find ile please try agin')
    except requests.exceptions.TooManyRedirects:
        print(Fore.MAGENTA +'[x] Saved results in HostsIP.txt')
   


#Fonction to get Hosts inside a specific server
def RevereseIP_Domain():
    url = "https://domains.yougetsignal.com/domains.php"
    ip = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter an IP to grab website from server (or use the previous tool to get IP\'s): '+ Fore.LIGHTWHITE_EX)
    print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scanning For WebSites On Entered IP Server , Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")     
    time.sleep(1)
    #using youGetSignal API  
    payload = {
        "remoteAddress": ip,
		"key": "",
		"_": ""
    }   
    res = requests.post(url, data=payload, headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
    data = res.json()
  
    for values in data.values():  
        try:
            #with open('GrabbedHostsByIP.txt', "w")as file:
            for i in data['domainArray']:
                var = "\n".join(i) 
                #file.write(var)    
                var = "".join(i)
                time.sleep(0.05) 
                print("\033[0;31m>>>\033[0m\033[0;31m"+" "+ Fore.WHITE+var)
                with open('ReverseIP.txt', "a") as r:
                    r.write(var + "\n")  
            print(Fore.MAGENTA +'[x] Saved results in ReverseIP.txt')        
            break
        except KeyError:
            if data['message'] == "No web sites found.":
                print('\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m No Website Found On These IP Server')
                break
            if  "Service unvailable." in data['message']:
                print('\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m Service unvailable')
                break
            if "Daily reverse IP limit reached" in data['message']:
                print(Fore.RED + '\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m You Reach The Limit, Change Your IP Or Retry Later')
                break

   

# Find admin panels       
def FindAdmin_panel():
    try:
        possiblity = (
            '/admin','/admin.php',"/admin/index.php","/login/index.php","/wp-login.php","/admin/login.php","/administrator.php","/login.php","/login/admin.php",
            "/login/administrator.php",'/dashboard/','/dashboard/index.php',"/dashboard/login.php","/admin/panel.php","/administration/login.php",
            '/admincontrol.html','/admin_login.php','/panel-administracion/login.html',
            "/node","/administrator/","/login/admin","/administration",
            '/admin/admin-login.html','/admin/admin-login.php','/admin.html',
            '/admin/adminLogin.html','/adminLogin.html','/admin/adminLogin.html' 
        )
        time.sleep(1.5)
        admin_list = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter The Name File : '+ Fore.LIGHTWHITE_EX)  
        file = open(admin_list, 'rb')
        line = file.read().splitlines()  
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scannig For Admin Panels, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        time.sleep(1.5)   
        for i in line:
            #decoding bytes
            i = i.decode('utf-8')
            i = str(i)  
            if not i.startswith('http'):
                i = 'http://'+ i 
                print(" \n \033[95m[\033[95m\033[5m+\033[0m\033[95m] \033[95mScan " + Fore.WHITE +  i  )
                for j in possiblity: 
                    tout = i + j
                    qq = tout.replace('\'', "")
                    try:
                        req = requests.get(qq, timeout = 5)
                        shit = req.text
                        if  req.status_code == 200 and 'type="password"' in shit:
                            print("\033[0;31m[\033[0;32m>>>\033[0;31m]\033[0;31m[\033[0;32mPanel Found\033[0;31m]\033[0;31m" + Fore.WHITE + qq)
                            with open('AdminPanles.txt' ,'a') as admin:
                                admin.write(qq + '\n')
                        else:
                            print('\033[0;31m[-]\033[0;31m[Not Found\033[0;31m]\033[0;31m\033[0;31m[-]' + Fore.WHITE + qq)
                    except requests.ConnectionError:
                        pass
                    except requests.exceptions.ChunkedEncodingError:
                        pass
            elif i.startswith('http'):
                print(" \n \033[95m[\033[95m\033[5m+\033[0m\033[95m] \033[95mScan " + Fore.WHITE +  i  )
                for j in possiblity:
                    tout = i + j
                    della3 = tout.replace("\'","")
                    try:
                        socket.setdefaulttimeout(1)
                        req = requests.get(della3, timeout= 5)
                        if  req.status_code == 200 and 'type="password"' in req.text :
                            print("\033[0;31m[\033[0;32m+\033[0;31m]\033[0;31m[\033[0;32mAdmin Panel Found\033[0;31m]\033[0;31m" + Fore.WHITE + della3)
                            with open('AdminPanles.txt' ,'a') as admin:
                                admin.write(della3 + '\n')
                        else:
                            print('\033[0;31m[-]\033[0;31m[Not Found\033[0;31m]\033[0;31m\033[0;31m[-]' + Fore.WHITE + della3)
                
                    except requests.ConnectionError:
                        pass
                    except requests.exceptions.ChunkedEncodingError:
                        pass
                    except:
                        pass
        print(Fore.MAGENTA +'[x] Saved results in AdminPanels.txt')
    except FileNotFoundError:
        print("file not found")        
           
                
   

def Grab_with_queries():
    code = {
        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    querie = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter A Querie To Grab Websites : '+ Fore.LIGHTWHITE_EX)
    p = 1 
    try:
        repetion = [] 
        while p < 251:     
            url = "https://www.bing.com/search?q="+str(querie)+"+&count=50&first="+str(p)
            req = requests.get(url, headers = code)
            page_content = req.content
            web_page = re.findall('<h2><a href="(.*?)"', str(page_content))
            for i in web_page:
                if i in repetion:
                    pass
                else:
                    repetion.append(i)
                    time.sleep(0.05)
                    print("\033[0;32m\033[0m\033[0;31m>>>\033[0;32m\033[0m" + " " + Fore.WHITE+i)
                    with open ("Grabbed_Dorks.txt", "a") as file:
                        file.write(i + "\n")     
            p += 2
        print(Fore.MAGENTA +'[x] Saved results in Grabbed_Dorks.txt')
    except requests.exceptions.ChunkedEncodingError:
        pass
    except requests.exceptions.SSLError:
        pass
    continueer = input(Fore.LIGHTRED_EX+'\n[*]Do you want to continue (y/n): ')
    if continueer == "y" or continueer == "Y":
        all_in_one()
    else:
        exit()



def Grab_Bing():
    try:
        file = input(Fore.YELLOW +'[\033[5m#\033[0m' + Fore.YELLOW+']Enter The IP\'s File : '+ Fore.LIGHTWHITE_EX)   
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Grabbing WebSites From Bing, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------") 
        file = open(file, "r")
        for i in file:
            headers = {      
                "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
            }
            p = 1 
            try:
                shity_repition = []
                while p< 251:    
                    url = "https://www.bing.com/search?q=ip%3A" + str(i) +"+&count=50&first="+ str(p)
                    req = requests.get(url,verify = True,headers = headers)  
                    page_shit = req.content          
                    pages = re.findall('<h2><a href="(.*?)"', str(page_shit))              
                    for j in pages:            
                        simple_url = j.split('/')
                    #simple_url = simple_url[0]+'//'+simple_url[2]
                        if simple_url[0] + "//" + simple_url[2] in shity_repition:
                            pass
                        else:
                            shity_repition.append(simple_url[0] + "//" + simple_url[2])    
                            time.sleep(0.05)
                            print("\033[0;32m\033[0m\033[0;31m>>>\033[0;32m\033[0m" +" " +"\033[0;37m"+ simple_url[0] + "//" + simple_url[2])
                            with open("Grabbed_Bing.txt", "a") as file:
                                file.writelines(simple_url[0] + "//" + simple_url[2] + "\n")           
                    p += 5
            except requests.exceptions.ChunkedEncodingError:
                pass
            except requests.exceptions.SSLError:
                pass
            except requests.exceptions.ConnectionError:
                pass
        print(Fore.MAGENTA +'[x] Saved results in Grabbed_Bing.txt')    
    except FileNotFoundError:
        print("file not found")




def zone_h():
    javaScript = '<html><body>-<script type="text/javascript"'
    captcha = "captcha"
    user_agent = {
        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    choose = (
        "\033[0;37m[\033[0;31m1\033[0;37m] \033[0m - \033[0;34mGrab From Archive Special\n"
        "\033[0;37m[\033[0;31m2\033[0;37m] \033[0m - \033[0;34mGrab From  Onhold\n"
        "\033[0;37m[\033[0;31m3\033[0;37m] \033[0m - \033[0;34mGrab with Notifier \n"
    )
    print("\n" + choose)
    ch = input("\033[0;31m[\033[0;32m\033[5m#\033[0;31m]\033[0m Choose a section: " +Fore.LIGHTWHITE_EX)
    
    if ch =="1":
        Cookies = input('\033[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0m Enter your \033[0;31m\033[3mZHE\033[0m from your Browser: ' + Fore.GREEN)
        cookies1 = input('\033[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0m Enter your \033[0;31m\033[3mPHPSESSID\033[0m from your Browser: '+ Fore.GREEN )
        if Cookies =="" or cookies1=="":
            print("\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Please Enter Your Cookies")
            exit() 
        all_ = {
            'ZHE' :   Cookies,
            'PHPSEDDID': cookies1
        }
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Grabbing Hosts From Zone-H.org / Archive Special , Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        time.sleep(1)
        #while count < 50:
        for page in range(1, 51):    
            url = "http://www.zone-h.org/archive/special=1/page=" + str(page)
            req = requests.get(url, headers = user_agent, cookies = all_)
            shit = req.text
            if javaScript in shit:
                print('\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Change Your Cookie Please')
                exit()
            elif captcha in shit:
                print("\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Enter the Captcha In Your Browser To Continue")
                exit()
            else:    
                url_zone = re.findall("<td>(.*)\n							</td>", shit) 
                for final in url_zone:
                    if "..." in final:
                        flenn  = final.replace("...", "")        
                        lil_pump = flenn.split("/")
                        time.sleep(0.05)
                        print("\033[0;32m\033[0m\033[0;31m\033[0;31m<...>\033[0;32m\033[0m"+" "+ lil_pump[0])
                    else:
                        lil_pump = final.split("/")
                        time.sleep(0.05)
                        print('\033[0;32m\033[0m\033[0;31m\033[0;31m<...>\033[0;32m\033[0m'+" "+lil_pump[0])   
                    with open("Archive_Special.txt", "a") as zone:
                        zone.write("http://" + lil_pump[0] + "\n")
        print(Fore.MAGENTA +'[x] Saved results in Archive_Special.txt')

    if ch == "2":
        Cookies = input('\033[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0m Enter your \033[0;31m\033[3mZHE\033[0m from your Browser: ' + Fore.GREEN)
        cookies1 = input('\033[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0m Enter your \033[0;31m\033[3mPHPSESSID\033[0m from your Browser: '+ Fore.GREEN )
        if Cookies =="" or cookies1=="":
            print("\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Please Enter Your Cookies")
            exit()
        all_ = {
            'ZHE' :   Cookies,
            'PHPSEDDID': cookies1
        }
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Grabbing Hosts From Zone-H.org / OnHold , Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        time.sleep(1)
        for page in range(1,51):
            url = "http://www.zone-h.org/archive/published=0/page=" + str(page) 
            req = requests.get(url, headers =user_agent,cookies = all_)
            zone_content = req.text  
            if javaScript in zone_content:
                print('\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Change Your Cookie Please')
                exit()
            if captcha in zone_content:
                print("\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Enter the Captcha In Your Browser To Continue")
                exit()
            else:
                url_zone = re.findall("<td>(.*)\n							</td>", zone_content) 
                for final_url in url_zone:
                    if "..." in final_url:
                        savage = final_url.replace("...", "")
                        Dak = savage.split("/")
                        time.sleep(0.05)
                        print("\033[0;32m\033[0m\033[0;31m<...>\033[0;32m\033[0m"+" "+Dak[0])
                    else:
                        Dak = final_url.split("/")
                        time.sleep(0.05)
                        print("\033[0;32m\033[0m\033[0;31m<...>\033[0;32m\033[0m"+" "+ Dak[0])
                        with open("OnHold.txt", "a") as zone:
                            zone.write("http://" + Dak[0] + "\n")
        print(Fore.MAGENTA +'[x] Saved results in OnHold.txt')
    
    if ch == "3":
        Cookies = input('\033[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0m Enter your \033[0;31m\033[3mZHE\033[0m from your Browser: ' + Fore.GREEN)
        cookies1 = input('\0python ignore oserror 33[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0m Enter your \033[0;31m\033[3mPHPSESSID\033[0m from your Browser: '+ Fore.GREEN )
        if Cookies =="" or cookies1=="":
            print("\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Please Enter Your Cookies")
            exit()
        all_ = {
            'ZHE' :   Cookies,
            'PHPSEDDID': cookies1
        }
        notifier =  input('\033[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0m Enter a \033[0;31m\033[3mNotifier\033[0m To Grab Hosts: ' + Fore.GREEN)
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Grabbing Hosts From Zone-H.org / Notfier , Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        time.sleep(1)
        for page in range(1,51):
            url = "http://www.zone-h.org/archive/notifier=" + str(notifier) + "/page="+ str(page)
            req = requests.get(url, headers = user_agent, cookies = all_)
            shity_content = req.text
            if javaScript in shity_content:
                print('\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Change Your Cookie Please !')
                exit()
            elif captcha in shity_content:
                print("\033[0;31m[\033[0;31m\033[5m!\033[0;31m]\033[0;31m Enter the Captcha In Your Browser To Continue")
                exit()
            else:
                no  = re.findall('<td>(.*)\n							</td>', shity_content)
                for nm in no:
                    if '...' in nm:
                        lil_peep = nm.replace('...', "")
                        pew = lil_peep.split('/')
                        time.sleep(0.05)
                        print("\033[0;32m\033[0m\033[0;31m<...>\033[0;32m\033[0m"+" "+pew[0]) 
                    else:
                        pew = nm.split("/")
                        time.sleep(0.05)
                        print("\033[0;32m\033[0m\033[0;31m<...>\033[0;32m\033[0m"+" "+pew[0])
                    with open('Notifier.txt', "a")as notif:
                        notif.write('http://' + pew[0] + "\n")           
        print(Fore.MAGENTA +'[x] Saved results in Notifier.txt')
    



def Ip_range():
    try:
        path = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter The IP\'s File : '+ Fore.LIGHTWHITE_EX)     
        file = open(path, "rb")
        zerf = file.read().splitlines()
        for i in zerf:
            ip = i.decode('utf-8')
            print( Fore.CYAN +" [*] Range {}" .format(ip))
            ip = ip.split('.') 
            try:
                a = 0
                while a <= 255:
                    headers = {
                        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
                    }
                    a  = str(a)
                    ip[3] =a
                    Final_IP = ".".join(ip)
                    url = 'https://www.bing.com/search?q=ip%3A"' + str(Final_IP) +'"'
                    req = requests.get( url,verify =True, headers= headers)
                    corona = req.text
                    naps = re.findall('<h2><a href="(.*?)"', str(corona))
                    for i in naps:
                        if i  in corona:
                            print("{} Up".format(Final_IP))
                            break
                    else:
                        print("{} down".format(Final_IP))    
                    a = int(a)                    
                    a += 1
            except requests.exceptions.SSLError as e:
                pass
    except requests.exceptions.ChunkedEncodingError:
        pass
    except FileNotFoundError:
        print("file not found")   


       
def mirroh_h():
    pass    




   

    

    
   

def network_scanner():
    pass
    



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
        #clean_scren()
        typing('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5mGrab Hosts With Dorks \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n')
        time.sleep(0.5)
        Grab_with_queries()    
    if choice == "2":
        #clean_scren()
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Zone-H.org Grabber \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        time.sleep(0.05)
        zone_h()
    if choice == "3":
        #clean_scren()
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Bing Grabber \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        time.sleep(0.5)
        Grab_Bing()
    if choice == "4":
       # clean_scren()
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Mass IP Scanner \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        time.sleep(0.5)
        MassIPScanner()
    if choice == "5":
        #clean_scren()
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Reverse IP Domain \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        time.sleep(0.5)
        RevereseIP_Domain()
    if choice == "6":
        #clean_scren()
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Admin Panel Finder \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        FindAdmin_panel()    
    if choice == "7":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m IP Range \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        Ip_range()
    if choice == "9":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Access Point Scanner \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        def hopper(iface):
            n = 1
            stop_hopper = False
            while not stop_hopper:
                time.sleep(0.50)
                os.system('iwconfig %s channel %d' % (iface, n))
                dig = int(random.random() * 14)
                if dig != 0 and dig != n:
                    n = dig

        F_bssids = []    # Found BSSIDs
        def findSSID(pkt):
            if pkt.haslayer(Dot11Beacon):
                if pkt.getlayer(Dot11).addr2 not in F_bssids:
                    F_bssids.append(pkt.getlayer(Dot11).addr2)
                    ssid = pkt.getlayer(Dot11Elt).info
                    if ssid == '' or pkt.getlayer(Dot11Elt).ID != 0:
                        print ("Hidden Network Detected")
    
                    print ("Network Detected: %s" % (ssid.decode('utf-8')))

        if __name__ == "__main__":
            try:
                interface = "wlan0mon"
                thread = threading.Thread(target=hopper, args=(interface, ), name="hopper")
                thread.daemon = True
                thread.start()
                sniff(iface=interface, prn=findSSID)
            except PermissionError:
                print("\033[0;31m[\033[5m-\033[0m\033[0;31m] Retry As Sudo [This Option Require root Privilege]")
                sys.exit()
    continueer = input(Fore.LIGHTRED_EX+'\n[*]Do you want to continue (y/n): '+ Fore.WHITE)
    if continueer == "y" or continueer == "Y":
        all_in_one()
    else:  
        print("Thanks For Using My Script  ^____^")
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
                                                  
                                Greetz to : Bylka_Inj  who taught me the basics                                            """)

    typing(Fore.LIGHTGREEN_EX+"""
                        [@]Script Name: HackThisShit
                        [@]Coded By: B1LLAl """)

    typing("""
    \033[0;31m[\033[1;33m\033[5mOPTIONS\033[0m\033[0;31m]:                                                          
            \033[0;37m---------[\033[0;36m\033[5mWEB-APP HACKING\033[0m\033[0;37m]---------                       \033[0;37m---------[\033[0;36m\033[5mWIRLESSE HACKING\033[0m\033[0;37m]---------                       
               \033[9m\033[0;31m[\033[0;32m1\033[0;31m]\033[0m: Grab Hosts With Dorks                                \033[9m\033[0;31m[\033[0;32m9\033[0;31m]\033[0m: Scan For Access Points [Monitor Mode Requiered]  
               \033[0;31m[\033[0;32m2\033[0;31m]\033[0m: Grab Sites From Zone-H.org [From 3 Sections]             
               \033[0;31m[\033[0;32m3\033[0;31m]\033[0m: Grab Hosts From Bing [With IP List]                                         
               \033[0;31m[\033[0;32m4\033[0;31m]\033[0m: Mass IP Scanner         
               \033[0;31m[\033[0;32m5\033[0;31m]\033[0m: Reverse IP Domain [Grab Hosts In a WebServer With IP]                     
               \033[0;31m[\033[0;32m6\033[0;31m]\033[0m: Find Admin Panels    
               \033[0;31m[\033[0;32m7\033[0;31m]\033[0m: Brute Force CMS [Wodpress, Joomla, Drupal]                                       
               \033[0;31m[\033[0;32m8\033[0;31m]\033[0m: IP Range
               
               """)
    choices() 

all_in_one()  
##coded By : ZERF ##
##All in one ##


