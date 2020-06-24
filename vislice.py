import bottle, model

ID_IGRE_COOKIE_NAME = 'id_igre'
COOKIE_SECRET = 'kakorkoli - secret key and passphrase'

vislice = model.Vislice()
vislice.preberi_iz_datoteke()

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def index():
    return bottle.template('Vislice-1\\views\\index.html')

@bottle.get('/img/<picture>')
def static_file(picture):
    return bottle.static_file(picture, root='Vislice-1\\img')

@bottle.post('/nova_igra/') #naredimo novo igro
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', str(id_nove_igre), path='/', secret=COOKIE_SECRET)
    bottle.redirect(f'/igra/') #MEEBE NAPAKA
    

@bottle.get('/igra/') #pokaze novo igro
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET)) 
    igra, stanje = vislice.igre[id_igre]

    return bottle.template('Vislice-1\\views\\igra.html', igra=igra, stanje=stanje, id_igre=id_igre, ZMAGA=igra.zmaga(), PORAZ=igra.poraz())

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/')

bottle.run(reloader=True, debug=True)
# reloader=True  -da zato ko kaj spremenimo v datotekah da ne rabmo na novo pognat programa
# debug=True  -da vidmo ko pride do napak