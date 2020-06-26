import web # pip installl web.py

urls = (
    '/formulario', 'application.controllers.form.Form', #/= raiz  Hello la clase 
    '/formulariovista', 'application.controllers.formvista.FormVista'

)
app = web.application(urls, globals())

render = web.template.render('templates/')





if __name__ == "__main__":
    web.config.debug= False
    app.run()