import bottle, model

vislice = model.Vislice()

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def index():
    return bottle.template('index')

@bottle.get('/img/<pictures>')
def static_file(picture):
    return bottle.static_file(picture, 'img')

@bottle.get('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect(f'/igra/{id_igre}/')

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]

    return bottle.template('igra', igra=igra, stanje=stanje, id_igre=id_igre, ZMAGA=model.zmaga, PORAZ=model.poraz)

def ugibaj(id_igre):
    crka = bottle.request.forms.get('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/{id_igre}/')

bottle.run(reloader=True, debug=True)