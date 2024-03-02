import pyautogui
import random
import time
import keyboard
import win32gui

start = False
test = ""
timesrepeated = 0

key = "f2" #KEY FOR ACTIVATE
index = 0 #WILL START FROM
howmany = 0 #0 IF REPEAT FOREVER
cooldown = 0.1 #Cooldown between messages
print(f"index = {index}")
print(f"key = {key}")
print(f"how many = {howmany}")

if howmany == 0:
    howmany = 9999999999

def keyholdtrue(key):
    
    if keyboard.is_pressed(str(key)):
        
        global start
        global timesrepeated
        
        print("True")
        pyautogui.write("TRUE")
        timesrepeated = 0
        
        time.sleep(cooldown)
        
        for i in range(5):
            pyautogui.press("backspace")
        
        start = True
        
        time.sleep(cooldown)
        
        return start
 
def keyholdfalse(key):
    
    if keyboard.is_pressed(str(key)):
        
            global start
            global timesrepeated
            
            print("False")
            pyautogui.write("FALSE")
            
            time.sleep(cooldown)
                                        
            for i in range(5):
                pyautogui.press("backspace")
            
            start = False
            
            time.sleep(cooldown)
            
            return start
            
while True:
    
    while not start:
        
        time.sleep(cooldown)
        
        keyholdtrue(key)
        if start:
                
            break
        
        time.sleep(cooldown)
        
    while start:
        
        for i in range(howmany):
            
            if timesrepeated == howmany:
                start = False
                break
            
            keyholdfalse(key)
            if not start:
                
                break
            
            pyautogui.write(f"{index + 1}")
            pyautogui.press("enter")
            timesrepeated += 1
            
            keyholdfalse(key)
            if not start:
                
                break
            
            index += 1
            time.sleep(cooldown)
            
            keyholdfalse(key)
            if not start:
                
                break
            
            time.sleep(cooldown)
            
            keyholdfalse(key)
            if not start:
                
                break
