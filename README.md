# Autonomous-Waste-Classification-System-TRASHBOT-

Project Motivation 
With increasing population and consumption, there is a growing amount of waste being generated, leading to various environmental, social, and health problems. It is, therefore, important to recycle. A trash sorting robot will help to sort trash and recycling materials to help reduce waste. 
There are different sorting methods used by waste management facilities such as, Mechanical sorting which separate materials based on size, weight, and magnetic properties and air classification in which Compressed air is used to separate lightweight materials such as paper and plastic from heavier materials such as glass and metal. 
Mechanical sorting of waste is unreliable due to variations in weight, size, and magnetic characteristics. Similar waste types may have differing physical characteristics and magnetic properties, leading to incorrect classification. Additionally, mechanical sorting requires a large space, making it an inefficient method of waste segregation.  
A small, movable robot for garbage segregation is being proposed as an alternative solution that is cheaper and faster than manual labor or mechanical machines. There is a gap in the field for autonomous robots and AI-developed robots due to a lack of investment, but this solution would be economically viable and have a positive impact on the industry. 
Project Aims:
The main goal of our proposal is to create a robot that can sort trash based on whether it is recyclable. The specific aims for 
this project include: 
1. Classify the waste into Plastic, Paper, Metal, Glass and Cardboard using Computer Vision and Image processing.  
2. Implement inverse kinematics to find the motion of the robot to reach desired position. 
Project Methodologies 
The methods that we plan to use for the development of Trashbot are the following: 
1. Computer Vision: 
1. Image is acquired with the help of Camera to get the top-view of the object. 
2. Image processing is used to Segment the object from the background. 
3. Convolutional Neural Network, which is a Deep Learning model, is used to analyze and classify the waste 
into Plastic, Paper, Metal, Glass and Cardboard. 
2. Find the position of the object: 
1. To get x, y, z coordinates in the 3D space, two cameras are installed. Top Camera gives the x, y coordinates 
and side camera gives z coordinates(depth) of the object. 
3. Path Planning: 
1. The path that the End Effector must follow is determined using Inverse Kinematics.
