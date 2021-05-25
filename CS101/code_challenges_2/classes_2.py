class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count +=1

    # override + method
    def __add__(self, value):
        self.speed += value

    # override - method
    def __sub__(self, value):
        self.speed -= value
    

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction) + 180 % 360 # turn around
            self.obstacle_found = False

# create DriveBot class

class DriveBot(Robot):
    
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10): # change speed for motor speed

        super().__init__(speed = motor_speed, direction = direction, sensor_range = sensor_range) # use superclass constructor

    def __add__(self, value):
        super().__add__(value=value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value=value)
        self.sensor_range -= value

# create WalBot class

class WalkBot(Robot):

    walkbot_count = 0 # class variable to count walkbots
    
    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):  # change speed for motor steps per minute. steps length as additional parameter

        super().__init__(speed = steps_per_minute, direction = direction, sensor_range = sensor_range) # use superclass constructor
        self.step_length = step_length
        WalkBot.walkbot_count += 1
        if Robot.robot_count >= 10 and WalkBot.walkbot_count >=5:
            Robot.all_disabled = True


    def __add__(self, value):
        super().__add__(value=value)
        self.step_length += value / 2
        
    def __sub__(self, value):
        super().__sub__(value=value)
        self.step_length -= value / 2


    # modify adjust_sensor method
    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range= new_sensor_range) # call the super class method
        self.obstacle_found = False # additional intruction
        self.step_length = 5 # additional intruction

    # modify avoid_obstacles
    def avoid_obstacles(self):

        if self.speed <= 60: # if speed is equal or lower than 60
            super().avoid_obstacles() # use superclass method
        else: # if speed is higher than 60
            self.direction = (self.direction + 90) % 360 # modify in 90 degrees the direction
            self.obstacle_found = False

        # independtly of the speed, we have to reduce by half speed and step_length
        self.speed /= 2
        self.step_length /= 2

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled)
robot_10 = WalkBot()
print(Robot.all_disabled)
