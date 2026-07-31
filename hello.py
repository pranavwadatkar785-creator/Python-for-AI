import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

# print(True and True and False)

line = "I am learning python for AI" #string are immutable so always store the result in a new variable or overwrite the existing variable
line = line.replace("Ai", "Artificial Intelligence")
print(line)
