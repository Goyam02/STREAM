# import requests
# import os

# # Replace these with your Spotify API credentials
# CLIENT_ID = '9a7cf55f463a473797efe87578dd08b2'
# CLIENT_SECRET = 'f0a5eb0dc489476abe7539474b1ca59c'

# def get_access_token(client_id, client_secret):
#     auth_url = 'https://accounts.spotify.com/api/token'
#     auth_response = requests.post(auth_url, {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret,
#     })

#     auth_response_data = auth_response.json()
#     return auth_response_data['access_token']

# def download_album_cover(songs, save_dir='album_covers'):
#     # Create the directory if it doesn't exist
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

#     access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#     }

#     for artist, song in songs:
#         search_query = f"{artist} {song}"
#         search_url = 'https://api.spotify.com/v1/search'
#         params = {
#             'q': search_query,
#             'type': 'album',
#             'limit': 1
#         }

#         response = requests.get(search_url, headers=headers, params=params)
#         data = response.json()

#         if data['albums']['items']:
#             album = data['albums']['items'][0]
#             album_name = album['name']
#             album_cover_url = album['images'][0]['url']

#             # Download the album cover
#             cover_response = requests.get(album_cover_url)
#             cover_filename = os.path.join(save_dir, f"{album_name}.jpg")
#             with open(cover_filename, 'wb') as file:
#                 file.write(cover_response.content)
#             print(f"Downloaded album cover for '{album_name}'")
#         else:
#             print(f"No album found for '{search_query}'")

# # List of songs to download covers for
# songs_list = [
#     ('Ariana Grande', 'Thank U, Next'),
#     ('Dua Lipa', 'Levitating'),
#     ('Ed Sheeran', 'Shape of You'),
#     ('Billie Eilish', 'Bad Guy'),
#     ('Taylor Swift', 'Shake It Off'),
#     ('Katy Perry', 'Firework'),
#     ('Justin Bieber', 'Sorry'),
#     ('The Weeknd', 'Blinding Lights'),
#     ('Shawn Mendes', 'Stitches'),
#     ('Olivia Rodrigo', 'drivers license'),
#     ('Queen', 'Bohemian Rhapsody'),
#     ('The Beatles', 'Hey Jude'),
#     ('Nirvana', 'Smells Like Teen Spirit'),
#     ('Led Zeppelin', 'Stairway to Heaven'),
#     ('The Rolling Stones', 'Paint It, Black'),
#     ('Coldplay', 'Fix You'),
#     ('U2', 'With or Without You'),
#     ('Linkin Park', 'In the End'),
#     ('Foo Fighters', 'Everlong'),
#     ('Green Day', 'Boulevard of Broken Dreams'),
#     ('Alicia Keys', 'If I Ain\'t Got You'),
#     ('Beyoncé', 'Halo'),
#     ('Marvin Gaye', 'Sexual Healing'),
#     ('SZA', 'Good Days'),
#     ('John Legend', 'All of Me'),
#     ('Whitney Houston', 'I Will Always Love You'),
#     ('Frank Ocean', 'Thinkin Bout You'),
#     ('Usher', 'Yeah!'),
#     ('Rihanna', 'Umbrella'),
#     ('Bruno Mars', 'Uptown Funk'),
#     ('Drake', 'God\'s Plan'),
#     ('Kendrick Lamar', 'HUMBLE.'),
#     ('Kanye West', 'Stronger'),
#     ('Cardi B', 'I Like It'),
#     ('Post Malone', 'Circles'),
#     ('Travis Scott', 'SICKO MODE'),
#     ('Eminem', 'Lose Yourself'),
#     ('Megan Thee Stallion', 'Savage'),
#     ('Nicki Minaj', 'Super Bass'),
#     ('J. Cole', 'Middle Child'),
#     ('Taylor Swift', 'Love Story'),
#     ('Blake Shelton', 'God\'s Country'),
#     ('Kenny Chesney', 'American Kids'),
#     ('Luke Bryan', 'Country Girl (Shake It for Me)'),
#     ('Carrie Underwood', 'Before He Cheats'),
#     ('Florida Georgia Line', 'Cruise'),
#     ('Tim McGraw', 'Humble and Kind'),
#     ('Johnny Cash', 'Ring of Fire'),
#     ('Miranda Lambert', 'The House That Built Me'),
#     ('Keith Urban', 'Blue Ain\'t Your Color'),
#     ('Calvin Harris', 'Summer'),
#     ('David Guetta ft. Sia', 'Titanium'),
#     ('Avicii', 'Wake Me Up'),
#     ('The Chainsmokers', 'Closer'),
#     ('Zedd ft. Alessia Cara', 'Stay'),
#     ('Marshmello ft. Bastille', 'Happier'),
#     ('Dua Lipa', 'Physical'),
#     ('Martin Garrix', 'Animals'),
#     ('Major Lazer & DJ Snake ft. MØ', 'Lean On'),
#     ('Kygo ft. Conrad Sewell', 'Firestone'),
#     ('Imagine Dragons', 'Radioactive'),
#     ('Tame Impala', 'The Less I Know the Better'),
#     ('Vampire Weekend', 'A-Punk'),
#     ('The Killers', 'Mr. Brightside'),
#     ('Foster the People', 'Pumped Up Kicks'),
#     ('Florence + The Machine', 'Shake It Out'),
#     ('Lorde', 'Royals'),
#     ('Arctic Monkeys', 'Do I Wanna Know?'),
#     ('MGMT', 'Electric Feel'),
#     ('The Strokes', 'Last Nite'),
#     ('Bob Marley & The Wailers', 'No Woman, No Cry'),
#     ('Shaggy', 'It Wasn\'t Me'),
#     ('Sean Paul', 'Get Busy'),
#     ('UB40', 'Red Red Wine'),
#     ('Inner Circle', 'Bad Boys'),
#     ('Damian Marley', 'Welcome to Jamrock'),
#     ('Peter Tosh', 'Legalize It'),
#     ('Tarrus Riley', 'She\'s Royal'),
#     ('Beres Hammond', 'I Feel Good'),
#     ('Steel Pulse', 'Your House'),
#     ('Frank Sinatra', 'Fly Me to the Moon'),
#     ('Billie Holiday', 'Strange Fruit'),
#     ('Nina Simone', 'Feeling Good'),
#     ('Ella Fitzgerald', 'Summertime'),
#     ('Louis Armstrong', 'What a Wonderful World'),
#     ('Etta James', 'At Last'),
#     ('Ray Charles', 'Georgia on My Mind'),
#     ('John Coltrane', 'Giant Steps'),
#     ('B.B. King', 'The Thrill Is Gone'),
#     ('Miles Davis', 'So What'),
#     ('Bob Dylan', 'Blowin\' in the Wind'),
#     ('Simon & Garfunkel', 'The Sound of Silence'),
#     ('Fleet Foxes', 'White Winter Hymnal'),
#     ('Mumford & Sons', 'Little Lion Man'),
#     ('The Lumineers', 'Ho Hey'),
#     ('Iron & Wine', 'Flightless Bird, American Mouth'),
#     ('Johnny Cash', 'Folsom Prison Blues'),
#     ('Ben Howard', 'Keep Your Head Up'),
#     ('The Avett Brothers', 'I and Love and You'),
#     ('First Aid Kit', 'Fireworks')
# ]

# # Download album covers for the list
# download_album_cover(songs_list)

# access_token = get_access_token('9a7cf55f463a473797efe87578dd08b2', 'f0a5eb0dc489476abe7539474b1ca59c')

# import os
# import requests

# def sanitize_filename(filename):
#     # Replace characters that are not allowed in filenames
#     return filename.replace('/', '_').replace(':', '-')

# def download_album_cover(album_names, save_dir='album_covers'):
#     # Create the directory if it doesn't exist
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

#     access_token = get_access_token('9a7cf55f463a473797efe87578dd08b2', 'f0a5eb0dc489476abe7539474b1ca59c')
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#     }

#     for album_name in album_names:
#         search_url = 'https://api.spotify.com/v1/search'
#         params = {
#             'q': album_name,
#             'type': 'album',
#             'limit': 1
#         }

#         response = requests.get(search_url, headers=headers, params=params)
#         data = response.json()

#         if data['albums']['items']:
#             album = data['albums']['items'][0]
#             album_name = album['name']
#             album_cover_url = album['images'][0]['url']

#             # Sanitize the album name for the filename
#             sanitized_album_name = sanitize_filename(album_name)
#             cover_filename = os.path.join(save_dir, f"{sanitized_album_name}.jpg")

#             # Download the album cover
#             cover_response = requests.get(album_cover_url)
#             with open(cover_filename, 'wb') as file:
#                 file.write(cover_response.content)
#             print(f"Downloaded album cover for '{album_name}'")
#         else:
#             print(f"No album found with name '{album_name}'")

# # Example usage
# songs_list = [
#     # Pop
#     'Ariana Grande - Thank U, Next',
#     'Dua Lipa - Levitating',
#     'Ed Sheeran - Shape of You',
#     'Billie Eilish - Bad Guy',
#     'Taylor Swift - Shake It Off',
#     'Katy Perry - Firework',
#     'Justin Bieber - Sorry',
#     'The Weeknd - Blinding Lights',
#     'Shawn Mendes - Stitches',
#     'Olivia Rodrigo - drivers license',
#     # Rock
#     'Queen - Bohemian Rhapsody',
#     'The Beatles - Hey Jude',
#     'Nirvana - Smells Like Teen Spirit',
#     'Led Zeppelin - Stairway to Heaven',
#     'The Rolling Stones - Paint It, Black',
#     'Coldplay - Fix You',
#     'U2 - With or Without You',
#     'Linkin Park - In the End',
#     'Foo Fighters - Everlong',
#     'Green Day - Boulevard of Broken Dreams',
#     # R&B/Soul
#     'Alicia Keys - If I Ain\'t Got You',
#     'Beyoncé - Halo',
#     'Marvin Gaye - Sexual Healing',
#     'SZA - Good Days',
#     'John Legend - All of Me',
#     'Whitney Houston - I Will Always Love You',
#     'Frank Ocean - Thinkin Bout You',
#     'Usher - Yeah!',
#     'Rihanna - Umbrella',
#     'Bruno Mars - Uptown Funk',
#     # Hip-Hop/Rap
#     'Drake - God\'s Plan',
#     'Kendrick Lamar - HUMBLE.',
#     'Kanye West - Stronger',
#     'Cardi B - I Like It',
#     'Post Malone - Circles',
#     'Travis Scott - SICKO MODE',
#     'Eminem - Lose Yourself',
#     'Megan Thee Stallion - Savage',
#     'Nicki Minaj - Super Bass',
#     'J. Cole - Middle Child',
#     # Country
#     'Taylor Swift - Love Story',
#     'Blake Shelton - God\'s Country',
#     'Kenny Chesney - American Kids',
#     'Luke Bryan - Country Girl (Shake It for Me)',
#     'Carrie Underwood - Before He Cheats',
#     'Florida Georgia Line - Cruise',
#     'Tim McGraw - Humble and Kind',
#     'Johnny Cash - Ring of Fire',
#     'Miranda Lambert - The House That Built Me',
#     'Keith Urban - Blue Ain\'t Your Color',
#     # Dance/Electronic
#     'Calvin Harris - Summer',
#     'David Guetta ft. Sia - Titanium',
#     'Avicii - Wake Me Up',
#     'The Chainsmokers - Closer',
#     'Zedd ft. Alessia Cara - Stay',
#     'Marshmello ft. Bastille - Happier',
#     'Dua Lipa - Physical',
#     'Martin Garrix - Animals',
#     'Major Lazer & DJ Snake ft. MØ - Lean On',
#     'Kygo ft. Conrad Sewell - Firestone',
#     # Indie/Alternative
#     'Imagine Dragons - Radioactive',
#     'Tame Impala - The Less I Know the Better',
#     'Vampire Weekend - A-Punk',
#     'The Killers - Mr. Brightside',
#     'Foster the People - Pumped Up Kicks',
#     'Florence + The Machine - Shake It Out',
#     'Lorde - Royals',
#     'Arctic Monkeys - Do I Wanna Know?',
#     'MGMT - Electric Feel',
#     'The Strokes - Last Nite',
#     # Reggae
#     'Bob Marley & The Wailers - No Woman, No Cry',
#     'Shaggy - It Wasn\'t Me',
#     'Sean Paul - Get Busy',
#     'UB40 - Red Red Wine',
#     'Inner Circle - Bad Boys',
#     'Damian Marley - Welcome to Jamrock',
#     'Peter Tosh - Legalize It',
#     'Tarrus Riley - She\'s Royal',
#     'Beres Hammond - I Feel Good',
#     'Steel Pulse - Your House',
#     # Jazz/Blues
#     'Frank Sinatra - Fly Me to the Moon',
#     'Billie Holiday - Strange Fruit',
#     'Nina Simone - Feeling Good',
#     'Ella Fitzgerald - Summertime',
#     'Louis Armstrong - What a Wonderful World',
#     'Etta James - At Last',
#     'Ray Charles - Georgia on My Mind',
#     'John Coltrane - Giant Steps',
#     'B.B. King - The Thrill Is Gone',
#     'Miles Davis - So What',
#     # Folk
#     'Bob Dylan - Blowin\' in the Wind',
#     'Simon & Garfunkel - The Sound of Silence',
#     'Fleet Foxes - White Winter Hymnal',
#     'Mumford & Sons - Little Lion Man',
#     'The Lumineers - Ho Hey',
#     'Iron & Wine - Flightless Bird, American Mouth',
#     'Johnny Cash - Folsom Prison Blues',
#     'Ben Howard - Keep Your Head Up',
#     'The Avett Brothers - I and Love and You',
#     'First Aid Kit - Fireworks'
# ]

# download_album_cover(songs_list)


# import os
# import requests

# def sanitize_filename(filename):
#     return filename.replace('/', '_').replace(':', '-')

# def download_album_cover(album_names, save_dir='album_covers'):
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

#     access_token = get_access_token('9a7cf55f463a473797efe87578dd08b2', 'f0a5eb0dc489476abe7539474b1ca59c')
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#     }

#     for album_name in album_names:
#         try:
#             search_url = 'https://api.spotify.com/v1/search'
#             params = {
#                 'q': album_name,
#                 'type': 'album',
#                 'limit': 1
#             }

#             response = requests.get(search_url, headers=headers, params=params)
#             response.raise_for_status()  # Raises an HTTPError for bad responses
#             data = response.json()

#             if data['albums']['items']:
#                 album = data['albums']['items'][0]
#                 album_name = album['name']
#                 album_cover_url = album['images'][0]['url']

#                 sanitized_album_name = sanitize_filename(album_name)
#                 cover_filename = os.path.join(save_dir, f"{sanitized_album_name}.jpg")

#                 cover_response = requests.get(album_cover_url)
#                 cover_response.raise_for_status()

#                 with open(cover_filename, 'wb') as file:
#                     file.write(cover_response.content)
#                 print(f"Downloaded album cover for '{album_name}'")
#             else:
#                 print(f"No album found with name '{album_name}'")
#         except requests.exceptions.RequestException as e:
#             print(f"An error occurred: {e}")

# # Example usage
# songs_list = [
    #     # Pop
    # 'Ariana Grande - Thank U, Next',
    # 'Dua Lipa - Levitating',
    # 'Ed Sheeran - Shape of You',
    # 'Billie Eilish - Bad Guy',
    # 'Taylor Swift - Shake It Off',
    # 'Katy Perry - Firework',
    # 'Justin Bieber - Sorry',
    # 'The Weeknd - Blinding Lights',
    # 'Shawn Mendes - Stitches',
    # 'Olivia Rodrigo - drivers license',
    # # Rock
    # 'Queen - Bohemian Rhapsody',
    # 'The Beatles - Hey Jude',
    # 'Nirvana - Smells Like Teen Spirit',
    # 'Led Zeppelin - Stairway to Heaven',
    # 'The Rolling Stones - Paint It, Black',
    # 'Coldplay - Fix You',
    # 'U2 - With or Without You',
    # 'Linkin Park - In the End',
    # 'Foo Fighters - Everlong',
    # 'Green Day - Boulevard of Broken Dreams',
    # # R&B/Soul
    # 'Alicia Keys - If I Ain\'t Got You',
    # 'Beyoncé - Halo',
    # 'Marvin Gaye - Sexual Healing',
    # 'SZA - Good Days',
    # 'John Legend - All of Me',
    # 'Whitney Houston - I Will Always Love You',
    # 'Frank Ocean - Thinkin Bout You',
    # 'Usher - Yeah!',
    # 'Rihanna - Umbrella',
    # 'Bruno Mars - Uptown Funk',
    # # Hip-Hop/Rap
    # 'Drake - God\'s Plan',
    # 'Kendrick Lamar - HUMBLE.',
    # 'Kanye West - Stronger',
    # 'Cardi B - I Like It',
    # 'Post Malone - Circles',
    # 'Travis Scott - SICKO MODE',
    # 'Eminem - Lose Yourself',
    # 'Megan Thee Stallion - Savage',
    # 'Nicki Minaj - Super Bass',
    # 'J. Cole - Middle Child',
    # # Country
    # 'Taylor Swift - Love Story',
    # 'Blake Shelton - God\'s Country',
    # 'Kenny Chesney - American Kids',
    # 'Luke Bryan - Country Girl (Shake It for Me)',
    # 'Carrie Underwood - Before He Cheats',
    # 'Florida Georgia Line - Cruise',
    # 'Tim McGraw - Humble and Kind',
    # 'Johnny Cash - Ring of Fire',
    # 'Miranda Lambert - The House That Built Me',
    # 'Keith Urban - Blue Ain\'t Your Color',
    # # Dance/Electronic
    # 'Calvin Harris - Summer',
    # 'David Guetta ft. Sia - Titanium',
    # 'Avicii - Wake Me Up',
    # 'The Chainsmokers - Closer',
    # 'Zedd ft. Alessia Cara - Stay',
    # 'Marshmello ft. Bastille - Happier',
    # 'Dua Lipa - Physical',
    # 'Martin Garrix - Animals',
    # 'Major Lazer & DJ Snake ft. MØ - Lean On',
    # 'Kygo ft. Conrad Sewell - Firestone',
    # # Indie/Alternative
    # 'Imagine Dragons - Radioactive',
    # 'Tame Impala - The Less I Know the Better',
    # 'Vampire Weekend - A-Punk',
    # 'The Killers - Mr. Brightside',
    # 'Foster the People - Pumped Up Kicks',
    # 'Florence + The Machine - Shake It Out',
    # 'Lorde - Royals',
    # 'Arctic Monkeys - Do I Wanna Know?',
    # 'MGMT - Electric Feel',
    # 'The Strokes - Last Nite',
    # # Reggae
    # 'Bob Marley & The Wailers - No Woman, No Cry',
    # 'Shaggy - It Wasn\'t Me',
    # 'Sean Paul - Get Busy',
    # 'UB40 - Red Red Wine',
    # 'Inner Circle - Bad Boys',
    # 'Damian Marley - Welcome to Jamrock',
    # 'Peter Tosh - Legalize It',
    # 'Tarrus Riley - She\'s Royal',
    # 'Beres Hammond - I Feel Good',
    # 'Steel Pulse - Your House',
    # # Jazz/Blues
    # 'Frank Sinatra - Fly Me to the Moon',
    # 'Billie Holiday - Strange Fruit',
    # 'Nina Simone - Feeling Good',
    # 'Ella Fitzgerald - Summertime',
    # 'Louis Armstrong - What a Wonderful World',
    # 'Etta James - At Last',
    # 'Ray Charles - Georgia on My Mind',
    # 'John Coltrane - Giant Steps',
    # 'B.B. King - The Thrill Is Gone',
    # 'Miles Davis - So What',
    # # Folk
    # 'Bob Dylan - Blowin\' in the Wind',
    # 'Simon & Garfunkel - The Sound of Silence',
    # 'Fleet Foxes - White Winter Hymnal',
    # 'Mumford & Sons - Little Lion Man',
    # 'The Lumineers - Ho Hey',
    # 'Iron & Wine - Flightless Bird, American Mouth',
    # 'Johnny Cash - Folsom Prison Blues',
    # 'Ben Howard - Keep Your Head Up',
    # 'The Avett Brothers - I and Love and You',
    # 'First Aid Kit - Fireworks'

    
# ]

# download_album_cover(songs_list)


# import os
# import requests
# from requests.auth import HTTPBasicAuth

# def get_access_token(client_id, client_secret):
#     auth_url = 'https://accounts.spotify.com/api/token'
#     auth_response = requests.post(auth_url, {
#         'grant_type': 'client_credentials'
#     }, auth=HTTPBasicAuth(client_id, client_secret))

#     auth_response_data = auth_response.json()
#     return auth_response_data['access_token']

# def sanitize_filename(filename):
#     return filename.replace('/', '_').replace(':', '-')

# def download_album_cover(album_names, save_dir='album_covers'):
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

#     # Replace these with your actual client ID and secret
#     client_id = '9a7cf55f463a473797efe87578dd08b2'
#     client_secret = 'f0a5eb0dc489476abe7539474b1ca59c'
    
#     access_token = get_access_token(client_id, client_secret)
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#     }

#     for album_name in album_names:
#         try:
#             search_url = 'https://api.spotify.com/v1/search'
#             params = {
#                 'q': album_name,
#                 'type': 'album',
#                 'limit': 1
#             }

#             response = requests.get(search_url, headers=headers, params=params)
#             response.raise_for_status()  
#             data = response.json()

#             if data['albums']['items']:
#                 album = data['albums']['items'][0]
#                 album_name = album['name']
#                 album_cover_url = album['images'][0]['url']

#                 sanitized_album_name = sanitize_filename(album_name)
#                 cover_filename = os.path.join(save_dir, f"{sanitized_album_name}.jpg")

#                 cover_response = requests.get(album_cover_url)
#                 cover_response.raise_for_status()

#                 with open(cover_filename, 'wb') as file:
#                     file.write(cover_response.content)
#                 print(f"Downloaded album cover for '{album_name}'")
#             else:
#                 print(f"No album found with name '{album_name}'")
#         except requests.exceptions.RequestException as e:
#             print(f"An error occurred: {e}")

# # Example usage
# songs_list = [
#            # Pop
#     'Ariana Grande - Thank U, Next',
#     'Dua Lipa - Levitating',
#     'Ed Sheeran - Shape of You',
#     'Billie Eilish - Bad Guy',
#     'Taylor Swift - Shake It Off',
#     'Katy Perry - Firework',
#     'Justin Bieber - Sorry',
#     'The Weeknd - Blinding Lights',
#     'Shawn Mendes - Stitches',
#     'Olivia Rodrigo - drivers license',
#     # Rock
#     'Queen - Bohemian Rhapsody',
#     'The Beatles - Hey Jude',
#     'Nirvana - Smells Like Teen Spirit',
#     'Led Zeppelin - Stairway to Heaven',
#     'The Rolling Stones - Paint It, Black',
#     'Coldplay - Fix You',
#     'U2 - With or Without You',
#     'Linkin Park - In the End',
#     'Foo Fighters - Everlong',
#     'Green Day - Boulevard of Broken Dreams',
#     # R&B/Soul
#     'Alicia Keys - If I Ain\'t Got You',
#     'Beyoncé - Halo',
#     'Marvin Gaye - Sexual Healing',
#     'SZA - Good Days',
#     'John Legend - All of Me',
#     'Whitney Houston - I Will Always Love You',
#     'Frank Ocean - Thinkin Bout You',
#     'Usher - Yeah!',
#     'Rihanna - Umbrella',
#     'Bruno Mars - Uptown Funk',
#     # Hip-Hop/Rap
#     'Drake - God\'s Plan',
#     'Kendrick Lamar - HUMBLE.',
#     'Kanye West - Stronger',
#     'Cardi B - I Like It',
#     'Post Malone - Circles',
#     'Travis Scott - SICKO MODE',
#     'Eminem - Lose Yourself',
#     'Megan Thee Stallion - Savage',
#     'Nicki Minaj - Super Bass',
#     'J. Cole - Middle Child',
#     # Country
#     'Taylor Swift - Love Story',
#     'Blake Shelton - God\'s Country',
#     'Kenny Chesney - American Kids',
#     'Luke Bryan - Country Girl (Shake It for Me)',
#     'Carrie Underwood - Before He Cheats',
#     'Florida Georgia Line - Cruise',
#     'Tim McGraw - Humble and Kind',
#     'Johnny Cash - Ring of Fire',
#     'Miranda Lambert - The House That Built Me',
#     'Keith Urban - Blue Ain\'t Your Color',
#     # Dance/Electronic
#     'Calvin Harris - Summer',
#     'David Guetta ft. Sia - Titanium',
#     'Avicii - Wake Me Up',
#     'The Chainsmokers - Closer',
#     'Zedd ft. Alessia Cara - Stay',
#     'Marshmello ft. Bastille - Happier',
#     'Dua Lipa - Physical',
#     'Martin Garrix - Animals',
#     'Major Lazer & DJ Snake ft. MØ - Lean On',
#     'Kygo ft. Conrad Sewell - Firestone',
#     # Indie/Alternative
#     'Imagine Dragons - Radioactive',
#     'Tame Impala - The Less I Know the Better',
#     'Vampire Weekend - A-Punk',
#     'The Killers - Mr. Brightside',
#     'Foster the People - Pumped Up Kicks',
#     'Florence + The Machine - Shake It Out',
#     'Lorde - Royals',
#     'Arctic Monkeys - Do I Wanna Know?',
#     'MGMT - Electric Feel',
#     'The Strokes - Last Nite',
#     # Reggae
#     'Bob Marley & The Wailers - No Woman, No Cry',
#     'Shaggy - It Wasn\'t Me',
#     'Sean Paul - Get Busy',
#     'UB40 - Red Red Wine',
#     'Inner Circle - Bad Boys',
#     'Damian Marley - Welcome to Jamrock',
#     'Peter Tosh - Legalize It',
#     'Tarrus Riley - She\'s Royal',
#     'Beres Hammond - I Feel Good',
#     'Steel Pulse - Your House',
#     # Jazz/Blues
#     'Frank Sinatra - Fly Me to the Moon',
#     'Billie Holiday - Strange Fruit',
#     'Nina Simone - Feeling Good',
#     'Ella Fitzgerald - Summertime',
#     'Louis Armstrong - What a Wonderful World',
#     'Etta James - At Last',
#     'Ray Charles - Georgia on My Mind',
#     'John Coltrane - Giant Steps',
#     'B.B. King - The Thrill Is Gone',
#     'Miles Davis - So What',
#     # Folk
#     'Bob Dylan - Blowin\' in the Wind',
#     'Simon & Garfunkel - The Sound of Silence',
#     'Fleet Foxes - White Winter Hymnal',
#     'Mumford & Sons - Little Lion Man',
#     'The Lumineers - Ho Hey',
#     'Iron & Wine - Flightless Bird, American Mouth',
#     'Johnny Cash - Folsom Prison Blues',
#     'Ben Howard - Keep Your Head Up',
#     'The Avett Brothers - I and Love and You',
#     'First Aid Kit - Fireworks'



# ]

# download_album_cover(songs_list)


import os
import requests
from requests.auth import HTTPBasicAuth

def get_access_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials'
    }, auth=HTTPBasicAuth(client_id, client_secret))

    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def sanitize_filename(filename):
    return filename.replace('/', '_').replace(':', '-')

def download_album_cover(album_names, save_dir='album_covers'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Replace these with your actual client ID and secret
    client_id = '9a7cf55f463a473797efe87578dd08b2'
    client_secret = 'f0a5eb0dc489476abe7539474b1ca59c'
    
    access_token = get_access_token(client_id, client_secret)
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    for album_name in album_names:
        try:
            search_url = 'https://api.spotify.com/v1/search'
            params = {
                'q': album_name,
                'type': 'album',
                'limit': 1
            }

            response = requests.get(search_url, headers=headers, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.json()

            if data['albums']['items']:
                album = data['albums']['items'][0]
                album_name = album['name']
                album_cover_url = album['images'][0]['url']

                sanitized_album_name = sanitize_filename(album_name)
                cover_filename = os.path.join(save_dir, f"{sanitized_album_name}.jpg")

                cover_response = requests.get(album_cover_url)
                cover_response.raise_for_status()

                with open(cover_filename, 'wb') as file:
                    file.write(cover_response.content)
                print(f"Downloaded album cover for '{album_name}'")
            else:
                print(f"No album found with name '{album_name}'")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

# Example usage
songs_list = [
    'Pehli Nazar Mein - Atif Aslam',
    'Tum Hi Ho - Arijit Singh',
    'Tum Jo Aaye - Rahat Fateh Ali Khan',
    'Channa Mereya - Arijit Singh',
    'Dil Diyan Gallan - Atif Aslam',
    'Tum Mile - Neeraj Shridhar',
    'Sun Saathiya - Priya Saraiya, Divya Kumar',
    'Jeene Laga Hoon - Atif Aslam',
    'Raabta - Arijit Singh',
    'Ae Mere Humsafar - Udit Narayan, Alka Yagnik',
    'Tum Tak - Arijit Singh',
    'Pee Loon - Mohit Chauhan',
    'Agar Tum Saath Ho - Alka Yagnik, Arijit Singh',
    'Raaz Aankhein Teri - Kunal Ganjawala',
    'Dilwale Dulhania Le Jayenge (title track) - Lata Mangeshkar, Udit Narayan',
    'Tumse Hi - Mohit Chauhan',
    'Tum Se Hi - Shreya Ghoshal, Sonu Nigam',
    'Hasi - Ami Mishra',
    'Janam Janam - Arijit Singh, Antara Mitra',
    'Badtameez Dil - Benny Dayal',
    'Kar Gayi Chull - Neha Kakkar, Badshah',
    'Gallan Goodiyan - Various Artists',
    'Dil Dhadakne Do - Priyanka Chopra, Farhan Akhtar',
    'Tamma Tamma Again - Badshah, Neha Kakkar',
    'Desi Girl - Shankar Mahadevan, Sunidhi Chauhan',
    'Lungi Dance - Yo Yo Honey Singh',
    'Kala Chashma - Amar Arshi, Neha Kakkar',
    'Sheila Ki Jawani - Sunidhi Chauhan, Vishal-Shekhar',
    'Chikni Chameli - Shreya Ghoshal',
    'Zinda - Siddharth Mahadevan',
    'Teri Yaad - Anirudh Bhola',
    'Pichle Saat Dinon Mein - Kailasa',
    'Bande Hain Hum Uske - Kailasa',
    'Dhoom Again - Kunal Ganjawala, Sonu Nigam',
    'Rock On!! - Jim, Arun, and Mohit',
    'Phir Se Udd Chala - Mohit Chauhan',
    'Chak De India - Sukhwinder Singh',
    'Woh Lamhe - Jal',
    'Saudagar Sauda Kar - Udit Narayan',
    'Tajdar-e-Haram - Atif Aslam',
    'Kun Faya Kun - A.R. Rahman, Javed Ali, Mohit Chauhan',
    'Allah Ke Bande - Kailasa',
    'Arziyan - Javed Ali, Kailasa',
    'Piya Haji Ali - A. R. Rahman, Sadhana Sargam',
    'Mast Kalandar - Kailasa',
    'Tera Ban Jaunga - Akhil Sachdeva, Mansheel Gujral',
    'Saanson Ko - Kunal Ganjawala',
    'Mast Mast - Ustad Nusrat Fateh Ali Khan',
    'Noori - Rabbi Shergill',
    'Patakha Guddi - Nooran Sisters',
    'Chaiyya Chaiyya - Sukhwinder Singh, Sapna Awasthi',
    'Madhaniya - Neha Bhasin',
    'Desi Girl - Sunidhi Chauhan',
    'Chunar - Arijit Singh',
    'Teri Deewani - Kailasa',
    'Meri Jaan - Neeraj Shridhar',
    'Kaun Tujhe - Palak Muchhal',
    'Dil Dhadakne Do - Zindagi Na Milegi Dobara',
    'Gallan Goodiyan - Various Artists',
    'Mushkil Hai - A.R. Rahman, Arjun Chandy',
    'Kailasa - Kailasa',
    'Meri Kahani - Shankar Ehsaan Loy',
    'Ankh Marey - Neha Kakkar',
    'Yeh Dooriyan - Mohit Chauhan',
    'Yaari Hai - Tony Kakkar, Neha Kakkar',
    'Tera Yaar Hoon Mai - Arijit Singh',
    'Suno Na Sangemarmar - Arijit Singh',
    'Tu Hi Hai - Aditya Rao, Amaal Mallik',
    'Dil Beparvah - Zayn',
    'Alvida - Shafqat Amanat Ali',
    'Sajda - Rahat Fateh Ali Khan, Shankar Mahadevan',
    'Laaga Chunri Mein Daag - Shreya Ghoshal',
    'Keh Do Ke Tum - Shaan',
    'Pardesi Pardesi - Udit Narayan',
    'Jai Jai Shivshankar - Vishal Dadlani, Benny Dayal',
    'Bairagi - Arijit Singh',
    'Koi Kahe Kehta Rahe - Shankar Mahadevan',
    'Ishq Sufiyana - Kailasa',
    'Madhurima - Kailasa',
    'Tujhse Naraz Nahi Zindagi - Lata Mangeshkar',
    'Zindagi Kuch Toh - Atif Aslam',
    'Kabira - Arijit Singh',
    'Ae Dil Hai Mushkil - Arijit Singh',
    'Sun Raha Hai - Shreya Ghoshal, Ankit Tiwari',
    'Dil Ke Paas - Kishore Kumar',
    'Munni Badnam Hui - Mamta Sharma, Aishwarya',
    'Dance Basanti - Asha Bhosle, Kunal Ganjawala',
    'Pappu Can\'t Dance - Mika Singh',
    'Chhote Chhote Peg - Neha Kakkar, Mika Singh',
    'Tunak Tunak Tun - Daler Mehndi',
    'Aap Jaisa Koi - Udit Narayan, Sadhana Sargam',
    'Anarkali Disco Chali - Mamta Sharma',
    'Dilliwali Girlfriend - Arijit Singh, Neeti Mohan',
    'Bachna Ae Haseeno - Neeraj Shridhar, Kunal Ganjawala'
]

download_album_cover(songs_list)
