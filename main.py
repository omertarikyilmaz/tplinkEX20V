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

def write_to_file(time_data, uptime, ram_usage, cpu_usage, wip_data, ssid_data2g, channel_data2g, bandwidth_data2g, ssid_data5g, channel_data5g, bandwidth_data5g, download_data, upload_data):
    with open(output_file, 'a', encoding='utf-8') as file:
        # Format the download_data and upload_data with two decimal places
        
        
        file.write(f"{str(time_data).ljust(26)}|{uptime.ljust(35)}|{ram_usage.ljust(12)}|%{cpu_usage.ljust(9)}|"
                   f"{wip_data.ljust(15)}|{ssid_data2g.ljust(24)}|{channel_data2g.ljust(16)}|{bandwidth_data2g.ljust(25)}|"
                   f"{ssid_data5g.ljust(24)}|{channel_data5g.ljust(14)}|{bandwidth_data5g.ljust(17)}|"
                   f"{download_data.ljust(11)}|{upload_data.ljust(11)}|\n")

    #----------------------------Interface Giris-----------------------------------#
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
    #----------------------------------------------------------------------------------------# 
   
   
    #--------------------------------Sistem Verileri----------------------------------#
def UPTIME(driver):
    uptimeValue = driver.find_element(By.XPATH, "//div[@id='main']/div/div/p[5]/span")
    uptime = uptimeValue.text
    return uptime

def RAM_USAGE(driver):
    # Total RAM is a constant value you already know
    total_ram = 423064  # Total RAM in KB

    # Extract the free RAM value (assumed to be in KB)
    ram_free_element = driver.find_element(By.ID, "memFree")
    ram_free = int(ram_free_element.text)  # Convert the free RAM value to an integer

    # Calculate used RAM percentage
    ram_used_percentage = ((total_ram - ram_free) / total_ram) * 100
    ram_used_percentage = round(ram_used_percentage, 2)  # Round to 2 decimal places

    print(f"Used RAM: %{ram_used_percentage}")
    return f"%{ram_used_percentage}"

def CPU_USAGE(driver):
    cpuUsing = driver.find_element(By.ID, "cpuinfo")
    time.sleep(2)
    cpuUsage = cpuUsing.text
    print(cpuUsage)
    return cpuUsage
    #----------------------------------------------------------------------------------------#
def WIP(driver):
    try:
        # Wait for the WAN IP element to be visible, up to 10 seconds
        wanip = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@id='wan_table']/tbody/tr[2]/td[4]"))
        )
        wipdata = wanip.text
        # Extract the part before the '/' character
        wipdata = wipdata.split('/')[0]
        print("WAN IP:", wipdata)
        return wipdata
    except TimeoutException:
        print("Error: WAN IP element not found.")
        return None

    #--------------------------------SSID: 2.4 GHZ Verileri----------------------------------#
def SSID_DATA1(driver):
    ssid1 = driver.find_element(By.XPATH, "//div[@id='wlan1']/p[3]/span") 
    ssid_data1 = ssid1.text
    print("SSID Data (2.4 GHz) degeri alindi.")
    return ssid_data1

def CH_DATA1(driver): #Sorun var
    ch1 = driver.find_element(By.ID, "wlchl0")
    ch1data = ch1.text
    print("Channel (2.4 GHz) degeri alindi.")
    return ch1data

def BW_DATA1(driver):
    bw1 = driver.find_element(By.ID, "wlbw0")
    bw1data = bw1.text
    print("Bandwidth (2.4 GHz) degeri alindi.")
    return bw1data
    #----------------------------------------------------------------------------------------#

def WAN_IP(driver):
    wip = driver.find_element(By.XPATH, "//span[@id='wlssid1']")
    wipdata = wip.text
    print("WAN IP degeri alindi.")
    return wipdata

    #-----------------------------------SSID: 5 GHZ Verileri---------------------------------#
def SSID_DATA2(driver):
    ssid2 = driver.find_element(By.XPATH, "(//div[@id='wlan1']/p[3]/span)[2]") 
    ssid_data2 = ssid2.text
    print("SSID Data (5 GHz) degeri alindi.")
    return ssid_data2

def CH_DATA2(driver): #Sorun Var
    ch2 = driver.find_element(By.ID, "wlchl1")
    ch2data = ch2.text
    print("Channel (5 GHz) degeri alindi.")
    return ch2data

def BW_DATA2(driver):
    bw2 = driver.find_element(By.ID, "wlbw1")
    bw2data = bw2.text
    print("Bandwidth (2.4 GHz) degeri alindi.")
    return bw2data
    #----------------------------------------------------------------------------------------#
def dl_ul_datapage(driver):
    systemToolsButton = driver.find_element(By.ID, "menu_infomenu")
    systemToolsButton.click()
    time.sleep(3)
    systemTrafficButton = driver.find_element(By.CSS_SELECTOR, "#menu_infomenutraffic")
    systemTrafficButton.click()
    time.sleep(8)

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
    OPENINTERFACE(driver)
    LOGINPANEL(driver)

    uptime = UPTIME(driver)
    ram_usage = RAM_USAGE(driver)
    cpu_usage = CPU_USAGE(driver)

    ssid_data2g = SSID_DATA1(driver)
    channel_data2g = CH_DATA1(driver)
    ssid_data5g = SSID_DATA2(driver)
    channel_data5g = CH_DATA2(driver)
    bandwidth_data2g = BW_DATA1(driver)

    bandwidth_data5g = BW_DATA2(driver)
    wip_data = WIP(driver)

    dl_ul_datapage(driver)
    time_data = datetime.now()
    download_data = DOWNLOAD_DATA(driver)
    upload_data = UPLOAD_DATA(driver)

    write_to_file(time_data, uptime, ram_usage, cpu_usage, wip_data, ssid_data2g, channel_data2g, bandwidth_data2g, ssid_data5g, channel_data5g, bandwidth_data5g, download_data, upload_data)
    driver.quit()

if __name__ == "__main__":
    for _ in range(50):
        main()
        time.sleep(2)