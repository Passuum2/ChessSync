-- schema.sql
-- ChessSync database schema

CREATE TABLE champion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year VARCHAR(4) NOT NULL,
    champion_name VARCHAR(255)
);

CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    championship_id INT NOT NULL,
    white_player VARCHAR(255) NOT NULL,
    black_player VARCHAR(255) NOT NULL,
    result VARCHAR(10),
    FOREIGN KEY (championship_id) REFERENCES champion(id)
);

CREATE TABLE elo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    player_name VARCHAR(255) NOT NULL,
    elo_rating INT,
    FOREIGN KEY (game_id) REFERENCES games(id)
);

CREATE TABLE location (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    event_name VARCHAR(255),
    site_location VARCHAR(255),
    FOREIGN KEY (game_id) REFERENCES games(id)
);

CREATE TABLE eco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    eco VARCHAR(10),
    moves TEXT,
    FOREIGN KEY (game_id) REFERENCES games(id)
);