# -*-coding:utf-8 -*

import os
from os import path
import sys
import random
from datetime import datetime
from time import sleep
import json
import logging
import inspect
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class Bot:
      
        #def __init__(self):                
                

        def trace(self,stck):
                #print ("{0} ({1}-{2})".format(stck.function, stck.filename, stck.lineno))
                print ("{0}".format(stck.function))
                #self.log.lg("{0}".format(stck.function))
 
        # init
        def init(self):            
                self.trace(inspect.stack()[0])
                try:
                        options = webdriver.ChromeOptions()       
                        #options.add_argument("user-agent={0}".format(self.jsprms.prms["useragent"]))            
                        options.add_argument("--start-maximized")
                        # ouvrir debugger 
                        #options.add_argument("--auto-open-devtools-for-tabs");
                        driver = webdriver.Chrome(executable_path=self.chromedriverbinpath, options=options)                      
                        
                        return driver
                except Exception as e:                             
                        print(e)
                        raise

        def newtab(self,url):            
                self.driver.execute_script("window.open('{0}');".format(url))
                self.driver.switch_to.window(self.driver.window_handles[-1]) 
                

        def main(self):
                          
                try:
                        self.rootApp = os.getcwd()
                        # InitBot
                        nbargs = len(sys.argv)
                        self.trace(inspect.stack()[0])     
                        self.chromedriverbinpath ="/usr/bin/chromedriver"
                        self.driver = self.init() 
                        #self.driver.get("http://localhost:8080")
                        input()
                        self.driver.close()


                        #ONGLETS
                        #driver.switch_to.window(driver.window_handles[-1])       

                except Exception as e:
                        self.driver.close()
                        raise
            


#INIT
bot = Bot()
bot.main()

              
               
    

        
                

        

