from abc import ABC, abstractmethod 
class absclass(ABC):

    def print(self,x):
        print("passed value:", x)

    @abstractmethod
    def task(self):
        print("we are inside  task")

class test_class(absclass):

    def task(self):
        print("we are inside test_class task")

test_obj = test_class()
test_obj.print(10)
test_obj.task()
test_obj.print(100)
 
        
        
