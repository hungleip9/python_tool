from selenium import webdriver
from selenium.webdriver.common.by import By  # Thêm dòng n
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

tk = 'D:\\taikhoan'

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('user-data-dir='+tk)

driver = webdriver.Chrome(options=chrome_options)

sleep(1)

driver.get('https://www.pinterest.com/')
try:
  sleep(1)
  driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[1]/nav/div[2]/div[2]/button').click()
  sleep(1)
  driver.find_element(By.ID, 'email').send_keys('hunglq.dev@gmail.com')
  sleep(1)
  driver.find_element(By.ID, 'password').send_keys('Quanghung998@')
  sleep(1)
  driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div[1]/div[1]/form/div[7]/button').click()
except:
  print('Đã đăng nhập rồi!')
  pass
sleep(2)
img = 'D:\\images\\2.jpg'
driver.get('https://www.pinterest.com/pin-creation-tool/')
sleep(4)
try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/input').send_keys(img)
except:
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/div/input').send_keys(img)
    except:
        pass
sleep(2)
# title
driver.find_element(By.ID, 'storyboard-selector-title').send_keys('Đây là tiêu đề')
# mô tả
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/span').send_keys('đây là title')
sleep(3)
# save
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div/button').click()
sleep(1)
# đợi load
try:
  WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/a/div/div/div/div[3]/button'))).click()
  print('Đã post xong ảnh lên peterest')
except:
  print('Có lỗi xảy ra')
  pass