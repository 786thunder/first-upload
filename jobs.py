class MarkeetingTeam():
    def Employee(self):
        print("there are 4 employee for markeeting")
    def Task(self):
        print("now a days markeeting team is working on gilgit app and invice")
    def Location(self):
        print("Uconnect room no # 5")

class ProductTeam():
    def Employee1(self):
        print("there are 20 employee in product team")
    def Task1(self):
        print("now a days they are working on gilgit app  invice and zoiky")
    def Location1(self):
        print("Uconnect room no # 1 ")
class Freelancin(ProductTeam, MarkeetingTeam):
    def employee3(self):
        print("there are 55 employee for ferrlancin")
    def Task3(self):
        print("they are working on multi tasks")
    def Location3(self):
        print("Uconnect room 2, 3, 4")

obj=Freelancin()
obj.Task()
obj.Task1()
obj.Task3()
obj.Employee()
obj.Employee1()
obj.employee3()
obj.Location()
obj.Location1()
obj.Location3()