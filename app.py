import web

urls = (
    '/', 'controllers.index.Index',
    '/login', 'controllers.login.Login',
    '/bienvenida', 'controllers.bienvenida.Bienvenida'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()