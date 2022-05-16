import Calender
import Holiday



def main():
 prompt_response=input("Want to check if you have to go to work today?: ")
 if (prompt_response=="Yes"):
   Bapi=Calender.calenderApi()
   result=Bapi.get()
   calender_result=str(result)
   Hapi=Holiday.holidayApi()
   result_2=Hapi.get()
   holiday_result=str(result_2)
   if "weekday" in calender_result:
     print("Today's a weekday, gotta go to work unless there's some holiday.")
     if "0" in holiday_result:
       print("Damn! No holidays today.")
     if "1" in holiday_result:
       print("Holiday today, Woohoo!")
   if "weekend" in calender_result:
     print("Todays a weekend, no work!")


main()