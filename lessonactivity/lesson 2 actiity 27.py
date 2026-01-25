file= open('New Document1.txt', 'x')
import os
print("checking if my_file exists or not")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")
my_file= open("my_file.txt", "w")
my_file.write("Hi! am a penguin and am 3 years old")
my_file.close()
os.remove('lessonactivity\Codingal.txt')
os.rmdir('Folder')