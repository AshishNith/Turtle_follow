import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from pynput import keyboard

class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('teleop_turtle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose = Pose()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def pose_callback(self, msg):
        self.pose = msg

    def on_press(self, key):
        twist = Twist()
        if key == keyboard.Key.up:
            twist.linear.x = 2.0
        elif key == keyboard.Key.down:
            twist.linear.x = -2.0
        elif key == keyboard.Key.left:
            twist.angular.z = 2.0
        elif key == keyboard.Key.right:
            twist.angular.z = -2.0
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    teleop_turtle = TeleopTurtle()
    rclpy.spin(teleop_turtle)
    teleop_turtle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
