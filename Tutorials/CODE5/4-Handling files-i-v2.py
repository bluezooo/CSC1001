def main():
    filename=input("Enter a filename:")
    numOfCh=0
    numOfWord=0
    numOfLine=0

    file=open(filename,'r')
    for line in file.readlines():
        numOfCh+=len(line)
        numOfWord+=len(line.split())
        numOfLine+=1
    file.close()

    print("In the file %s, there are"%filename)
    print(numOfCh,"characters,")
    print(numOfWord,"words,")
    print(numOfLine,"lines.")

main()
