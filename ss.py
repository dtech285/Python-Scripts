#!/usr/bin/env python
import json
from urllib.request import Request
import urllib.request



def main():
    r = urllib.request.urlopen('https://api.spotify.com/v1/search?type=artist&q=snoop')
    #r.json()

    # Make a get request to get the latest position of the international space station from the opennotify api.
    #response = request.get("http://api.open-notify.org/iss-now.json")

    # Print the status code of the response.
    #print(response.status_code)

    print("DONE")





if __name__ == '__main__':
    main()
