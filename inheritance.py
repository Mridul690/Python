class Employee:
    comapany = "Bharat Gas"
    salary = 4500
    salary_bonus = 500
    #total_salary = 5000

    @property
    def TotalSalary(self):
        return self.salary+self.salary_bonus
 
    @TotalSalary.setter
    def TotalSalary(self,val):
        self.salary_bonus = val-self.salary


G = Employee()
G.TotalSalary = 2344
print(G.TotalSalary)
print(G.salary_bonus)