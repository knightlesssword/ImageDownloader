from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import win32gui
import time
from bs4 import BeautifulSoup
import urllib.request
import re
import sys
from urllib.request import urlopen
import pprint

browser = webdriver.Chrome()
print ("\t\t\tImgur Image Downloader")
print ("\t\tby Abu Bakr")
def enumWindowFunc(hwnd, windowList):
   
    text = win32gui.GetWindowText(hwnd)
    className = win32gui.GetClassName(hwnd)
    if 'chromedriver' in text.lower() or 'chromedriver' in className.lower():
        win32gui.ShowWindow(hwnd, False)
        
win32gui.EnumWindows(enumWindowFunc, [])
browser.set_window_position(12000,12000)

site = input("\nEnter the site extension eg. gallery or r/cute : ")
site2 = "http://imgur.com/" + site
try:
    time.sleep(1)
    browser.get(site2)
    
    print("""Scroll Help:
                 Sorry, I haven't completely implemented this feature.
        The page loads as such and it takes appx. 4 scrolls to add a page.
        Each page contains 60 images.
        So 60 images will be extracted in one go.
        Still in testing, bugs may occur! :)
        """)
    no_of_pagedowns = int(input("Length of scroll? : "))
    elem = browser.find_element_by_tag_name("body")
    
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.4)
        no_of_pagedowns-=1
        
    innerHTML = browser.execute_script("return document.body.innerHTML")
    
    soup = BeautifulSoup(innerHTML,features="html.parser")
    images = []
    i=0
    for img in soup.findAll('img'):
        images.append(img.get('src'))
##        if i==5:
##            break
##        i = i+1  
    newlist = []
    newlist2 = []
    for x in images:
            temp1 = x.rsplit(".",1)
            newlist.append(temp1[0][:-1] )
            temp2 = x.rsplit("/",1)
            newlist2.append(temp2 )

    storename = []
    for list1 in newlist2:
        for list2 in list1:
            storename.append(list1[1])

    storename = list(set(storename))

    final = []
    for y in storename:
        temp3 = y.rsplit(".",1)
        final.append(temp3[0][:-1])

    ffinal = []
    for m in final:
        if len(m) <= 7:
            k = "http://i.imgur.com/" + m
            night = k + ".jpg"
            if night != "http://i.imgur.com/4.jpg":
                ffinal.append(night)
    pprint.pprint(ffinal)
    print("""Please be patient, this may take a while :)
        You will get a message when done.
        """)
    
    n = 0
    for what in ffinal:
        img = urllib.request.urlopen(what)
        word = str(final[n]) + ".jpg"
        localFile = open(word,'wb')
        localFile.write(img.read())
        localFile.close()
        print(n+1)
        print("Done")
        n = n + 1

    print("\nFinished Successfully :)")
    
except urllib.error.HTTPError:
    print("Incorrect subreddit or does not exist")
    sys.exit(0)
    
browser.quit()
sys.exit()
