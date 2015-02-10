from __future__ import division
import praw
import collections
import pylab as plt

username = raw_input("Input your username: ")

r = praw.Reddit("Comment Sorting for individual user")
Redditor = r.get_redditor(username)

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

list1 = []

counter = collections.Counter(words) # counts number of times each word is used
five_most_common = (counter.most_common(5)) # displays top 5 most used words

# adds all words to list1 so that they can be counted below by collections.Counter(list1)
for thing in words:
    list1.append(thing)

# counts number of times each word is used, format is
# topwords = [('cat' 1), ('dog' 5)] where topwords[0] = ('cat' 10)
# and topwords[0][0] = 'cat' etc...

topwords = collections.Counter(list1)
top5 = counter.most_common(5)

# we want to graph the top 15 items, this creates a list in the same
# form as above, list = [('item' 4]
items_to_plot = counter.most_common(15) # grabs top 15 words used and the number they were used

# this list and related lines below are not really being used. However,
# it is just
top5list = []

for item in top5:
    top5list.append(item)

first_word = top5list[0]
second_word = top5list[1]
third_word = top5list[2]
fourth_word = top5list[3]
fifth_word = top5list[4]


total_word_count = len(list1)

percent_word1 = int(first_word[1]) / float(int(total_word_count)) * 100
rounded_percent_word1 = round(percent_word1, 4)

first_word_string = str(first_word[0])

top15words = []                 # list of strings
top15words_number_occur = []    # list of number of each string's occurrence in entire comments history

for item in items_to_plot:                      # these lines create separate lists for each variable
    top15words.append(item[0])                  # that is graphed. The first for loop is creating a list using
for item in items_to_plot:                      # only the first position from the items_to_plot list (the strings)
    top15words_number_occur.append(item[1])     # The second loop is doing the same, but with the second position
                                                # of each item (the integer). It is basically splitting the tuple into
thisisx = []                                    # two separate lists
x_for_thisisx = 0
y_for_thisisx = 1

while x_for_thisisx < len(top15words):          # this is creating the x-axis for the bottom of the graph. It should
    thisisx.append(y_for_thisisx)               # create one that is equal to the number of items that are to be graphed
    y_for_thisisx += 1                          # that is the reason for the condition x_for_thisisx < len(top15words)
    x_for_thisisx += 1

plt.bar(thisisx, top15words_number_occur, align='center')
plt.xticks(thisisx, top15words)
plt.show()

# print items_to_plot[0], items_to_plot[1], items_to_plot[2]

print "The most used word for /u/%s is '%s'. It was used %s percent of the time." \
      " There were %s total words in the sample." % \
      (username, first_word_string, rounded_percent_word1, total_word_count)