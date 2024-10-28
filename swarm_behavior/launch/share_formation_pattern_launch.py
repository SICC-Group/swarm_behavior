import os
import launch_ros.actions
from launch.actions import TimerAction
from webots_ros2_driver.webots_launcher import WebotsLauncher
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from webots_ros2_driver.utils import controller_url_prefix


def generate_launch_description():
    ld = LaunchDescription()

    config_dir = os.path.join(get_package_share_directory('swarm_behavior'), 'config')

    # Webots
    webots = WebotsLauncher(
        world=os.path.join(get_package_share_directory('swarm_behavior'), 'worlds', 'mul_epuck_world.wbt')
    )
    ld.add_action(webots)

    formation_id = [0, 2, 3, 4,7]
    formation_name = [f'epuck_{id}' for id in formation_id]
    total_ids = range(8)

    # Controller node
    for i in formation_id:
        robot_name = 'epuck_' + str(i)
        controller = Node(
            package='swarm_behavior',
            executable='test',
            output='screen',
            additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + robot_name},
            parameters=[
                {'formation_name': formation_name, 
                'formation_id': formation_id
                }
            ],
        )
        ld.add_action(controller)

    for robot_id in total_ids:
        if robot_id not in formation_id:
            robot_name = 'epuck_' + str(robot_id)
            controller = Node(
                package='swarm_behavior',
                executable='random_pattern',
                output='screen',
                additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + robot_name},
                parameters=[PathJoinSubstitution([config_dir, 'combined_pattern.yaml'])],
            )
            ld.add_action(controller)

    return ld