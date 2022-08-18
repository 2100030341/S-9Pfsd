class Student:
    def cal(self, r1, r2, c1, t1, t2, t3):
        if r1 > 0 and r2 > 0 and c1 > 0 and t1 > 0 and t2 > 0 and t3 > 0:
            self.calperimeterrec(r1, r2)
            self.calperimetercircle(c1)
            self.calperimetertriangle(t1, t2, t3)
        else:
            print("GIVE PROPER INPUTS")

    def calperimeterrec(self, r1, r2):
        print("THE PERIMETER OF RECTANGLE IS ", 2 * (r1 + r2))

    def calperimetercircle(self, c1):
        print("THE PERIMETER OF CIRCLE IS ", 2 * (22 / 7) * (c1))

    def calperimetertriangle(self, t1, t2, t3):
        print("THE PERIMETER OF TRIANGLE IS ", (t1 + t2 + t3))


s = Student()
r1 = float(input())
r2 = float(input())
c1 = float(input())
t1 = float(input())
t2 = float(input())
t3 = float(input())
s.cal(r1, r2, c1, t1, t2, t3)
