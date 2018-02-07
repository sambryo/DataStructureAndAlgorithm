class Coordinator: 
    def __init__(self,x, y): 
        self.x = x 
        self.y = y 

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


def add(a,b): 
    return Coordinator(a.x + b.x, a.y+b.y)
def sub(a,b): 
    retutn Coordinator(a.x-b.x, a.y-b.y)

one = Coordinator(100,300)
two = Coordinator(200,200)


add(one, two)
