import calendar
y=int(input("enter year"))
m=1
print("\n calender of year",y,'\n')

Cal=calendar.TextCalendar(calendar.MONDAY)
#here monday is guven so that the calender starts from monday
i=1
while i<=12:
    Cal.prmonth(y,i)
    i+=1
    #prmonth is function to print yr and month
