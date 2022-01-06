# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 16:31:08 2021

@author: zedde
"""

from time import sleep
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

def getHashtags(arguments):
    lista = []
    for argument in arguments:    
        URL = 'https://top-hashtags.com/search/?q='+argument+'&opt=top'
        page = requests.get(URL)  
        doc = lh.fromstring(page.content)
        for i in range(6):    
            tr_elements = doc.xpath('//*[@id="post-268"]/div/ul/li['+str(i)+']')
            try: 
                ax = str(tr_elements[0].text_content())
                pattern = r'[0-9]'
                mod_string = re.sub(pattern, '', ax)
                pattern2 = r'[KM.]'
                mod2_string = re.sub(pattern2, '', mod_string)
                print(mod2_string)
                lista.append(mod2_string)
            except:
                print('no more')
    return lista

def login(username, password):
    global browser 
    browser= webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')
    login_link = browser.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
    login_link.click()
    sleep(2)
    username_input = browser.find_element_by_css_selector("div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
    password_input = browser.find_element_by_css_selector("div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
    username_input.send_keys(username)
    sleep(2)
    password_input.send_keys(password)
    sleep(2)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    browser.implicitly_wait(10)
    memorize_cred = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    memorize_cred.click()
    browser.implicitly_wait(10)
    try:
        notifications_off = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        notifications_off.click()
    except:
        try:    
            notifications_off = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
            notifications_off.click()
        except:
            try:
                notifications_off = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
                notifications_off.click()               
            except:
                print("error")
    '''            
    sleep(3)
    scroll_home_and_like()
   
def scroll_home_and_like():
    sleep(random.randrange(2,3))
    browser.execute_script("window.scrollTo(0, 980)")
    like_post()
    sleep(random.randrange(2.3,3.4))
    /html/body/div[6]/div[2]/div/article/div/div[1]/div/div/div[1]/div[1]/img
 '''        
def like_post():
    try:
        img = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div[2]/div/div/div[1]")
    except:
        try:
           img = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[1]/div/div/div[2]") 
        except:
            print("cannot like")
    browser.execute_script("arguments[0].click();", img)
    like = webdriver.common.action_chains.ActionChains(browser)
    like.move_to_element_with_offset(img, 15, 15)
    like.click()
    sleep(0.5)
    like.click()
    like.perform()
    sleep(4)
    
def search_tag(tag):
    sleep(5)
    search_bar = browser.find_element_by_css_selector(".XTCLo")
    search_bar.send_keys(tag)
    sleep(2)
    select_tag = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[2]/div")
    select_tag.click()
    sleep(5)
    body = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]")
    browser.execute_script("arguments[0].click();", body)
    action = webdriver.common.action_chains.ActionChains(browser)
    action.move_to_element_with_offset(body, 15, 15)
    action.click()
    action.perform()
    sleep(5)

def go_next():
    try:
        next_img = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/a")
        next_img.click()
    except:
        print("You are not iny he first page.")
    browser.implicitly_wait(5)
    sleep(3)
    img_to_skip = random.randint(2,5)   
    for i in range(img_to_skip):       
        next_next_img = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div/a[2]")
        next_next_img.click()
        browser.implicitly_wait(10)
        sleep(random.randint(3,7))
        
def comment_post():
    comment = browser.find_element_by_css_selector(".Ypffh")
    comment.click()
    comment = browser.find_element_by_css_selector(".Ypffh")
    comment.send_keys("Interested in algorithmic trading? Check my profile ;)")
    comment.send_keys(Keys.ENTER)

def follow():
    try:
        follow = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
    except:
        try:
            follow = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button")
        except:
            print('cannot find "segui"')
    try:     
        follow.click()
    except:
        print('cannot follow')
        
def start_bot(username,password,arguments):
    
    #gethashtags
    tags = getHashtags(arguments)
    print(tags)
    login(username,password)
    
    like_count=0
    follow_count=0
    
    for tag in tags:
        #sub_tag = "trading"
        sleep(3)
        search_tag(tag)       
        like_post()
        
        '''
        try:
            if sub_tag in tag:
                print("Comment this post ...")
                comment_post()
        except:
            print("Comments disabled")'''
        try:
            go_next()      
        except:
            print("no more imgs")
        like_post() 
        
        follow()
        
        try:
            go_next()
        except:    
            print("no more imgs")
            
        like_post()     
        
        like_count = like_count + 3
        follow_count += 1
        print(like_count)
        print(follow_count)
        
        browser.get("https://www.instagram.com/")
        
        print("we just finish with tag: " + tag)
        
        sleep(300)
        print("300s")
        try:
            notifications_off = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
            notifications_off.click()
        except:
            try:    
                notifications_off = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
                notifications_off.click()
            except:
                try:
                    notifications_off = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
                    notifications_off.click()               
                except:
                    print("no notification")
        sleep(300)
        
    print(like_count)
    print(follow_count)
    
start_bot("USERNAME","PASSWORD", [ "TAG","TAG","TAG"]) #without '#'
  