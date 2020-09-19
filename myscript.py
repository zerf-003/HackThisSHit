### path: /home/hacker/Bureau/python/myscripyt.py ###
### codage : "UTF-8" ###
### Coded BY : Z3RF-003 ###
### Script name : HackThisShit ###

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
    """
        Docstring: a function to scan IP's in the inputed file of the user 
        we try to get the IP using socket module. If an Socket error proucures during 
        the IP gathering , it means that the host is down"""
    try:
        path = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter a Hosts File : '+ Fore.LIGHTWHITE_EX)
        file = open(path, "rb")
        lines = file.read().splitlines()
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scanning For IP\'s, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        for i in lines:
            i = i.decode("utf-8")
            if i.startswith('http'):
                try:
                    a = i.split('/')
                    a = a[2]
                    v = socket.gethostbyname(a)
                    print("\033[0;36m[Server]\033[0m {}    \033[0;32m[IP] \033[0m\033[0;31m{}".format(i, v))
                    with open("HostsIP.txt", "a") as file:
                        file.write(v+'\n')
                except socket.error:
                    print('\033[0;31m[Server Don\'t Respond] \033[1;30m{}'.format(i))
            else:
                i = "http://" + i
                try:
                    a = i.split('/')
                    a = a[2]
                    v = socket.gethostbyname(a)
                    print("\033[0;36m[Server]\033[0m {}    \033[0;32m[IP] \033[0m\033[0;31m{}".format(i, v))
                    with open("HostsIP.txt", "a") as file:
                        file.write(v+'\n')
                except socket.error:
                    print('\033[0;31m[Server Don\'t Respond] \033[1;30m{}'.format(i))
        print(Fore.MAGENTA +'[x] Saved results in HostsIP.txt')
    except FileNotFoundError:
        print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')



#using youGetSignal API
def RevereseIP_Domain():
    """function to grab hosts in a webserver IP entered by the user
        using Json module we exract the data after sending a POSTS requests with using 
        YouGetSignal API """
    ip = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter An IP To Grab Website From A Server: '+ Fore.LIGHTWHITE_EX)
    print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scanning For WebSites On Entered IP Server , Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")     
      
    payload = {
        "remoteAddress": ip,
		"key": "",
		"_": ""
    }   
    url = "https://domains.yougetsignal.com/domains.php"
    res = requests.post(url, data=payload, headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}, timeout=20)
    data = res.json()
    if data['status'] == "Success" and data['domainCount']=='0' and data["message"] == "No web sites found.":
        print('\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m Can\'t Find Hosts On These IP Server')
    elif data['status'] == 'Fail' and data['message']=='Service unavailable.':
        print("\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m Opss, There Is An Error Please Retry Again")
    elif data['status'] == "Fail" and 'Daily reverse IP check' in data['message']:
        print(Fore.RED + '\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m You Reach The Limit, Change Your IP Or Retry Later')
    elif data["status"] == "Success" and int(data['domainCount']) > 0:
        for i in data["domainArray"]:
            var = "\n".join(i)    
            var = "".join(i)
            time.sleep(0.05) 
            print("\033[0;31m>>>\033[0m\033[0;31m"+" "+ Fore.WHITE+var)
            with open('ReverseIP.txt', 'a') as file:
                file.write(var + '\n')
        print(Fore.MAGENTA +'[x] Saved results in ReverseIP.txt')
   
   
       
def FindAdmin_panel():
    """function to find admin panels of hosts in a file entered by the user
        we check the requests status than we try different possibilites to find the Admin Panel"""
    try:
        possiblity = (
            '/admin','/admin.php',"/admin/index.php","/login/index.php","/wp-login.php","/admin/login.php","/administrator.php","/login.php","/login/admin.php",
            "/login/administrator.php",'/dashboard/','/dashboard/index.php',"/dashboard/login.php","/administration/login.php"
            ,'/admin_login.php',"/administrator/","/login/admin","/administration",
            '/admin/admin-login.php' 
        )
        time.sleep(1)
        admin_list = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter The Name File : '+ Fore.LIGHTWHITE_EX)  
        file = open(admin_list, 'rb')
        line = file.read().splitlines()  
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scannig For Admin Panels, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
       
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
                        req = requests.get(qq, timeout = 10)
                        shit = req.text
                        if  req.status_code == 200 and 'type="password"' in shit:
                            print("\033[0;31m[\033[0;32m>>>\033[0;31m]\033[0;31m[\033[0;32mPanel Found\033[0;31m]\033[0;31m" +"    "+ Fore.WHITE + qq)
                            with open('AdminPanles.txt' ,'a') as admin:
                                admin.write(qq + '\n')
                        else:
                            print('\033[0;31m[-]\033[0;31m[Not Found\033[0;31m]\033[0;31m\033[0;31m[-]' + Fore.WHITE + qq)
                    except requests.ConnectionError:
                        pass
                    except requests.exceptions.ChunkedEncodingError:
                        pass
                    except requests.exceptions.ReadTimeout:
                        pass
            elif i.startswith('http'):
                print(" \n \033[95m[\033[95m\033[5m+\033[0m\033[95m] \033[95mScan " + Fore.WHITE +  i  )
                for j in possiblity:
                    tout = i + j
                    della3 = tout.replace("\'","")
                    try:
                        socket.setdefaulttimeout(1)
                        req = requests.get(della3, timeout= 10)
                        if  req.status_code == 200 and 'type="password"' in req.text :
                            print("\033[0;31m[\033[0;32m>>>\033[0;31m]\033[0;31m[\033[0;32mPanel Found\033[0;31m]\033[0;31m" +"    "+ Fore.WHITE + della3)
                            with open('AdminPanles.txt' ,'a') as admin:
                                admin.write(della3 + '\n')
                        else:
                            print('\033[0;31m[-]\033[0;31m[Not Found\033[0;31m]\033[0;31m\033[0;31m[-]' + Fore.WHITE + della3)    
                    except requests.ConnectionError:
                        pass
                    except requests.exceptions.ChunkedEncodingError:
                        pass
                    except requests.exceptions.ReadTimeout:
                        pass
                    except:
                        pass                
        print(Fore.MAGENTA +'[x] Saved results in AdminPanels.txt')
    except FileNotFoundError:
        print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')       
           
                
   

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
            p += 1
        print(Fore.MAGENTA +'[x] Saved results in Grabbed_Dorks.txt')
    except requests.exceptions.ChunkedEncodingError:
        pass
    except requests.exceptions.SSLError:
        pass
    except requests.exceptions.ConnectionError:
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
        print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')




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
        print(Fore.MAGENTA +'[x] Saved Results In Notifier.txt')
    



def Ip_range():
    try:
        path = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter The IP\'s File : '+ Fore.LIGHTWHITE_EX)     
        file = open(path, "rb")
        zerf = file.read().splitlines()
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Start IP\'s Range , Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        for i in zerf:
            print(" \033[0;31m[\033[5m+\033[0m\033[0;31m] \033[1;30mRange \033[0;36m{}" .format(i.decode('utf-8')))
            a = 0 
            while a <= 255:
                ip = i.decode('utf-8')
                #print( Fore.CYAN +" [*] Range {}" .format(ip))
                ip = ip.split('.') 
                a = str(a)
                ip[3] =a 
                final_IP = '.'.join(ip)
                response = subprocess.Popen(["ping", "-c", "1",final_IP ],
                stdout = subprocess.PIPE,
                stderr = subprocess.STDOUT)
                stdout, stderr = response.communicate()
                if (response.returncode == 0):
                    print(
                            "        "+'\033[0;37m'+final_IP +"        "+"\033[0;32mLive")
                    with open("IP_Range.txt", "a") as file:
                        file.write(final_IP + "\n")
                else:
                    print(
                            "        "+'\033[0;37m'+final_IP +"        "+"\033[0;31mDead")
                a = int(a)                    
                a += 1
        print(Fore.MAGENTA +'[x] Saved Results In IP_Range.txt')        
    except FileNotFoundError:
        print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')
    
    
    


def brute():
    choose = (
        "\033[0;37m[\033[0;31m1\033[0;37m] \033[0m - \033[0;34mBrute Force Wordpress Panels\n"
        "\033[0;37m[\033[0;31m1\033[0;37m] \033[0m - \033[0;34mBrute Force Joomla Panels\n"
        "\033[0;37m[\033[0;31m1\033[0;37m] \033[0m - \033[0;34mBrute Force Drupal Panels\n"
        "\033[0;37m[\033[0;31m1\033[0;37m] \033[0m - \033[0;34mBrute Force Open Cart Panels"
    )
    print(choose)
    ch = input('Enter A Section')

def mirroh_h():
    pass    

def network_scanner():
    pass
    


def SQL_Scanner():
    try:

        path = input('Enter the file:')
        file = open(path, "rb")
        line =  file.read().splitlines()
        sss =( "DB Error", "SQL syntax;", "mysql_fetch_assoc", "mysql_fetch_array", "mysql_num_rows","is_writable",
                "mysql_result", "pg_exec", "mysql_result", "mysql_num_rows", "mysql_query", "pg_query",
                "System Error","io_error", "privilege_not_granted", "getimagesize", "preg_match",
                "mysqli_result", 'mysqli'
        )
        headers  = {
            "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        for i in line:
            i = i.decode("utf-8")
            print(" \n \033[95m[\033[95m\033[5m+\033[0m\033[95m] \033[95mScan " + Fore.WHITE +  i  )
            if i.startswith('http'):
                for error in sss:
                    
                    req = requests.get(i + "'", headers= headers)
                    if error in req.text:
                        print('[+]' + "" + i.replace("'", "") + "Vulerable For SQL Injection")
                        with open('SQL_Injection.txt', "a") as  sql:
                            sql.write(i+ "\n")
                    else:
                        pass
                   
            else:
                i="http://" + i
                for error in sss:
            #        try:
                    req = requests.get(i + "'" , headers=headers)
                    if error in req.text:
                        print(i +"vulenrabe")
                        with open("SQL_Injection.txt", "a") as sql:
                            sql.write(i + "\n")
                    else:
                        pass
    #                except requests.exceptions.ConnectionError:
     #                   pass

        
    except FileNotFoundError:
        print("file not found retry")

def clean_scren():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

def typing(string):
    for words in string: 
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.005)

def local_IP():
    my_hostName = platform.node()
    my_ip = socket.gethostbyname(my_hostName)

def Public_Ip():
    url_publicIp =  "http://api.ipify.org/"
    req =requests.get(url_publicIp, headers={"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
    print(" Your Public IP IS >>> " + req.text)

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
    if choice == "8":
        SQL_Scanner()
    if  choice == "9":
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
                    if ssid == '': #or pkt.getlayer(Dot11Elt).ID != 0:
                        print ("Hidden Network Detected")
                    else:
                        print ("\033[0;31mNetwork Detected: \033[0;36m%s" % (ssid.decode('utf-8')))

        if __name__ == "__main__":
            try:
                idk = input(" enter the name of the interface on minotr mode (default; wlan0mon)")
                interface = idk
                thread = threading.Thread(target=hopper, args=(interface, ), name="hopper")
                thread.daemon = True
                thread.start()
                try:
                    sniff(iface=interface, prn=findSSID)
                except OSError:
                    pass
            except PermissionError:
                print("\033[0;31m[\033[5m-\033[0m\033[0;31m] Retry As Sudo [This Option Require root Privilege]")
                sys.exit()
    if choice == '10':
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Public IP Sniffer \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        Public_Ip()
    if choice =="11":
        local_IP()
        
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
                                                  
                                Greetz To : Bylka_Inj  Who Taught Me The Basics                                            """)
    typing(Fore.LIGHTGREEN_EX+"""
                        [@]Script Name: HackThisShit
                        [@]Coded By: B1LLAl """)
    print("""
    \033[0;31m[\033[1;33m\033[5mOPTIONS\033[0m\033[0;31m]:                                                          
            \033[0;37m---------[\033[0;36m\033[5mWEB-APP HACKING\033[0m\033[0;37m]---------                       \033[0;37m---------[\033[0;36m\033[5mWIRLESSE HACKING\033[0m\033[0;37m]---------                       
               \033[9m\033[0;31m[\033[0;32m1\033[0;31m]\033[0m: Grab Sites With Dorks                                \033[9m\033[0;31m[\033[0;32m9\033[0;31m]\033[0m: Scan For Access Points [Monitor Mode Requiered]  
               \033[0;31m[\033[0;32m2\033[0;31m]\033[0m: Grab Sites From Zone-H.org [From 3 Sections]         \033[9m\033[0;31m[\033[0;32m10\033[0;31m]\033[0m: My Public IP
               \033[0;31m[\033[0;32m3\033[0;31m]\033[0m: Grab Sites From Bing [With IP List]                  \033[9m\033[0;31m[\033[0;32m11\033[0;31m]\033[0m: IfConfig                       
               \033[0;31m[\033[0;32m4\033[0;31m]\033[0m: Mass IP Scanner         
               \033[0;31m[\033[0;32m5\033[0;31m]\033[0m: Reverse IP Domain [Grab Hosts In a WebServer With IP]                     
               \033[0;31m[\033[0;32m6\033[0;31m]\033[0m: Find Admin Panels    
               \033[0;31m[\033[0;32m7\033[0;31m]\033[0m: Auto scan for sql  injection                                       
               \033[0;31m[\033[0;32m8\033[0;31m]\033[0m: IP Range [Check IP Dead/Alive]
               """)
    choices() 

all_in_one()  
##cockkd By : ZERF ##
##All in one ##


