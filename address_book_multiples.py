import re

names_file = open("names.txt", encoding='utf-8')
data = names_file.read()
names_file.close()

last_name = r'Love'
first_name = r'Kenneth'
#print(re.match(last_name, data))
#print(re.search(first_name, data))
#print(re.search(r'\(\d\d\d) \d\d\d-\d\d\d\d', data))
#print(re.search(r'\(\d{3}\) \d{3}-\d{4}', data))

# question mark after paranthesis means optional
#print(re.search(r'\(?\d{3}\)? \d{3}-\d{4}', data))

# findall phone numbers, will move through the whole string and find all places where it doesn't overlap
#print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}', data))

#findall phone numbers, optional hyphen and optional space (\s)
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

#character at least once (+)
#print(re.search(r'\w+, \w+', data))

#find zero or an infinite number of times (*)
print(re.findall(r'\w*, \w+', data))