# BuildSpace

BuildSpace is a full-stack developer collaboration platform with:
- Vue frontend (`frontend/`)
- Flask backend API (`backend/`)

## Features
- Authentication flow (home, login, register, logout)
- Developer feed with post creation and likes
- Projects listing and project creation
- Opportunities listing and opportunity creation
- Profile editing and activity timeline
- Notifications and messages pages
- Light/Dark theme toggle

## Project Structure
- `backend/` Flask API, SQLite DB models, seed scripts
- `frontend/` Vue app (Vite), pages/components/styles

## Prerequisites
- Node.js 18+ and npm
- Python 3.10+ (or compatible)

## Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Backend runs at: `http://127.0.0.1:5000`

## Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://127.0.0.1:5173` (default Vite port)

## Build Frontend
```bash
cd frontend
npm run build
```

## Notes
- API base URL is configured in `frontend/src/api.js`.
- Backend currently uses a mock current user for local development.
