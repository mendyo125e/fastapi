from typing import Optional
from fastapi import FastAPI
import aiofiles,json
from fastapi.responses import HTMLResponse, JSONResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib3,urllib.parse
import random,time
import os
import random
app = FastAPI()
def random_color_by_name(testcolor):
    if testcolor=="test":
        color_names = [
            "blue", "green", "orange","red", "lightblue","grey","black","white" ,"yellow" ,"purple" ,"pink" ,"brown" ,"cyan","magenta","lime","gold","teal","navy","olive","maroon"       
        ]
    else:
        color_names = [
            "blue", "green", "orange","red", "lightblue","grey","black" 
        ]
    # Chọn ngẫu nhiên một màu
    return random.choice(color_names)
def updatestatus(user,url,cookie):
    # Khởi tạo PoolManager
    http = urllib3.PoolManager()
    # URL API cần gửi yêu cầu
    data = {'namefolder': f'{user}',"cookie": cookie,}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request( 'POST',   url,  body=encoded_data,   headers={'Content-Type': 'application/json'})
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def send_alertzy_notification(account_key, title, message,priority, group, buttons=None):
    url = "https://alertzy.app/send"
    data = {"accountKey": account_key,"title": title,"message": message,"group": group,}
    data["priority"]=priority
    if buttons:
        data["buttons"] = json.dumps(buttons)
    http = urllib3.PoolManager()
    response = http.request('POST',url,fields=data)
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def guisms(account_key,user,message,chotot):
    http = urllib3.PoolManager()
    data = {"token": account_key,"user": user,"message": message,"sound": chotot,}
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")  # Phải encode thành bytes
    response = http.request(
        "POST",
        "https://api.pushover.net/1/messages.json",
        body=encoded_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def guismssystem(title,message,nologin,random_color):
    # Khởi tạo PoolManager
    http = urllib3.PoolManager()
    # URL API cần gửi yêu cầu
    url = 'https://hieuphp.name.vn/api/undetected/message.php?all=1'
    data = {'title': f'{title}','message': f'{message}','nologin': f'{nologin}','random_color': f'{random_color}'}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request( 'POST',   url,  body=encoded_data,   headers={'Content-Type': 'application/json'})
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def convert_boolean_values(cookie):
    # Kiểm tra nếu cookie là kiểu dict
    if isinstance(cookie, dict):
        for key, value in cookie.items():
            if isinstance(value, bool):
                cookie[key] = value  # Đảm bảo giá trị boolean đúng (True/False)
    return cookie
def fetch_data_from_api(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    if response.status == 200:
        try:
            data = json.loads(response.data.decode('utf-8'))
            return data
        except json.JSONDecodeError:
            print("Lỗi khi giải mã dữ liệu JSON.")
            return None
    else:
        print(f"Lỗi khi gửi yêu cầu GET, mã trạng thái: {response.status}")
        return None
def lambda_handler():
    # Cấu hình trình duyệt
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Chạy chế độ không giao diện
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-notifications")
    message_value = 0 
    i=0
    vonglap=True
    url = "https://hieuphp.name.vn/api/undetected/systemapi.php?all=1"  
    data = fetch_data_from_api(url)
    namesms = data.get("name", None)
    tokensms = data.get("token", None)
    usersms = data.get("user", None)
    random_color = random_color_by_name(namesms)
    # Khởi tạo WebDriver
    try:
        url = "https://hieuphp.name.vn/api/undetected/getdata.php"  
        data = fetch_data_from_api(url)
        try:
            message_value = data.get("message", None)
        except Exception as e:
            message_value=0
            
        if message_value!=1:
            # In dữ liệu trả về (có thể tùy chỉnh để chỉ lấy các trường cụ thể)
           
            for record in data:
               
                #print(f"Email: {record.get('email', 'Không có email')}")
                cookie_data=record.get('cookie', 'Không có cookie')
                cookies = json.loads(cookie_data)
                 #cookies = cookie_dict.get("cookies", [])
                #print(f"Cookie: {cookies}") 
                namefolder=record.get('namefolder', 'Không có namefolder')
                #print(f"Name Folder: {namefolder}")
                nameapp=record.get('nameapp', 'Không có nameapp')
                #print(f"Name App: {nameapp}")
                cookieactive=record.get('cookieactive', 'Không có cookieactive')
                #print(f"Cookie Active: {cookieactive}")
                testversion=record.get('testversion', 'Không có testversion')
                #print(f"Test Version: {testversion}")
                testbodyelement=record.get('testbodyelement', 'Không có testbodyelement')
                print(f"Test Body Element: {testbodyelement}")
                viewtmp=record.get('viewtmp', 'Không có xem tmp')
                print(f"Xem tmp: {viewtmp}")
                nhansms=record.get('nhansms', 'Không có nhansms')
                print(f"nhansms: {nhansms}")
                noidungtin=record.get('noidungtin', 'Không có noidungtin')
                print(f"noidungtin: {noidungtin}")
                status=record.get('status', 'Không có status')
                print(f"Status: {status}") 
                                   
        else:
            print("Đã kiểm tra hết các trang")
            url = "https://hieuphp.name.vn/api/undetected/updatestatus.php?all=1"  
            fetch_data_from_api(url)
            vonglap=False
       
        driver = webdriver.Remote(command_executor="https://standalone-chrome-6je7.onrender.com/wd/hub",options=chrome_options)
        
        cookieactive=0
            
            #driver = uc.Chrome(options, driver_executable_path=driver_path, browser_executable_path=browser_path,version_main=108 )
        if int(noidungtin)==1:
            url="https://chat.chotot.com/chat"
            driver.get(url)    
            passtranglogin=0
            try:
            # Tìm phần tử chứa chữ "Đăng nhập"
                login_element = driver.find_element(By.CSS_SELECTOR, ".styles_linkMessage__shp7Q")
                passtranglogin=1
                nologin=2
                print("Bạn đã login page chat ")                 
            except Exception as e:
                print("Lỗi Không tìm thấy 'cookie chat' ")
                nologin=1
        else:    
                url="https://www.chotot.com/my-ads"
                driver.get(url)    
                time.sleep(2) 
                passtranglogin=0
                try:
                # Tìm phần tử chứa chữ "Đăng nhập"
                    login_element = driver.find_element(By.CSS_SELECTOR, ".flex.whitespace-pre").text
                    if login_element == "Tạo cửa hàng":
                        print(f"{namefolder} Đã có cookie Chợ Tốt")  # Thông báo nếu tìm thấy
                        passtranglogin=1
                        nologin=3
                        print("Bạn đã login danh sách sản phẩm")
                except Exception as e:
                    print("Lỗi Không tìm thấy 'cookie my-ads' ")
                    nologin=4
         time.sleep(1)   
            if passtranglogin==0:
                timeout = 20
                end_time = time.time() + timeout
                while True:
                    try:
                    # Tìm phần tử chứa chữ "Đăng nhập"
                        login_element = driver.find_element(By.CSS_SELECTOR, ".mocked-styled-29.b13ldopu").text
                        if login_element == "Đăng nhập":
                            print(f"{namefolder} Chưa đăng nhập")  # Thông báo nếu tìm thấy
                            cookieactive=1
                            
                    except Exception as e:
                        print("Đợi load đăng nhập xong cái")
                        time.sleep(1) 
                    if time.time() > end_time:
                        print("Lỗi Không tìm thấy chữ 'Đăng nhập' thời gian tối đa") 
                                   
        time.sleep(1)
        driver.quit()
        return f"Title of the page is"
    except Exception as e:
        return f"Error abc "

@app.get("/", response_class=HTMLResponse)
async def read_index():
    try:
        async with aiofiles.open("index.html", mode="r") as f:
            html_content = await f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        return {"error": "index.html not found"}
        
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if item_id == 123:
        result = lambda_handler()
        return JSONResponse(content={"item_id": item_id, "result": result})
    return {"item_id": item_id, "q": q}
    

        


