
file=open("libro.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print "-------------------"
print "Palabra \t Contador"
print "-------------------"

for k,v in sorted(wordcount.items()):
    print "{0} \t {1}".format(k,v)
