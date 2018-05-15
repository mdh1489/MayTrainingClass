import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

arrayValue1 = ['0', '1', '2']
arrayValue2 = ['button', 'finish']
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com')
driver.find_element_by_link_text('Dynamic Loading').click()
driver.find_element_by_link_text('Example 2: Element rendered after the fact').click()
driver.find_element_by_tag_name(arrayValue2[0]).click()
wait = WebDriverWait(driver, 60)
wait.until(EC.visibility_of_element_located((By.ID, arrayValue2[1])))

try:
    assert driver.find_element_by_id(arrayValue2[1]).is_displayed(), "Loading Failed"
except AssertionError as e:
    print("load and wait unsuccessful")
finally:
    driver.close()
# wait.until(EC.visibility_of_element_located(driver.find_element_by_id('username')))
# driver.find_element_by_id('username').send_keys(username)
# driver.find_element_by_id('password').send_keys(password)
# driver.find_element_by_class_name('radius').click()

# assert driver.find_element_by_class_name('error').is_displayed(), \
#     "Success Message failed to display"
# assert not 'your password is invalid' in driver.find_element_by_class_name('error').text.lower(), \
#     "Wrong Password displayed"
# assert not 'your username is invalid' in driver.find_element_by_class_name('error').text.lower(), \
#     "Wrong username displayed"
# finally:

# select = Select(driver.find_element_by_id('dropdown'))
#
# options_list = driver.find_elements_by_xpath('option')
#
# for option in options_list
#     if option.get_attribute('value') == '1':
#         option.click()
#
#     if option.text == 'Option 1':
#         option.click()
#
# for i in arrayValue1:
#     select.select_by_index(i)

#select.select_by_value('2')
#select.select_by_index('2')
#select.select_by_visible_text('Option 2')

# select.deselect_all()

# element_List = driver.find_elements_by_tag_name('a')
#
# for name in element_List:
#     if 'JavaScript' in name.text:
#         print(name.text)
#         print(name.get_attribute('href'))

#driver.quit()

# example_list = []
# example_list.append(1)
# example_list.append("asdasd")
# example_list.append([])
#
# for example in example_list:
#     print(example)
#
# dictionary_example = {}
# dictionary_example = {'key_1':"value_1", 'key_2':1,'key_3':[1,2,3]}
#
# valu = dictionary_example['key_1']
#
# for key in dictionary_example.keys():
#     print(dictionary_example[key])
#
# example_string = "Hello World"
# # TODO:
# # FIXME:
# example_string.upper() # returns the all uppercase driver.get('https://www.youtube.com')
#
# print(example_string[0])
# example_string(example_string.strip())