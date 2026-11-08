# Smart Bookmarks

An AI-powered bookmark manager: save links, get summaries,search by meaning, and chat with your saved content.

## Status
Work in progress. Day 1: FastAPI setup and web content extraction.

## Run locally
    python -m venv venv
    source venv/bin/activate
    pip install -r backend/requirements.txt
    cd backend && uvicorn app.main:app --reload