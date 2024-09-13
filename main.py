from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

output_file = r"C:\Users\owery\OneDrive\Masaüstü\Python\tplinkEX20v\logs.txt"

def write_to_file(data):
    with open(output_file, 'a') as file:
        file.write(data)

def OPENINTERFACE(driver):
    driver.get("http://192.168.1.1/")
    time.sleep(2)
    print("Arayuz acildi.")

def LOGINPANEL(driver):
    try:
        userName = "admin"
        userPassword = "turktelekom2024"
        userNameInput = driver.find_element(By.ID, "userName")
        userNameInput.send_keys(userName)
        userPasswordInput = driver.find_element(By.ID, "pcPassword")
        userPasswordInput.send_keys(userPassword)
        loginButton = driver.find_element(By.ID, "loginBtn")
        loginButton.click()
        time.sleep(2)
        print("Giris yapildi.")
    except:
        print("Hata var")
    
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        popup = driver.switch_to.alert
        popup.accept()
        print("Pop-up accepted.")
        time.sleep(5)
    except TimeoutException:
        print("No pop-up alert appeared.")
    except Exception as e:
        print(f"Error handling alert: {e}")

def UPTIME(driver):
    uptimeValue = driver.find_element(By.XPATH, "//div[@id='main']/div/div/p[5]/span")
    uptime = uptimeValue.text
    return uptime

def RAM_USAGE(driver):
    ramNotUsingValue = driver.find_element(By.ID, "memFree")
    ramNotUsing = ramNotUsingValue.text
    return ramNotUsing

def CPU_USAGE(driver):
    cpuUsing = driver.find_element(By.ID, "cpuinfo")
    time.sleep(2)
    cpuUsage = cpuUsing.text
    print(cpuUsage)
    return cpuUsage

def SSID_DATA(driver):
    ssid = driver.find_element(By.ID, "wlssid1")
    ssid_data = ssid.text
    return ssid_data

def CHANNEL_DATA(driver):
    channel = driver.find_element(By.ID, "wlchl1")
    channel_data = channel.text
    return channel_data

def BANDWIDTH_DATA(driver):
    bandwidth = driver.find_element(By.ID, "wlbw1")
    bandwidth_data = bandwidth.text
    return bandwidth_data

def dl_ul_datapage(driver):
    systemToolsButton = driver.find_element(By.ID, "menu_infomenu")
    systemToolsButton.click()
    time.sleep(3)
    systemTrafficButton = driver.find_element(By.CSS_SELECTOR, "#menu_infomenutraffic")
    systemTrafficButton.click()
    time.sleep(3)

def DOWNLOAD_DATA(driver):
    downloadspeed = driver.find_element(By.CSS_SELECTOR, "#pvc_stat_table tr:nth-child(1) > td:nth-child(9)")
    download_data = downloadspeed.text
    return download_data

def UPLOAD_DATA(driver):
    uploadspeed = driver.find_element(By.CSS_SELECTOR, "#pvc_stat_table tr:nth-child(1) > td:nth-child(8)")
    upload_data = uploadspeed.text
    return upload_data

def main():
    driver = webdriver.Chrome(service=Service("C:/Program Files (x86)/chromedriver.exe"))
    
    try:
        OPENINTERFACE(driver)
        LOGINPANEL(driver)
        
        uptime = UPTIME(driver)
        ram_usage = RAM_USAGE(driver)
        cpu_usage = CPU_USAGE(driver)
        ssid_data = SSID_DATA(driver)
        channel_data = CHANNEL_DATA(driver)
        bandwidth_data = BANDWIDTH_DATA(driver)
        
        dl_ul_datapage(driver)
        download_data = DOWNLOAD_DATA(driver)
        upload_data = UPLOAD_DATA(driver)
        
        time_data = datetime.now()

        write_to_file(f"\n{time_data} | {uptime} | {ram_usage} KB  | %{cpu_usage}        | {ssid_data}    | {channel_data} | {bandwidth_data} | {download_data}            | {upload_data}")
    
    finally:
        driver.quit()



if __name__ == "__main__":
    for _ in range(10):
        main()
        time.sleep(3)
