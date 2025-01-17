# 1. Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
#
#
# class car:
#     brand ="Maruti"
#     Model="VXI"
#     Year = "2014"
#
# cartype = car()
# print(cartype.brand)
# print(cartype.Model)
# print(cartype.Year)
#
# 2. Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?


# class Student:
#
#     name = "Anil"
#     Rollno="10"
#     Marks="65"
# s1= Student()
# print(s1)
# print(s1.name)
# print(s1.Rollno)
# print(s1.Marks)


# 3. Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?

# class rectangle():
# def __init__(self,length,width):
#     self.length = length
#     self.width = width
#     def display_area(self):
#         return self.length*self.width
#         def display_perimeter(self):
#             return 2*(self.length+self.width)
#      def display_info(self):
#          print("Method 1")
#          print(f"Area of the rectangle: {s1.display_area()}")
#         print(f"perimeter of the rectangle: {s1.display_perimeter()}")
#  s1 = rectangle(30,50)
#  s1.display_info()
#  print("Method 2")
#  print(f"Area of the rectangle : {s1.display_area()}")
#  print(f"Perimeter of the rectangle : {s1.display_perimeter()}")


# 4. Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?
#  class circle():
#      def __init__(self,radius):
#          self.radius =  radius
#      def getarea(self):
#          return math.pi*self.radius**2
#      def getcircumference(self):
#          return 2*math.pi*self.radius
#      def display_info(self):
#          print(f"Area of the circle : {c1.getarea()}")
#          print(f"Circumference of the circle : {c1.getcircumference()}")
#
#  c1 = circle(5)
#  c1.display_info()




# 5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
#  class account:
#      def __init__(self,debit,credit,acc_no):#         self.debit = debit
#          self.credit = credit
#          self.acc_no = acc_no
#      def balance(self):
#         return self.credit-self.debit
#      def display_info(self):
#          print(f"The balance in account no {self.acc_no} is {acc.balance()}")
#  acc = account(56,3400,123457)
#  acc.display_info()


# 6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.

 # class employee:
 #     current_employee = 1
 #    def __init__(self,name):
 #        self.name = name
 #         employee.increment_employee()
 #     @classmethod
 #     def increment_employee(cls):
 #         employee.current_employee += 1
 #     @classmethod
 #     def display_info(cls):
 #         print(f"Total employee is : {employee.current_employee}")
 # emp1 = employee("Anil")
 # emp1.display_info()
 #
 # emp2 = employee("Data")
 # emp2.display_info()




# 7. Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.

# Need help on this

# 8. Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.
# Need help on this
# 9. Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.
# Need help on this
#Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.
# Need help on this