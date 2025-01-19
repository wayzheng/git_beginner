import random
print("这是一个随机数%d"%random.randint(1, 100))
for i in range(random.randint(1, 100)):
    print(f"这是一个随机数字{random.randint(1, i+1)}")
def demo(function):
    def demo1():
        function()
        print("这是一个装饰器函数")
    return demo1

@demo
def test():
    print("这是一个测试函数")

test() # 最后的结果是：这是一个测试函数 这是一个装饰器函数 这是由于装饰器函数得到的结果

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = x ** 2
plt.plot(x, y, color = "red")
plt.legend()
plt.show()
