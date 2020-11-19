
class Person:
    def p(self):
        print("i am a person1")
class Person():
    def p(self):
        print("i am a person2")

Person.p("a")

p = Person()
p.p()