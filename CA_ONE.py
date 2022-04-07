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
            #separating standard and overtime hours for logging/book-keeping purposes
            stdHours = hours
            overHours = 0
            
            #calculating standard and overtime pay individually
            stdPay = hours * self.__stdRate
            overPay = 0
        
        elif hours > self.__stdCut: #if the employeed worked enough hours for overtime pay
            #separating standard and overtime hours for logging/book-keeping purposes
            stdHours = self.__stdCut
            overHours = hours - self.__stdCut

            
            #calculating standard and overtime pay individually
            stdPay = self.__stdCut * self.__stdRate
            overPay = (hours - self.__stdCut) * self.__overRate


