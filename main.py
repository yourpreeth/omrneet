from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "OMR NEET Checker Running"}

@app.post("/check")
async def check_omr(file: UploadFile, answer_key: str = Form(...)):
    # Mock processing
    return JSONResponse({"status": "success", "score": 180})

