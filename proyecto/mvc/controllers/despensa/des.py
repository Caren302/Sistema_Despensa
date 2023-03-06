import web

class Despensa:
    def GET(self):
        render = web.template.render("mvc/views/despensa")
        b=""
        return render.lista(b)
