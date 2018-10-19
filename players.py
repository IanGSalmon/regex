# Create a variable named 'players' that is an re.search() or re.match() to capture three groups
# Groups named 'last_name' 'first_name' 'score'
# Should include re.MULTILINE

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
	(?P<last_name>[-\w ]+),\s
    (?P<first_name>[-\w ]+):\s
    (?P<score>[\d{2}]+)
''', string, re.X|re.I|re.M)

# Create a class named "Player" that has those same 3 attributes
# I should be able to set them through __init__
class Player:
    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score