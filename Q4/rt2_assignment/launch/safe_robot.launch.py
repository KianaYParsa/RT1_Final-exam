from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    # Include original robot.launch.py
    robot_pkg_share = get_package_share_directory('gazebo_differential_drive_robot')
    robot_launch = os.path.join(robot_pkg_share, 'launch', 'robot.launch.py')

    include_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(robot_launch)
    )

    # Safety node (output remapped to /cmd_vel)
    safety = Node(
        package='rt2_assignment',
        executable='safety_node',
        name='safety_node',
        output='screen',
        remappings=[
            ('/safe_cmd_vel', '/cmd_vel'),
        ],
    )

    # Manual control node
    manual = Node(
        package='rt2_assignment',
        executable='manual_control',
        name='manual_control_node',
        output='screen',
    )

    return LaunchDescription([
        include_robot,
        safety,
        manual,
    ])
