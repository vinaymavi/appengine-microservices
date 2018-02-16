import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World! From Service1')


app = webapp2.WSGIApplication([
    (r'/service1/', MainPage),
], debug=True)