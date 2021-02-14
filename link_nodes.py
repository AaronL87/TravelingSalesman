# Will eventually not use only midpoint to account for issues with
# collinear points and other cases that do not work

class LinkNodes: 
    # Left and right are from perspective facing convex hull from outside
    def __init__(self,array,i,MP_dictionary):
        self.point = array[i]
        self.left = array[(i-1)%len(array)] # Clockwise
        self.right = array[(i+1)%len(array)] # Counterclockwise
        self.left_MP = self.get_MP(self.point,self.left)
        self.right_MP = self.get_MP(self.point,self.right)
        
        # update MP_dictionary
        # These lists are organized [left of midpoint,right of midpoint]
        if i == 0:
            MP_dictionary.update({self.left_MP:[self.point]})
            MP_dictionary.update({self.right_MP:[self.point]})
        elif i != len(array)-1:
            MP_dictionary[self.left_MP].append(self.point)
            MP_dictionary.update({self.right_MP:[self.point]})
        elif i == len(array)-1:
            MP_dictionary[self.left_MP].append(self.point)
            MP_dictionary[self.right_MP] = [self.point] + MP_dictionary[self.right_MP]

    @staticmethod
    def get_MP(point1,point2): # get_MP Formula
        return ((point1[0]+point2[0])/2,(point1[1]+point2[1])/2)


class AddNode:
    def __init__(self,point,left,right,MP_dictionary):
        self.point = point
        self.left = left # Clockwise
        self.right = right # Counterclockwise
        self.left_MP = self.get_MP(self.point,self.left)
        self.right_MP = self.get_MP(self.point,self.right)

        # update MP_dictionary
        MP_dictionary[self.left_MP] = [left,point]
        MP_dictionary[self.right_MP] = [point,right]
        
        print("MP_dictionary:",MP_dictionary,"\n"*2)

    @staticmethod
    def get_MP(point1,point2): # get_MP Formula
        return ((point1[0]+point2[0])/2,(point1[1]+point2[1])/2)
