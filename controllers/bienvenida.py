import web

render = web.template.render('views/')

class Bienvenida:
    def GET(self):
        username = web.cookies().get("username")
        return render.bienvenida(username)