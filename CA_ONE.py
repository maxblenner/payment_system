#Create a class Employee, and create and test a function to compute net pay from payment, work and tax credit information.

class Employee(object):

    #variables needed are: accNo, name, standard rate, overtime rate, tax credit, standard band
    def __init__(self, accNo, name, stdRate, overRate, stdCut, taxCredit, stdBand) -> None:
        self.__accNo = accNo
        self.__name = name
        self.__stdRate = stdRate
        self.__overRate = overRate
        self.__stdCut = stdCut #the point (hour) at which overtime pay kicks in
        self.__taxCredit = taxCredit
        self.__stdBand = stdBand
    
    def computePayment(self,hours):
        if hours <= self.__stdCut: #if the employee did not work enough hours for overtime payment
            #separating standard and overtime hours 
            stdHours = hours
            overHours = 0
            
        elif hours > self.__stdCut: #if the employeed worked enough hours for overtime pay
            #separating standard and overtime hours
            stdHours = self.__stdCut
            overHours = hours - self.__stdCut

        #calculating standard and overtime pay individually
        stdPay = stdHours * self.__stdRate
        if overHours == 0: #if there are no overtime hours to calculate, avoid multiplication of 0
            overPay = 0
        elif overHours > 0:
            overPay = overHours * self.__overRate

        #print statements to ensure payment calcuations are working as intended
        print("Standard hours worked: ", stdHours)
        print("Standard pay: ", stdPay)
        print("Overtime hours worked: ", overHours)
        print("Overtime pay: ", overPay) 

e1 = Employee(12110,'John Greene', 15.45, 18.25, 35, 60.50, 700)

e1.computePayment(35)

