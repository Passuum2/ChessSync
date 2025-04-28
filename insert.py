import chess.pgn
import mysql.connector

# Connect to your MySQL server
conn = mysql.connector.connect(
    host="warren.sewanee.edu",
    user="daritm0_ADM",
    password="Destiny2",
    database="daritm0"
)
cursor = conn.cursor()

# Open PGN file
with open("WorldChamp2024.pgn") as pgn_file:
    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break

        headers = game.headers

        # --- 1. Insert Championship (if not exists) ---
        year = headers["Date"][:4]
        champion = headers.get("Champion", headers["White"])  # If "Champion" not provided, fallback

        cursor.execute("SELECT id FROM champion WHERE year = %s", (year,))
        row = cursor.fetchone()

        if row:
            championship_id = row[0]
        else:
            cursor.execute(
                "INSERT INTO champion (year, champion_name) VALUES (%s, %s)",
                (year, champion)
            )
            championship_id = cursor.lastrowid

        # --- 2. Insert Game ---
        white = headers["White"]
        black = headers["Black"]
        result = headers["Result"]

        cursor.execute(
            """INSERT INTO games (championship_id, white_player, black_player, result)
               VALUES (%s, %s, %s, %s)""",
            (championship_id, white, black, result)
        )
        game_id = cursor.lastrowid

        # --- 3. Insert ELOs ---
        white_elo = headers.get("WhiteElo", None)

        if white_elo:
            cursor.execute(
                "INSERT INTO elo (game_id, player_name, elo_rating) VALUES (%s, %s, %s)",
                (game_id, white, white_elo)
            )

        # --- 4. Insert Location/Event ---
        event = headers.get("Event", "Unknown Event")
        site = headers.get("Site", "Unknown Site")

        cursor.execute(
            "INSERT INTO location (game_id, event_name, site_location) VALUES (%s, %s, %s)",
            (game_id, event, site)
        )

        moves = game.accept(chess.pgn.StringExporter(headers=False, variations=False, comments=False))
        event = headers.get("ECO", "Unknown ECO")

        cursor.execute(
            "INSERT INTO eco (game_id, eco, moves) VALUES (%s, %s, %s)",
            (game_id, event, moves)
        )

        conn.commit()
        print(f"Imported game: {white} vs {black} ({year})")

# Clean up
cursor.close()
conn.close()