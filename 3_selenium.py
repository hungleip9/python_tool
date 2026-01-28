from selenium import webdriver
from selenium.webdriver.common.by import By  # Thêm dòng n
from time import sleep

tk = 'D:\\ToolPython\\taikhoan'

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('user-data-dir='+tk)

driver = webdriver.Chrome(options=chrome_options)

sleep(1)

driver.get('https://stockproxx.com/')
try:
  sleep(3)
  driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/div/div/button').click()
  sleep(2)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/header/div[1]/div/div[2]/div[2]/div').click()
  sleep(1)
  driver.find_element(By.ID, 'custom-validation-update-info-user_PhoneNumber').send_keys('0898562269')
  sleep(1)
  driver.find_element(By.ID, 'custom-validation-update-info-user_Password').send_keys('hungle')
  sleep(1)
  driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/div/div/div/button').click()
  sleep(77)
except:
  print('lỗi')
  pass
sleep(77)