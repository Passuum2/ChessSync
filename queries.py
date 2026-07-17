games = """SELECT * FROM games"""
champion = """SELECT * FROM champion"""
elo = """SELECT * FROM elo group by player_name"""
eco = """SELECT * FROM eco"""
player_query = """
    SELECT 
        g.id AS game_id,
        g.white_player,
        g.black_player,
        g.result,
        c.year,
        e.moves
    FROM games g
    JOIN champion c ON g.championship_id = c.id
    LEFT JOIN eco e ON g.id = e.game_id
    WHERE g.white_player = '%s' OR g.black_player = '%s'
    ORDER BY c.year DESC;
    """