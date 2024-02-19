import web

render = web.template.render('views/')

class Bienvenida:
    def GET(self):
        cookies = web.cookies(username=None)
        username = cookies.username
        if username:
            return render.bienvenida(username)
        else:
            raise web.seeother('/login')
