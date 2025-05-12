# IPL Player Assignment App

A Flask-based web app to assign IPL players to random teams using creat.xyz's global database.

## Features
- Assign or update players
- Auto-generate unique codes
- Stylish frontend and admin-only name entry

## Setup

1. Clone the repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your `.env` with creat.xyz DB string
4. Run the app:
   ```
   python app.py
   ```

## Deployment
This app can be deployed on [Render](https://render.com/). Set environment variable `DATABASE_URL` in the Render dashboard.
