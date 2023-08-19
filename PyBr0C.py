'''
    This Python Program is for EDUCATIONAL PURPOSES only! Dont use it to generate something like YouTube, TikTok, Instagram Views, etc.!
    Using View Bots is against the TERMS OF SERVICE OF (I guess the most) Social Media Platforms!
    There is a chance that you get banned from YouTube, TikTok, etc. if you use my service for Things that are against TOS!
    You CAN use my service for social media platforms, such as Instagram, Facebook, Twitter to bot them, but its not my Fault if you do Things that are against TOS.
    So, please, PLEASE dont cry in Issues on my Github when u got banned banned because you got banned, i warned you several times.
    Botting Views (and likes, followers/Subs, etc.) is a bad way to get a Audience. Please just create good Content and many videos in a regular Time.
    Like 1 to 2 Videos per day, more is not good for your algorithm.
    By the Way if you flood your subs who turned on the notification bell they will just be annoyed with the time.
    Damn i wrote an entire Tutorial how to be a better content creator in this Program xD
'''
FPS = 30 #Dont need that in that Code but I was bored so, who cares ¯\_(ツ)_/¯

import webbrowser, time

def Count():
    Count = 0

def main():
    while Count < 10:
        webbrowser.open_new_tab("www.youtube.com/") #Opens a new Tab in your Standard Webbrowser.
        time.sleep(1) #Waits for 1 second before Counting one Up.
        Count += 1 #Counts one Up.
        print("starting a new Webbrowser Tab...") #WIP
        time.sleep(2) #Waits for 1 second before executing the print
        print("started a new Webbrowser Tab.") #WIP
    if Count == 10:
        webbrowser.close_new_tab("www.youtube.com/") #Closes the new Tab which were opened in your Standard Webbrowser.
        time.sleep(2)
        print("PyBr0C.py will be restarted in 5 seconds.")
        time.sleep(5)
        print("restarting PyBr0C.py...")
        exec("PyBr0C.py")
        print("PyBr0C.py has been restarted.")
        time.sleep(2)
        print("PyBr0C.py exiting this instance...")
        time.sleep(1)
        print("PyBr0C.py exits now.")
        exit()