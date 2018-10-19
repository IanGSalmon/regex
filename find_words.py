#Create a function named find_words that takes a count and a string.
#Return a list of all the words in the string that are count chars or longer.
#Have to concatenate count into the regex, need it's VALUE

def find_words(count, str1):
    return re.findall(r'\w{' + str(count) + ',}' , str1)