from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = FastAPI()

def lambda_handler():
    # Cấu hình trình duyệt
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy chế độ không giao diện
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Khởi tạo WebDriver
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        # Mở trang web
        driver.get("https://www.chotot.com/")
        
        # Lấy tiêu đề trang
        title = driver.title
        
        # Đóng trình duyệt
        driver.quit()

        return f"Title of the page is: {title}"
    except Exception as e:
        return f"Error occurred: {str(e)}"

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

