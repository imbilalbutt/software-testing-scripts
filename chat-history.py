from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium  import webdriver
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
toSearch = "hi"
time.sleep(2)

# /html/body/div[1]/section[2]/div[1]/ul/li[1]/div[1]/a
chatRoom = driver.find_element_by_xpath("//*[@id='lcb-client']/section[2]/div[1]/ul/li[1]/div[1]/a")
chatRoom.click()

historyButton = driver.find_element_by_xpath("//*[@id='lcb-client']/section[2]/div[2]/header/div[2]/div[1]/a[2]")
historyButton.click()
# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform();


window_after = driver.window_handles[1];
driver.switch_to_window(window_after);

searchBar = driver.find_element_by_xpath("//*[@class='lcb-search-entry form-control']");
searchBar.send_keys(toSearch);
