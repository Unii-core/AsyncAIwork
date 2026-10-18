import numpy as np
x=np.array([1, 2, 3, 4, 5, 6, 7, 8],dtype=float)
y=np.array([52, 55, 61, 67, 72, 78, 83, 89],dtype=float)
w=0
b=0
mse=0
alpha=0.01
for i in range(1000):
    y_pre = w * x + b
    error = y_pre - y
    mse=np.mean(np.square(error))
    dw=np.mean(2*error*x)
    db=np.mean(2*error)
    w-=alpha*dw
    b-=alpha*db
    if i%100==0:
        print(f"函数为y={w}x+{b},均方误差为{mse}")
print(f"最终方程为：y={w}x+{b},最终均方误差为{mse}")
