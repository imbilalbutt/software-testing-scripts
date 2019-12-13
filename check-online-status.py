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
driver.find_element_by_name('username').send_keys('XYZ');
time.sleep(2);
driver.find_element_by_name('password').send_keys('XYZ');
time.sleep(1);
loginButton = driver.find_element_by_tag_name('button');
loginButton.click();
driver.maximize_window();
time.sleep(4);

group = driver.find_element_by_css_selector('.lcb-rooms-list-item-name');
group.click();
time.sleep(1);

groupOption = driver.find_element_by_css_selector('.btn.btn-action.lcb-room-toggle-sidebar');
groupOption.click();

time.sleep(1);


onlineName = driver.find_element_by_tag_name('span').text;
print(onlineName);

time.sleep(1);

if onlineName  == 'XYZ':
    print("User is online (status available)")
else:
    print("User is NOT online (status available)")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




