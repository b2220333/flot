import rospy
from std_msgs.msg import Float32, Imu
from geometry_msgs.msg import TwistWithCovarianceStamped
from sensor_msgs.msg import Image

class Controller():

	def __init__(self, node_name, msg_type, queue_size=10, hr_sr04_topic='hr_sr04', bno055_topic='bno055'):
		rospy.init_node(node_name, anonymous=True)
		self.rate = rospy.Rate(10)
		rospy.Subscriber(hr_sr04_topic, Float32, self.hr_sr04_callback)
		rospy.Subscriber(bno055_topic, Imu, self.bno055_callback)
		self.hr_sr04_msg = None 
		self.bno055_msg = None
		
	def hr_sr04_callback(data):
    	self.hr_sr04_msg = data
    
    def bno055_callback(data):
    	self.bno055_msg = data
    
