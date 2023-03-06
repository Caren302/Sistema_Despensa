import web

class Tiendas:
    def GET(self):
        render = web.template.render("mvc/views/tiendas")
        b=""
        return render.lista(b)
