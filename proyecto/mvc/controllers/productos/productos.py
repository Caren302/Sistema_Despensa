import web

class Productos:
    def GET(self):
        render = web.template.render("mvc/views/productos")
        b=""
        return render.lista(b)
