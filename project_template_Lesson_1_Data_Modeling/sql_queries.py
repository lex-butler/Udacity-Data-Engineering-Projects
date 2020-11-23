# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplay 
    (
    songplay_id int PRIMARY KEY, 
    start_time time, 
    user_id int, 
    level int, 
    song_id int, 
    artist_id int, 
    session_id int, 
    location int, 
    user_agent int
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (
    user_id int PRIMARY KEY, 
    first_name varchar, 
    last_name varchar, 
    gender varchar(1), 
    level int
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS user
    (
    song_id int PRIMARY KEY,
    title varchar, 
    artist_id int, 
    year int, 
    duration int
    )
    """)

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS user
    (
    artist_id int PRIMARY KEY, 
    name varchar,
    location varchar, 
    latitude int, 
    longitude int
    )
    """)


time_table_create = ("""
    CREATE TABLE IF NOT EXISTS user
    (
    start_time time[8], 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday varchar
    )
    """)

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
            SELECT *
            FROM song
            """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]