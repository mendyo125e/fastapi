from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import aiofiles

app = FastAPI()

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
    print("abc")
    return {"item_id": item_id, "q": q}
