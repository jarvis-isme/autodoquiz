from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# make a browser    
browser=webdriver.Chrome(executable_path="./chromedriver")
# open lms
browser.get('http://lms-undergrad.fpt.edu.vn/login/index.php')
sleep(5)

#click login with google
link_loginGoogle=browser.find_element_by_xpath('/html/body/div[4]/div/div/div/form/div[8]/a[1]')
link_loginGoogle.click()
sleep(10)


#get and input email
email=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email.send_keys('accountfpt')
sleep(5)

email.send_keys(Keys.ENTER)
sleep(5)
# get and input password
password=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password.send_keys('passwordfpt')
sleep(5)
password.send_keys(Keys.ENTER)
# get link vao course and join
sleep(10)
course=browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/aside/div[2]/div[2]/ul/li/ul/li[3]/ul/li[27]/p/a')
course.click()
# join quiz
sleep(10)
quiz=browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/section/div/div/ul/li[1]/div[3]/ul/li[6]/div/div/div[2]/div/a/span')
quiz.click()
#input
input=browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/section/div/div[4]/div/form/div/input[1]')
input.click()
#
quiz_password=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/form/fieldset[1]/div/div[2]/div[2]/input')
quiz_password.send_keys('automationtest')
quiz_password.send_keys(Keys.ENTER)
sleep(10)
#check answer
answer=browser.find_elements_by_tag_name('span')
answer2=browser.find_elements_by_tag_name('label')
for e in answer:
    if(e.text =='Option 1'):
        e.click()
for e in answer2:
    if('Option 1' in e.text):
        e.click()
#finsh
finish_atemp=browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/section/div/form/div/div[4]/input')
finish_atemp.click() 
sleep(5)
#sumitall
submitallandsumit=browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/section/div/div[4]/div/div/form/div/input[1]')
submitallandsumit.click()
sleep(5)
#submit 2
submit2=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[2]/input[1]')
submit2.click()
sleep(10)
browser.close()
