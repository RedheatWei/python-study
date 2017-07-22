#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月29日
Email: weipeng@sinashow.com
@author: Redheat

'''
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()