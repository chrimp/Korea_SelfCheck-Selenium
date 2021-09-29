from selenium import webdriver
from selenium.webdriver.support.ui import Select
#import selenium.common.exceptions as selex
import time
import sys

#Remove "[" and "]" when replace the text

#notification_url = 'https://tenta.me/[API_ID]' #decomment here and type your API ID to get Tenta notification
password = list('placeholder)') #replace placeholder with your 4-digit password

def main(err):

    errcount = err

    try:
        driver = webdriver.Chrome('[PATH_TO_WEBDRIVER]') #type the path to chromedriver (or any browser you want, replace Chrome to your one if then) on your computer
        driver.implicitly_wait(3)

        driver.get('https://hcs.eduro.go.kr/')

        driver.find_element_by_id("btnConfirm2").click()
        driver.find_element_by_class_name("searchBtn").click()
        sch = Select(driver.find_element_by_id("sidolabel"))
        sch.select_by_value("10")
        schtype = Select(driver.find_element_by_id("crseScCode"))
        schtype.select_by_visible_text("[City/Province]") #type the name of your city/province (Use Korean Supported editor)
        driver.find_element_by_id("orgname").send_keys('[SCHOOL_NAME]') #type the EXACT name of your institution
        driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(3) > td:nth-child(3) > button').click()
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click()
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
        driver.find_element_by_id("user_name_input").send_keys('[YOUR_NAME]')
        driver.find_element_by_id("birthday_input").send_keys('030323')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="password"]').click()
        time.sleep(1)

        a = driver.find_elements_by_class_name('transkey_div_3_2')
        a_i = []
        b = driver.find_elements_by_class_name('transkey_div_3_3')
        b_i = []

        for i in a:
            a_i.append(i.get_attribute('outerHTML'))

        for i in a_i:
            if 'aria-label="'+password[0]+'"' in i:
                loc_1 = a_i.index(i)
                loc_1_ind = 'a'
            if 'aria-label="'+password[1]+'"' in i:
                loc_2 = a_i.index(i)
                loc_2_ind = 'a'
            if 'aria-label="'+password[2]+'"' in i:
                loc_3 = a_i.index(i)
                loc_3_ind = 'a'
            if 'aria-label="'+password[3]+'"' in i:
                loc_4 = a_i.index(i)
                loc_4_ind = 'a'

        for i in b:
            b_i.append(i.get_attribute('outerHTML'))

        for i in b_i:
            if 'aria-label="'+password[0]+'"' in i:
                loc_1 = b_i.index(i)
                loc_1_ind = 'b'
            if 'aria-label="'+password[1]+'"' in i:
                loc_2 = b_i.index(i)
                loc_2_ind = 'b'
            if 'aria-label="'+password[2]+'"' in i:
                loc_3 = b_i.index(i)
                loc_3_ind = 'b'
            if 'aria-label="'+password[3]+'"' in i:
                loc_4 = b_i.index(i)
                loc_4_ind = 'b'

        if loc_1_ind == 'a':
            a[loc_1].click()
        elif loc_1_ind == 'b':
            b[loc_1].click()

        if loc_2_ind == 'a':
            a[loc_2].click()
        elif loc_2_ind == 'b':
            b[loc_2].click()

        if loc_3_ind == 'a':
            a[loc_3].click()
        elif loc_3_ind == 'b':
            b[loc_3].click()

        if loc_4_ind == 'a':
            a[loc_4].click()
            driver.find_element_by_css_selector('//*[@id="btnConfirm"]').click()
        elif loc_4_ind == 'b':
            b[loc_4].click()
            driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    
        time.sleep(3)
        driver.find_element_by_class_name('name').click()
        driver.find_element_by_id('survey_q1a1').click()
        driver.find_element_by_id('survey_q2a1').click()
        driver.find_element_by_id('survey_q3a1').click()
        driver.find_element_by_id('btnConfirm').click()
        time.sleep(3)
        driver.quit()
    except Exception as Error:
        errcount = errcount + 1
        if errcount >= 5:
            data_dict = {
                "title": '자가진단 실패',
                "description": Error
            }
            #requests.post(notification_url, data= data_dict) #decomment here to get Tenta notification
            sys.exit(0)
        else:
            driver.quit()
            main(errcount)

main(0)

data_dict = {
    "title": '자가검진 완료',
    "description": '증상이 있으실 경우 자가진단을 다시 진행해주세요'
}

#requests.post(notification_url, data= data_dict) #decomment here to get Tenta notification