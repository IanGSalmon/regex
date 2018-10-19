# Create a variable 'names' that is an re.match() against 'string'
# The pattern should provide two groups, one for last name match, one for first name match
# The name parts are separated by a comma and a space

import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'''
	([-\w ]+),\s
	([-\w ]+)
''', string, re.X)

# Did not have to name groups for this challenge