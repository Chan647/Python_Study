'''class Student :
    def __init__(self, name, korean, math, english, science) :
        self.name = name
        self.korean = korean
        self.math = math
        self.enghlish = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.enghlish + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    
students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
]

print("이름", "총점", "평균", sep="\t")
for student in students :
    print(student.to_string())

class Father :
    def run(self):
        print("달린다")

class Son(Father):
    def run(self):
        super().run()
        print("러닝한다")


s = Son()
s.run()
'''
class Soccer:

    def __init(self,name) :
        self.name = name

    def __str__(self) :
        return "나는 {}입니다.".format(self.name)
        
        
messi = Soccer()
cruief = Soccer()
