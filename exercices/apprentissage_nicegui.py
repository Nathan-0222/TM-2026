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

##
#Input elements
##

file_input = ui.input(label = 'File Name', placeholder = 'Enter a file name', password = False)   #si j'aurais mis en plus "password = True" on verrait pas les caractères

button = ui.button('Show Image', on_click = lambda : update())

def update():
    image.set_source(str(file_input.value))

image = ui.image('').classes('w-32')

##
#Text Area = zone de texte libre
##

name_input = ui.input (label = 'Name', placeholder='Enter the name of the sender')

text_area = ui.textarea(label = 'Message', placeholder = 'Write your message')

ui.button('Send Message', on_click = lambda : send())

def send():
    ui.chat_message(f'{text_area.value}', name = f'{name_input.value}', avatar = 'https://robohash.org/ui')
    name_input.value = ''
    text_area.value = ''

##
#Number Input : Insertion de deux nombres, selon bouton cliqué renvoie opération différente (+, -, ...)
##

first_number = ui.number(label='First Number', placeholder='Enter the first number')
second_number = ui.number(label='Second Number', placeholder='Enter the second number')

add_button = ui.button('+', on_click=lambda:calculate(add_button.text))
sub_button = ui.button('-', on_click=lambda:calculate(sub_button.text))
mul_button = ui.button('*', on_click=lambda:calculate(mul_button.text))
div_button = ui.button('/', on_click=lambda:calculate(div_button.text))

result = ui.label('Result')

def calculate(e):

    if e=='+':
        result.set_text(f'Result : {first_number.value+second_number.value}')
    if e=='-':
            result.set_text(f'Result : {first_number.value-second_number.value}')
    if e=='*':
            result.set_text(f'Result : {first_number.value*second_number.value}')
    if e=='/':
            result.set_text(f'Result : {first_number.value/second_number.value}')

##
#Knob Element : Roue comme les heures avec selon "l'heure" cela affiche une image
##

knob = ui.knob('0', min=0, max=100, color = 'red', show_value=True, on_change=lambda e: reset(e.value))

def reset(e):
    if e > 0 and e < 50:
        label.set_text('Football')
        image.set_source('football.jpg')
    if e > 50:
        label.set_text('Basketball')
        image.set_source('basketball.jpg')
    label1.set_text(f'{e}')


label = ui.label('/')
label1 = ui.label('')
image = ui.image ('').classes('w-32')

 ##
 #Color elements : Chnager grâce à un input directement ou grâce à une palette de couleur la couleur d'un élément (ici un label)
 ##

label = ui.label('Hello Nathan')

color_input = ui.color_input(label='Color', value='#000000', on_change=lambda:update())

def update():
    label.style(f'color:{color_input.value}')

button = ui.button(icon='colorize', on_click=lambda:picker())

def picker():
    ui.color_picker(on_pick=lambda e:button.style(f'background-color : {e.color}!important'))

##
#Date Input Element : Calendrier, quand selectionné met par exemple cb de jours avant cette date

import datetime   #important
first_date = ui.date(value='2000-01-01', on_change=lambda:calculate())

def calculate():
    first_date_value = first_date.value
    current_date = str(datetime.datetime.now())

    t1 = datetime.datetime(year=int(first_date_value[0:4]),
                           month=int(first_date_value[5:7]),
                           day=int(first_date_value[8:10]))

    t2 = datetime.datetime(year=int(current_date[0:4]),
                               month=int(current_date[5:7]),
                               day=int(current_date[8:10]))
    label.set_text(str(t2-t1)[:-9])

label = ui.label('')

##
#Time element : la date et le temps (en input interractif) seront connectés et indiqués via un label
##

clock = ui.time(value='', on_change=lambda:update())

date = ui.date(value='', on_change=lambda:update())

label = ui.label('Time')

def update():
    label.set_text(f'Time : {str(clock.value)} {str(date.value)}')

##
#File upload : Téléchargement d'un fichier sur la page web
#

from nicegui import ui, events

def uploads(e: events.UploadEventArguments):
    text = e.content.read().decode("utf-8")
    label.set_text(text)

ui.upload(
    on_upload=lambda e: uploads(e), 
    on_rejected=lambda e: ui.notify('Only text files !!')
).props('accept=.txt').classes('max-w-full')

label = ui.label('Voici le texte de votre fichier')

##
#Image Elements : quand cliqué, redirigé par un lien
##

with ui.row():   #Pour les aligner

    with ui.link(target ='https://www.youtube.com/watch?v=srEtZH79atw&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=19'):
        with ui.image('football.jpg').classes('w-40'):
            ui.label('Football !!').classes('absolute-bottom text-subtitle2 text-center')

    with ui.link(target ='https://www.youtube.com/watch?v=srEtZH79atw&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=19'):
        with ui.image('basketball.jpg').classes('w-40'):
            ui.label('Basketball !!').classes('absolute-bottom text-subtitle2 text-center')

##
#Audio Element
##

#label = ui.label('Audio Tutorial')

#audio = ui.audio('music.mp3)

#with ui.row():

    #ui.button = ('Play', color ='blue', on_click=audio.play)
    #ui.button = ('Pause', color = 'red', on_click=audio.pause)
    #ui.button = ('Jump to 0:45', on_click = lambda : audio.seek(45))


##
#Vidéo Element
##

#label = ui.label('Video Tutorial')

#video = ui.video('drone.mp4').classes('w-50')

#with ui.row():
    #ui.button = ('Play', color ='blue', icon='play_circle', on_click=video.play)
    #ui.button = ('Pause', color = 'red', icon ='pause_circle', on_click=video.pause)
    #ui.button = ('Jump to 0:05', on_click = lambda : video.seek(5))


##
#Table Element : Input puis résultat stockés dans un tableau
#

name = ui.input('Name', placeholder='Enter your name')
age = ui.input('Age', placeholder='Enter your age')

save = ui.button('Save', on_click=lambda:save())

def save():
    new_dict = {'name':f'{name.value}','age':f'{age.value}'}
    rows.append(new_dict)
    table.update()
    name.value=''
    age.value=''

columns = [{
    'label':'Name', 'field':'name'},
    {'label':'Age', 'field':'age'}]

rows = []

table = ui.table(columns=columns, rows=rows)


##
#Highchart Element : Stockage des valeurs d'un input dans un Graphique (pas dans un tableau)
##


company = ui.input('Company Name', placeholder='Enter the name of your Company')
stocks = ui.input('Stocks', placeholder='Enter your stocks')

save = ui.button('Save', on_click=lambda:save_button())

list_company = []

def save_button():
    new_dict = {'name':f'{company.value}','data':[int(stocks.value)]}
    list_company.append(new_dict)
    chart.update()

chart = ui.highchart({
    'title': False,                
    'chart': {'type': 'bar'},      
    'xAxis': {'categories': ['Companies']},
    'series': list_company
}).classes('w-100')


##
#Linear Progress Element : S'il y à par exemple 4 Input à remplir, la barre sera à 0% et augmentera de 25% par input rempli (progression de chose à remplir sous forme de barre)
##

name = ui.input('Name', on_change = lambda:update())
surname = ui.input('Surname', on_change = lambda:update())
gender = ui.radio(['Male','Female'], on_change = lambda:update())   #Choix entre les deux
country = ui.select(['Germany','England','France','Switzerland'], on_change = lambda:update())

button = ui.button('Save', icon='save', color = 'green', on_click=lambda:save())

slider = ui.slider(min=0,max=100,step=25, value=0)

linear_progress = ui.linear_progress().bind_value_from(slider,'value')

def update():
    if name.value != '' and slider.value < 25:
        slider.value = slider.value + 25
    if surname.value != '' and slider.value <= 25:
            slider.value = slider.value + 25
    if gender.value != None and slider.value <= 50:
            slider.value = slider.value + 25
    if country.value != None and slider.value <= 75:
            slider.value = slider.value + 25

def save():
     ui.label(f'{name.value} {surname.value} {gender.value} {country.value}')



##
# Circular Progress Element : Avancée de la progression comme avant, mais ous forme de rond circulaire (pas ligne). Deux version
##

##Première version : Barre linéaire (step = 25), tous les 25 change d'image, progression circulaire l'illustre avec valeur au centre
slider = ui.slider(min=0,max=100,step=25,value=0, on_change=lambda:set_image())

circular = ui.circular_progress().bind_value_from(slider,'value')

def set_image():
    if slider.value <= 25:
            image.set_source('football.jpg')
    if slider.value <= 50 and slider.value > 25:
            image.set_source('messi.jpg')
    if slider.value <= 75 and slider.value > 50:
            image.set_source('ronaldo.jpg')
    if slider.value <= 100 and slider.value > 75:
            image.set_source('basketball.jpg')

image = ui.image('').classes('w-32')

##Deuxième Version : Chaque fois que bouton pressé, image change
with ui.circular_progress(min=0, max=100, value=0, show_value=False) as progress:
     ui.button(
          icon='star',
          on_click=lambda:set_image()
     ).props('flat round')

def set_image():
    progress.set_value(progress.value + 25)
    if progress.value <= 25:
            image.set_source('football.jpg')
    if progress.value <= 50 and progress.value > 25:
            image.set_source('messi.jpg')
    if progress.value <= 75 and progress.value > 50:
            image.set_source('ronaldo.jpg')
    if progress.value <= 100 and progress.value > 75:
            image.set_source('basketball.jpg')

image = ui.image('').classes('w-32')


##
#Leaflet element : Carte région/pays/..., bouton servant à zoomer, etc..
##

map = ui.leaflet(center=(48.864, 2.349))   #Donne le centre de notre carte (eniron zone d'action au début) en donnant la lattitude et longitude

ui.label().bind_text_from(map, 'center', lambda center:f'Center : {center[0]:.3f}, {center[1]:.3f}')

ui.label().bind_text_from(map, 'zoom', lambda zoom:f'Zoom : {zoom}')

with ui.row():
    ui.button('New-York', color='red', on_click=lambda:map.set_center((40.730, -73.935)))
    ui.button('London', color='green', on_click=lambda:map.set_center((51.509, -0.118)))

with ui.row():
    ui.button(icon='zoom_in', on_click=lambda:map.set_zoom(map.zoom + 1))
    ui.button(icon='zoom_out', on_click=lambda:map.set_zoom(map.zoom - 1))


##
#Tree Element : Arbre affichant les différents groupe d'input (Sujet puis description), dès que save enregistré et lors d'un nouveau save le nouveau groupe sera enregistré en dessous
##

topic = ui.input('Topic')
text = ui.textarea(label = 'Description')

save = ui.button('Save', color = 'green', icon = 'save', on_click = lambda:save())

dict_list=[]

def save():
    new_dict = {'id' : f'{topic.value}', 'description':f'{text.value}'}
    dict_list.append(new_dict)

tree = ui.tree('id' : 'topic', 'text', 'children':dict_list)

tree.add_slot('default-header', '''
    <span:props='props>Node<strong>{{props.node.id}}</strong></span>    
''')   #Html code

tree.add_slot('default-body', '''
    <span:props='props>Text: '{{props.node.text}}'</span> 
''')   #Html code


##
# Log record view : Lorsque deux input rempli et 'save' grâce au bouton,  affiche les résultats qu'on a mis dans une sorte de "terminal" avec l'heure aussi
##

from datetime import datetime

name = ui.input('Name')
surname = ui.input('Surname')

save = ui.button('Save', color = 'green', icon = 'save', on_click = lambda:save())
log = ui.log (max_lines=10).classes('w-full h-20')   #Sorte de 'Terminal' mentionné

def save ():
     log.push(f'You enterred -> Name : {name.value}, Surname : {surname.value}\{datetime.now().strftime('%X.%f')[:-5]}')




ui.run()   #lancer programme