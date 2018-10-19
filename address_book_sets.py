import re

names_file = open("names.txt", encoding='utf-8')
data = names_file.read()
names_file.close()

last_name = r'Love'
first_name = r'Kenneth'

#findall email addresses(NOT ALWAYS EMAIL SOLUTION, consult stack overflow)
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

#if email ends in .gov, and we want to leave it out
#print(re.findall(r'''
#    \b@[-\w\d.]* #Find a word boundary, an @, and then any num or chars
#    [^gov\t]+ #Ignore 1+ instances of letters 'g' 'o' or 'v' and a TAB ('t)
#    \b  #Match another word boundary
#''', data, re.VERBOSE|re.I))

# Find names and where they work
print(re.findall(r"""
    \b[-\w]*, # Find a word boundary, 1+ hyphens or chars, and a comma
    \s # Find 1 whitespace
    [-\w]+ # 1+ hyphens and chars and explicit spaces
    [^\t\n] # Ignore tabs and newlines
""", data, re.X))

#all instances of the word 'treehouse', IGNORECASE flag, can also use re.I
#print(re.findall(r'\b[trehous]+\b', data, re.IGNORECASE))

#all instances of the word 'treehouse',, EXACTLY 9 CHARS, IGNORECASE flag, can also use re.I
#print(re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))
