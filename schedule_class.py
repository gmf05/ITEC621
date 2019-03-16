# from random import random
from datetime import datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains

_SHORT_TIMEOUT = 1.5
_LONG_TIMEOUT = 5

password = ''
course_name = 'ITEC-621-020'
start_date = datetime(2019, 4, 1)
target_hour = '7'
target_min = '30'
target_pm = 'pm'

def format_date(date_str):
    temp = re.sub(' 0([\d])', ' \g<1>', date_str)
    temp = re.sub('(?<=[\d])(?:st|nd|rd|th)', '', temp)
    return temp


def match_time(time_box, target_hour, target_min, target_pm):
    """Click time box and find active element"""
    time_box.click()

    def find_active_element():
        # time_box.click()
        current_hour, current_min, current_pm = time_box.get_attribute('aria-label').split('Start Time of meeting: ')[1].split(' ')
        time_box.send_keys(keys.Keys.ARROW_DOWN)
        next_hour, next_min, next_pm = time_box.get_attribute('aria-label').split('Start Time of meeting: ')[1].split(' ')
        time_box.send_keys(keys.Keys.ARROW_UP)
        time_box.send_keys(keys.Keys.ARROW_UP)
        prev_hour, prev_min, prev_pm = time_box.get_attribute('aria-label').split('Start Time of meeting: ')[1].split(' ')
        time_box.send_keys(keys.Keys.ARROW_DOWN)
        # which one is diff??
        if current_hour != next_hour or current_hour != prev_hour:
            return 'hour'
        elif current_min != next_min or current_min != prev_min:
            return 'min'
        # elif current_pm != next_pm or current_pm != prev_pm:
        #     return 'pm'
        else:
            # return None
            return 'pm'

    elements = ['hour', 'min', 'pm']
    target_vals = [target_hour, target_min, target_pm]
    for n in range(3):
        idx = elements.index(find_active_element())
        print(idx)
        current_val = time_box.get_attribute('aria-label').split('Start Time of meeting: ')[1].split(' ')[idx]
        target_val = target_vals[idx]

        num_iter = 0
        while current_val != target_val and num_iter <= 24:
            time_box.send_keys(keys.Keys.ARROW_DOWN)
            current_val = time_box.get_attribute('aria-label').split('Start Time of meeting: ')[1].split(' ')[idx]
            num_iter += 1
        time.sleep(0.2)
        time_box.send_keys(keys.Keys.ARROW_RIGHT)
        time.sleep(0.2)

# Login - Can do manually, too
driver = webdriver.Chrome('/Users/gfiddyment/bin/chromedriver')
driver.get('https://2ksb.onlinebusiness.american.edu')
time.sleep(_SHORT_TIMEOUT)
driver.find_element_by_xpath('//input[@id="username"]').click()

actions_user = ActionChains(driver)
actions_user.move_to_element(driver.find_element_by_xpath('//input[@id="username"]'))\
    .send_keys('gfiddy@american.edu').perform()
driver.find_element_by_xpath('//button[@id="login-submit"]').click()
time.sleep(_SHORT_TIMEOUT)

actions_pwd = ActionChains(driver)
actions_pwd.move_to_element(driver.find_element_by_xpath('//input[@id="password"]'))\
    .send_keys(password).perform()
driver.find_element_by_xpath('//button[@id="login-submit"]').click()

time.sleep(_LONG_TIMEOUT)

#  Go to course url
course_url = 'https://2ksb.onlinebusiness.american.edu/course/view.php?id=398&group=1138'
driver.get(course_url)

# Loop!
# for week_number in range(1, 11):
for week_number in range(2, 11):

    print('Week', week_number)

    class_date = start_date + timedelta(weeks=week_number-1)
    target_date = format_date(class_date.strftime('%A %B %d %Y'))

    # Click create meeting
    driver.find_element_by_xpath('//button[@id="open-create-modal"]').click()
    time.sleep(_SHORT_TIMEOUT)

    # Select invitees
    driver.find_element_by_xpath('//input[@id="invitee_value"]').send_keys(course_name)
    time.sleep(_SHORT_TIMEOUT)
    class_matches = driver.find_elements_by_xpath('//div[@class="angucomplete-title ng-binding ng-scope"]')
    for m in class_matches:
        try:
            if m.text == course_name:
                m.click()
        except:
            pass

    # Select meeting type = class discussion
    driver.find_element_by_xpath('//option[@label="class discussion"]').click()

    # Name session
    driver.find_element_by_xpath('//input[@name="name"]').send_keys('W' + str(week_number))

    # Attendance tracking click and go (week_number / 1) entries down
    driver.find_element_by_xpath('//option[@label="Week {} Live Session"]'.format(str(week_number))).click()

    # Set duration = 110
    driver.find_element_by_xpath('//input[@id="meetingduration"]').send_keys(keys.Keys.BACKSPACE)
    driver.find_element_by_xpath('//input[@id="meetingduration"]').send_keys(keys.Keys.BACKSPACE)
    driver.find_element_by_xpath('//input[@id="meetingduration"]').send_keys('110')

    # Set recording = invitees
    driver.find_element_by_xpath('//option[@label="Invitees"]'.format(str(week_number))).click()

    # Set date and time
    date_box = driver.find_element_by_xpath('//input[@id="meetingdate"]')
    time_box = driver.find_element_by_xpath('//input[@id="meetingtime"]')
    date_box.click()
    current_input_date = format_date(date_box.get_attribute('aria-label').split('Meeting Date: ')[1])
    while current_input_date != target_date:
        date_box.send_keys(keys.Keys.ARROW_RIGHT)
        current_input_date = format_date(date_box.get_attribute('aria-label').split('Meeting Date: ')[1])
    driver.find_element_by_xpath('//textarea[@id="meetingdescription"]').click()  # click out
    match_time(time_box, target_hour, target_min, target_pm)
    driver.find_element_by_xpath('//textarea[@id="meetingdescription"]').click()  # click out

    # Click create
    driver.find_element_by_xpath('//button[@ng-click="meetingFormCtrl.submit($event)"]').click()

    print('Success!')
    time.sleep(_SHORT_TIMEOUT)