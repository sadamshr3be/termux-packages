#librys   المكتبات
import os
import sys
import time
import datetime
import random
import compileall
#start
c = ['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
os.system('clear' )
os.system('clear') 
print(random.choice(c))
#__________________________________________________________________________
banner=""" 
    _    _       _                     _     _       / \  | |  ___| |__   __ _ _ __ __ _| |__ (_)
  / _ \ | | / __| '_ \ / _` | '__/ _` | '_ \| |    / ___ \| | \__ \ | | | (_| | | | (_| | |_) | |
/_/   \_\_| |___/_| |_|\__,_|_|  \__,_|_.__/|_|
                       """
#                       
print(banner)

print('\033[1;31m [+]Follow Me :')
print('\033[1;34m [1]YOUTUBE  : sadamalsharabi80 ' )
print('\033[1;34m [2]Tiktok   : sadamalsharabi ')
print('\033[1;34m [3]Telegram : @termuxalsharabi ')
print('\033[1;31m [+]TOOLS: ')
def main():
    print('')
    print("\033[1;31m[1] \033[1;34mInstall pkg Termux\033[1;31m(termux)")
    time.sleep(0.3)
#________________
    print("\033[1;31m[2] \033[1;34mInstall metasploit\033[1;31m(termux)")
    time.sleep(0.3)
#__________________
    print("\033[1;31m[3] \033[1;34mInstall ngrok\033[1;31m(termux,kali)")
    time.sleep(0.3)
#___________________
    print("\033[1;31m[4] \033[1;34mEncrypt tools\033[1;31m(termux)")
    time.sleep(0.3)
#____________________
    print('\033[1;31m[5] \033[1;34mscript metesploit\033[1;31m(termux,kali)')
    time.sleep(0.3)
#____________________
    print("\033[1;31m[6] \033[1;34mEvil-Droid\033[1;31m(kali)")
    time.sleep(0.3)
#______________________
    print("\033[1;31m[7] \033[1;34mnexphisher\033[1;31m(termux,kali)")
    time.sleep(0.3)
#______________________
    print("\033[1;31m[8] \033[1;34msqlmap\033[1;31m(termux,kali)")
    time.sleep(0.3)
#_______________________
    print("\033[1;31m[9] \033[1;34mnikto\033[1;31m(termux,kali)")
    time.sleep(0.3)
#________________________
    print("\033[1;31m[10] \033[1;34mnmap\033[1;31m(termux,kali)")
    time.sleep(0.3)
#___________________________
    print("\033[1;31m[11] \033[1;34mnethunter kali\033[1;31m(termux)")
    time.sleep(0.3)
#______________________________________
#___________________________
    print("\033[1;31m[11] \033[1;34mnethunter kali\033[1;31m(termux)")
    time.sleep(0.3)
#______________________________________
    print('\033[1;31m[12] \033[1;34m Ip_Web \033[1;31m(termux,kali) ')
    time.sleep(0.3)
#______________________________________
    print('\033[1;31m[13] \033[1;34m Dork_google \033[1;31m(termux,kali) ')
    time.sleep(0.3)
#__________________________________________
    print('\033[1;31m[14] \033[1;34m Scan Ports \033[1;31m(termux,kali) ')
    time.sleep(0.3)
#_________________________________________________________________________
    print('\033[1;31m[15] \033[1;34m apktoolfix \033[1;31m(kali) ')
    time.sleep(0.3)
main()
choose = input("\033[1;37mChoose an option : ")
time.sleep(0.3)
#_______________________________________________________
#commands
if choose == '1':
    jalan("Just wait for the download to finish")
    os.system('pip install --upgrade pip ')
    os.system('pkg update && upgrade -y ;pip install --upgrade pip ; pkg install git -y ; pkg install nano -y ; pkg install python -y ; pkg install python2 -y ; pkg install php -y;pkg install unzip -y ; pkg install openssh -y ; pkg install cat -y ; pkg install curl -y ; pkg install wget -y ; pkg install w3m -y  ; pkg install havij -y ; pkg install db -y ; pkg install postgresql -y ; pkg install uftrace -y ; pkg install ruby -y ; pkg install perl -y; pkg install bash -y ;pkg install figlet -y;pkg install cowsay -y; pkg install tar -y;pkg install zip -y; pkg install tor -y; pkg install toilet -y;pkg install proot -y ; pkg install openssl -y; pkg install cmatrix -y ; pkg install macchanger ;pkg install root-repo -y;pkg install unstable-repo -y;pkg install x11-repo -y ; pip install --upgrade pip ')
    os.system('clear')
    print("\033[1;31mThe installation was successful")
    time.sleep(3)
##############################################################
elif choose == '2':
    Y=input("install termux[1] linux[2] : ")
    if Y =='1':
        a=input('step[1] , step[2]  :')
        if a =='1':
            os.system('wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh')
            os.system('chmod +x  metasploit.sh')
            os.system('bash metasploit.sh')
        elif a=='2':
            os.system('apt update && apt upgrade')
            os.system('pkg install git python python2 -y')
            os.system('pip install lolcat')
            os.system('git clone https://github.com/h4ck3r0/Metasploit-termux')
            print('please copy and paste :')
            print('cd Metasploit-termux')    
            print('bash metasploit.sh')
##############################################################
elif choose == '3':
    q=input("install termux[1] linux[2] : ")
    if q =='1':
        os.system('cd $HOME')
        os.system("clear")
        os.system('pkg install tar ')
        os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz')
        os.system('cd /sdcard/Download')
        os.system('tar zxvf ngrok-stable-linux-arm.tgz')
        os.system('mv ngrok $HOME')
        os.system('cd')
        os.system('chmod +x ngrok')
        jalan ('\033[1;31mThe tool was loaded successfully')
        os.system('clear')
        print("Done")
        time.sleep(3)
        #print(logo)
        main()
        time.sleep(0.3)
    elif q == '2':
        os.system("cd /root/Desktop")
        os.system('wget  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip  ')
        os.system('unzip ngrok-stable-linux-amd64.zip ')
        os.system('xdg-open https://dashboard.ngrok.com/signup ')
        os.system('chmod +x ngrok')
        os.system("rm -rf ngrok-stable-linux-amd64.zip")
        os.system("mv ngrok /root/Desktop")
        print('\033[1;31m please copy the {2}  to Connect your account:  and copy paste here ')
        jalan ('\033[1;31mThe tool was loaded successfully')
##############################################################
elif choose == '4':
    tool_list = str(input(" \033[1;36mType the path for the tool: "))
    compileall.compile_file(tool_list)
    e=input("linux[1] TERMUX [2] : ")
    if e =='1':
        jalan('\033[1;31mEncryption successful')
        jalan("\033[1;36mSave to /Desktop/)_____Dark_____") 
        time.sleep(3)
        os.system('exit')
    elif e=="2":
        jalan('\033[1;31mEncryption successful')
        jalan("\033[1;36mSave to /sdcard/)_____Dark_____")
################################################################
elif choose =='5':
    os.system('clear')
    e=input("linux[1] TERMUX [2] : ")
    if e =='1':
        os.system('xdg-open https://drive.google.com/file/d/1Qr9ieS5h6PPaDjwm6AT1suQc8iwkMdnc/view')
        jalan ('\033[1;31mThe tool was loaded successfully')
    elif e =='2':
        jalan ('\033[1;31mThe tool was loaded successfully')
        os.system('xdg-open https://drive.google.com/file/d/1Qr9ieS5h6PPaDjwm6AT1suQc8iwkMdnc/view')
#################################################################################################
elif choose =='6':
    os.system('git clone https://github.com/M4sc3r4n0/Evil-Droid.git')
    print('#################################')
    print('please copy and paste here 😗️>>>>>>>>>>>>>>>>..🥰️:')
    print("##################################")
    print('====================================')
    print('cd Evil-Droid')
    print('chmod +x *')
    print('./evil-droid')
    print('=====================================')
######################################################
elif choose =='7':
    os.system('clear')
    os.system('cd $HOME ' )
    os.system('git clone https://github.com/htr-tech/nexphisher.git')
    os.system('clear')
    print('please copy and paste here 😗>>>>>>>>>>>>>>>>..🥰:')
    print("##################################")
    print('====================================')
    print('cd nexphisher ')
    print('chmod +x *')
    print('bash setup(kali)')
    print('bash tmux_setup(termux)')
    print('=====================================')
#####################################################################
elif choose=='8':
    os.system('clear')
    os.system('git clone https://github.com/sqlmapproject/sqlmap.git ')
    print('TO Run Tool =====>')
    print('cd sqlmap')
    print('python3 sqlmap.py')
#########################################################################
elif choose=='9':
    os.system('git clone https://github.com/sullo/nikto')
    print('TO Run Tool =====>')
    print('cd nikto/program')
    print('./nikto.pl -h ')
##########################################################################
elif choose=='10':
    os.system('clear')
    a=input('Termux[1] Linux[2] :')
    if a =='1':
        os.system('clear')
        os.system('pkg install nmap')
    else:
        os.system('sudo apt-get install nmap')
###########################################################################

elif choose=='11':
    os.system('clear')
    print(banner)
    os.system('pkg update')
    os.system('pkg upgrade')
    os.sytem('clear')
    os.sytem('pkg install wget')
    os.system('wget -O install-nethunter-termux https://offs.ec/2MceZWr')
    os.system('chmod +x install-nethunter-termux')
    os.system('./install-nethunter-termux')
#########################################################################
elif choose=='12':
    os.system('clear')
    print(banner)
    import os
    import socket 
    import sys
##############
    print('Enter you DNS : ')
    hostname=input('')
    ip=socket.gethostbyname(hostname)
    print('Target IP is:  ',ip)
###################################
elif choose=='13':
    print(banner)
    ###################
    #googlesearch
    #sql injection 
    #dork
    import os
    from googlesearch import *
    os.system('clear')
    print('\033[1;31m')
###############################################
    print(banner)
    user=input('\033[1;37m Enter your Dork : ')
    for url in search(user):
        print(url)
###########################################
elif choose=='14':
    print(banner)
    import socket
    target=input('Enter your IP: ')
    port=input('Enter your Port to Scan :')
    for p in port :
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        r=s.connect_ex((target,p))
        if r =='0':
            service=socket.getservbyport(p)
            print('..{ *{} * is open --> '.format(p,service))
        s.close()
######################################################\
elif choose=='15':
    os.system('clear')
    print(banner)
    os.system('git clone https://github.com/graylagx2/apktoolfix')
    print('cd apktoolfix ')
    print('bash apktoolfix_2.1.2.sh')
######################################################################
