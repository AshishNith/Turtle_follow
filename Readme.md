# ROS2 Humble TurtleSim Project

This project demonstrates a simple ROS2 application using the TurtleSim package. In this project, two turtles are spawned. One turtle is controlled by keyboard teleop key , and the other turtle follows the first one.

## Table of Contents
- [What is this Project](#what-is-this-project)
- [What I Learnt from this Project](#what-i-learnt-from-this-project)
- [Concepts Used in this Project](#concepts-used-in-this-project)
- [How to clone and use this repo](#How-to-clone-and-use-this-repo)



## What is this Project

This project is a demonstration of using ROS2 (Robot Operating System 2) with the TurtleSim package to create a simple simulation where one turtle can be controlled by keyboard and another turtle autonomously follows the first turtle. The project helps to understand the basics of ROS2 nodes, topics, and services.

## What I Learnt from this Project

Through this project, I have learnt:
- How to set up and configure a ROS2 workspace.
- The basics of creating and running ROS2 nodes using Python.
- How to use ROS2 topics to publish and subscribe to messages.
- Implementing teleoperation using keyboard inputs.
- Using ROS2 services to spawn additional turtles in the simulation.
- Basic concepts of autonomous behavior by programming a follower turtle.

## Concepts Used in this Project

- **ROS2 Nodes**: Independent processes that perform computation.
- **ROS2 Topics**: Channels for nodes to communicate with each other by publishing and subscribing to messages.
- **ROS2 Services**: Synchronous communication mechanism in ROS2 for handling requests and responses.
- **TurtleSim**: A ROS2 package used to simulate a turtle's movement in a 2D space.
- **Teleoperation**: Controlling the turtle using keyboard inputs.
- **Autonomous Behavior**: Programming the second turtle to follow the first turtle based on its position.

## How to clone and use this repo

1. **Make a Ros_ws and clone it**: 

2. **Set up your ROS2 workspace**:
   ```sh


   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws
   git clone git@github.com:AshishNith/Turtle_follow.git
   
   colcon build 

   source ~/ros2_ws/install/setup.bash

   # How to run this -- 

   ros2 run turtlesim turtlesim_node
   ros2 service call /spawn turtlesim/srv/Spawn "{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}"
   ros2 run teleop_turtle teleop_turtle
   ros2 run follower_turtle follower_turtle


