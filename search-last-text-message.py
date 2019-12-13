#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium  import webdriver


# In[1]:


driver = webdriver.Chrome("E:\chromedriver.exe");
driver.get("localhost:5000");
time.sleep(2);
driver.find_element_by_name('username').send_keys('jamalbutt1232');
time.sleep(2);
driver.find_element_by_name('password').send_keys('jamalbutt1232');
time.sleep(1);
loginButton = driver.find_element_by_tag_name('button');
loginButton.click();
driver.maximize_window();
time.sleep(4);

group = driver.find_element_by_css_selector('.lcb-rooms-list-item-name');
group.click();
time.sleep(1);

if (driver.find_elements_by_xpath("//*[contains(text(), 'hi?')]")):
    print("Last Text message FOUND\n")
else:
    print("Last Text message NOT FOUND")


# In[ ]:




