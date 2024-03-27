#Katie Pimentel
#Last time I worked on this: 12 July 2022

#References:
#lines 89 - 97: https://www.youtube.com/watchv=2h8e0tXHfk0ab_channel=LearnLearnScratchTutorials

#-----------------------------------------------------------


#putting things in different files and trying to import it here just to lesson the amount of code here
from inv_int import inventory, interactions
from effect_type import typewriter
from beg_screen import title_screen

#inventory function
def the_inventory():
	input('Welcome to your inventory.. ')  #welcoming message
	print('You currently have this in it: ')
	inv_things = ', '.join(inventory)  #to print out what is in your inventory nicely
	print(inv_things)
	user_input = input('What would you like to interact with? ')
	
	if user_input == 'matches':
			input('I used this to light the wall light. I wonder if it\'s for something else.')
		
	elif user_input == 'watch':
			if 'watch' in inventory:  #have to check if it's here. if not, it will say it's not a valid input
					if 'journal' in interactions:  #after interacting with the journal, you have the option to smash it open
							if 'watch key' not in inventory:  #to make sure that it you don't get to break open the watch twice
									input('So, there\'s a secret compartment in here. ')
									user = input(
											'Should I break this open and see if there\'s anything inside? (Y/N) '
									)
									if user in y:
											input('Okay, time to smash this. ')
											input(
													'I look down on what I smashed, and out comes a key. '
											)
											inventory.append('watch key')
											input('I wonder what I can use this key for.. ')
											room()

									if user in n:
											room()

									else:
											print('That is not a valid input. ')
											the_inventory()

					elif 'watch key' in inventory:  #it will just give a message saying that it's broken and you got a key from it. You can also choose to interact with the watches memory again.
							input('I already broke this watch and got a key from it. ')
							user = input('Should I interact with this watch again? (Y/N) ')
							if user in y:
									watch()
							if user in n:
									room()
							else:
									print('That is not a valid input.\n')
									the_inventory()

					elif 'journal' not in interactions:
							watch()

			elif 'watch' not in inventory:
					print('That is not a valid input. ')
					the_inventory()

	elif user_input == 'closet key':
			if 'closet key' in inventory:
					input('I could use this key to open something.. ')
					room()
			else:
					print('That is not a valid input. ')
					the_inventory()

	elif user_input == 'watch key':
			if 'watch key' in inventory:
					input('I could use this key to open something.. ')
					room()
			else:
					print('That is not a valid input. ')
					the_inventory()

	else:
			print('That is not a valid input. ')
			the_inventory()

#for the things that people input. I don't really need all of this tho since like i could just put something like bed = "bed" and just put user.lower == bed. you know? I have to make that change tho to almost every single piece of code that says that. Maybe there's an easier way to do it, so for now, it's gonna stay like this. too tired to be making changes like that rn. 

things_like_bed = ['BED','bed', 'Bed']  #when people type in anything having to do with bed
things_like_closet = ['CLOSET', 'closet', 'Closet']  #when people type in anything having to do with the closet
things_like_nightstand = ['NIGHTSTAND', 'nightstand', 'Nightstand']  #when people type in anything having to do with the nightstand
things_like_door = ['DOOR', 'door', 'Door']  #when people type in anything having to do with the door
things_like_bookshelf = ['BOOKSHELF', 'SHELF', 'bookshelf', 'bookcase', 'shelf', 'Bookshelf']  #when people type in anything having to do with the bookshelf
like_inventory = ['INVENTORY', 'inventory', 'Inventory']
y = ['Y', 'y']
n = ['N', 'n']
snuffles = ['Snuffles', 'SNUFFLES', 'snuffles']
journal = ['Journal', 'journal', 'JOURNAL']
newspaper = ['Newspaper', 'NEWSPAPER', 'newspaper']


#main loop for the room
def room():
	while 'candle' not in interactions:  #candle is the last thing that you have to interact with
		print('\nWhat would you like to interact with? Type the following... ')
		user_input = input('bed, closet, nightstand, door, bookshelf, inventory: ')
		if user_input in things_like_bed:
			bed()
		elif user_input in things_like_closet:
			closet()
		elif user_input in things_like_nightstand:
			nightstand()
		elif user_input in things_like_door:
			exit_door()
		elif user_input in things_like_bookshelf:
			bookshelf()
		elif user_input in like_inventory:
			the_inventory()
		else:
			print('That is not a valid input. ')
	input('Oh wow, looks like I\'ve gotten all of the clues. ')
	input('A hatchet in the middle of the floor opened. ')
	the_end()


#---------------------------------------------------------
#for interactions with the bed


#the story behind the stuffed animal
def watch():
	message = 'This watch ... is Adriana\'s fathers. I was there when she found out that her dad died. He had killed himself with his own power ... It must\'ve been so hard for her mother to find him burnt to a crisp at his desk. This watch is all she has left of him.\n'

#have to add after the person interacts with the journal, they can access their inventory and open the watch. Have to make a function to interact with the inventory
	if 'watch' not in inventory:
		print('\nThere seems to be a thread hanging out of this stuffed animal..')
		input ('I just want to... ')
		typewriter('Pull it. ')
		input ('\nWoops, the head came off. But there seems to be something in it. A watch? ')

		typewriter(message)
		inventory.append('watch')
		input('\nWow.. Adriana. I\'m so sorry about your dad. ')
		input('There was no response. ')
		room()

	elif 'watch' in inventory:
			user_input = input('Would you like to interact with this watch again?(Y/N) ')
			if user_input in y:
					print(message)
					room()
			if user_input in n:
					room()
			else:
					room()


def stuffed_animal():
	message = '\nI remember this stuffed animal. When I was about 4 years old, there was this girl who would always get bullied. She never really paid attention to them and just played with her stuffed animal. \nOne day, they were really going at it and ripped the head of her stuffed animal open... It was so evil. Nobody knew how she was going to respond. Everyone thought she was just going to throw a tantrum. Instead, she stood there in rage. \nShe held out her hand and they were all in the air, choking. There were going to die if she continued, so I tackled her to the ground. She snapped out of it and then she ran away. \nI felt really bad for her. Even though it was a bit scary, she couldn\'t control what powers she got. Her stuffed animal was on the floor. I took it home and sewed it with a sewing kit I found in a closet.\nThe next day, I went up to her and gave her the stuffed animal. The head was a bit lopsided, but she took it anyways. She said "I love it." She told me that was the first time she used her powers.\nWe became friends after that and for a long time too.\n'

	if 'stuffed animal' not in interactions:
			user_input = input('\nDo you want to interact with it? (Y/N) ')
			if user_input in y:
					typewriter(message)
					interactions.append('stuffed animal')
					input('\n... Her name is Adriana ... Adriana Fauna Polanco.. ')
					input('\nWait... Are you Adriana? ')
					input('"Yes." ')
					input('Why did we stop being friends? ')
					input('"You\'re going to have to find that out on your own." ')
					input('Was it bad? ')
					input(
							'There was a pause before she said, "I guess that depends." ')
					input('The mic cut off. ')
					watch()
					room()

			if user_input in n:
					room()
			else:
					print('That is not a valid input')
					stuffed_animal()

	elif 'stuffed animal' in interactions:
			user_input = input(
					'\nWould you like to interact with the stuffed animal again? (Y/N) '
			)
			if user_input in y:
					print(message)
					watch()
					print('\nokay, now back to everything else..')
					room()

			if user_input in n:
					room()
			else:
					print('That is not a valid input.\n')
					stuffed_animal()


#interaction with the bed
def bed():
	print('\nYou have interacted with the bed. ')
	print('There seems to be a stuffed animal on the bed. ')
	stuffed_animal()


#---------------------------------------------------------
#for the bookshelf
def book():
	message = 'I remember this book. It was one of my favorite books as a kid. Me and Adriana would always act things out with our dolls. Adriana would always make them move with her powers. It was always so fun. Her favorite character was Snuffles. Snuffles was quite shy and would always overthink everything. Mine was Sera because she never took shit from everyone. She was everything I aspired to be. And she had the same power as me: being able to make things stop. A weird power, but I learned a lot from her.\n'

	if 'book' not in interactions:
		if 'stuffed animal' in interactions:
				typewriter(message)
				interactions.append('book')
				input('\nHmm.. Snuffles. That was the name of her stuffed animal. ')
				room()

		elif 'stuffed animal' not in interactions:
				input('This doesn\'t seem to give me anything ... Maybe I need to go somewhere else. ')
				room()

	elif 'book' in interactions:
		user = input('Do you want to interact with the book again? (Y/N) ')
		if user in y:
				print(message)
				room()
		if user in n:
				room()
		else:
				input('That is not a valid input. ')
				book()


def bookshelf():
	print('You have interacted with the bookshelf. There seems to be a book...')
	user = input('\nDo you want to interact with this book? (Y/N) ')

	if user in y:
			book()
	if user in n:
			room()
	else:
			print('That is not a valid input. \n')
			bookshelf()


#---------------------------------------------------------
#for the closet
def costume():
	message = 'I know these costumes. One of them are Adriana\'s. and oh wow.. my costume. When I was 18, I started living with Adriana. I ran away from my aunt\'s house. I packed all of my things and never looked back. \nWe went to college together. But, we didn\'t feel fulfilled with what they were doing. The justice system is absolute shit. It would take decades of change in order to change things. \nAdriana had always been one for waiting, but I wasn\'t. I gave her the idea of us becoming a superhero duo to keep awful people off of the streets. All of this while doing things for our community. We fought so many people. I was Red Light since I had the power to stop things. Her name was Celebre which is just brain in Spanish. I thought it was kind of dumb, but she loved it, which was cute. That was honestly so fun.\n '
	if 'costume' not in interactions:
		typewriter(message)
		interactions.append('costume')
	elif 'costume' in interactions:
		user = input('Do you want to interact with the costume again? ')
		if user in y:
				print(message)
		if user in n:
				room()
		else:
				print('That is not a valid input. ')
				costume()


def closet_key():
	if 'closet key' in inventory:
			input('I already have this key.. ')
	elif 'closet key' not in inventory:
			input('Look a key! This might open something in this room... ')
			inventory.append('closet key')


def closet():
	print('\nYou have clicked the closet.. ')
	
	if 'costume' in interactions:
			input('It\'s still unlocked. ')
			costume()

	if 'costume' not in interactions:
		if 'book' in interactions:
			print('There seems to be a lock on the door. It requires a word to unlock it. ')
			input('"You have touched the book, so I will give you a clue to unlock this." ')
			input('"What is something that is close to my heart?" ')
			
			user_input = input('What is something that is close to Adriana\'s heart? \nTYPE YOUR ANSWER HERE:  ')
			if user_input in snuffles:
				input('Aww really? It was that important to you? ')
				input('"I treasured that stuffed animal a lot. You had sewn it for me. Even if the head was tilted." ')
				input('\nWell, I opened the closet door! In it, there seems to be some sort of costume and a key. ')
				user_input = input('What would you like to interact with? The costume or key? \nTYPE YOUR ANSWER HERE: ')
			
				if user_input == 'costume':
					costume()
					input ("\nTime to interact with the key.")
					closet_key()
					room()
				elif user_input == 'key':
					closet_key()
					input('\nTime to interact with the costume. ')
					costume()
					room()
				else:
					print ("That is not a valid input. ")
					closet()
			
			else:
					print('Wrong input. Maybe try looking a little closer. ')
					user = input('Do you want to try again? (Y/N) ')
					if user in y:
							closet()
					if user in n:
							room()
					else:
						print('That is not a valid input. \n')
						room()

		elif 'book' not in interactions:
			input('There\'s a lock on this.')
			input('Maybe I should look around a little more. There seems to be no clues ... ')
			room()


#---------------------------------------------------------
#for the nightstand


#ontop of the nightstand
def picture():
	message = '\nI know who these people are... \nThey\'re my parents... I don\'t remember much about them, but I know this picture. There\'s tears falling out of my eyes, and I felt my entire body scrunch up. \nThey left me... \nNot only did they leave me, but they left me with my aunt. \nMy aunt was a terrible woman. Nothing I did was ever enough. I would go home, and the first thing she would do was scream. Scream about how I\'m useless. How I shouldn\'t exist. I was a disgrace. When she would hit me, I would go to my room and just look at this picture. Asking them to save me... \nTo come back home. \nBut, they never did. They left me with that horrible fucking woman and for what? I don\'t even know to this day.\nI would tell Adriana about it sometimes. I would sleep over there a lot. My aunt never cared enough to check my room that often. Adriana was always so supportive. She never knew what to say, but just being near her made me calm down. \n'
	if 'picture' in interactions:
		user = input('Do you want to interact with this picture again? (Y/N)')
		if user in y:
				print(message)
		elif user in n:
				room()
		else:
				print('That is not a valid input. \n')
				picture()

	if 'picture' not in interactions:
			typewriter(message)
			interactions.append('picture')


#in the first drawer
def newspaper():
	message = '\nThis was the night of our first big bust... We had never really gotten a lot of recognition since we would only do small things such as stop petty robberies and lead them to places where they could get the help they needed. Then, we got news about something big: a trafficking ring. We were able to take down the leaders and save as many of the people in it. We worked with them to get back to their families, and made sure they had enough money funded by things such as donations (which people gave them since it was on the news) especially for thos who had no family. But, this was the first time Adriana and I had a conflict on how to deal with the leaders we took down. I wanted to kill the people who led this trafficking ring, but Adriana wanted to put them in rehabilitation centers so they could get help. I thought it was absolute bullshit and we should\'ve just killed them. They were better off dead. Especially after doing that to those children? It was disgusting. But, I went along with Adriana..... this time '

	if 'newspaper' in interactions:
		user = input(
				'\nWould you like to interact with the newspaper again? (Y/N) ')
		if user in y:
				print(message)
		if user in n:
				room()
		else:
				room()
	elif 'newspaper' not in interactions:
		typewriter(message)
		interactions.append('newspaper')


#in the first drawer
def journal():
	message = '\nThis is ... my journal. The entries read as follows \n"January 4th, 2020 ~ Bro, I am so fucking angry right now. Today, I saw my aunt. We had to go to my old street for a job. I saw her and just stopped. But, she literally rushed up to us ?? I didn\'t know what to do, so I just stood there. \nYou know what she had the motherfucking AUDACITY to say??!! I don\'t remember it exactly but it was like, "Oh my god!!! Red Light and Celebre!" I had never seen her so excited. \nThen, she had MORE to say. This goddamn whore said, "Thank you so much for what you\'ve done for this community." I was about to punch her forreal. I thought she would say this is criminal behavior, but nah. idek... ugh. But when I punched someone for touching my friends ass, it was "none of my business.." The HYPOCRISY. \nughhiefhiwhieghwig, I hate her so much. I was ready to fucking strangle her on the spot. And Adriana saw, so she said, "No problem. We have to go now." Adriana grabbed me by the arm. \nShe started trying to calm me down, but I barely knew what she said. I started to storm back and when I saw her, I couldn\'t control myself. \nI started to do something I have been wanting to do for so long.. stop her breathing. I revealed who I actually was. You wanna know what this girl said.. "You piece of shit." I was filled with rage at that point. Then, Adriana did something and I was knocked out. \nI was home when I woke up. I was yelling at her asking why she did that. It was my right. She had fucking abused me for so long. She gave me no reaction at all. Then, I saw her dad\'s watch. I did something so fucked omg. I don\'t know if she\'s gonna forgive me. I\'m honestly so scared. You see, at the time I was thinking "How would you like it if I fucked something up that was personal to you for no reason?" Then, I slammed her father\'s watch on the ground and stomped on it. \nShe whimpered. I felt bad right after I did that. I tried picking up the pieces. Then, I found a secret compartment in the side of the watch. A small piece of paper was there. Adriana saw it and she immediately took it from me. I don\'t know what\'s on there." \nOh, so this is when things started getting rocky between us. '

	if 'journal' not in interactions:
		typewriter(message)
		interactions.append('journal')
		input('\nHer father\'s watch... split open.. ')

	elif 'journal' in interactions:
		user = input('Do you want to interact with the journal again? (Y/N) ')
		if user in y:
				print(message)
				room()

		if user in n:
				room()
		else:
				print('That is not a valid input.\n')
				journal()


#in the last drawer
def candle():
	message = 'This scent is so familiar. It makes me feel so calm, but so enraged? It reminds me of Adriana. She gave this to me as a present when I came to live with her. Now that I think of it, this was the same scent I smelled when we did our first big bust. When we were talking about what to do with them. And right before I passed out when I was trying to kill my aunt. \n... Hold up. Has she had been using this candle to control me? Wait a fucking second... She never let me light the candle because it\'s a fire hazard or some bs like that. I never lit that candle. Kind of forgot about it. She told me to not, and I kept asking why. She came clean and said that whenever I would ... '
	while 'candle' not in interactions:
		input('Oh look! A candle. ')
		input('I\'m not getting anything from this. ')
		input('Maybe something in my inventory will help??? ')
		inv_things = ', '.join(inventory)
		print(inv_things)
		user = input('What do you want to interact with? ')
		if user == 'matches':
			typewriter(message)
			interactions.append('candle')
			input('\nYou used it to control me? ')
			input('"Yes.. I\'m not proud of it.." ')
			input('Wow... okay ')
			room()
		else:
			print('Hmm.. not quite')
		candle()
	user = input('Do you want to interact with this again (Y/N) ')
	if user in y:
			print(message)
	if user in n:
			room()
	else:
			print('That is not a valid input.\n')
			candle()


def top_drawer():
	if 'closet key' not in inventory:
		input('This drawer is locked.. I need a key for this.. ')
		room()
		
	elif 'closet key' in inventory:
		input('The key I got from the closet seems to open this! ')
		user = input('Should I open this drawer? (Y/N) ')
		
		if user in y:
			input('I opened the drawer and it has two things: a journal and a newspaper. ')
			user_input = input('What should I interact with? journal or newspaper: \nTYPE YOUR ANSWER HERE: ')
		
			if user_input == 'journal':
				journal()
				input('\nTime to interact with this newspaper. ')
				newspaper()
				room()

			if user_input == 'newspaper':
				newspaper()
				input ("\nTime to interact with the journal. ")
				journal()
				room()


def bottom_drawer():
	if 'watch key' not in inventory:
		input('This drawer is locked.. I need a key for this .. ')
		room()

	elif 'watch key' in inventory:
		input('I have a key to open this drawer! ')
		user = input('Should I use the key to open this drawer? (Y/N) ')
		if user in y:
				candle()
		if user in n:
				room()
		else:
				bottom_drawer()


def nightstand():
	input('You have interacted with the nightstand. ')
	input('On the nightstand, there seems to be a picture. There are also two drawers, but they seem to be locked. ')
	user_input = input('What do you want to interact with? picture, top drawer, or bottom drawer: \nTYPE YOUR ANSWER HERE: ')
	
	if user_input.lower() == 'picture':
		picture()
		user = input(
				'Do you want to interact with the rest of the nighstand? (Y/N) ')
		if user in y:
				nightstand()
		if user in n:
				room()
		else:
			print('That is not a valid input. \n')
			room()

	elif user_input == 'top drawer':
		top_drawer()
		user = input('Do you want to interact with the rest of the nighstand? (Y/N) ')
		if user in y:
				nightstand()
		if user in n:
				room()
		else:
				print('That is not a valid input. \n')
				nightstand()

	elif user_input == 'bottom drawer':
		bottom_drawer()
		user = input('Do you want to interact with the rest of the nightstand? (Y/N) ')
		if user in y:
				nightstand()
		if user in n:
				room()
		else:
				print('That is not a valid input. \n')
				nightstand()

	else:
		input('That is not a valid input.')


#---------------------------------------------------------
#for the list


def the_list():
	message = 'This is a list of people. At the top, it says "Casualties from Environment Incorporate." I remember when I did this. This was the last thing I remember doing actually. Environment Incoporate was a shitty corporation. They were putting power plants in poor, low-income neighborhoods. They were outsourcing, overall shitty people. It was one of my proudest moments. I was able to stop oxygen flow in the room with all of the Board of Directors for the corporation. \nI don\'t know why this was here. It wasn\'t a long list. \nThen, I saw it... \n"Athena Polanco" \nAdriana\'s mom... '
	typewriter(message)
	interactions.append('list')


#---------------------------------------------------------
#for the exit door


def exit_door():
	answer = ['evil', 'love', 'Love', 'Evil', 'LOVE', 'EVIL']
	print('This is the door to exit')
	if 'list' in interactions:
		input('"Now that you\'ve seen the list, I can give you the clue to leave." ')
		input('"It is a four letter word. What is our friendship built on?" ')
		print('Now, I have a clue...')

		user = input ('Do you want to look back at the things you\'ve interacted with? (Y/N) ')
		while user not in n:
			print("There was the following in the room: \nbed, \nnightstand \ncloset, \nbookshelf. \nThere is also \nmy inventory and \nthe door")
			user = input('What do you want to interact with? ') #have to put things that are actually in interactions instead of bed, nightstand, etc
			if user in things_like_bed:
				bed()
				user = ('Do you want to look back at the things you\'ve interacted with? (Y/N) ')
				
			elif user in things_like_closet:
				closet()
				user = ('Do you want to look back at the things you\'ve interacted with? (Y/N) ')
				
			elif user in things_like_nightstand:
				nightstand()
				user = ('Do you want to look back at the things you\'ve interacted with? (Y/N) ')
				
			elif user in things_like_door:
				exit_door()
				user = ('Do you want to look back at the things you\'ve interacted with? (Y/N) ')
				
			elif user in things_like_bookshelf:
				bookshelf()
				user = ('Do you want to look back at the things you\'ve interacted with? (Y/N) ')
				
			elif user in like_inventory:
				the_inventory()
				user = ('Do you want to look back at the things you\'ve interacted with? (Y/N) ')
				
			else:
				print('That is not a valid input. ')

		user_input = input(
			'A 4-letter word... What was our friendship built on? \nTYPE YOUR ANSWER HERE: ')
		
		if user_input in answer: #this does not work. you can input anything and it will say the door opened
			print('The door opened... ')
		else:
			input('No ... that\'s not it. ')
			exit_door()
			
	elif 'list' not in interactions:
		input('Hmm... I wonder what I need to do to open this door... ')
		room()

# things for the end -----------------------------------------

#first dialogue from the game
def beginning_dialogue():

	print('\nYou wake up in a room with no one around you. There is a camera at the side of the room.\n')
	input('"Hello Myra." ')
	input('Who was that? ')
	input('"You will find that out soon enough... I put you in this room for a reason. Please don\'t disappoint me."')
	input('What is that supposed to mean? What am I doing here? ')
	input('"This is a room filled with your memories. ')
	input('Go around and with each object you touch, a memory comes back. ')
	input('There are some things you have to figure out first. Some require keys. Some require words." ')
	input('Okay.. so I have to basically escape the room? ')
	input('"Yes, precisely. There are a pack of matches in your pocket so you can light the room. I wish you the best of luck, Myra." ')
	input('Wait, who are you? ')
	input('There was no response. ')
	input('\nMaybe I should light the room first.. ')
	input('... ')
	input('I can see the room way better now. \nNow, what to do first... ')

#end dialogue talking to Adriana and finding out you love eachother

def end_dialogue():
	input('Adriana.. what the actual fuck was that? ')
	input('"I just wanted to give you a second chance. You KILLED my fucking mother. You decided to do all this \"justice shit\", but the only thing you ever did was hurt everyone around you." She started to tear up. ')
	input ("I didn't know what to say.")
	input('"I don\'t think you understand Myra... After all of this shit that you do, the thing that you did... and I know you wouldn\'t have done it if you had known.. ugh, I just keep making excuses.." ')
	input('Making excuses? You have always been so high and fucking mighty about everything. Have you always tried to make excuses for me? Why don\'t you just say what you mean? ')
	input('"No Myra." I could hear her voice crack. "" ')
	typewriter('I love you...')
	input('I stared at her. Her eyes were full of what I can only call... pain. It took me a bit to understand. ')
	input('Adriana... ')
	input('She just looked down. ')
	input('Adriana... I never knew... I killed your MOM, I broke your dad\'s watch... and you still love me? ')
	input('"When you put it in that way, it doesn\'t make sense. You always thought that my family was the best. That my mom was everything to me. But, she wasn\'t. She taught me how to conceal all of my feelings. How to hide everything. We never talked. She really only talked to me when you moved to my house. Even then... But she was still my mother Myra." She looked down and could tell she was holding back tears. Slowly putting her sleeves over her hands and wiping her eyes.')
	input('I didn\'t know.. ')
	input('Do you mind if I ask what your mom was doing in that room? ')
	input('"She was there... fighting against it as a lawyer. She called all of the board of directors there so she could talk about all of the legal shit that was going to go down if they don\'t pull out.." ')
	input('Oh wow... I-I don\'t even know what to say.')
	input('"It\'s okay. You don\'t have to say anything." ')
	input('"Look, Myra. I\'m giving you one more chance. We can join forces again... We can work on this together. I know you\'re not a bad person." ')
	input('\n')
	input('Now how do I feel.. ')
	input('Wait... have I loved Adriana this whole time? ')
	input('I\'ve always loved her determination even if I didn\'t care much for what she used it for. She was always there for me, but that\'s what friends do right? ')
	input('You also think about having a future with your best friend too. Living together till we\'re old.. Doing things together all the time, raising animals and kids together. ')
	input('Getting lost in their eyes when they\'re speaking. Thinking they\'re really cute. Not minding being in a relationship with them if they asked.. ')
	input('Right? ')
	input('Oh shit...I like her.. ')
	typewriter('No.. I love her.')
	input('Shit.. what am I supposed to do now. ')
	input('I only have three options. ')
	input('\n1 - Go with her and give up most of my morals. I can\'t believe she controled me with that candle. But, I could be with her my whole life.. ')
	input('2 - Go back to my life and go on without her. Do things the way I want to do them.')
	input('3 - Kill her. ')



#making the decision of staying with her or not.
def the_decision():
	user = input('So, 1, 2 or 3? ')
	if user == '1':
		first_choice()
		end_screen()
	if user == '2':
		second_choice()
		end_screen()
	if user == '3':
		third_choice()
		end_screen()
	else:
		print ("I don't think that's an option.. ")
		the_decision()



def first_choice():
	input('I want to be with her more than anything. ')
	input('After we left this room, we started to understand each other more. I don\'t think she\'ll ever get over me killing her mom. She says she has, but I know that\'ll never be true. I tried to understand and take the slower route and not resorting to killing anyone. ')
	input('I also started going to therapy and controlling my anger, especially towards my aunt. A lot of unresolved feelings there. It\'s been so helpful. ')
	input('What Adriana did was a little controlling, but I understood why she did it. I love her so much and I\'m glad I got to stay with her. ')


def second_choice():
	input('I can\'t just give up my morals because of love. Maybe one day she\'ll understand. ')
	input('I had to tell her gently. She cried a lot. We hugged a lot. But, we both knew that this is what\'s best for me right now. I can\'t turn back anymore. She won\'t be my enemy, but she also wouldn\'t be my ally.. ')
	input('At least she\'ll always be in my life... Always stopping the same crimes somehow. ')
	input('No matter how much I love her, she\'ll never be with me if I keep killing and it\'s the only way anything can get done. ')
	input ("I will always love Adriana.\n")
	
	
def third_choice():
	input('I can\'t show any weakness. If she continues to live, I will always have someone that people can use against me when I try to advance society. ')
	input('It hurt me a little when I stopped her nervous system from working. I wanted it to be as painless and fast for her. But, it had to be done. ')
	input('I went into the world with nothing to hold me down. Nothing to hold me back. ')
	input('She was very important to me...')
	input('What have I done? ')
	input('I went home. I stared at myself in the mirror. I started to cry. Why did I do that? ')
	input('There\'s no point in living if she\'s not here.')
	input('I put my hand over my heart. ')
	input('I\'ll meet you soon, my love. ')



def end_screen():
	input ("You have finished the game! ")
	user = input('Do you want to pick a different decision?(Y/N) ')
	while user not in n:
		if user in y:
			the_end()
		else:
			print('That is not a valid input.. ')
	user = input('Do you want to play again? (Y/N) ')
	if user in y:
			main()
	if user in n:
		print('Okay thank you for playing!! ')
		quit()



def the_end():
	the_list()
	input('\nNow, time to open this door.. ')
	exit_door()
	input('When I left the room, Adriana was right there, and we started talking.. ')
	end_dialogue()
	the_decision()

	
#---------------------------------------------------------

#main function
def main():
	title_screen()
	beginning_dialogue()
	room()


if __name__ == '__main__':
	main()