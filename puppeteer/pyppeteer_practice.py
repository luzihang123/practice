# -*- coding:utf-8 -*-
# @Author: clark
# @Time: 2019-12-27 16:14
# @File: pyppeteer_practice.py
# @project demand:参考https://cuiqingcai.com/6942.html

'''
1、初入
'''
# from pyppeteer import launch
# import asyncio
# from pyquery import PyQuery as pq
#
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto("http://quotes.toscrape.com/js/")
#     doc = pq(await page.content())
#     print(f"Quotes {doc('.quote').length}")
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())

'''
2、截图、存文件
'''
# import asyncio
# from pyppeteer import launch
#
#
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('http://quotes.toscrape.com/js/')
#     await page.screenshot(path='example.png')
#     await page.pdf(path='example.pdf')
#     dimensions = await page.evaluate('''() => {
#         return {
#             width: document.documentElement.clientWidth,
#             height: document.documentElement.clientHeight,
#             deviceScaleFactor: window.devicePixelRatio,
#         }
#     }''')
#
#     print(dimensions)
#     # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())

'''
3、访问个淘宝
'''
# import asyncio
# from pyppeteer import launch
#
#
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(100)
#
#
# asyncio.get_event_loop().run_until_complete(main())

'''
4、执行js，似乎失效
'''
# import asyncio
# from pyppeteer import launch
#
#
# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
#     await page.evaluate(
#         '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
#     await asyncio.sleep(100)
#
#
# asyncio.get_event_loop().run_until_complete(main())


'''
5、设置userDataDir，继承登陆状态
'''
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False, userDataDir='~/userdata', args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())
