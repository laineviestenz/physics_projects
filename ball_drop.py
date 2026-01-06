# d = 0.5*g*(t^2)

class FallingObject():
    """a model of a falling object, where the height, fall distance, and 
    fall time can be accessed through methods. All values must be represented
    in meters and seconds"""
    def __init__ (self, height, time):
        self.height = height
        self.time = time
    
    def get_height(self):
        #calculate height based on fall time
        height = round(self.height - (4.905*(self.time**2)), 3)
        # height can not be negative
        if height < 0:
            height = 0
        #round and display the height
        print('The ball is ' + str(height) + ' meters from the ground.')

    def get_distance(self):
        #get distance based on fall time
        distance = round(4.905*(self.time**2), 3)
        #can't fall further than initial height
        if distance > self.height:
            distance = self.height
        print('The ball falls ' + str(distance) + ' meters.')

    def get_fall_time(self):
        """finds the fall time regardless of the time value given"""
        #find the time that it takes for the height to equal zero
        time = round((self.height/4.905)**0. , 3)
        print('The ball takes ' + str(time) + ' seconds to hit the ground.')

ball = FallingObject(100, 4)
ball.get_height()
ball.get_distance()
ball.get_fall_time()