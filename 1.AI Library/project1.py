import os
import sys

def start():
    fr = open(source,"r")
    tempDic = dict()
    
    for line in fr:
        sList = line.split()
        id, name = sList[0],sList[1]+' '+sList[2]
        mid, final = list(map(int, sList[3:]))
        tempDic[id] = list(calculate(id, name, mid, final))
     
    stuDic = dict(sorted(tempDic.items(), key= lambda x : x[1][3], reverse = True))
    printlist(stuDic)
    return stuDic
    fr.close()

def calculate(id, name, mid, final):
    avg = round((mid+final)/2,1)
    if avg >= 90:
        grade = 'A'
    elif avg >= 80 and avg < 90:
        grade = 'B'
    elif avg >= 70 and avg < 80:
        grade = 'C'
    elif avg >= 60 and avg < 70:
        grade = 'D'
    else:
        grade = 'F'
    return name, mid, final, avg, grade

def printlist(stuDic):
    stuDic = dict(sorted(stuDic.items(), key= lambda x : x[1][3], reverse = True))
    strFormat = '%12s%15s%12s%12s%12s%10s'
    strOut = strFormat % ('Student','Name','Midterm','Final','Average','Grade')
    print(strOut)
    print("  -------------------------------------------------------------------------  ")
    for k, v in stuDic.items():
        print("%12s%15s%10s%12s%12s%10s" %(k,v[0],v[1],v[2],v[3], v[4]))
    print("")

def show(stuDic):
    printlist(stuDic)
    
def search(stuDic):
    stu_id = input("Student Id: ")
    if stu_id in stuDic:
        printlist({stu_id:stuDic[stu_id]})
    elif stu_id == "-1":
        print("Moved back.\n")
    else:
        print("NO SUCH PERSON. – Please try again(If you want to back. please typing \"-1\")\n")
        search(stuDic)

def changescore(stuDic):
    stu_id = input("Student Id: ")
    if stu_id in stuDic:
        midfinal = input("Mid/Final? ").lower()
        if midfinal == "mid":
            midScore = int(input("Input new score: "))
            if midScore < 0 or midScore > 100:
                print("Value is out of range(0~100)\n")
            else:
                printlist({stu_id:stuDic[stu_id]})
                stuDic[stu_id] = list(calculate(stu_id,stuDic[stu_id][0],midScore,stuDic[stu_id][2]))
                print("Score changed\n")
                printlist({stu_id:stuDic[stu_id]})
        elif midfinal == "final":
            finalScore = int(input("Input new score: "))
            if finalScore < 0 or finalScore > 100:
                print("Value is out of range(0~100)\n")
            else:
                printlist({stu_id:stuDic[stu_id]})
                stuDic[stu_id] = list(calculate(stu_id,stuDic[stu_id][0],stuDic[stu_id][1],finalScore))
                printlist({stu_id:stuDic[stu_id]})
                print("Score changed\n")
        else:
            print("Your answer was incorrect – Please try again\n")
    elif stu_id == "-1":
        print("Moved back.\n")
    else:
        print("NO SUCH PERSON. – Please try again(If you want to back. please typing \"-1\")\n")
        changescore(stuDic)

def add(stuDic):
    new_id = input("Student Id: ")
    if new_id in stuDic:
        print("ALREADY EXISTS. – Please try again(If you want to back. please typing \"-1\")\n")
        add(stuDic)
    elif new_id == "-1":
        print("Moved back.\n") 
    else:
        new_name = input("Name: ")
        new_mid = int(input("Midterm Score: "))
        new_final = int(input("Final Score: "))
        
        stuDic[new_id] = list(calculate(new_id, new_name, new_mid, new_final))
        print("Student added.\n")

def searchgrade(stuDic):
    grade_list = ["A","B","C","D","F","-1"]
    tempDic = dict()
    stu_grade = input("Grade to search: ").upper()
    if stu_grade not in grade_list:
        print("A/B/C/D/F 중 입력바랍니다.(If you want to back. please typing \"-1\")\n")
        searchgrade(stuDic)
    else:
        for k, v in stuDic.items():
            if v[4] == stu_grade:
                tempDic[k]=v
        if tempDic == {}:
            if stu_grade == "-1":
                print("Moved back.\n")
            else:
                print("NO RESULTS.\n")
        else:
            printlist(tempDic)

def remove(stuDic):
    if stuDic == {}:
        print("List is empty.\n")
    else:
        stu_id = input("Student Id: ")
        if stu_id in stuDic:
            del stuDic[stu_id]
            print("Student removed.\n")
        elif stu_id == "-1":
            print("Moved back.\n") 
        else:
            print("NO SUCH PERSON. – Please try again(If you want to back. please typing \"-1\")\n")
            remove(stuDic)
    
def quit(stuDic):
    quityn = input("Save data?[yes/no] ").lower()
    if quityn == "yes":
        filename = input("File name: ")
        fw = open(filename, "w")
        strFormat = '%12s%15s%12s%12s%12s%10s'
        strOut = strFormat % ('Student','Name','Midterm','Final','Average','Grade\n')
        fw.write(strOut)
        fw.write("  -------------------------------------------------------------------------  \n")
        stuDic = dict(sorted(stuDic.items(), key= lambda x : x[1][3], reverse = True))
        for k, v in stuDic.items():
            fw.write("%12s%15s%10s%12s%12s%10s\n" %(k,v[0],v[1],v[2],v[3], v[4]))
        fw.write("\n")
        fw.close()
    elif quityn == "no":
        pass
    else:
        quit(stuDic)
    
def main():
    stuDic = start()
    
    while True:
        command = input("#").lower()
        if command == "show":
            show(stuDic)
        elif command == "search":
            search(stuDic)
        elif command == "changescore":
            changescore(stuDic)
        elif command == "add":
            add(stuDic)
        elif command == "searchgrade":
            searchgrade(stuDic)
        elif command == "remove":
            remove(stuDic)
        elif command == "quit":
            quit(stuDic)
            break
        else:
            print("Your answer was incorrect – Please choose from the following\n- show, search, changescore, searchgrade, add, remove, quit\n")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        source = "students.txt"
    else:
        source = sys.argv[1]
        
    if os.path.exists(source):
        main()
    else:
        print(source,"file does not exists\n")