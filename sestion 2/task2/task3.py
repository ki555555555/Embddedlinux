import requests

def get_public_ip():
    url = "https://api.ipify.org/?format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        ip_address = data.get("ip", "No IP address found.")
        return ip_address
    else:
        return "Failed to retrieve public IP."

if __name__ == "__main__":
    public_ip = get_public_ip()
    print("Your Public IP:", public_ip)
