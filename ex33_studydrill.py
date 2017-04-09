numbers = []

def numberfunc(counter, increment):
    i = 0

    while i < counter:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print numberfunc(6, 2)
print "The numbers: "

for num in numbers:
    print num

# How could I do this without having numbers = [] be global?
# When I run this, an unexpected 'none' prints in the ouput before the for-loop
