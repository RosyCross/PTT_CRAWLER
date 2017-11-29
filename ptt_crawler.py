# -*- coding: cp950 -*-
# Hello World program in Python
    
import telnetlib
import sys
import time
import re

username = ''
password = ''
press_any_key = '\s'
#ctrl+L

def ptt_m_crawler():
    main()
    
def reloadScreen(tn):
    tn.write(b'\x0C')
    
def logout(tn):
        print("crawler ==> logging out...")  
        tn.write(b"qqqqqqqqqg\r\ny\r\n")
        time.sleep(1)
        tn.close()
        print("crawler ==> logged out")
        
def is_connected(content):
    #print(content.find("批踢踢實業坊"))
    #print(content.find("我是"))    
    return all(x in content for x in ["批踢踢實業坊","我是"] )      

def go_movie(tn):
    commands = 'smovie'+'\r'+'\s\s\s'
    tn.write(commands.encode('ascii'))
    time.sleep(1)
    
#=============================
def main():
    tn = telnetlib.Telnet('ptt.cc')
    time.sleep(1)
    content = tn.read_very_eager().decode('big5','ignore')
    #content = tn.read_very_eager()
    #print(type(content))
    #print(content)

    if "請輸入代號" not in content:
        print ('crawler ==> cannot input username/password. leave')
        sys.exit(1)
        
    print("crawler ==> inputing username/password...")
    print('Username:');
    username = input();
    print('Password:');
    password = input();    
    tn.write( (username+"\r\n").encode('big5') )
    time.sleep(1)
    tn.write( (password+"\r\n").encode('ascii') )
    time.sleep(1)
    content = tn.read_very_eager().decode('big5','ignore')
    print (content)
    print ('===================')
    while "任意鍵" in content:
        tn.write( press_any_key.encode('big5') )
        time.sleep(1)
        content = tn.read_very_eager().decode('big5','ignore')
    print (content)
    print('================')  
    time.sleep(1)              
    print('================')
    
    print(content.find('批踢踢實業坊'))        
    print (is_connected(content))

    go_movie(tn)
    content = tn.read_very_eager().decode('big5','ignore')
    print (content)
    print("should read nothing")
    content = tn.read_very_eager().decode('big5','ignore')
    print(content)
    reloadScreen(tn);
    print("should read somethingthing")
    content = tn.read_very_eager().decode('big5','ignore')
    print(content)
    
    
    logout(tn)

if __name__ == "__main__":
    main()
