#test skript filter_ghoghnos
#GHOGHNOS_BLACK
import os
import sys
os.system("pip install time")
import time
from time import sleep
import random

#start


h='.'
g=random.randint(100,999)
e=random.randint(10,99)
d=random.randint(1,9)
c=random.randint(1,9)
b=random.randint(1000,9999)

#ABC

print(f'\033[31m')
x = ("""
                             ___          
                            /   \         
                           |  o  |         
                            \   /            
                     ________) (________            
                    |                   |     
                    '------.     .------'      
                            |   |               
                            |   |               
                            |   |                
                            |   |               
                            |   |                  
                 /\         |   |         /\      
                /_ \        /   \        / _\       
                  \ '.    .'     '.    .' /          
                   \  '--'         '--'  /           
                    '.                 .'            
                      '.             .'              
                          '-.   .-'                 
                             \ /                        
                              !
		""")
for CoursNight in x :
	sleep(0.002)
	print(CoursNight,end='' ,flush=True)
for i in range(1):
    a=input("""" 
            >>> accont rubika   = 1
            >>> chanel rubika   = 2
            >>> Group  rubika   = 3
            >>> guid   rubika   = 4
            <<>>
            >>>>>>>>>>>>>>>> """)
    print(' ')
    time.sleep(2)

    
    if a == '1':
        print('\033[93m')
        j = input(' ID ACCONT : @')
        time.sleep(2)
        print('ID accont : ', '@',j)
        time.sleep(2)
        print('your report received / Tracking...! ')
        time.sleep(2)
        
        
    elif a == '2':
        print('\033[95m')
        l = input(' ID chanel : @')
        time.sleep(2)
        print('ID canel : ', '@',l)
        time.sleep(2)
        print('your report received / Tracking...! ')
        time.sleep(2)
    

    elif a == '3':
        print('\033[96m')
        o = input(' link grup:')
        time.sleep(2)
        print('link Group : ',o)
        time.sleep(2)
        print('your report received / Tracking...! ')
        time.sleep(2)


    elif a == '4':
        print('\033[36m')
        n = input(' guid:')
        time.sleep(2)
        print(' guid : ',n)
        time.sleep(2)
        print('your report received / Tracking...! ')
        time.sleep(2)

         
