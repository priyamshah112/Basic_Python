"""4.	Write a program to declare a Gross Salary for a employee and find it’s Basic Pay based on following condition:              
	House Allowance = 30% of Gross Salary
       	Medical Allowance = 20% of Gross Salary
        	Basic Salary = Gross Salary – (House Allowance + Medical Allowance )"""
def basic_salary():
         gross_salary = float(input("enter amount= "))
         house_allowance =(gross_salary*30)/(100.0)
         medical_allowance =(gross_salary*20)/(100.0)
         print(str(gross_salary))
         return( gross_salary -(house_allowance+medical_allowance))
	
