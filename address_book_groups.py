import re

names_file = open("names.txt", encoding='utf-8')
data = names_file.read()
names_file.close()

last_name = r'Love'
first_name = r'Kenneth'


# Define groups with parenthesis
# But if they don't have every item we're looking for, they don't get included
# No Dave, or King Arthur
#print(re.findall(r'''
#    ([-\w ]+,\s[-\w ]+)\t # Last and first names
#    ([-\w\d.+]+@[-\w\d.]+)\t # Email
#    (\(?\d{3}\)?-?\s?\d{3}-\d{4})\t # Phone number
#    ([\w\s]+,\s[\w\s]+)\t # Job and company
#    (@[\w\d]+) # Twitter
#''', data, re.X))

# ^ and $ mark beginning and end of string, re.MULTILINE to treat end of line as end of string
# used ? to mark phone num and twitter optional
# had to mark tab after job optional (if no twitter, no tab after job)
#print(re.findall(r'''
#    ^([-\w ]*,\s[-\w ]+)\t # Last and first names
#    ([-\w\d.+]+@[-\w\d.]+)\t # Email
#    (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
#    ([\w\s]+,\s[\w\s.]+)\t? # Job and company
#    (@[\w\d]+)?$ # Twitter
#''', data, re.X|re.MULTILINE))

# Name our groups with above code, using ?P<name>
# Store as variable 'line' so we can create a dictionary
line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', data, re.X|re.MULTILINE)
print(line)
print(line.groupdict())