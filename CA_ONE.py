#Create a class Employee, and create and test a function to compute net pay from payment, work and tax credit information.

class Employee(object):

    #variables needed are: self, staffID, fName, lName, regHours, hourlyRate, OTMulti, taxCredit, stdBand
    def __init__(self, staffID, fName, lName, regHours, hourlyRate, OTMulti, taxCredit, stdBand):
        self.__staffID = staffID
        self.__fName = fName
        self.__lName = lName
        self.__regHours = regHours #the point (hour) at which overtime pay kicks in
        self.__hourlyRate = hourlyRate
        self.__OTMulti = OTMulti #the multiple by which overtime pay is calculated 
        self.__taxCredit = taxCredit
        self.__stdBand = stdBand
    
    def computePayment(self,hours):

        overRate = self.__hourlyRate * self.__OTMulti

        if hours <= self.__regHours: #if the employee did not work enough hours for overtime payment
            #separating standard and overtime hours 
            stdHours = hours
            overHours = 0
            
        elif hours > self.__regHours: #if the employeed worked enough hours for overtime pay
            #separating standard and overtime hours
            stdHours = self.__regHours
            overHours = hours - self.__regHours

        #calculating standard and overtime pay individually
        stdPay = stdHours * self.__hourlyRate
        if overHours == 0: #if there are no overtime hours to calculate, avoid multiplication of 0
            overPay = 0
        elif overHours > 0:
            overPay = overHours * overRate

        #print statements to ensure payment calcuations are working as intended
        print("Standard hours worked: ", stdHours)
        print("Standard pay: ", stdPay)
        print("Overtime hours worked: ", overHours)
        print("Overtime pay: ", overPay) 

e1 = Employee(12110,'Green', 'Joe', 35, 15.45, 1.5, 60.50, 700)

e1.computePayment(37)

