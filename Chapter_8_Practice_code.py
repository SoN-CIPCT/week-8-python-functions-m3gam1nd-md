#defining a function
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
# greet_user()

#passing info to a function
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")
# greet_user('jesse')
# greet_user('demian')

#practice 8-1
# def display_message():
#     """Display what I'm learning about in this chapter."""
#     print("I am learning about Python functions.")
# display_message()

#practice 8-2
# def favorite_book(title):
#     """Display favorite book titles."""
#     print(f"One of my favorite books is {title.title()}.")
# favorite_book('the hunt for red october')
# favorite_book('the inifinite game')

#call a function - positional argument
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type.title()}.")
#     print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')
# describe_pet('yorkipoo', 'paisley')

#call a function - keyword arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(animal_type='yorkipoo', pet_name='paisley')

#default parameter value
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='edward', animal_type='cat')
# describe_pet(pet_name='willie')
# describe_pet(pet_name='hercules')
# describe_pet(pet_name='chico')

#practice 8-3
# def make_shirt(text_size, text_message):
#     """Print a sentence summarizing the size and message for a shirt."""
#     print(f"\nThe text size for the shirt's lettering is {text_size}.")
#     print(f"The message printed on the shirt should be {text_message.title()}.")
# make_shirt(text_size='two inches', text_message='just do it')

#practice 8-4
# def make_shirt(shirt_size='large', text_message='i love pyhthon'):
#     """Print a sentence summarizing the size and message for a shirt."""
#     print(f"\nThe shirt size is {shirt_size}.")
#     print(f"The message printed on the shirt should be {text_message.title()}.")
# make_shirt(shirt_size='medium')
# make_shirt()
# make_shirt(shirt_size='small', text_message='i hate mondays')

#practice 8-5
# def describe_city(city_name, country='united states'):
#     """Print a sentence stating what country a city is in."""
#     print(f"{city_name.title()} is a city in {country.title()}.")
# describe_city(city_name='sacramento')
# describe_city(city_name='tacoma')
# describe_city(city_name='toronot', country='canada')

#returning a simple value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# president = get_formatted_name('george', 'washington')
# print(musician)
# print(president)

#making positional arguments optional - middle name is optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

#returning a dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name.title(), 'last': last_name.title()}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# return a dictionary and store an age
# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

#using a function in a loop
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     m_name = input("Middle name: ")
#     if m_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
    
#     if m_name:  
#         formatted_name = get_formatted_name(f_name, l_name, m_name)  
#     else:  
#         formatted_name = get_formatted_name(f_name, l_name)  

#     print(f"\nHello, {formatted_name}!")

#practice 8-6
# def city_country(city_name, country_name):
#     """Print city-country pairs"""
#     city_country_pair = f"{city_name.title()}, {country_name.title()}"
#     return city_country_pair
# pair_1 = city_country('paris', 'france')
# pair_2 = city_country('london', 'england')
# pair_3 = city_country('doha', 'qatar')
# print(pair_1)
# print(pair_2)
# print(pair_3)

#practice 8-7 - build a dictionary describing a music album with optional value
# def make_album(artist_name, album_title, number_songs=''):
#     """Return a dictionary of information about singers and their album."""
#     if number_songs:
#         album = f"{artist_name.title()}, {album_title.title()}, {number_songs} total songs on album"
#     else:
#         album = f"{artist_name.title()}, {album_title.title()}"
#     return album

# while True:
#     print(f'"\nEnter Artist Name:')
#     print("(enter 'q' at any time to quit)")
#     art_name = input("Artist Name: ")
#     if art_name == 'q':
#         break
#     alb_name = input("Album Name: ")
#     if alb_name == 'q':
#         break
#     num_songs = input("Enter total number of album songs: ")
#     if num_songs == 'q':
#         break
#     if num_songs:
#         full_info = make_album(art_name, alb_name, num_songs)
#     else:
#         full_info = make_album(art_name, alb_name)

#     print(f"\nAlbum Info: {full_info}")

# #passing a list to a function
# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

#modifying a list in a function
# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
# completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


#reorganize that code into two functions
# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none are left. Move each design to completed_models after printing."""

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# #input information
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #call both functions
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#practice 8-9 = pass list of short messages to function show_messages()
# def show_messages(texts):
#     """Print a series of messages from a list."""
#     for text in texts:
#         msg = f"Here's your message: {text.title()}!"
#         print(msg)
# messages = ['hi', 'hello', 'yo']
# show_messages(messages)

#practice 8-10 - print texts and move them to another list
# def messages(unprinted_text, printed_texts):
#     """Print texts and move to another list then confirm moved."""

#     while unprinted_text:
#         current_text = unprinted_text.pop()
#         print(f"Here's your message: {current_text}")
#         printed_texts.append(current_text)

# def show_printed_texts(printed_texts):
#     """Shows all printed texts"""
#     print("\nThe following texts have been printed:")
#     for printed_text in printed_texts:
#         print(printed_text)

# unprinted_text = ['hello you', 'where you at', 'when are you leaving']
# printed_texts = []

# messages(unprinted_text, printed_texts)
# show_printed_texts(printed_texts)

#practice 8-11 - add to last - call function send_messages() with a copy of the list of messages, then print both lists to show original has retained list
def messages(unprinted_text, printed_texts):
    """Print texts and move to another list then confirm moved."""

    while unprinted_text:
        current_text = unprinted_text.pop()
        print(f"Here's your message: {current_text}")
        printed_texts.append(current_text)

def show_printed_texts(printed_texts):
    """Shows all printed texts"""
    print("\nThe following texts have been printed:")
    for printed_text in printed_texts:
        print(printed_text)

def show_unprinted_texts(unprinted_text):
    """shows all what's still in the unprinted text list"""
    print(f"\nThese texts are preserved in the list: ")
    for unprinted_text in printed_texts:
        print(unprinted_text)

unprinted_text = ['hello you', 'where you at', 'when are you leaving']
printed_texts = []

messages(unprinted_text[:], printed_texts)
show_printed_texts(printed_texts)
show_unprinted_texts(unprinted_text)

