#!/usr/bin/env python
# license removed for brevity
import tf
import rospy
from sensor_msgs.msg import Imu

imu_out = Imu()

def imu_callback(imu_in):
	global imu_out
	imu_out.orientation.x = imu_in.orientation.y;
	imu_out.orientation.y = imu_in.orientation.x;

def rviz_filter():
	rospy.Subscriber('imu/data', Imu, imu_callback)
	pub = rospy.Publisher('imu/rviz_data', Imu, queue_size=10)
	rospy.init_node('rviz_imu_filter', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		pub.publish(imu_out)
		rate.sleep()

if __name__ == '__main__':
    try:
        rviz_filter()
    except rospy.ROSInterruptException:
        pass