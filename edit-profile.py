#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from selenium  import webdriver


# In[4]:


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
settings = driver.find_element_by_css_selector('.lcb-account-button-name');
settings.click();

# adding new data
profileEditing = driver.find_element_by_link_text('Edit Profile').click();
time.sleep(2);
display_name = driver.find_element_by_name('display-name');
display_name.clear();
time.sleep(1);
driver.find_element_by_name('display-name').send_keys('ABC');
time.sleep(1);
first_name = driver.find_element_by_name('first-name');
first_name.clear();
driver.find_element_by_name('first-name').send_keys('DCO');
time.sleep(1);
last_name = driver.find_element_by_name('last-name');
last_name.clear();
driver.find_element_by_name('last-name').send_keys('TRU');
time.sleep(1);



driver.find_element_by_css_selector('.submit-edit-profile.btn.btn-info.indicator').click();
time.sleep(2);
driver.find_element_by_css_selector('.confirm').click();
time.sleep(1);


# Checking if edited testing
settings = driver.find_element_by_css_selector('.lcb-account-button-name');
settings.click();
time.sleep(2);
profileEditing = driver.find_element_by_link_text('Edit Profile').click();
time.sleep(2);

display_name = driver.find_element_by_name('display-name');
d_name = display_name.get_attribute('value');

if (d_name == 'ABC'):
    print('Correct');
else:
    print('Not edited yet');
    

time.sleep(1);
first_name = driver.find_element_by_name('first-name');
d_name = first_name.get_attribute('value');

if (d_name == 'Bamal'):
    print('Correct');
else:
    print('Not edited yet');


# In[ ]:





# In[ ]:





# In[ ]:




