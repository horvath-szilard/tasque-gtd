# Tasque

**Tasque** is a lightweight GTD-based task manager built with FastAPI.  
Track projects, contexts, and actions with clarity and speed.

## Features

- Projects and Contexts (GTD)
- Next actions, inbox, waiting, someday
- FastAPI backend
- Simple UI (Streamlit) for testing

## How to run

### Prerequisites

**Tasque** is a Python project, in order to run the application you need to install some necessary packages. 
- Python 3.11.9 or above
- Python libraries in requirements.txt

### First run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### Backend

```bash
cd backend
uvicorn app.main:app --reload
```

### Frontend

```bash
cd backend
streamlit run ui/ui.py
```