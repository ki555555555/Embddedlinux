import webbrowser

# List of favorite websites
favorite_websites = [
    "https://play.anghami.com/mymusic",
    "https://anime4up.site/anime/kimetsu-no-yaiba-movie-mugen-ressha-hen-78/",
    # Add more websites here
]

def Firefox(url):
    webbrowser.open(url)

# Example usage
if __name__ == "__main__":
    for website in favorite_websites:
        Firefox(website)
