#this is an assignment on regexp from py4e
#this program runs through a text file containing some numbers
#and extract those numbers and gives us the sum of such values

#impor regular expressions as we deal with regex while extracting required advantage
import re

#promt for input of file name
fname=input("enter file name: ")
#if we enter any single string it directly takes the sample file as input
#if len(fname)<1:
    #fname=("regex_sum.txt")
#a list for storing numbers
nums=list()
#opening file
handle=open(fname)
#looping through lines
#i.e, runs through every line at a time
for line in handle:
    #removes new line character at end of every line and stores in line var
    line=line.rstrip()
    #finds all from 0 to 9 without space in a line and stores as a list in n
    #since there may be more than one number so all numbers in line are stored in list
    n=re.findall('[0-9]+', line)
    #looping through list n for numbers
    for i in n:
        #for every number in n(list) converts it into a float and stores it in num var
        num=float(i)
        #and adds that num to nums(list)
        nums.append(num)
#outputs the sum of all numbers found in file as an integer
print(int(sum(nums)))

#for getting all numbers found in file
#count=0
#for i in nums:
#    count=count+1
#    print(count, i)
