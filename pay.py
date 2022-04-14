#payscale calculator with out use of try/except block
#official regural work hours are 200/month and for excess hours your are gonna pay one and half times the regular pay
#promt for input from user for number of hours and pay rate for hours
str_reg_hrs=input("number of regular working hrs per month: ")
str_hrs=input("number of hours worked: ")
str_reg_rate=input("pay rate for reg hour:")
str_or_rate=input("pay rate for over hours: ")

 #convert this strings into float for math calculations
flt_reg_hrs=float(str_reg_hrs)
flt_hrs=float(str_hrs)
flt_reg_rate=float(str_reg_rate)
flt_or_rate=float(str_or_rate)
#
if flt_hrs >flt_reg_hrs:
    #for excess work hours
    print("Overtime;")
    pay_rg=flt_reg_hrs*flt_reg_rate
    pay_or=(flt_hrs-flt_reg_hrs)*flt_or_rate
    print("pay:", pay_rg+pay_or)
else:
    #for regular hours
    print("regular;")
    pay=flt_hrs*flt_reg_rate
    print("pay:", pay)
