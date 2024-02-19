import web
from models.modelo_usuario import Usuario

m_usuario = Usuario()

render = web.template.render('views/')

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        data = web.input()
        if data.username == m_usuario.usuario and data.password == m_usuario.password:
            web.setcookie("username", data.username)
            raise web.seeother('/bienvenida')
        else:
            return render.login()
