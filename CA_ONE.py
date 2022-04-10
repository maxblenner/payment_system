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
    
    def computePayment(self,hours,date):

        print("Tax Credit: ",self.__taxCredit)

        #assertions made before calculations are processed
        myDict = {}
        overRate = self.__hourlyRate * self.__OTMulti
        stdTax = 0.20
        highTax = 0.40
        PRSI = 0.04

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
        
        grossPay = stdPay + overPay #pay before tax calculations

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
        
        totalTax = netTax + PRSI #taxes to be paid

        netPay = grossPay - totalTax

        name = self.__fName + self.__lName

        myDict = {
            'Name' : name,
            'Date' : date,
            'Regular Hours Worked' : stdHours,
            'Overtime Hours Worked' : overHours,
            'Regular Rate' : self.__hourlyRate,
            'Overtime Rate' : overRate,
            'Regular Pay' : stdPay,
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
            'Net Deductions' : totalTax,
            'Net Pay' : netPay
        }

        print(myDict)

        #print statements to ensure payment calcuations are working as intended
        print("Standard hours worked: ", stdHours)
        print("Standard pay: ", stdPay)
        print("Overtime hours worked: ", overHours)
        print("Overtime pay: ", overPay) 
        print("Gross pay: ", grossPay)
        print("PRSI: ", PRSICharge)
        print("Standard Tax: ", stdTaxCharge)
        print("Higher Tax: ", highTaxCharge)
        print("Taxes added: ", taxAdded)
        print("Tax charge (after tax credit): ", netTax)
        print("Total taxes to be paid: ", totalTax)
        print("Net pay: ", netPay)

e1 = Employee(12110,'Green', 'Joe', 35, 18.45, 1.5, 60.50, 700)

e1.computePayment(40,'09/04/22')

