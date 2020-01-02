# 一、协程
'''
1、以下代码片段（需要Python 3.7+）打印“ hello”，等待1秒钟，然后打印“ world”
'''
# import asyncio
#
#
# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")
#
#
# asyncio.run(main())

'''
2、 等待一个协程。以下代码段会在等待 1 秒后打印 "hello"，然后 再次 等待 2 秒后打印 "world":
'''
# import time
# import asyncio
#
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())

'''
3、asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
'''
# import time
# import asyncio
#
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))
#
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
#
#     print(f"started at {time.strftime('%X')}")
#
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())

# 可等待对象:有三种主要类型: 协程, 任务 和 Future
'''
1、协程：Python 协程属于 可等待对象，因此可以在其他协程中被等待.
协程函数: 定义形式为 async def 的函数;
协程对象: 调用 协程函数 所返回的对象。
'''
# import asyncio
#
#
# async def nested():
#     return 42
#
#
# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     nested()
#
#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".
#
#
# asyncio.run(main())

'''
2、任务：任务 被用来设置日程以便 并发 执行协程。
当一个协程通过 asyncio.create_task() 等函数被打包为一个 任务，
该协程将自动排入日程准备立即运行
'''
# import asyncio
#
#
# async def nested():
#     return 42
#
#
# async def main():
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     print(await task)
#
#
# asyncio.run(main())

'''
3、Future对象：Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。

当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。

在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。

通常情况下 没有必要 在应用层级的代码中创建 Future 对象。

Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:

async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
'''

# 运行asyncio程序
# import asyncio
#
#
# async def main():
#     await asyncio.sleep(1)
#     print('hello')
#
#
# asyncio.run(main())

# 创建任务
# syncio.create_task(coro, *, name=None)
# 将 coro 协程 打包为一个 Task 排入日程准备执行。返回 Task 对象。

# 休眠
'''
coroutine asyncio.sleep(delay, result=None, *, loop=None)
阻塞 delay 指定的秒数。
'''
# import asyncio
# import datetime
#
#
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
#
# asyncio.run(display_date())

# 并发运行任务：并发 运行 aws 序列中的 可等待对象。
# import asyncio
#
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#
#
# async def main():
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#
#
# asyncio.run(main())


# 屏蔽取消操作¶
'''
awaitable asyncio.shield(aw, *, loop=None)
保护一个 可等待对象 防止其被 取消。
'''

# 超时
'''
coroutine asyncio.wait_for(aw, timeout, *, loop=None)¶
等待 aw 可等待对象 完成，指定 timeout 秒数后超时。
'''

# 简单等待
'''
coroutine asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)¶
并发运行 aws 指定的 可等待对象 并阻塞线程直到满足 return_when 指定的条件。
'''


