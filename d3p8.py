
class Word(object):
	def __init__(self, string, index):
		self.string = string
		self.index = index



try:
    def createDupArray(string, size):
        dupArray = []

        for i in range(size):
            dupArray.append(Word(string[i], i))

        return dupArray


    def printAnagramsTogether(wordArr, size):
        dupArray = createDupArray(wordArr, size)

        for i in range(size):
            dupArray[i].string = ''.join(sorted(dupArray[i].string))

        dupArray = sorted(dupArray, key=lambda k: k.string)
        print("[",end=' ')
        for word in dupArray:
            print (wordArr[word.index],end=" ")
        print("]")
        print("")
except TabError:
    print(" ")



wordArr = []
ele=int(input("Enter the no. of elements: "))
print("Enter the values: ")
for i in range(0,ele):
    val=input()
    wordArr.append(val)
size = len(wordArr)
printAnagramsTogether(wordArr, size)

