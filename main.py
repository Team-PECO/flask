from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# fastapi 설정
from fastapi import FastAPI
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
	"*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get("/control", response_class=HTMLResponse)
async def read_control():
    with open("static/control.html", encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get("/map", response_class=HTMLResponse)
async def read_map():
    with open("static/map.html", encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get("/up")
async def up():
    print("up")
    return "up"

@app.get("/down")
async def down():
    print("down")
    return "down"

@app.get("/right")
async def right():
    print("right")
    return "right"

@app.get("/left")
async def left():
    print("left")
    return "left"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)