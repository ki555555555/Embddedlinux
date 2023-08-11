import webbrowser

class WebsiteOpener:
    def open_website(self, url):
        webbrowser.open(url)

def Firefox(url):
    webbrowser.open(url)

# Example usage
if __name__ == "__main__":
    favorite_website = "https://play.anghami.com/mymusic"
    Firefox(favorite_website)