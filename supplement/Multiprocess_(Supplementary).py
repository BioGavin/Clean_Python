# 多进程与进程池

import time
from multiprocessing import Process, Pool, Queue


def func(name):
    time.sleep(2)
    print(name)


num = 10


def sun():
    global num  # 调用全局变量
    num += 10
    print(num)


def func1(q):
    for i in range(10):
        q.put("123")  # 传递数据
    print('end')


def func2(q):
    for i in range(10):
        data = q.get()  # 获取数据
        print(data)
        time.sleep(3)

if __name__ == '__main__':
    # 多进程
    # print('main process run')
    # p = Process(target=func, name='process', args=('gavin',))
    # p.start()  # 进入就绪状态
    # print('test')
    # p.join(timeout=3)  # 等待子进程结束, timeout 主进程等待多长时间
    # print('main process end')


    # 进程池
    # print('main process run')
    # po = Pool(3)  # 同一时间只有3个子进程运行
    # for i in range(5):
    #     po.apply_async(func, args=('gavin',))
    # po.close()
    # po.join()

    # 进程间通信
    queue = Queue(3)  # 队列里面最多存放3条数据
    p1 = Process(target=func1, args=(queue,))
    p2 = Process(target=func2, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()