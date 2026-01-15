file1= open('lessonactivity\Codingal.txt', 'r')
file2= open('lessonactivity\sample_doc (1).txt', 'w')
for line in file1.readlines():
    if not(line.startswith('coding')):
        print(line)
        file2.write(line)
file2.close()
file1.close()