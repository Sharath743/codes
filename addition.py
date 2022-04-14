#for adding numbers given by users
num=0
sum=0
#infinte loop for continuously asking user for input
while True:
    #literally promts for user input
    s_put=input("enter number and done at the end:")
    #to break infinite loop when user is done with input
    if s_put=="done":
        #word break literally breaks the loop and goes for next block of code
        break
    else:
        #try is used where the code block might go wrong due to unknown or undesired in put values
        #here if user provides input other than numbers it cannot be converted into float. so,try this if anything goes wrong use expect
        try:
            f_put=float(s_put)
        except:
            print("""invalid input:
            enter number"or"done""")
            #continue stops current iteration and goes to next iteration 
            continue
        num=num+1
        sum=sum+f_put
print("num:",num,"sum:",sum, "avg:",sum/num)
