#Method overloading
class Math:
    def add(a,b,c=0):
        sum = a+b+c
        print("SUM :",sum) 
    
m= Math
m.add(1,2)
m.add(1,2,3)
print('----------------------------------------------------------------------')
#Method overriding
print('Method overriding')
class Animal:
    def speaks(self):
        print("Animal speaks")
        
class Dog(Animal):
    def speaks(self):
        print('Dog barks')
        
a=Animal()
d=Dog()
a.speaks()
d.speaks()
