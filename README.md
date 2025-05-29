# Tasque

**Tasque** is a lightweight GTD-based task manager built with FastAPI.  
Track projects, contexts, and actions with clarity and speed.

## Features

- Projects and Contexts (GTD)
- Next actions, inbox, waiting, someday
- FastAPI backend
- Simple UI (Streamlit) for testing

## How to run

### Backend

```bash
uvicorn app.main:app --reload
```

### Frontend

```bash
streamlit run ui/ui.py
```