import os

import tornado.ioloop
import tornado.web
from tornado.options import define, options

from handlers import ProductHandler

define("port", default=8080, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self, db):
        self.db = db
        handlers = [
            (r"/", ProductHandler),
        ]

        settings = dict(
            blog_title=u"Indonesia Native Plant",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=True,
        )

        super(Application, self).__init__(handlers, **settings)


if __name__ == "__main__":
    application = Application([
        (r'/', ProductHandler)
    ]
    )

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
