def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    word = sorted(words) #could have been one command
    return word

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    sorted_words = sorted(words)    # can this be 1 line of code?
    return sorted_words             #Yes, return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    first_word = print_first_word(words)
    last_word = print_last_word(words)
    return first_word      #can you return both in one line?
    return last_word        #Yes, noted above

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    first_word = print_first_word(words)
    last_word = print_last_word(words)
    return first_word
    return last_word
# Above successfully debugged first try 3/29
# noted that I made it very redundant with the return statements

print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

# I see no issues with poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (jelly_beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We\'d have %d beans, %d jars, and %d crates." % secret_formula(start_point)


sentence = "All good things come to those who wait."

# shouldn't these be coommands typed into the terminal
# while running python?
words = ex26.break_words(sentence)
sorted_words = ex26.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex26.sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
