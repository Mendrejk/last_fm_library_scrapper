import requests
from bs4 import BeautifulSoup

from collections import OrderedDict


def get_soup(endpoint):
    __user_library_url = 'https://www.last.fm/user/Maendrake/library/'

    # Make a GET request to the URL and retrieve the HTML content
    response = requests.get(__user_library_url + endpoint)
    html_content = response.text

    # Use BeautifulSoup to parse the HTML content and extract the relevant information
    return BeautifulSoup(html_content, 'html.parser')


def scrap_tracks():
    soup = get_soup('tracks')
    songs = [s.text.strip() for s in soup.select('.chartlist-name')]
    artists = [r.text.strip() for r in soup.select('.chartlist-artist')]

    return songs, artists


def scrap_albums():
    soup = get_soup('albums')
    albums = [a.text.strip() for a in soup.select('.chartlist-name')]
    artists = [a.text.strip() for a in soup.select('.chartlist-artist')]

    return albums, artists


def scrap_artists():
    soup = get_soup('artists')
    artists = [a.text.strip() for a in soup.select('.chartlist-name')]

    return artists


def main():
    songs, artists_from_tracks = scrap_tracks()
    albums, artists_from_albums = scrap_albums()
    artists = scrap_artists()

    # Create ordered dictionaries to store the unique items from each list
    unique_songs = OrderedDict.fromkeys(songs)
    unique_albums = OrderedDict.fromkeys(albums)
    unique_artists = OrderedDict.fromkeys(artists + artists_from_albums + artists)

    print(unique_artists.keys())


if __name__ == '__main__':
    main()
