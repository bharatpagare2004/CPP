class Employee:
    emp_count=0
    m_count=0
    f_count=0
    ass_man=0
    salary_10=0
    def __init__(self):
        Employee.emp_count+=1
        self.name
        self.designation
        self.gender
        self.DOJ
        self.salary
        self.check_employee()
    def check_employee(self):
        if self.designation.lower()=="asst manager": 
           Employee,asst_man +=1
        if self.gender=="m":
            Employee.m_count =+1
        else:
            Employee.f_count+=1
        if self.salary>10000:
            Employee.salary_10k +=1
        return None
    def total_employee():  
        return Employee.emp_count
    def male_female_count():
        return Employee          
    


