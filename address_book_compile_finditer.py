import re

names_file = open("names.txt", encoding='utf-8')
data = names_file.read()
names_file.close()

last_name = r'Love'
first_name = r'Kenneth'

# Name our groups with above code, using ?P<name>
# Store as variable 'line' so we can create a dictionary
#line = re.search(r'''
#    ^(?P<name>[-\w ]*,\s[-\w ]+)\t # Last and first names
#    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
#    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
#    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
#    (?P<twitter>@[\w\d]+)?$ # Twitter
#''', data, re.X|re.M)
#print(line)
#print(line.groupdict())

# Compile instead of search
# Took out 'data' bc we don't compile with what it will be run against
# Added last and first sub groups
line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X|re.M)
#print(re.search(line, data).groupdict())

# Can omit re, since 'line' is compiled
#print(line.search(data).groupdict())

# Using .group - show me whatever is inside the group, e.g. nothing, an index number, group name
#for match in line.finditer(data):
#    print(match.group('name'))

# Print, this time using sub groups
for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))