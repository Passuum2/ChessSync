#ChessSync
Chess Sync is a full-stack web analytics platform built with Python (Flask), MySQL, and Bootstrap. It imports, normalizes, and indexes a database of World Chess Championship games from 2000 to 2025, exposing the data through APIs and a responsive dashboard that aggregates and displays player statistics analysis.

## Features
- Imports and normalizes World Chess Championship game data (2000–2025)
- Indexed MySQL database for efficient querying
- Player statistics dashboard
- [List actual stats shown — win/loss record, opening frequency, rating trend, etc.]

## Screenshots


## Tech Stack
- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** Bootstrap, HTML/CSS

## Setup & Installation
### Prerequisites
- Python 3.x
- pip
- **Note:** Requires your own MySQL instance — see [Status](#status) below.

### Steps
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in your own MySQL credentials
4. Set up MySQL database using `schema.sql`
5. Run the app: `python ChessSync.py`
6. Visit `http://localhost:5000` in your browser

## Project Structure
ChessSync.py   — main Flask app

db.py          — Flask app config and MySQL connection setup

insert.py      — data import/indexing

modules.py     — shared logic (Chess.com API calls)

queries.py     — SQL query definitions

search.py      — standalone search/query logic

templates/     — HTML views

static/css/    — styling

## Data Source
  Database: [Chess Archive World Championship PGN Collection](https://chessarchive.net/en/chess-collections/world-championship-pgn)

  PubAPI: https://support.chess.com/en/articles/9650547-what-is-the-pubapi-and-how-do-i-use-it

## Database Schema
See [`schema.sql`](./schema.sql) for full table definitions and relationships.

## Status
This project was originally built and tested using a university-provided MySQL instance, which is no longer active. The application logic, database schema, and query functionality were fully working as demonstrated in development (see Screenshots).

**Currently not runnable out of the box** — a live MySQL connection is required and is not included.

**Planned:** Migrating to a hosted deployment on AWS (RDS + EC2/Elastic Beanstalk), with a live, publicly accessible version of the dashboard. Until then, see the Screenshots section and [schema/queries file, if you add one] for evidence of functionality.
