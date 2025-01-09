# team.py


class Company:
    def __init__(self, name: str):
        self.name = name


class Team:
    def __init__(self, name: str, company: Company):
        self.name = name
        self.company = company
        self.members = set()
    
    def add_member(self, employee: 'Employee'):
        employee.set_team(self)
        self.members.add(employee)

    def remove_member(self, employee: 'Employee'):
        self.members.remove(employee)


class Employee:
    def __init__(self, name: str, team: Team = None):
        self.name = name
        self.team = team
    
    def set_team(self, new_team):
        if self.team:
            self.team.remove_member(self)

        self.team = new_team
    

# Udělejte třídu Employee
# atributy: name, team


it_security = Company('IT Guards s.r.o.')
team_A = Team('Team A', it_security)
team_B = Team('Team B', it_security)
team_B.add_member()


l1 = Employee('Lena')
l2 = Employee('Lena')
l3 = Employee('Lena 2')

team_B.add_member(l1)
team_B.add_member(l2)
team_B.add_member(l3)
print(team_B.members)

kuba = Employee('Kuba', team_A)
jana = Employee('Jana')

print(kuba.name)
print(kuba.team.name)
print(kuba.team.company.name)
# print(jana.team.company.name)


it_security.name = 'IT Gurus 222'
print(team_A.company.name)
print(team_B.company.name)


it_security2 = Company('IT 2 Guards s.r.o.')


