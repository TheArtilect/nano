
import os
import jinja2
import webapp2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class MainPage(Handler):
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post "
                            "ORDER BY created DESC")
        self.render("front.html", posts = posts)



class NewPost(Handler):
    def render_new(self, subject="", content="", error=""):
        posts = db.GqlQuery("SELECT * FROM Post "
                            "ORDER BY created DESC")

        self.render('new_post.html', subject=subject, content=content,
                    error=error, posts = posts)


    def get(self):
        self.render_new()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if (subject and content):
            p = Post(subject = subject, content = content)
            p.put()
            p_id = p.key().id()
## redirect to template page that retrieves object with id
            self.redirect("/" + str(p_id))

        else:
            error = "A subject and content must be specified in each post!"
            self.render_new(subject = subject, content = content, error=error)


app = webapp2.WSGIApplication([
                                ("/", MainPage),
                                ("/newpost", NewPost)
                                ],
                                debug=True)
