import web

class Index:
    def GET(self):
        try:
            return "Hola mundo"
        except Exception as e:
            return "Error" + str(e.args)
    