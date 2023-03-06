import web

class Nav:
    def GET(self):
        render = web.template.render("mvc/views/")
        b=""
        return render.index(b)
    def POST(self):
        form=dict(web.input())
        if form['opcion']=='tienda':
           web.seeother('/tienda')
        elif form['opcion']=='despensa':
           web.seeother('/despensa')    
        elif form['opcion']=='productos':
           web.seeother('/productos')    
        elif form['opcion']=='history':
                web.seeother('/historial')  


    



    