import web
urls=(
   '/','mvc.controllers.bienvenida.login.Login',
   '/index', 'mvc.controllers.bienvenida.nav.Nav',
   '/tienda','mvc.controllers.tienda.tiendas.Tiendas',
   '/despensa', 'mvc.controllers.despensa.des.Despensa',
   '/productos', 'mvc.controllers.productos.productos.Productos',
   '/historial', 'mvc.controllers.history.history.History',


)


app=web.application(urls,globals())

if __name__=="__main__":
    app.run()