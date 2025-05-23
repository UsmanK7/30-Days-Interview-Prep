class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(self.name)
        self.printAverage(self.marks)
    def printAverage(self,marks):
        sum = 0
        for subject in marks:
            sum += subject
        avg = sum/len(marks)
        print(avg)


st1 = Student("usman",[40,50,60])
