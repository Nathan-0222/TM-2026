from nicegui import ui

##
#Texte
##

ui.label('Welcome')  #texte simple

ui.link('La vidéo 2 de la playlist',
        'https://www.youtube.com/watch?v=YJcsmwP9tJM&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=2')   #lien

ui.markdown('This is **markdown**')   #gras

ui.html('This is <strong>HTML</strong>')   #html

##
#Bouton sans/avec action
##

ui.button('Click', color = 'red')   #bouton

ui.button('Click for a Nice', color = 'red', on_click = lambda : ui.label('Nice'))   #bouton avec action label

ui.button('Click for a Nice', color = 'blue', on_click = lambda : ui.link('La vidéo 2 de la playlist',
        'https://www.youtube.com/watch?v=YJcsmwP9tJM&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=2'))   #bouton avec action lien

ui.button('Click for a notify', color = 'green', on_click = lambda : ui.notify('You clicked'))   #bouton avec action notif

with ui.button('Click', color = 'red', on_click = lambda : badge.set_text(int(badge.text)+1)):   

    badge = ui.badge ('0', color = 'yellow').props('floating')    #bouton, si on clique cela augmente nombre en haut à droite du bouton

label = ui.label('Hi')

##
#Toggle = Choisir 1 sur plusieurs éléments, avec animation ou couleur changée qd chosi (choisir man mettra l'image d'un mec, woman d'une femme)
##

toggle_text = ui.toggle (['Text 1','Text 2'], value = 'Text 2', on_change = lambda : label.set_text(f'You clicked on {toggle_text.value}'))

#possible de faire les images pareils

#Dans le cas ou on aurait une image "man,png" et "women.png" et "england.png" avec "usa.png":

    #gender_image = ui.image('').classes('w-48')       w.48 pour la taille
    #radio.image = ui.image('').classes('w-48')

    #toggle_gender = ui.toggle(['man','woman'], on_click = lambda : gender.image.set_source(f"{toggle_gender.value}.png))
    # 
    # radio_country = ui.radio(['England','Usa'], on_click = lambda : radio.image.set_source(f"{radio.image.value}.png'))    #Radio = autre type de toggle

##
#Select elements = chosir dans une liste un club de foot par exemple et lorsqu'on le valide avec un bouton on voit son image
##

players = ['Ibrahimovic','Messi','Ronaldo']

select_players = ui.select(players)

ui.button('Save Choice', color = 'blue', on_click = lambda : player_image.set_source(f'{select_players.value}.jpg'))

player_image = ui.image('').classes('w-38')


##
# Checkbox element : doit choisir un élément unique, si zéro ou deux marche pas. Mets à jour l'image + message d'erreur si pas possible
##

messi = ui.checkbox('Messi')
ronaldo = ui.checkbox('Ronaldo')

label = ui.label('Who do you choose ?')
player = ui.image('').classes('w-32')

def update_selection():
    if messi.value and ronaldo.value:
        label.set_text('You cannot choose both')
        player.set_visibility(False)
    elif not messi.value and not ronaldo.value:
        label.set_text('You need to choose one')
        player.set_visibility(False)
    elif messi.value:
        label.set_text('You chose Messi')
        player.set_visibility(True)
        player.set_source('messi.jpg')
    elif ronaldo.value:
        label.set_text('You chose Ronaldo')
        player.set_visibility(True)
        player.set_source('ronaldo.jpg')

ui.button('Save', on_click=update_selection)

##
#Switch element : bouton sur ligne si cliqué bouge du coté opposé, action si bouton du côté droit par exemple (sorte de checkbox)
##

def update():
    if football_switch.value:
        image.set_visibility(True)
        label.set_visibility(True)
        image.set_source('football.jpg')
        label.set_text('I prefer Football')
    elif basketball_switch.value:
        image.set_visibility(True)
        label.set_visibility(True)
        image.set_source('basketball.jpg')
        label.set_text('I prefer Basketball')
    elif football_switch.value and basketball_switch.value:
        image.set_visibility(False)
        label.set_visibility(False)
    elif not football_switch.value and not basketball_switch.value:
        image.set_visibility(False)
        label.set_visibility(False)

basketball_switch = ui.switch('Basketball', on_change=update)
football_switch = ui.switch('Football', on_change = update)

label = ui.label ('What do you prefer ?')
image = ui.image ('').classes('w-32')

##
#Slider element : barre dont on règle la valeur et selon elle cela fait une action différente
##

image = ui.image('').classes('w-32')

def refresh():

    label.set_text(f'Value : {slider.value}')

    if slider.value == 0:
        image.set_visibility(False)
    elif slider.value == 1:
        image.set_visibility(True)
        image.set_source('football.jpg')
    elif slider.value == 2:
        image.set_visibility(True)
        image.set_source('basketball.jpg')
    elif slider.value == 3:
        image.set_visibility(False)
        slider.disable()   #Bloque le curseur

label = ui.label ('Value : 0')
slider = ui.slider (min=0,max=3, on_change = lambda : refresh()).props('label-always')

##
#Joystick : Selon placement action différente (en X et Y)
##

joystick = ui.joystick(color = 'red', on_move = lambda e:set(e), on_end = lambda : coordinates.set_text('0, 0'))

def set(e):
    coordinates.set_text(f"{e.x:.3f}, {e.y:.3f}")

    if e.x > 0 and e.y > 0:
        image.set_source('football.jpg')
    elif e.x < 0 and e.y < 0:
        image.set_source('basketball.jpg')

coordinates = ui.label('0, 0')

image = ui.image('').classes('w-32')


ui.run()   #lancer programme