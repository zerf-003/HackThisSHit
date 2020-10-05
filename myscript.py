### path: /usr/bin/python3.8 ###
### codage : "UTF-8" ###
### Coded BY : Z3RF-003 ###
### Script name : HackThisShit ###

#import modules
import socket 
import os
import sys 
import platform
from platform import system
import requests
import json
import  time
import random
import re
import subprocess
try:
    import colorama
except ModuleNotFoundError:
    var = subprocess.Popen(['pip3', "install", "colorama"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    print('Installing Colorama Module')
from colorama import init,Fore
try:
    import networkscan
except ModuleNotFoundError:
    var = subprocess.Popen(['pip3', "install", "networkscan"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    print('\033[0;32m[\033[1;33m+\033[0;32m] Installing Network Scanner Module')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def MassIPScanner():
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
                    print('\033[0;31m[Server Doesn\'t Respond] \033[1;30m{}'.format(i))
           
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
                    print('\033[0;31m[Server Doesn\'tn\'t Respond] \033[1;30m{}'.format(i))
        print(Fore.MAGENTA +'[x] Saved results in HostsIP.txt')
    except FileNotFoundError:
        print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#using youGetSignal API
def RevereseIP_Domain():

    ip = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter An IP To Grab Website From A Server: '+ Fore.LIGHTWHITE_EX)
    print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scanning For WebSites On Entered IP Server , Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")     
      
    payload = {
        "remoteAddress": ip,
		"key": "",
		"_": ""
    }   
    url = "https://domains.yougetsignal.com/domains.php"
    res = requests.post(url, data=payload,verify=True, headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}, timeout=20)
    data = res.json()
    
    if data['status'] == "Success" and data['domainCount']=='0' and data["message"] == "No web sites found.":
        print('\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m Can\'t Find Hosts On These IP Server')
    elif data['status'] == 'Fail' and data['message']=='Service unavailable.':
        print("\033[1;30m[\033[0;31m\033[5m-\033[0m\033[1;30m]\033[0m\033[0;31m Opss, Please Retry Again")
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
   
   


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       
def FindAdmin_panel():
   
    try:
        possiblity = (
            '/wp-login.php','/admin','/admin.php',"/admin/index.php","/login/index.php","/admin/login.php","/administrator.php","/login.php","/login/admin.php",
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
                        req = requests.get(qq,verify=True, timeout = 10)
                        shit = req.text
                        if req.status_code == 200 and 'type="password"' in shit:
                            print("\033[0;31m[\033[0;32m>>>\033[0;31m]\033[0;31m[\033[0;32mPanel Found\033[0;31m]\033[0;31m" +"    "+ Fore.WHITE + qq)
                            with open('AdminPanles.txt' ,'a') as admin:
                                admin.write(qq + '\n')
                        else:
                            print('\033[0;31m[---]\033[0;31mNot Found\033[0;31m\033[0;31m\033[0;31m'+ " "+ Fore.WHITE + qq)
                            
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
                        req = requests.get(della3,verify=True, timeout= 10)
                        if  req.status_code == 200 and 'type="password"' in req.text :
                            print("\033[0;31m[\033[0;32m>>>\033[0;31m]\033[0;31m[\033[0;32mPanel Found\033[0;31m]\033[0;31m" +"    "+ Fore.WHITE + della3)
                            with open('AdminPanles.txt' ,'a') as admin:
                                admin.write(della3 + '\n')
                        else:
                            print('\033[0;31m[---]\033[0;31mNot Found\033[0;31m\033[0;31m\033[0;31m' +" "+ Fore.WHITE + della3)    
                   
                   
                    except requests.ConnectionError:
                        pass
                    except requests.exceptions.ChunkedEncodingError:
                        pass
                    except requests.exceptions.ReadTimeout:
                        pass
                                   
        print(Fore.MAGENTA +'[x] Saved results in AdminPanels.txt')
    except FileNotFoundError:
        print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')       
           
                
   
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def Grab_with_queries():
    code = {
        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    ch = (
        "\033[0;37m[\033[0;31m1\033[0;37m] \033[0m - \033[0;34m Grab With Dork List \n"
        "\033[0;37m[\033[0;31m2\033[0;37m] \033[0m - \033[0;34m Grab With An Entered Dork\n"  
    )
    print("\n" + ch)
    fff  = input("\033[0;31m[\033[0;32m\033[5m#\033[0;31m]\033[0m Choose a section: " +Fore.LIGHTWHITE_EX)
    if fff == "1":
        try:
            path = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter A Dorks File To Grab Websites : '+ Fore.LIGHTWHITE_EX)
            file = open(path)
            lines = file.read().splitlines()
            print(Fore.RED +"\n------------"+ Fore.CYAN +"[Grab Site With Dork List, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
            for i in lines:
                print("\n\033[0;32m[+]\033[1;33mGrabbing With Dork: \033[0;31m{}".format(i))
                page = 1
                try:
                    repetion = []
                    while page<251:
                        url = "https://www.bing.com/search?q="+str(i)+"+&count=50&first="+str(page)
                        req = requests.get(url, verify=True, headers=code)
                        content = req.content
                        urls = re.findall('<h2><a href="(.*?)"', str(content))
                        for jj in urls:
                            if jj in repetion:
                                pass
                            else:
                                repetion.append(jj)
                                time.sleep(0.05)
                                print("\033[0;32m\033[0m\033[0;31m>>>\033[0;32m\033[0m" + " " + Fore.WHITE+jj)
                                with open('Grabbed_Dorks.txt', 'a') as file:
                                    file.write(jj + '\n')
                        page += 5 
                   
                except requests.exceptions.ChunkedEncodingError:
                    pass
                except requests.exceptions.SSLError:
                    pass
                except requests.exceptions.ConnectionError:
                    pass
            print(Fore.MAGENTA +'[x] Saved results in Grabbed_Dorks.txt')          
        except FileNotFoundError:
            print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')
    elif fff == "2":
        querie = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter A Querie To Grab Websites : '+ Fore.LIGHTWHITE_EX)
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Grabbing Sites With Dork, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        p = 1 
        try:
            repetion = [] 
            while p < 251:     
                url = "https://www.bing.com/search?q="+str(querie)+"+&count=50&first="+str(p)
                req = requests.get(url,verify=True, headers = code)
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
    else:
        print("chosse a section bitch")
    

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def Grab_Bing():
    try:
        file = input(Fore.YELLOW +'[\033[5m#\033[0m' + Fore.YELLOW+']Enter The IP\'s File : '+ Fore.LIGHTWHITE_EX)   
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Grabbing Sites From Bing, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------") 
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



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
            req = requests.get(url, verify=True,headers = user_agent, cookies = all_)
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
            req = requests.get(url,verify=True, headers =user_agent,cookies = all_)
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
            req = requests.get(url,verify=True, headers = user_agent, cookies = all_)
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
    


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
    
    

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def SQL_Scanner():
    try:

        path = input(Fore.YELLOW+'[\033[5m#\033[0m' + Fore.YELLOW+']Enter a Hosts File : '+ Fore.LIGHTWHITE_EX)
        file = open(path, "rb")
        line =  file.read().splitlines()
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scannig For SQL Injection Vuln, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        sss =( "DB Error", "SQL syntax;", "mysql_fetch_assoc", "mysql_fetch_array", "mysql_num_rows","is_writable",
                "mysql_result", "pg_exec", "mysql_result", "mysql_num_rows", "mysql_query", "pg_query",
                "System Error","io_error", "privilege_not_granted", "getimagesize", "preg_match",
                "mysqli_result", 'mysqli', 'SmartyException'
        )
        headers  = {
            "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }

        for i in line:
            i = i.decode("utf-8")
            print(" \n \033[95m[\033[95m\033[5m+\033[0m\033[95m] \033[95mScan " + Fore.WHITE +  i  )
            if i.startswith('http'):
                try:
                    req = requests.get(i,verify=True, headers = headers)
                    if req.status_code == 200:
                        cont = req.text
                        find =re.findall(r'href=[\'"]?([^\'" >]+)', cont)
                        if len(find) == 0:
                            print('\033[0;31m[\033[0;31m\033[5m-\033[0;31m]' +' \033[0;31mCan\'t Find Injections Points')
                        elif len(find) != 0:
                            for _ in find:
                                if '.php?' in str(_):
                                    print("\033[0;31m[\033[1;33m+\033[0;31m] \033[1;34mInjcetion Points Found....Checking For SQL Errors (Trying SQLi)") 
                                    try:
                                        req =requests.get(i + "/" + _ +"'",verify=True, headers = headers)
                                        for err in sss:
                                            if err in req.text: 
                                                print('\033[1;33m[\033[0;32m+\033[1;33m] \033[0;31m>>>' + " " +"\033[0;35m"+ i.replace("'", "") +" " +  """\033[0;32mVulerable For SQL Injection
                                                \033[1;33m[\033[0;32m+\033[1;33m] \033[0;31m>>> \033[0;35mInjection Point: \033[0;31m{}    """.format( i + '/' + _)) 
                                                with open('SQLiTargets.txt', 'a') as sql:
                                                    sql.write(i + "/" + _  +"\n")
                                                break 
                                            else:
                                                time.sleep(0.5)
                                                print('\033[0;31m[\033[0;31m\033[5m-\033[0;31m]' +' \033[0;31mNot Vulnerable')          
                                        break                 
                                    except requests.exceptions.ChunkedEncodingError:
                                        pass
                                    except requests.exceptions.SSLError:
                                        pass
                                    except requests.exceptions.ConnectionError:
                                        pass   
                                    except requests.exceptions.MissingSchema:
                                        pass                                
                                else:
                                    pass
                    else:
                        print('\033[0;31m[\033[0;31m\033[5m-\033[0;31m]' +' \033[0;31mCrashed')
                except requests.exceptions.ChunkedEncodingError:
                    pass
                except requests.exceptions.SSLError:
                    pass
                except requests.exceptions.ConnectionError:
                    pass    
                except requests.exceptions.MissingSchema:
                    pass
            else:
                try:
                    req = requests.get(i,verify=True, headers = headers)
                    if req.status_code == 200:
                        cont = req.text
                        find =re.findall(r'href=[\'"]?([^\'" >]+)', cont)
                        if len(find) ==0:
                            print('\033[0;31m[\033[0;31m\033[5m-\033[0;31m]' +' \033[0;31mCan\'t Find Injections Points')
                        elif len(find) != 0:
                            for _ in find:
                                if '.php?' in str(_):
                                    print("\033[0;31m[\033[1;33m+\033[0;31m] \033[1;34mInjcetion Points Found....Checking For SQL Errors (Trying SQLi)")  
                                    try:
                                        req =requests.get(i + "/" + _ +"'",verify=True, headers = headers)
                                        for err in sss:
                                            if err in req.text: 
                                                print('\033[1;33m[\033[0;32m+\033[1;33m] \033[0;31m>>>' + " " +"\033[0;35m"+ i.replace("'", "") +" " +  """\033[0;32mVulerable For SQL Injection
                                                \033[1;33m[\033[0;32m+\033[1;33m] \033[0;31m>>> \033[0;35mInjection Point: \033[0;31m{}    """.format( i + '/' + _)) 
                                                with open('SQLiTargets.txt', 'a') as sql:
                                                    sql.write(i + "/" + _  +"\n")
                                                break 
                                            else:
                                                time.sleep(0.5)
                                                print('\033[0;31m[\033[0;31m\033[5m-\033[0;31m]' +' \033[0;31mNot Vulnerable')                
                                        break               
                                    except requests.exceptions.ChunkedEncodingError:
                                        pass
                                    except requests.exceptions.SSLError:
                                        pass
                                    except requests.exceptions.ConnectionError:
                                        pass                           
                                    except requests.exceptions.MissingSchema:
                                        pass        
                                else:
                                    pass
                    else:
                        print('\033[0;31m[\033[0;31m\033[5m-\033[0;31m]' +' \033[0;31mCrashed')
                except requests.exceptions.ChunkedEncodingError:
                    pass
                except requests.exceptions.SSLError:
                    pass
                except requests.exceptions.ConnectionError:
                    pass  
        print(Fore.MAGENTA +'[x] Saved Results In SQLiTargets.txt')   
    except FileNotFoundError:
        print('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;31mFile Not Found')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def wifi_jammer():
    if not os.geteuid() == 0:
        print("\033[0;31m[\033[5m-\033[0m\033[0;31m] Rerun The Script as sudo [This Option Require root Privilege]")
        sys.exit()
    else:
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scannig Access Points, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        iwconfig = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
        a = iwconfig.stdout.read()
        a= a.decode("utf-8")
        a = a.split("\n")
        print("\033[0;32m[\033[1;33m+\033[0;32m] \033[0;31mChecking All Network Interfaces")
        for i in a:
            search =re.findall("eth[0-9]|em[0-9]|p[1-9]p[1-9]", i) 
            if not search:
                iface = i[:i.find(' ')]
                if len(iface)< 1:
                    pass
                elif len(iface)>= 1:
                    scannig = subprocess.Popen(['iwlist', iface, "scan"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
                    proc = scannig.stdout.read()
                    proc = proc.decode("utf-8")
                    if '- Address' in str(proc):
                        airmon_ng = subprocess.Popen(['which', "airmon-ng"],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
                        airodump_ng = subprocess.Popen(['which', 'airodump-ng'], stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
                        stderr,stdout = airmon_ng.communicate()
                        stderr, stdout = airodump_ng.communicate()
                        if airmon_ng.returncode == 0 and airodump_ng.returncode==0:
                            print('\033[0;32m[\033[1;33m+\033[0;32m] \033[0;31mKilling The Processes')
                            scan = subprocess.Popen(["sudo",'airmon-ng', 'check', "kill"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
                            scan = subprocess.Popen(["sudo",'airmon-ng', 'start', iface], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
                            time.sleep(5)    
                            iwconfig = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr = subprocess.STDOUT)   
                            print('\033[0;32m[\033[1;33m+\033[0;32m] \033[0;31mGetting The Interface Card In Monitor Mode')
                            a = iwconfig.stdout.read()
                            a = a.decode('utf-8')
                            a = a.split('\n')
                            for i in a:
                                search =re.findall("eth[0-9]|em[0-9]|p[1-9]p[1-9]", i)
                                if not search:
                                    iface = i[:i.find(' ')]
                                    if len(iface)<1:
                                        pass
                                    elif len(iface)>=1:
                                        netw = subprocess.Popen(args=['echo', "0",'sudo', 'airodump-ng', iface], stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
                                        commun = netw.communicate()
                                        if netw.returncode == 0:
                                            netw.terminate() 
                                            shit = subprocess.Popen(['sudo',"xterm", '-e', 'airodump-ng', iface])                                          
                                        else:
                                            pass
                                else:
                                    pass
                        else:
                            print('\033[0;31m[\033[5m-\033[0m\033[0;31m] Check That Aircrack-ng & Xterm Tools Are Installed On Your Operating System')
                    else:
                        pass
               

def network_scanner():
    try:
        net1 = input('\033[0;31m[\033[0;36m\033[5m>\033[0;31m]\033[0mEnter a Network/IP To Scan (Ex:192.168.0.0/24, 10.0.0.1...etc): ')
        print(Fore.RED +"\n------------"+ Fore.CYAN +"[Scannig For IP\'s In The Networks, Please Wait\033[0m"+Fore.CYAN+"]"+Fore.RED+"------------")
        my_scan = networkscan.Networkscan(net1)    
        my_scan.run()
        print('\033[0;32m[\033[1;33m+\033[0;32m] \033[0;31mScan Network For IP\'s')
        for i in my_scan.list_of_hosts_found:
            time.sleep(0.05)
            print("\033[1;33m[\033[0;32m+\033[1;33m] \033[0;31m>>>" + " " +"\033[0;35m" + i   )
        print("[+]Number Of Hosts Found: \033[0;37m" + str(my_scan.nbr_host_found))
    except:
        print('\033[0;31m[-] Sorry, Something Is Going Wrong, Check That You Are Connected To A Network')

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
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print('\033[0;32m[\033[1;33m+\033[0;32m] \033[0;31mPlease wait... Scanning...')
        time.sleep(1.5)
        print("\033[0;36m[\033[0;31m+\033[0;36m]\033[0;36m \033[0;37mMy Local IP Is:"+"\033[0;31m"+s.getsockname()[0])
        s.close()
    except:
        print('\033[0;31m[-] Sorry, Something Is Going Wrong, Check That You Are Connected To A Network')

def Public_Ip():
    try:
        url_publicIp =  "http://api.ipify.org/"
        req =requests.get(url_publicIp, headers={"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
        print('\033[0;32m[\033[1;33m+\033[0;32m] \033[0;31mPlease wait... Scanning...')
        time.sleep(1.5)
        print("\033[0;36m[\033[0;31m+\033[0;36m]\033[0;36m \033[0;37mMy Public IP Is: " + "\033[0;31m"+ req.text)
    except:
        print('\033[0;31m[-] Sorry, Something Is Going Wrong, Check That You Are Connected To A Network')
    
def choices():    
    choice = input(Fore.LIGHTCYAN_EX +" \n[x] Choose options:  "+ Fore.LIGHTWHITE_EX)
    if choice == "1":
        typing('\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5mGrab Hosts With Dorks \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n')
        Grab_with_queries()    
    if choice == "2":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Zone-H.org Grabber \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        zone_h()
    if choice == "3":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Bing Grabber \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        Grab_Bing()
    if choice == "4":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Mass IP Scanner \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        MassIPScanner()
    if choice == "5":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Reverse IP Domain \033[0m \033[0;32mOption \033[0;36mENJOY ^__^ \n")
        RevereseIP_Domain()
    if choice == "6":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Admin Panel Finder \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        FindAdmin_panel()    
    if choice == "7":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m IP Range \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        Ip_range()
    if choice == "8":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m SQLi Scanner \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        SQL_Scanner()
    if  choice == "9":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Access Point Scanner \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")  
        wifi_jammer()      
    if choice == '10':
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Network Sniffer \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        network_scanner()
    if choice =="11":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Public IP Sniffer \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        Public_Ip()
    if choice == "12":
        typing("\033[0;37m[\033[0;31m\033[5mx\033[0;37m] \033[0;32m Welcome to \033[1;36m\033[5m Local IP Sniffer \033[0m \033[0;32mOption \033[0;36m ENJOY ^__^ \n")
        local_IP() 
    continueer = input(Fore.LIGHTRED_EX+'\n[+]Do you want to continue (y/n): '+ Fore.WHITE)
    if continueer == "y" or continueer == "Y":
        all_in_one()
    else: 
        clean_scren() 
        print("\033[0;31mThanks For Using My Script  ^____^")  
        exit()

#main fonction
def all_in_one():
    clean_scren()
    print("""
                             \033[0;31m ______   _____    ______     _________               ____     ____   _____   
                             (____  )  )__  \  (   __ \   (_   _____)             / __ \   / __ \  )__  \  
                                 / /    __) /   ) (__) )    ) (___     ________  ( (  ) ) ( (  ) )  __) /  
                             ___/ /_   (__ (   (    __/    (   ___)   (________) ( (  ) ) ( (  ) ) (__ (   
                            /__  ___)     \ \   ) \ \  _    ) (                  ( (  ) ) ( (  ) )    \ \  
                              / /____  ___/  ) ( ( \ \_))  (   )                 ( (__) ) ( (__) ) ___/  ) 
                             (_______) )____/   )_) \__/    \_/                   \____/   \____/  )____/  
               """)
      
    typing(Fore.LIGHTGREEN_EX+"""
                        \033[1;32m[@]Script Name: \033[0;31mHackThisShit                          \033[0;35mGreetz To: \033[0;32mAlg\033[0;31meri\033[0;37mans \033[0;37mHackers
                        \033[1;32m[@]Coded By: \033[0;31mB1LLAl                                   \033[0;35mGreetz To: \033[0;31mBylka_Inj \033[0;37m[Who Taught Me The Basics]                                 """)
    print("""
    \033[0;31m[\033[1;33m\033[5mOPTIONS\033[0m\033[0;31m]:                                                          
            \033[0;37m---------[\033[0;36m\033[5mWEB-APP HACKING\033[0m\033[0;37m]---------                                  
               \033[9m\033[0;31m[\033[0;32m1\033[0;31m]\033[0m: \033[0;37mGrab Sites With Dorks [By List / By Entered Dork]         
               \033[0;31m[\033[0;32m2\033[0;31m]\033[0m: \033[0;37mGrab Sites From Zone-H.org [From 3 Sections]         
               \033[0;31m[\033[0;32m3\033[0;31m]\033[0m: \033[0;37mGrab Sites From Bing [With IP List]                                         
               \033[0;31m[\033[0;32m4\033[0;31m]\033[0m: \033[0;37mMass IP Scanner [Fast]     
               \033[0;31m[\033[0;32m5\033[0;31m]\033[0m: \033[0;37mReverse IP Domain [Grab Hosts In a WebServer With IP]                     
               \033[0;31m[\033[0;32m6\033[0;31m]\033[0m: \033[0;37mFind Admin Panels    
               \033[0;31m[\033[0;32m7\033[0;31m]\033[0m: \033[0;37mIP Range [Check IP Dead/Alive]                                      
               \033[0;31m[\033[0;32m8\033[0;31m]\033[0m: \033[0;37mAuto Scan For SQL_INJECTION [With SQL Injection Point Finder]

            \033[0;37m---------[\033[0;36m\033[5mWIRLESSE HACKING\033[0m\033[0;37m]--------- 
               \033[9m\033[0;31m[\033[0;32m9\033[0;31m]\033[0m: \033[0;37mScan For Access Points [BSSID, ESSID, Encryption..etc]          
               \033[9m\033[0;31m[\033[0;32m10\033[0;31m]\033[0m: \033[0;37mNetwork Scanner [Find IP\'s In The Network]
               \033[9m\033[0;31m[\033[0;32m11\033[0;31m]\033[0m: \033[0;37mPublic IP Finder
               \033[9m\033[0;31m[\033[0;32m12\033[0;31m]\033[0m: \033[0;37mLocal IP Finder
               """)
    choices() 

all_in_one()  
##cockkd By : ZERF ##
##All in one ##

                                                          
    
