import web
urls=(
    '/.*','mvc.controllers.bienvenida.login.Login'
)


app=web.application(urls,globals())

if __name__=="__main__":
    app.run()