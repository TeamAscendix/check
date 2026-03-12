from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# simple status variable
status_code = 0
@app.get("/")
def root():
    return {"code": status_code}

@app.get("/status")
def get_status():
    return JSONResponse(content={"code": status_code})
