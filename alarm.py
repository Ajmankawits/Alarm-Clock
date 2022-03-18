class Alarm:
    def __init__(self):
     self.time_current = "12:00pm"
     self.clock_on = True
     self.alarm_time = "8:00am"
    
    def current_time(self):
        print("The current time is", self.time_current)
    
    
    def set_time(self):
        self.time_current = input("Set time ")
        print("The time is now", self.time_current)
        pass
         

    def toggle_alarm(self):
        if self.clock_on == True:
            print("Your alarm clock is on would you like to turn it off? Enter: y/n ")
            clock_input = input("")
            if clock_input == "y":
                self.clock_on = False
                if self.clock_on == False:
                    print("Your alarm clock is now off. Would you like to turn it back on? Enter: y/n")
                    clock_input = input("")
                    if clock_input == "y":
                        self.clock_on = True
                        print("Your alarm clock is on")
                    else:
                      pass
    
    def set_alarm(self):
        self.alarm_time = input("Set alarm time ")
        print("Your alarm is now set to", self.alarm_time)

                
               

        
        
        
           
        




        
