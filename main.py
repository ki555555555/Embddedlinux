from web_module import Firefox, favorite_websites

# Example usage
if __name__ == "__main__":
    for website in favorite_websites:
        Firefox(website)
