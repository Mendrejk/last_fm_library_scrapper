import requests
from bs4 import BeautifulSoup

from collections import OrderedDict
from typing import List, Tuple, Any

from requests import Response


# This method only scraps data from the first page of data
def get_soup(endpoint: str) -> BeautifulSoup:
    __user_library_url: str = 'https://www.last.fm/user/Maendrake/library/'

    # Make a GET request to the URL and retrieve the HTML content
    response: Response = requests.get(__user_library_url + endpoint)
    html_content: str = response.text

    # Use BeautifulSoup to parse the HTML content and extract the relevant information
    return BeautifulSoup(html_content, 'html.parser')


def scrap_tracks() -> Tuple[List[str], List[str]]:
    soup: BeautifulSoup = get_soup('tracks')
    songs: list[str] = [s.text.strip() for s in soup.select('.chartlist-name')]
    artists: list[str] = [r.text.strip() for r in soup.select('.chartlist-artist')]

    return songs, artists


def scrap_albums() -> Tuple[List[str], List[str]]:
    soup: BeautifulSoup = get_soup('albums')
    albums: list[str] = [a.text.strip() for a in soup.select('.chartlist-name')]
    artists: list[str] = [a.text.strip() for a in soup.select('.chartlist-artist')]

    return albums, artists


def scrap_artists() -> list[str]:
    soup: BeautifulSoup = get_soup('artists')
    artists: list[str] = [a.text.strip() for a in soup.select('.chartlist-name')]

    return artists


def main():
    songs, artists_from_tracks = scrap_tracks()
    albums, artists_from_albums = scrap_albums()
    artists = scrap_artists()

    # Create ordered dictionaries to store the unique items from each list
    unique_songs: OrderedDict[str, None] = OrderedDict.fromkeys(songs)
    unique_albums: OrderedDict[str, None] = OrderedDict.fromkeys(albums)
    unique_artists: OrderedDict[str, None] = OrderedDict.fromkeys(artists + artists_from_albums + artists)

    print('Songs:', list(unique_songs.keys()))
    print('Albums:', list(unique_albums.keys()))
    print('Artists:', list(unique_artists.keys()))


if __name__ == '__main__':
    main()
