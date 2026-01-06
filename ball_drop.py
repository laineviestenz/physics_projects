# d = 0.5*g*(t^2)

class FallingObject():
    """a model of a falling object, where the height, fall distance, and 
    fall time can be accessed through methods. All values must be represented
    in meters and seconds. The initial height is defined when the function is
    created, while time is given when the method is used."""
    def __init__ (self, height):
        self.height = height
    
    def get_height(self, time):
        #calculate height based on fall time
        height = round(self.height - (4.905*(time**2)), 3)
        # height can not be negative
        if height < 0:
            height = 0
        #round and display the height
        print('The ball is ' + str(height) + ' meters from the ground.')

    def get_distance(self, time):
        #get distance based on fall time
        distance = round(4.905*(time**2), 3)
        #can't fall further than initial height
        if distance > self.height:
            distance = self.height
        print('The ball falls ' + str(distance) + ' meters.')

    def get_fall_time(self):
        """finds the fall time regardless of the time value given"""
        #find the time that it takes for the height to equal zero
        time = round((self.height/4.905)**0.5 , 3)
        print('The ball takes ' + str(time) + ' seconds to hit the ground.')

ball = FallingObject(100)
ball.get_height(3)
ball.get_distance(3)
ball.get_fall_time()