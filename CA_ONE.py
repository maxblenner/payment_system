#GitHub Link: https://github.com/maxblenner/payment_system

#Advanced Programming Techniques CA ONE
#Max Blennerhassett 10342271


#Create a class Employee, and create and test a function to compute net pay from payment, work and tax credit information.

#The steps taken were:
#Creating the class, 
#Testing that an object could be made,
#Made the payment calucations and used print statements to check if everything was working
#Cleaned everything up and created a dictionary output. 
#Created test method and test cases
#Final bug fixes
#Finished

import unittest

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
    
    def computePayment(self,hours,date):

        if hours > 0 and hours < 85: #checking that sufficient hours are entered, for no hours and 85 (84 is 12 hours a day for 7 days)
            
            #assertions made before calculations are processed
            myDict = {}
            overRate = self.__hourlyRate * self.__OTMulti
            stdTax = 0.20
            highTax = 0.40
            PRSI = 0.04

            if hours <= self.__regHours: #if the employee did not work enough hours for overtime payment
                #separating standard and overtime hours 
                regHours = hours
                overHours = 0
                
            elif hours > self.__regHours: #if the employeed worked enough hours for overtime pay
                #separating standard and overtime hours
                regHours = self.__regHours
                overHours = hours - self.__regHours

            #calculating standard and overtime pay individually
            regPay = regHours * self.__hourlyRate
            if overHours == 0: #if there are no overtime hours to calculate, avoid multiplication of 0
                overPay = 0
            elif overHours > 0:
                overPay = overHours * overRate
            
            grossPay = regPay + overPay #pay before tax calculations

            if grossPay > self.__stdBand: #if a higher tax rate needs to be accounted for
                stdPayTaxable = self.__stdBand
                stdTaxCharge = stdPayTaxable * stdTax
                highPayTaxable = grossPay - self.__stdBand
                highTaxCharge = (highPayTaxable) * highTax
                
            elif grossPay <= self.__stdBand: #if a higher tax rate does not need to be accounted for
                stdPayTaxable = grossPay
                stdTaxCharge = stdPayTaxable * stdTax
                highPayTaxable = 0 #for book-keeping reasons
                highTaxCharge = 0 #for book-keeping reasons
            
            taxAdded = stdTaxCharge + highTaxCharge
            PRSICharge = grossPay * PRSI #calculated separately as it is not subject to tax credit

            if self.__taxCredit > 0: #if the employee has any tax credit
                if self.__taxCredit > taxAdded: #an if statement to avoid negative taxes
                    taxCredit = self.__taxCredit #for book-keeping
                    self.__taxCredit = self.__taxCredit - taxAdded #reducing tax credit based on how much was used
                    netTax = 0
                elif self.__taxCredit <= taxAdded: #if tax credit is less than the tax charge
                    netTax = taxAdded - self.__taxCredit
                    taxCredit = self.__taxCredit #for book-keeping
                    self.__taxCredit = 0 #reducing tax credit based on how much was used
            
            netDeduct = netTax + PRSICharge #taxes to be paid

            netPay = grossPay - netDeduct

            name = self.__lName + ' ' + self.__fName

            myDict = {
                'Name' : name,
                'Date' : date,
                'Regular Hours Worked' : regHours,
                'Overtime Hours Worked' : overHours,
                'Regular Rate' : self.__hourlyRate,
                'Overtime Rate' : overRate,
                'Regular Pay' : regPay,
                'Overtime Pay' : overPay,
                'Gross Pay' : grossPay,
                'Standard Rate Pay' : stdPayTaxable,
                'Higher Rate Pay' : highPayTaxable,
                'Standard Tax' : stdTaxCharge,
                'Higher Tax' : highPayTaxable,
                'Total Tax' : taxAdded,
                'Tax Credit' : taxCredit,
                'Net Tax' : netTax,
                'PRSI' : PRSICharge,
                'Net Deductions' : netDeduct,
                'Net Pay' : netPay
            }

            return(myDict)

        else:
            raise ValueError("Insufficent hours entered")

e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700)

print(e1.computePayment(40,'09/04/22'))    

class testEmployee(unittest.TestCase):

    def testNetLessEqualGross(self): #Net pay cannot exceed gross pay
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700)
        pi=e1.computePayment(1,'09/04/22')
        self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])

    def testOverPayNegative(self): #Overtime pay cannot be negative
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700)
        pi=e1.computePayment(1,'09/04/22')
        self.assertGreaterEqual(pi['Overtime Pay'],0)
        
    def testOverHoursNegative(self): #Overtime hours cannot be negative
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700)
        pi=e1.computePayment(1,'09/04/22')
        self.assertGreaterEqual(pi['Overtime Hours Worked'],0)
    
    def testRegHoursLessHoursWorked(self): #Hours worked cannot be less than regular hours worked
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700)
        pi=e1.computePayment(35,'09/04/22')
        self.assertLessEqual(pi['Regular Hours Worked'],35) #checking if regular hours worked is <= 35 which is the total hours worked

    def testHighTaxNegative(self): #High tax cannot be negative
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 200, 700) #200 Euro Tax credit
        pi=e1.computePayment(1, '09/04/22')
        self.assertGreaterEqual(pi['Higher Tax'], 0)

    def testNetPayNegative(self): #Net pay cannot be negative
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700)
        pi=e1.computePayment(1,'09/04/22')
        self.assertGreaterEqual(pi['Net Pay'],0)

    def testStdTaxNegative(self): #Standard tax cannot be negative
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 200, 700) #200 Euro Tax credit
        pi=e1.computePayment(1, '09/04/22')
        self.assertGreaterEqual(pi['Standard Tax'], 0)

    def testNegHoursWorked(self): #Hours worked cannot be negative
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700) #200 Euro Tax credit
        with self.assertRaises(ValueError):
            e1.computePayment(-1, '09/04/22') #negative amount of hours worked tested

    def testTooManyHoursWorked(self): #Hours worked cannot exceed 84
        e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700) #200 Euro Tax credit
        with self.assertRaises(ValueError):
            e1.computePayment(85, '09/04/22') #negative amount of hours worked tested
    
    
unittest.main(argv=['ignored'],exit=False)



