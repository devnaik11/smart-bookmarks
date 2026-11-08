from fastapi import FastAPI, HTTPException
from app.services.extractor import extract_web_content
app = FastAPI(title = "Smart Book")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/extract")
def extract(url: str):
    try:
        data = extract_web_content(url)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return {
        "title": data["title"],
        "word_count": len(data["text"].split()),
        "preview": data["text"][:500],
    }