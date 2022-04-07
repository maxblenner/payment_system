CA_ONE Advanced Programming techniques, 
Spec given:

Create a class Employee, and create and test a function to compute net pay from payment, work and tax credit information.

Employee should have the following attributes:
StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand,

For Example:

jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)

Create a method computePayment in class Employee which takes HoursWorked and date as input, and returns a payment information dictionary as follows: (if jg is an Employee object for worker Joe Green)

We will assume a standard rate of 20% and a higher rate of 40%, and that PRSI at 4% is not subject to allowances. (we will ignore USC etc.)

>>>jg.computePayment(42, '31/10/2021')

{'name': 'Joe Green', 'Date':'31/10/2021', 'Regular Hours Worked':37,'Overtime Hours Worked':5,'Regular Rate':16,'Overtime Rate':24, 'Regular Pay':592,'Overtime Pay':120,'Gross Pay':712, 'Standard Rate Pay':710,'Higher Rate Pay':2, 'Standard Tax':142,'Higher Tax':0.8,'Total Tax':142.8,'Tax Credit':72, 'Net Tax':70.8, 'PRSI': 28.48,'Net Deductions':99.28, 'Net Pay': 612.72}

Test your class and method thoroughly, and at a minimum include test cases testing the following:

Net pay cannot exceed gross pay 

#TestMethod

def testNetLessEqualGross(self):
  e=Employee(#Joe Green's Information)
  pi=e.computePayment(1,'31/10/2021')
  self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])

Overtime pay or overtime hours cannot be negative.

Regular Hours Worked cannot exceed hours worked

Higher Tax cannot be negative.

Net Pay cannot be negative.