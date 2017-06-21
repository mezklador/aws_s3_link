import tornado.ioloop
import tornado.web

from get_link import getS3link


HOST = '127.0.0.1'
PORT = 3663


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.s3_result()
        self.finish()

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def s3_result(self):
        self.write(getS3link())



if __name__ == '__main__':
    try:
        app = tornado.web.Application([
            (r'/', MainHandler),
        ])
        app.listen(PORT, address=HOST)
        print(f"-- Tornado serving on http://{HOST}:{PORT}")
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("-- Stopping server...")
        pass
