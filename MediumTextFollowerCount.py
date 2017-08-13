# Python3

# import libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client

# Twilio Account SID

account_sid = "ACCOUNTSID"

# Twilio Auth Token

auth_token = "AUTHTOKEN"

# Creating client variable 

client = Client(account_sid, auth_token)

# Requests a page listing a specific tag. 

req = Request('https://medium.com/[publication slug]/tagged/[Tag]', headers={'User-Agent': 'Mozilla/5.0'})

# Reads into variable parsepage

parsepage = urlopen(req).read()

# Parses data to variable page

page = BeautifulSoup(parsepage, 'html.parser')

# Searches for class containing follower number

pagetext = page.find('div', attrs={'class': 'u-fontSize14 u-lineHeightBaseSans u-textColorDark u-paddingBottom15'})

# Removes everything but the text

followerstext = pagetext.text.strip()

# Removes the word "Followers"

followers = followerstext.replace('Followers', '')

# Creates and sends a SMS containing the number of Medium followers

message = client.messages.create(
	to="+15555557896", 
	from_="+15555551987", # Twilio Number
	body="You currently have " + followers + " followers on Medium for [Insert Publication Name] publication!")

