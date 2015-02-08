from __future__ import division
import praw
import collections

username = raw_input("Input your username: ")

r = praw.Reddit("Comment Sorting for individual user")
Redditor = r.get_redditor(username)

# text

allcomments = Redditor.get_comments(limit=None)

# creat a textfile in the working directory named comments.txt
# the 'w' option will truncate the file
name = "comments.txt"
textfile = open(name, 'w')


# iterate through all all words in the comments pulled from reddit
# turn each word into a string, write the contents to the textfile
for word in allcomments:
    word1 = word.body
    word2 = word1.encode('utf-8') # https://docs.python.org/2/howto/unicode.html
    word3 = word2.lower() # change all words to lowercase
    chars_removed = word3.translate(None, '",(.!?)') # remove characters in string
    textfile.write(chars_removed) # write to textfile


# formerly    textfile.write(word.body.encode('utf-8').lower())


# close textfile and open in read only mode
textfile.close()
toread = open(name, 'r')

# split strings into separate words,
words = toread.read().split()

textfile.close()

list = []

counter = collections.Counter(words) # counts number of times each word is used
five_most_common = (counter.most_common(5)) # displays top 5 most used words

for thing in words:
    list.append(thing)

topwords = collections.Counter(list)
top5 = counter.most_common(5)

top5list = []

for item in top5:
    top5list.append(item)

first_word = top5list[0]
second_word = top5list[1]
third_word = top5list[2]
fourth_word = top5list[3]
fifth_word = top5list[4]

# top5list[0][0]

total_word_count = len(list)

percent_word1 = int(first_word[1]) / float(int(total_word_count)) * 100
rounded_percent_word1 = round(percent_word1, 4)

first_word_string = str(first_word[0])

# print first_word[0], first_word[1]
# print total_word_count
# print first_word[0], rounded_percent_word1

print "The most used word for /u/%s is '%s'. It was used %s percent of the time." \
      " There were %s total words in the sample." % \
      (username, first_word_string, rounded_percent_word1, total_word_count)