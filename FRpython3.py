

'''
classes & methods

methods --> funcs inside class

To access objs inside methods, call method first:

    rect1.area_func()
    print(rect1.area_var)


'''
class Rect:
    def __init__(self, col, w, l):
        self.width = w
        self.length = l
        self.color = col
    
    def area_func(self):
        self.area = self.width*self.length
        return self.area

c1='red'
w1,l1 = 3,4        
rect1 = Rect(c1,w1,l1) #rect1 is an obj, give same params as init
print(rect1.color, rect1.width)

areaR1 = rect1.area_func()
print(areaR1,'\n')


c2 = 'blue'
w2,l2 = 5,6
rect2 = Rect(c2,w2,l2)
a2 = rect2.area_func()
print(a2)