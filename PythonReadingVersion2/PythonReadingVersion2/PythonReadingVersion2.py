#cookToCode
#Written for my final project in beginner python
import csv

##IF YOU DIDNT CHANGE THE TXT FILE DESTINATION ON LINE 69 (lol) THEN IT WONT WORK

#------------Variable Dictionary---------------
numRec=0        #Holds the value of the amount of students on the file
name=[]         #List holds the value of the student's name
test1=[]        #List holds the value of test 1
test2=[]        #List holds the value of test 2
test3=[]        #List holds the value of test 3
test4=[]        #List holds the value of test 4
test5=[]        #List holds the value of test 5
testAvg=[]      #List holds the avg of the first 4 tests
classAvg=0      #Holds the value of the total avg of the whole class
testTotal=0     #Holds the total of test1-5 added up
option=[]       #Holds the options for the menu function
choice=0        #Holds the value of the option chosen from the menu function
again='y'       #Holds the value for the user wanting to search again
found=-1        #For the binary search to see if the student was found
#------------Functions-------------------------
def menu():
    option=['Search by Name','Search by Average Grade','Exit']
    print('\t\t  Menu\n')
    print(f'1) {option[0]:20} 2) {option[1]}\n3) {option[2]}')
    choice=input('(1-3) : ')
    while choice!='1' and choice!='2' and choice!='3':
        choice=input('Please only choose 1, 2, or 3 : ')
    return choice

def bubble(n, j): #n= the name of the array  j= the index value in the array
    t=n[j]
    n[j]=n[j+1]
    n[j+1]=t

def bSearch(x, L): #L=list searching in x=What you are searching for
    found=-1        #This being here is awesome because each search is then reset
    if x in L:
        start=0
        last=int(len(L)-1)
        guess=int((start+last)/2)
        while start<last and x!=L[guess]:
        
            if x<L[guess]:
                last=guess-1
            else:
                start=guess+1
            guess=int((start+last)/2)
        if x==L[guess]:
            found=guess
    #else:
        #print('**Error**Search Never Started')
    return found

def searchAgain():
    print('Would you like to search again?')
    answer=input('(y/n) : ')
    while answer!= 'y' and answer!='n': #Lets the user ONLY input 'y' or 'n'
        answer=input('Please only type "y" for yes or "n" for no : ')
    return answer

def goodbye():
    print('\n\n\nThank you for searching!\nGOODBYE')
    return 
#------------Program Begins--------------------

#-----file------
with open("G:\\Folder\\final.txt") as csvfile: ##You have to change this to your txt file destination
    file=csv.reader(csvfile)
    for rec in file:
        numRec+=1
        name.append(rec[0])
        test1.append(int(rec[1]))
        test2.append(int(rec[2]))
        test3.append(int(rec[3]))
        test4.append(int(rec[4]))
        test5.append(int(rec[5]))

#----/file-----        
for i in range(numRec):#This for loop sets the test averages and saves them to a list
    testTotal=test1[i]+test2[i]+test3[i]+test4[i]+test5[i]
    testTotal=testTotal/5
    classAvg+=testTotal
    testAvg.append(testTotal)
classAvg=classAvg/12

while again=='y':
    for i in range(numRec):
        print(f'{name[i]:15} {test1[i]:4} {test2[i]:4} {test3[i]:4} {test4[i]:4} {test5[i]:4}\tAvg: {testAvg[i]}')
    print(f'\n{numRec} students in the class. Class average: {classAvg:.1f}')
    print('\n\n\n')
    choice=menu()
    print()
    if choice=='1':
        for i in range(len(name)-1):       #Bubble sort before the search
            for k in range(len(name)-1):
                if name[k]>name[k+1]:
                    bubble(name, k)
                    bubble(test1, k)
                    bubble(test2, k)
                    bubble(test3, k)
                    bubble(test4, k)
                    bubble(test5, k)
                    bubble(testAvg, k)
                    
        print('Please type the name you are looking for')
        userName=input(': ')
        found=bSearch(userName, name)
        if found>-1:#----------------SEARCH BY NAME
            print(f'\n{name[found]:15} {test1[found]:4} {test2[found]:4} {test3[found]:4} {test4[found]:4} {test5[found]:4}\tAvg: {testAvg[found]}\n')
        else:
            print('\nName not found -- Please check spelling')
    elif choice=='2':#---------------SEARCH BY GRADE
        print('Please type the letter grade you are looking for')
        userGrade=input('(A-F) : ')
        while userGrade!='A' and userGrade!='B' and userGrade!='C' and userGrade!='D' and userGrade!='F':
            userGrade=input('Please just choose ("A", "B", "C", "D", or "F") : ')
        if userGrade=='A':
            for i in range(numRec):
                if testAvg[i]>=90:
                    print(f'{name[i]:15} {test1[i]:4} {test2[i]:4} {test3[i]:4} {test4[i]:4} {test5[i]:4}\tAvg: {testAvg[i]}')
        elif userGrade=='B':
            for i in range(numRec):
                if testAvg[i]<90 and testAvg[i]>=80:
                    print(f'{name[i]:15} {test1[i]:4} {test2[i]:4} {test3[i]:4} {test4[i]:4} {test5[i]:4}\tAvg: {testAvg[i]}')
        elif userGrade=='C':
            for i in range(numRec):
                if testAvg[i]<80 and testAvg[i]>=70:
                    print(f'{name[i]:15} {test1[i]:4} {test2[i]:4} {test3[i]:4} {test4[i]:4} {test5[i]:4}\tAvg: {testAvg[i]}')
        elif userGrade=='D':
            for i in range(numRec):
                if testAvg[i]<70 and testAvg[i]>=60:
                    print(f'{name[i]:15} {test1[i]:4} {test2[i]:4} {test3[i]:4} {test4[i]:4} {test5[i]:4}\tAvg: {testAvg[i]}')
        elif userGrade=='F':
            for i in range(numRec):
                if testAvg[i]<60:
                    print(f'{name[i]:15} {test1[i]:4} {test2[i]:4} {test3[i]:4} {test4[i]:4} {test5[i]:4}\tAvg: {testAvg[i]}')
        print()
    else:
        goodbye()
        break
    again=searchAgain()
    print('\n\n\n')
