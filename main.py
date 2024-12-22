from typing import Optional
from fastapi import FastAPI
import aiofiles
from fastapi.responses import HTMLResponse, JSONResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib3,urllib.parse
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
def guismssystem(title,message,nologin,random_color):
    # Khởi tạo PoolManager
    http = urllib3.PoolManager()
    # URL API cần gửi yêu cầu
    url = 'https://hieuphp.name.vn/api/undetected/message.php?all=1'
    data = {'title': f'{title}','message': f'{message}','nologin': f'{nologin}','random_color': f'{random_color}'}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request( 'POST',   url,  body=encoded_data,   headers={'Content-Type': 'application/json'})
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def lambda_handler():
    # Cấu hình trình duyệt
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy chế độ không giao diện
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Khởi tạo WebDriver
    try:
        random_color = random_color_by_name("test")
        chrome_options = Options()
        
        chrome_options.browser_version = "130"
        chrome_options.platform_name = "Windows 10"
        lt_options = {};
        lt_options["username"] = "alexschmidt63ng";
        lt_options["accessKey"] = "evq0nRPGqRSZOQtu2hcYW2xy18CgxDjUotY1vYFD491PfVxPcd";
        lt_options["smartUI.project"] = "alexschmidt63ng";
        lt_options["resolution"] = "1024x768";
        lt_options["recordVideo"] = "true";
        lt_options["browserName"] = "Chrome";
        lt_options["w3c"] = True;
        lt_options["selenium_version"] = "4.0.0";
        lt_options["plugin"] = "python-python";
        chrome_options.set_capability('LT:Options', lt_options);
        
        # Desired capabilities can be set directly in the options if needed
        
            # Initialize Remote WebDriver with command_executor and desired capabilities
        driver = webdriver.Remote(command_executor="http://10.210.92.158:4444/wd/hub",options=chrome_options)
        
        driver.get("https://google.com")
        time.sleep(1)
        title = "sdfsdf"
        message=f"ok bạn"
        nologin=1
        result =guismssystem(title,message,nologin,random_color)   
        print("click xong")    
        
        # Lấy tiêu đề trang
       
        
        # Đóng trình duyệt


        return f"Title of the page is: {title}"
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
    

        


