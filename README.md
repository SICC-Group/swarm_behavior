## swarm_behavior_framework to Webots2023b

1、安装Webots 2023b

2、克隆、编译代码

```python
mkdir -p swarm_frame/src

cd swarm_frame/src

git clone https://github.com/SICC-Group/swarm_behavior.git

colcon build --symlink-install

```

3、向~/.bashrc文件添加source

```
source ~/swarm_frame/install/local_setup.sh
```

4、运行demo文件夹中的例程

python3 /home/jzx/swarm_frame/src/swarm_frame/swarm_frame/demo  *.py