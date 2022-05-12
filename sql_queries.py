# DROP TABLES

songplay_table_drop = " DROP TABLE IF EXISTS songplays" # drops songplays table
user_table_drop = "DROP TABLE IF EXISTS users"  # drops users table
song_table_drop = "DROP TABLE IF EXISTS songs"  # drops songs table
artist_table_drop = "DROP TABLE IF EXISTS artists"  # drops artists table
time_table_drop = "DROP TABLE IF EXISTS time"  # drops time table

# CREATE TABLES
    # Star schema: 1 fact table (songplays), 4 dimension tables (users, songs, artists, time)

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    start_time TIMESTAMP NOT NULL,
    user_id INTEGER NOT NULL,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INTEGER,
    location VARCHAR,
    user_agent VARCHAR,
    UNIQUE (start_time, user_id, session_id))
;""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER NOT NULL PRIMARY KEY, 
    first_name VARCHAR NOT NULL, 
    last_name VARCHAR NOT NULL, 
    gender VARCHAR(10), 
    level VARCHAR);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY, 
    title VARCHAR NOT NULL, 
    artist_id VARCHAR NOT NULL,
    year INTEGER,
    duration NUMERIC NOT NULL);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY, 
    name VARCHAR NOT NULL, 
    location VARCHAR, 
    latitude FLOAT, 
    longitude FLOAT);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time VARCHAR PRIMARY KEY, 
    hour INTEGER NOT NULL, 
    day INTEGER NOT NULL, 
    week INTEGER NOT NULL, 
    month INTEGER NOT NULL, 
    year INTEGER NOT NULL, 
    weekday INTEGER NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time, user_id, session_id) DO NOTHING;
    ;""") # INSERTS songplay records into songplays table

user_table_insert = ("""
INSERT INTO users (
    user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
;""") # INSERTS users records into users table

song_table_insert = ("""
INSERT INTO songs (
    song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
    ; """) # INSERTS song records into songs table

artist_table_insert = ("""
INSERT INTO artists (
    artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (artist_id) DO NOTHING
    ; """) # INSERTS artist records into artists table

time_table_insert = ("""
INSERT INTO time (
    start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING
    ; """) # INSERTS time records into time table

# FIND SONGS

song_select = ("""
SELECT 
    s.song_id, a.artist_id 
FROM 
    songs s 
JOIN 
    artists a 
ON 
    s.artist_id = a.artist_id 
WHERE 
    s.title = %s AND a.name = %s AND s.duration = %s
; """) # SELECTS song_id and artist_id from songs and artists tables

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]