#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys


def autonomous_controller():
    rospy.init_node('autonomous_controller')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    vel = Twist()

    while not rospy.is_shutdown():
        vel.linear.x = 1.0
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 1.0

        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        autonomous_controller()
    except rospy.ROSInterruptException:
        pass
