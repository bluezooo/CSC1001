import random

words={}
file=open("Dictionary.txt",'r')
for line in file.readlines():
    word=line.split(':')
##  strip can remove the new line symbol, see python document
    words[word[1].strip()]=word[0].strip()
file.close()

k=list(words.keys())
total=len(k)

correct_count=0
go_on = True
while k and go_on: #bool([])->False
    i=random.randint(0,len(k)-1)
##  Print how many words you have guessed, including the current
    print('(%d/%d)'%(total-len(k)+1,total),k[i])
    answer=input('Please guess the word:')
    if answer==words[k[i]]:
        print("√√√\nYour answer is correct!\n")
        correct_count+=1
    else:
        print("×××\nThe correct answer should be \"%s\".\n"%words[k[i]])
##  Romove the word that you have just guessed
    k.remove(k[i])
    go_on = eval(input('go on?(0/1):'))

print('Finished!You have correctly guess %d out of %d words!'%(correct_count,total))

