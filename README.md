## swarm_behavior to Webots2023b

1、安装Webots 2023b

2、克隆、编译代码

```python
mkdir -p swarm_behavior/src

cd swarm_behavior/src

git clone -- branch swarm_behavior https://github.com/SICC-Group/swarm_behavior.git

colcon build --symlink-install

```

3、向~/.bashrc文件添加source

```
source ~/swarm_behavior/install/local_setup.sh
```

4、启动群机器人行为

```python
ros2 launch swarm_behavior attraction_pattern_launch.py
```

