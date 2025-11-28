class distance:
    def __init__(self,inch,feet):
        self.inch=inch
        self.feet=feet

    def __add__(self,obj):
        inch1=self.inch+obj.inch
        feet1=self.feet+obj.feet
        return distance(inch1,feet1)
    
    def display(self):
        print(f"inch={self.inch},feet={self.feet}")


d1=distance(2,2)
d2=distance(3,4)

d1.display()
d2.display()

d3=d1+d2
d3.display()