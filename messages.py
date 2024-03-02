import pyautogui
import random
import time
import keyboard
import win32gui

index = 0
start = False
howmany = 10000
messages = ["a", "a"]
time.sleep(0)


#   #TXT

# with open("messages.txt", "r") as file:
#     lines = file.readlines()
# for i in range(len(lines)):
#     py.write(lines[index])
#     time.sleep(3)
#     py.press("enter")
#     index += 1
    

#   #RANDOM ORDER

# # for i in range(howmany):
# #     msg = random.choice(messages)
# #     py.write(msg)
# #     py.press("enter")
# index = 0


#   #LIST ORDER

# # for i in range(len(messages)):
# #     py.write(messages[index])
# #     py.press("enter")
# #     index += 1
# index = 0



#   #COUNTER
index = 0
key = "p"

print(index)

def keyholdtrue(key):
    
    if keyboard.is_pressed(str(key)):
        
        global start
        
        print("True")
        pyautogui.write("TRUE")
        
        time.sleep(0)
        
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        start = True
        
        time.sleep(0)
        
        return start
 
def keyholdfalse(key):
    
    if keyboard.is_pressed(str(key)):
        
            global start
            
            print("False")
            pyautogui.write("FALSE")
            
            time.sleep(1)
            
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")
            start = False
            
            time.sleep(1)
            
            return start
            
while True:
    
    while not start:
        
        time.sleep(1)
        keyholdtrue(key)
        time.sleep(1)
        
    while start:
        
        for i in range(howmany):
            
            keyholdfalse(key)
            if not start:
                
                break
            
            pyautogui.write(f"{index + 1}")
            pyautogui.press("enter")
            
            keyholdfalse(key)
            if not start:
                
                break
            
            index += 1
            time.sleep(1)
            
            keyholdfalse(key)
            if not start:
                
                break
            
            time.sleep(1)
            
            keyholdfalse(key)
            if not start:
                
                break
            


