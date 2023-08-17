# 导入pynput和threading库
import pynput
from time import sleep
# 创建一个鼠标控制器对象
mouse = pynput.mouse.Controller()

# 创建一个列表用于存储最近movewall次的光标位置
cursor_positions = []

# 定义一个阈值，只有当y值变化超过这个阈值时，才输出滚轮操作
threshold = 5
#定义movewall的阈值
movewall = 15

# 定义一个函数用于监测光标位置并记录到列表中
def monitor_cursor(x,y): # 添加一个参数x，用于接收鼠标移动事件的对象
    # 获取当前的光标位置
    current_position = mouse.position
    # 将当前的光标位置添加到列表的末尾
    cursor_positions.append(current_position)
    # 如果列表的长度超过movewall，就删除最早的一个元素
    if len(cursor_positions) > movewall:
        cursor_positions.pop(0)

# 定义一个函数用于检查光标位置的变化并输出滚轮操作
def check_cursor():

# 获取当前的光标位置
    current_position = mouse.position
    # 等待0.05秒
    sleep(0.05)
    # 再次获取当前的光标位置
    new_position = mouse.position
    # 如果两次获取的光标位置相同，说明鼠标静止了
    if current_position != new_position:
        # 如果列表中有至少movewall个元素，才进行检查
        if len(cursor_positions) == movewall:
            # 获取列表中所有元素的y值
            y_values = [y for x, y in cursor_positions]
            # 计算y值的最大值和最小值之差
            y_range = max(y_values) - min(y_values)
            # 如果y值的范围大于阈值，说明光标有明显的上下移动
            if y_range > threshold:
                # 如果y值是递减的，说明光标向上移动，就输出滚轮向下滚动
                if y_values == sorted(y_values, reverse=True):
                    print("mouse.scroll(0, -1)")
                    mouse.scroll(0, -1)
                # 如果y值是递增的，说明光标向下移动，就输出滚轮向上滚动
                elif y_values == sorted(y_values):
                    print("mouse.scroll(0, 1)")
                    mouse.scroll(0, 1)

# 创建一个监听器对象，用于监测鼠标移动事件，并调用monitor_cursor函数
listener = pynput.mouse.Listener(on_move=monitor_cursor)
# 启动监听器
listener.start()

# 创建一个循环，不断调用check_cursor函数，并设置间隔时间为0.1秒
while True:
    check_cursor()
    sleep(0.1)
