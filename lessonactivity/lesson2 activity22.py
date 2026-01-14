file= open("lessonactivity\Codingal.txt", "r")
counter= 0
content= file.read()
CoList= content.split("\n")
for i in CoList:
    if i:
        counter += 1
print("TThis is the number of lines in the file")
print(counter)