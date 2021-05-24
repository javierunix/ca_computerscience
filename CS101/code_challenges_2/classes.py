class DriveBot():
	# class variables 
	all_disabled = True 
	latitud = -999999
	longitud = -999999
	robot_count = 0 # this class variable will increment in 1 after each instance


	def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
		self.motor_speed = motor_speed
		self.direction = direction
		self.sensor_range = sensor_range
		DriveBot.robot_count += 1 # increment by 1 the counter
		self.id = DriveBot.robot_count # assign the counter as instance id
	
	# Add a method called control_bot which accepts parameters: new_speed and new_direction. 
	# These should replace the associated instance variables

	def control_bot(self, new_speed, new_direction):
		self.motor_speed = new_speed
		self.direction = new_direction


	#  Create another method called adjust_sensor which accepts a parameter called new_sensor_range 
	# which replaces the sensor_range instance variable.

	def adjust_sensor(self, new_sensor_range):
		self.sensor_range = new_sensor_range 

robot_1 = DriveBot(35, 75, 25)
robot_2 = DriveBot(20, 60, 20)

print(robot_1.id)
print(robot_2.id)
