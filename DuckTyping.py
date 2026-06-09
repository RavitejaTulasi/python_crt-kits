class Duck:
    def walk(self):
        print("thapak")
class Horse:
    def walk(self):
        print("tabdak")
def myfunction(obj):
    obj.walk()
d = Duck()
myfunction(d)

h = Horse()
myfunction(h)