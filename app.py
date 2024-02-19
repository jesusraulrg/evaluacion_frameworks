import web

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/bienvenida', 'Bienvenida'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.index()

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        data = web.input()
        if data.username == "usuario" and data.password == "1234":
            web.setcookie("username", data.username)
            raise web.seeother('/bienvenida')
        else:
            return render.login()

class Bienvenida:
    def GET(self):
        username = web.cookies().get("username")
        return render.bienvenida(username)

if __name__ == "__main__":
    app.run()