import os
import jinja2
import webapp2
import hashing

from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))



class MainPage(Handler):
    def get(self):
        self.response.headers["Content-Type"] = 'text/plain'
        visits = 0
        visit_cookie_str = self.request.cookies.get("visits")

        if visit_cookie_str:
            cookie_val = hashing.check_secure_val(visit_cookie_str)
            if cookie_val:
                visits = int(cookie_val)


        visits += 1

        new_cookie_val = hashing.make_secure_val(str(visits))

        self.response.headers.add_header("Set-Cookie", 'visits=%s' % new_cookie_val)

        if visits > 20:
            self.write("You are the best ever")
        else:
            self.write("You've been here %s times!" % visits)


app = webapp2.WSGIApplication([
                                ("/", MainPage)
                                ],
                                debug=True)
