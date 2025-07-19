import requests
key2 = '40f8ff8bf1e473beedeab4c01c04865c' 
url = f'http://api.openweathermap.org/data/2.5/weather?q=varanasi&appid='+key2

def temp():
    # Replace with your actual API URL and parameters
    key2 = '40f8ff8bf1e473beedeab4c01c04865c'  # Ensure you have a valid API key
    #city = 'your_city'  # Set the city you want to fetch the weather for
    url = f'http://api.openweathermap.org/data/2.5/weather?q=varanasi&appid='+key2

    response = requests.get(url)
    json_data = response.json()
    
    # Print the raw response to see the structure
    print(json_data)  # This will help you understand the structure of the response
    
    # Check if 'main' is in the response before trying to access it
    if 'main' in json_data:
        temperature = round(json_data["main"]["temp"] - 273, 1)
        return temperature
    else:
        return "Error: Could not fetch weather data"
def des():
    json_data=requests.get(url).json()
    description=json_data["weather"][0]["description"]
    return description

# Call the temp function
print(temp())
print(des())
