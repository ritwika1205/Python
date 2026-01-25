outputfile= open('UpdatedFile.txt', "w")
input= open('lessonactivity\sample_doc (1).txt', "r")
lines_seen_so_far= set()
print("Eliminating duplicate lines")
for line in input:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)
input.close()
outputfile.close()

    
    