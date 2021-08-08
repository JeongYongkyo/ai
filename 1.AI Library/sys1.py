import sys
print(sys.argv)
#['sys1.py', 'new.txt', 'new2.txt']
#[파일명, param1, param2]

source = sys.argv[1]
target = sys.argv[2]

fr = open(source,"r")
fw = open(target,"w")

for line in fr:
    fw.write(line)
    
fr.close()
fw.close()