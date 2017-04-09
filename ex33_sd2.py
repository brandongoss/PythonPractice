numbers = []

def numberfunc(counter, increment):
    i = 0

    for i in range(0, counter, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print numberfunc(6, 1)
print "The numbers: "

for num in numbers:
    print num

# where is 'none' output coming from ?
