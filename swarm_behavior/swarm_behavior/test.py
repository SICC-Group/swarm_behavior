import rclpy
import time
import threading
import multiprocessing
import os
from swarm_frame.EpuckNode import EpuckNode
from swarm_frame.Behavior import Behavior
from swarm_frame.BehaviorTree import NodeState, Rotate, Away, Close, Patrol, Selector, Sequence
from geometry_msgs.msg import Twist
from rclpy.node import Node
from enum import Enum
from swarm_behavior.interpolation import interpolate_lookup_table
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data
import numpy  as np

class CheckAway():
    def __init__(self, start_time):
        self.start_time = start_time
        
    def run(self):
        current_time = time.time()  
        if current_time - self.start_time > 10 and current_time - self.start_time <20:                  
            return NodeState.SUCCESS
        else:  
            return NodeState.FAILURE
			
class CheckClose():
    def __init__(self, start_time):
        self.start_time = start_time
        
    def run(self):
        current_time = time.time()  
        if current_time - self.start_time < 5:                  
            return NodeState.SUCCESS
        else:  
            return NodeState.FAILURE
    
def euclidean_distance(point1, point2):
    return np.sqrt((point1['x'] - point2['x']) ** 2 + (point1['y'] - point2['y']) ** 2)

def calculate_distance_matrix(pose_dict):
    robot_ids = list(pose_dict.keys())
    num_robots = len(robot_ids)
    
    distance_matrix = np.zeros((num_robots, num_robots))
    
    for i in range(num_robots):
        for j in range(num_robots):
            if i != j: 
                distance_matrix[i][j] = euclidean_distance(pose_dict[robot_ids[i]], pose_dict[robot_ids[j]])
 
    return distance_matrix

# def spin_thread(node):
#     rclpy.spin(node)


# def main():
#     rclpy.init()

#     robot1 = EpuckNode('epuck')
#     robot1.start_device()

#     root = Selector([
#         Sequence([CheckAway(robot1), Away(robot1)]),
#         Sequence([CheckClose(robot1), Close(robot1)]),
#         Patrol(robot1)
#         ])

#     spin_t = threading.Thread(target=spin_thread, args=(robot1,))
#     spin_t.start()

#     try:
#         while True:
#             root.run()
#             time.sleep(0.5)

#     except KeyboardInterrupt:
#         pass  

#     finally:
#         robot1.destroy_node()
#         rclpy.shutdown()
#         spin_t.join() 

# if __name__ == '__main__':
#     main()
    
    
# def spin_thread(node):
#     rclpy.spin(node)

# def robot_logic(robot_id):
#     rclpy.init()
    
#     print("环境变量：", os.environ["WEBOTS_CONTROLLER_URL"])
#     # 创建节点实例
#     robot_node = EpuckNode(f'epuck_{robot_id}')
#     robot_node.start_device()

#     # 定义行为树
#     root = Selector([
#         Sequence([CheckAway(robot_node), Away(robot_node)]),
#         Sequence([CheckClose(robot_node), Close(robot_node)]),
#         Patrol(robot_node)
#     ])

#     # 启动ROS事件循环
#     spin_t = threading.Thread(target=spin_thread, args=(robot_node,))
#     spin_t.start()

#     try:
#         while True:
#             root.run()
#             time.sleep(0.5)

#     except KeyboardInterrupt:
#         pass  

#     finally:
#         robot_node.destroy_node()
#         rclpy.shutdown()
#         spin_t.join()

# def main():
#     num_robots = 3  # 可以根据需要设置机器人的数量
#     threads = []

#     for i in range(num_robots):
#         os.environ["WEBOTS_CONTROLLER_URL"] = f"ipc://1234/epuck_{i}"
#         t = multiprocessing.Process(target=robot_logic, args=(i,))
#         t.start()
#         threads.append(t)
#         time.sleep(0.5)
#     try:
#         for t in threads:
#             t.join()  # 等待所有机器人线程结束

#     except KeyboardInterrupt:
#         pass

# if __name__ == "__main__":
#     main()

