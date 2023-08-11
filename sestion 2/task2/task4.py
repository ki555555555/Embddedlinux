import requests

def get_location(ip_address):
    url = f"https://ipinfo.io/{ip_address}/geo"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        location = data.get("city", "Location information not available.")
        return location
    else:
        return "Failed to retrieve location."

if __name__ == "__main__":
    your_ip_address = "102.47.44.60"  # Replace this with your actual IP address
    location = get_location(your_ip_address)
    print("Your Location:", location)
