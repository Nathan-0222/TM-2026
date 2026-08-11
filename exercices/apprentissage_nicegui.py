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

tree = ui.tree([{'id': 'topic', 'text': 'Valeur_du_texte', 'children': dict_list}])

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


##
#Editor Element : Zone de texte, dans laquelle on peut modifier le texte séléctionné avec des boutons (mettre en italique, mettre en gras,...)
##

editor = ui.editor(placeholder='Type something', on_change=lambda:write())

def write():
    text.set_text(f'HTML code : {editor.value}')

text = ui.label('')


##
#Code Element : Zone de texte dans laquelle on écrit en code ce qu'on veut, puis cela nous renvoie le code bien structuré
##

text_area = ui.textarea('Text', placeholder='Type your cods here !!')

button = ui.button('Save', color ='green', icon='save', on_click=lambda:save())

def save():
    ui.code(text_area.value)


##
#JSON Editor : Deux Input, quand sauvegarder renvoie un element json avec les valeurs saisies(si deuxième nom mis après, crée un nouveau)
##

name = ui.input('Name')
surname = ui.input('Surname')

save_button = ui.button('Save', icon = 'save', color='green')

def save():
     json = {'name' : name.value, 'surname' : surname.value}

     ui.json_editor({'content' : {'json':json}})


##
# Bind Text From : Exemple d'utilisation de la fonction 'bind text from', avec deux input puis un choix entre les deux nombres, pour que avec deux boutons on puisse augmenter ou diminuer la valeur du nombre choisi
##

data = {'number_1':20, 'number_2':25}

ui.label().bind_text_from(data, 'number_1', backward=lambda a:f'First Number : {a}')
ui.label().bind_text_from(data, 'number_2', backward=lambda a:f'Second Number : {a}')

select = ui.select (['first number', 'second number'])


with ui.row():
    ui.button('UP', color = 'green', icon = 'trending_up', on_click=lambda:up())
    ui.button('DOWN', color = 'red', icon = 'trending_down', on_click=lambda:down())

def up():
    if select.value == 'first number':
         date.update(number_1 = data['number_1'] + 1) 
    if select.value == 'second number':
             date.update(number_2 = data['number_2'] + 1) 

def down():
    if select.value == 'second number':
         date.update(number_2 = data['number_2'] - 1) 
    if select.value == 'first number':
             date.update(number_1 = data['number_1'] - 1) 


##
#Card element : Crée deux cartes avec du texte dessus, une image, un lien ou un choix, ...
##
with ui.row():
    with ui.card():
        ui.label('Messi Card')
        with ui.card().tight():
            ui.image('messi.jpg').classes('w-35')
            with ui.card_section():
                ui.label('Here is messi')
                with ui.expansion('Show the video', icon='work').classes('w-full'):
                     ui.link('Video', 'https://www.youtube.com/watch?v=9Dh-B_kLOpc&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=33')

    with ui.card():
        ui.label('Ronaldo Card')
        with ui.card().tight():
            ui.image('ronaldo.jpg').classes('w-35')
            with ui.card_section():
                 ui.label('Here is ronaldo')
                 with ui.expansion('Show the video', icon='work').classes('w-full'):
                                      ui.link('Video', 'https://www.youtube.com/watch?v=9Dh-B_kLOpc&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=33')


##
#Grid element : On saisit des valeurs dans des input, puis quand bouton pressé les données s'enregistrent dans un élément nommé le 'grid element' = renvoie données saisies
##

name = ui.input('Name')
surname = ui.input('Surname')
height = ui.input('Height')

save = ui.button('Save', icon = 'save', color = 'green', on_click = lambda:save_func())

with ui.grid(columns=2):
    name_title = ui.label('Name :')
    name_value = ui.label('')

    age_title = ui.label('Age :')
    age_value = ui.label('')

    height_title = ui.label('Name :')
    height_value = ui.label('')

def save_func():
     name_value.set_text(name)
     age_value.set_text(age)
     height_value.set_text(height)


##
#Expansion Element : Deux input, quand save grâce à bouton, renvoie un 'expansion object', donc une sorte de carte et lorsque tu appuis dessus, un menu défile avec une image et un texte qui peut être un lien,...
##

expansion_input = ui.input('Name')
image_file = ui.input('Image file')

save = ui.button('Save', icon = 'save', color = 'green', on_click = lambda:save_funct())

def save_funct():
     with ui.expansion(f'{expansion_input.value}', icon ='work').calsses('w-full'):
          ui.image(f'{image_file.value}.jpg').classes('w-40')
          ui.label(f'Free {image_file.value} Course!!')


##
#Scroll Area Element : Deux cartes avec un expension element, lorsque cliqué sur cet élément on voit une text area avec du texte qu'on peut scroller(barre latérale de défilement)
##

with ui.row():
    with ui.card().tight():
        ui.image('messi.jpg').classes('w-35')
        with ui.expansion('Messi secret', icon = 'work').classes('w-full'):
            with ui.scroll_area('w-80 h-64 border'):
                ui.label('Exemple') 

    with ui.card().tight():
            ui.image('ronaldo.jpg').classes('w-35')
            with ui.expansion('Ronaldo secret', icon = 'work').classes('w-full'):
                with ui.scroll_area('w-80 h-64 border'):
                    ui.label('Exemple') 


##
#Separator and splitter element : Deux éléments à coté qu'ont peut bouger sur la page en largeur sur une taille définie, élément peut recouvrir l'autre... = Elements aujstables sur la page directement
##

#Separator Element (barre fin grise servant de séparateur):
ui.image('messi.jpg').classes('w-32')

ui.separator()

ui.image('ronaldo.jpg').classes('w-32')

#Splitter Element (éléments déplaçable):
with ui.splitter().classes('w-64') as splitter:
     with splitter.before:
          ui.image('ronaldo.jpg').classes('w-12')
          ui.label('Ronaldo')
     with splitter.after:
          ui.image('messi.jpg').classes('w-12')
          ui.label('Messi')


##
#Tabs Element : Deux colonnes (Login et Sign up), sous ligné lorsque entrain de remplir éléments de la colonne(input). Si je suis sur les éléments de la colonne Login, je ne verrai pas les éléments de la colonne Sign up
##

with ui.tabs().classes('w-96') as tabs:
     login = ui.tab('Login')
     signup = ui.tab('Sign up')

with ui.tab_panels(tabs, value = login).classes('w-96'):
     with ui.tab_panel(login):
          username = ui.input('Username')
          password = ui.input('Password', password = True)
          button = ui.button('Save', icon = 'login', color = 'green')
     with ui.tab_panel(signup):
               username = ui.input('Username')
               password = ui.input('Password', password = True)
               button = ui.button('Sign up',)


##
#Stepper Element : Séries de tâches à remplir en complétant un input par exemple, lorsque remplit passe au suivant (on voit pas le contenu des autre 'tâches' lorsqu'on complète les input d'une par exemple) + boutons d'actions
##

with ui.stepper().props('vertical').classes('w-full') as stepper:
     with ui.step('Enter your name'):
          name = ui.input('Name')
          with ui.stepper_navigation():
               ui.button('Next', on_click = stepper.next)
     with ui.step('Enter your age'):
          age = ui.input('Age')
          with ui.stepper_navigation():
                         ui.button('Next', on_click = stepper.next)
                         ui.button('Back', on_click = stepper.previous).props('flat')
     with ui.step('Enter your Country'):
               country = ui.input('Country')
               with ui.stepper_navigation():
                              ui.button('Done', on_click = lambda:ui.notify('Completed!', type = 'positive'))
                              ui.button('Show input', on_click = lambda:show())
                              ui.button('Back', on_click = stepper.previous).props('flat')
def show():
     ui.label(f'Name:{name.value} - Age:{age.value} - Country:{country.value}')


##
#Timeline Element : éléments comme image référés à une certaine date placés dans l'ordre chronologique de leur arrivée (1ère guerre mondiale, 2ème, ...)
##

with ui.timeline(side = 'right'):

     ui.image('messi.jpg').classes('w-32')
     ui.timeline_entry('Messi', title = 'First', subtitle = 'July 24, 2019')

     ui.image('ronaldo.jpg').classes('w-32')
     ui.timeline_entry('Ronaldo', title = 'Second', subtitle = 'March 28, 2021')

     ui.image('ibrahimovic.jpg').classes('w-32')
     ui.timeline_entry('Ibrahimovic', title = 'Third', subtitle = 'February 4, 2024')


##
#Carousel Element : Une série d'image, une seule affichée mais flèches à droite et à gauche pour la faire passer à la suivante/précédente
##

with ui.carousel(arrows = True, navigation = True).props('height = 340px'):
     
     with ui.carousel_slide().classes('p-0'):
         with ui.card().tight():
            ui.label('Messi')
            with ui.card_section:
                ui.image('messi.jpg').classes('w-[280px]')

     with ui.carousel_slide().classes('p-0'):
         with ui.card().tight():
            ui.label('Ronaldo')
            with ui.card_section:
                ui.image('ronaldo.jpg').classes('w-[280px]')

     with ui.carousel_slide().classes('p-0'):
         with ui.card().tight():
            ui.label('Ibrahimovic')
            with ui.card_section:
                ui.image('ibrahimovic.jpg').classes('w-[280px]')


##
#Pagination Element : Sortes de pages web. Image et texte par exemple sur page 1. En bas avec des flèches on peut changer la page (1-2-3), et voir donc une autre image et texte
##

image = ui.image('').classes('w-32')
a = ui.label('')
p = ui.pagination(1,3, direction_links=True, on_change=lambda:show())

def show():
     if p.value == 1:
          image.set_source('messi.jpg')
          a.set_text('Messi')

     if p.value == 2:
              image.set_source('ronaldo.jpg')
              a.set_text('Ronaldo')

     if p.value == 1:
              image.set_source('ibrahimovic.jpg')
              a.set_text('Ibrahimovic')


##
#Menu Element : 3 petites barres en haut à droite de l'écran pour changer de 'page' -> Menu de site web (comme une nav)
##

with ui,row().classes('w-full items-center'):
     result = ui.label().classes('mr-auto')
     with ui.button(icon = 'menu'):
          with ui.menu() as menu:
               ui.menu_item('Ronaldo', lambda:show_ronaldo())
               ui.menu_item('Messi', lambda:show_messi())
               ui.menu_item('Ibrahimovic', lambda:show_ibra())
               ui.separator()
               ui.menu_item('Close', on_click = menu.close)
     

image = ui.image('').classes('w-72')
text = ui.label('')

def show_ronaldo():
     image.set_source('ronaldo.jpg')
     text.set_text('Ronaldo')

def show_messi():
     image.set_source('messi.jpg')
     text.set_text('Messi')

def show_ibra():
     image.set_source('ibrahimovic.jpg')
     text.set_text('Ibrahimovic')


##
#Tooltip Element : Lorsque curseur sur image par exemple, texte apparaît en bas
##

with ui.row():
     
    with ui.image('messi.jpg').classes('w-16'):
        ui.tooltip('Messi').classes('w-48')

    with ui.image('ronaldo.jpg').classes('w-16'):
        ui.tooltip('Ronaldo')

    with ui.image('Ibrahimovic.jpg').classes('w-16'):
        ui.tooltip('Ibrahimovic')


##
#Notify Element : 3 Input avec bouton, si 3 éléments saisis notif comme quoi c'est tout bon, si une pas mise message d'erreur en disant qu'il faut tout noter, si aucune notée message d'erreur complet
##

name = ui.input('Name')
age = ui.input('age')
Country = ui.input('Country')

ui.button('Save', color = 'green', on_click = lambda:show_notify())

def show_notify():

     value = 0
     
     if name.value == '' and country.value == '' and age.value == '':
        value = 1
        ui.notify('You entered none of them!', type = 'negative')

     if (name.value == '' or country.value == '' or age.value == '') and value == 0:
             ui.notify('You did not enter one of theme!', type = 'warning')

     if (name.value != '' and country.value != '' and age.value == '') and value == 0:
             ui.notify('That is okay!', type = 'positive')


##
#Dialog Element : Deux Input, un bouton 'show' qui renvoit une question à l'utilisateur : il demande s'il veut montrer ses input avec deux coix possible, oui ou non. Si non, rien montré, si oui, résultat des deux input montré
##

with ui.dialog() as dialog, ui.card:
     ui.label('Are you Sure ?')
     with ui.row():
          ui.button('Yes', on_click = lambda: dialog.submit('Yes'))
          ui.button('No', on_click = lambda: dialog.submit('No'))

async def show():
     result = await dialog
     if result == 'Yes':
         text.set_text(f'{name.value} {country.value}')
         name.value = ''
         country.value = ''

     if result == 'No':
          text.set_text('')

ui.button('Show', on_click = show)

name = ui.input('Name')
country = ui.input('Country')
text = ui.label('Info!')







ui.run()   #lancer programme