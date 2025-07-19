import requests

# URL to get a random joke from the API
url = "https://official-joke-api.appspot.com/random_joke"

# Get the JSON response
json_data = requests.get(url).json()

# Store the setup and punchline in an array
arr = [json_data["setup"], json_data["punchline"]]

# Define a function to return the joke
def joke():
    return f"Here's a joke:\n{arr[0]}\n{arr[1]}"

# Call the function and print the joke
#print(joke())
