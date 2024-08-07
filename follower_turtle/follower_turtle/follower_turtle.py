import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class FollowerTurtle(Node):
    def __init__(self):
        super().__init__('follower_turtle')
        self.publisher_ = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.leader_pose_callback, 10)
        self.subscriber_2 = self.create_subscription(Pose, '/turtle2/pose', self.follower_pose_callback, 10)
        self.leader_pose = Pose()
        self.follower_pose = Pose()

    def leader_pose_callback(self, msg):
        self.leader_pose = msg
        self.update_follower()

    def follower_pose_callback(self, msg):
        self.follower_pose = msg
        self.update_follower()

    def update_follower(self):
        twist = Twist()
        twist.linear.x = 1.5 * (self.leader_pose.x - self.follower_pose.x)
        twist.linear.y = 1.5 * (self.leader_pose.y - self.follower_pose.y)
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    follower_turtle = FollowerTurtle()
    rclpy.spin(follower_turtle)
    follower_turtle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
