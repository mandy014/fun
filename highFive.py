/* 
A basic high-five call and response class, where users can create extended 
child classes with their own personal responses to high-fives sent their way. 

Project inspired by a discussion with @danasaur 
*/

from random import randint

class PyLady(object):
    def __init__(self, name):
        self.name = name
        
    def highFive(self, person):
        resp = person.response()
        print self.name + " went in for a high-five and " + resp
    
    def response(self):
        return self.name + " high-fived you back!"

#As a child class of PyLady, Dana customises her high-five responses    
class Dana(PyLady):
    def response(self):
        rand = randint(1,3)
        if rand == 1:
            return self.name + " high-fived you back!"
        elif rand == 2:
            return self.name + " ignored you. Ouch."
        elif rand == 3:
            return self.name + " tried to high-five you but missed, forgetting the elbow trick."
        
#anna is a PyLady with default high-five response()       
anna = PyLady("Anna")

#dana is a PyLady child, a Dana, with customised overridden response()
dana = Dana("Dana") 

#anna high-fives dana
anna.highFive(dana) 

#dana high-fives anna
dana.highFive(anna)  
