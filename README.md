## swarm_behavior_framework to Webots2023b

1、安装Webots 2023b

2、克隆、编译代码

```python
mkdir -p swarm_frame/src

cd swarm_frame/src

git clone -- branch swarm_frame https://github.com/SICC-Group/swarm_behavior.git

colcon build --symlink-install

```

3、向~/.bashrc文件添加source

```
source ~/swarm_frame/install/local_setup.sh
```

4、在demo文件夹下运行案例

```python
python3 *.py
```

