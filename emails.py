# Create a new variable named 'contacts' that is an re.search() 
# where the pattern catches the email address and phone number from string
# Name the email pattern 'email' and the phone number pattern 'phone'
# The comma and spaces should not be part of the groups

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s # Email
    (?P<phone>\d{3}-\d{3}-\d{4}) # Phone number
''', string, re.X|re.I)

# Now make a new variable, 'twitters', that is an re.search() 
# where the pattern catches the Twitter handle for a person
# Remember to mark it as being at end of string
# Also want to use multiline flag
twitters = re.search(r'''
	(?P<twitter>@[\w\d]+)$
''', string, re.X|re.I|re.M)