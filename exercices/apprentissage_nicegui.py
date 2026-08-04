from nicegui import ui

ui.label('Welcome')  #texte simple

ui.link('La vidéo 2 de la playlist',
        'https://www.youtube.com/watch?v=YJcsmwP9tJM&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=2')   #lien

ui.markdown('This is **markdown**')   #gras

ui.html('This is <strong>HTML</strong>')   #html

ui.button('Click', color = 'red')   #bouton

ui.button('Click for a Nice', color = 'red', on_click = lambda : ui.label('Nice'))   #bouton avec action label

ui.button('Click for a Nice', color = 'blue', on_click = lambda : ui.link('La vidéo 2 de la playlist',
        'https://www.youtube.com/watch?v=YJcsmwP9tJM&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=2'))   #bouton avec action lien

ui.button('Click for a notify', color = 'green', on_click = lambda : ui.notify('You clicked'))   #bouton avec action notif

with ui.button('Click', color = 'red', on_click = lambda : badge.set_text(int(badge.text)+1)):   

    badge = ui.badge ('0', color = 'yellow').props('floating')    #bouton, si on clique cela augmente nombre en haut à droite du bouton

label = ui.label('Hi')

toggle_text = ui.toggle (['Text 1','Text 2'], value = 'Text 2', on_change = lambda : label.set_text(f'You clicked on {toggle_text.value}'))

#possible de faire les images pareils

#Dans le cas ou on aurait une image "man,png" et "women.png" et "england.png" avec "usa.png":

    #gender_image = ui.image('').classes('w-48')       w.48 pour la taille
    #radio.image = ui.image('').classes('w-48')

    #toggle_gender = ui.toggle(['man','woman'], on_click = lambda : gender.image.set_source(f"{toggle_gender.value}.png))
    # 
    # radio_country = ui.radio(['England','Usa'], on_click = lambda : radio.image.set_source(f"{radio.image.value}.png')) 


ui.run()   #lancer programme