class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


cb = Employee()
cb.language = "JavaScript" # This is an instance attribute
print(cb.language, cb.salary)