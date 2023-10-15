import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import webbrowser
from sys import exit
import os 

load_dotenv('.env')

# storing my client id and secret
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=str(os.getenv('CLIENT_ID')), client_secret=str(os.getenv('CLIENT_SECRET'))))

# searches for the artist
def search_result(artist):
    result = spotify.search(q='artist:' + artist, type='artist')
    return result['artists']['items'][0]

# display the artist info and the query to whether to open artist page or not
def display(artist):

    # variables 
    follower_count = ((search_result(artist))['followers'])['total']
    genre = (search_result(artist))['genres']  

    print('-------------------')
    print(f'Artist Name: {artist.capitalize()}')
    print(f'Follower count: {follower_count}')
    print(f'Top Genre: {genre[0]}, {genre[1]}, {genre[2]}')
    page = input(f'Open {artist}\'s spotfiy page? [type \'y\' to proceed]: ')
    get_artist_page(artist, page)

# opens artist's spotify page in default browser 
def get_artist_page(artist, page):

    if page == 'y':
        url = (search_result(artist)['external_urls'])['spotify']
        webbrowser.open(url)

# beginning of the program 
def main():

    while True:
        search = input('Enter artist\'s name or quit(q): ')

        if search == 'q':
            exit()

        display(search)
        print('-----------------')
    
if __name__ == "__main__":
    main()