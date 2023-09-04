'''
Program 1: Read Python.txt file and Print it in Reverse.
Program 2: Read Python.txt file and Print total number of lines and words in it.
Program 3: Read Python.txt file and Print unique word with its count.
Program 4: Read Python.txt file and Print largest and smallest word from it.
Program 5: Read Python.txt file. Convert it into upper case and write into another file "Python_Upper.txt"

Python.txt [Content]:-

Python is a popular general-purpose programming language.
It was created by Guido van Rossum, and released in 1991.
It is used in machine learning, web development, desktop applications, and many other fields.
Fortunately for beginners, Python has a simple, easy-to-use syntax.
This makes Python a great language to learn for beginners.
Why Learn Python?
Python is easy to learn. Its syntax is easy and code is very readable.
Python has a lot of applications. It's used for developing web applications, data science, rapid application development,and so on.
Python allows you to write programs in fewer lines of code than most of the programming languages.
The popularity of Python is growing rapidly. Now it's one of the most popular programming languages.'''
# Writing Content inside Python.txt
def writeFun():
    with open("D:\\pythonnote\\Python.txt","w") as file_writer:
        text_data=[['Python is a popular general-purpose programming language. \n'],
                   ['It was created by Guido van Rossum, and released in 1991. \n'],
                   ['It is used in machine learning, web development, desktop applications, and many other fields. \n'],
                   ['Fortunately for beginners, Python has a simple, easy-to-use syntax. \n'],
                   ['This makes Python a great language to learn for beginners. \n'],
                   ['Why Learn Python? \n'],
                   ['Python is easy to learn. Its syntax is easy and code is very readable. \n'],
                   ["Python has a lot of applications. It's used for developing web applications, data science, rapid application development, and so on. \n"],
                   ['Python allows you to write programs in fewer lines of code than most of the programming languages. \n'],
                   ["The popularity of Python is growing rapidly. Now it's one of the most popular programming languages. \n"]]
        for line in text_data:
            file_writer.writelines(line)     
    print("File Written Successfully")
# Reversing Lines from File
def reverseFun():
    with open("D:\\pythonnote\\Python.txt","r") as rev_data:
        lines=rev_data.readlines()
        reversed_line=lines[::-1]      #Negative Indexing to reverse list
        print("File Reversed: \n\n")
        for line in reversed_line:
            print(line)
# Printing Number of Lines and Words
def numberFun():
    wordList = []
    with open("D:\\pythonnote\\Python.txt", 'r') as reader_file:
        line_count=0
        for line in reader_file:
            line_count=line_count+1
            words = line.split()
            for word in words:
                word = word.strip('.,!?()[]{}":;')    # Remove punctuations
                word = word.lower()        #Converts to lowercase
                wordList.append(word)     #Appending in a list of words
        wordList=len(wordList) 
    print("Number of Lines: {}".format(line_count))
    print("Number of words: {}".format(wordList))
# Unique Word inside File
def UniqueFun():
    def getKey(minValue,wordDict):
        for key, value in wordDict.items():
            if minValue == value:
                return key
    wordDict = {}
    with open("D:\\pythonnote\\Python.txt", 'r') as reader_file:
        for line in reader_file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?()[]{}":;')    #Remove Punctuations
                word = word.lower()        #Converts to lowercase
                if word in wordDict:
                    wordDict[word] += 1     #If already exist in list, count gets incremented
                else:
                    wordDict[word] = 1      #If doesn't exist, gets added with counter 1
    unique_counter=min(wordDict.values())    #Taking smallest counter value
    unique_word=getKey(unique_counter,wordDict)    #Taking key of the counter
    print("Unique Word is '{}' with {}".format(unique_word,unique_counter))
# Smallest Word and Largest Word in File
def SmallandLargeFun():
    wordList = []
    with open("D:\\pythonnote\\Python.txt", 'r') as reader_file:
        for line in reader_file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?()[]{}":;')    #Remove Puntuations
                word = word.lower()       #Converts to lowercase
                if word not in wordList:
                    wordList.append(word)    #If doesn't exist, gets added
        smallest = min(wordList, key=len)    #Smallest word from list using len and min
        largest = max(wordList, key=len)     #Largest word from list using len and max
        print("The smallest word is: {}".format(smallest))
        print("The largest word is: {}".format(largest))
# Converts text into Uppercase and Saves it into Python_Upper.txt
def UpperFun():
    with open("D:\\pythonnote\\Python.txt", 'r') as reader_file:
        lines=[]
        for line in reader_file:
            lines.append(line.upper())   #Appending lines into uppercase format
    with open("D:\\pythonnote\\Python_Upper.txt", 'w') as write_file:
        for line in lines:
            write_file.writelines(line)
    print("File created and text added in Uppercase")
def operationFun():
    print("\n\n-----------------------------------------------------------------------\n")
    writeFun()    #Writing text into file
    print("\n\n-----------------------------------------------------------------------\n")
    reverseFun()    #1- Reversing lines
    print("\n\n-----------------------------------------------------------------------\n")
    numberFun()     #2- Number of Words and Lines
    print("\n\n-----------------------------------------------------------------------\n")
    UniqueFun()     #3- Unique word with counter
    print("\n\n-----------------------------------------------------------------------\n")
    SmallandLargeFun()     #4-Largest and Smallest Word
    print("\n\n-----------------------------------------------------------------------\n")
    UpperFun()      #5- Write it into uppercase in Python_Upper.txt
    print("\n\n-----------------------------------------------------------------------\n")
operationFun()      #All Operation inside Function

