class names:
  num=0

  def __init__(self,name,age):
   self.name=name
   self.age=age
   names.num+=1
#  def count(self):
#      print("count is :",names.num)
  def intro(self):
    print ("name of user is :",self.name, ",age  of user is :", self.age)

obj=names("Rashid",25)
obj1=names("Awais",21)
obj.intro()
obj1.intro()
#obj.count()
print("count is:",names.num)
