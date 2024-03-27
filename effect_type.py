import sys, time  #imported for typewriter effect

#for typewriter effect https://www.youtube.com/watchv=2h8e0tXHfk0ab_channel=LearnLearnScratchTutorials
def typewriter(message):
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()

		if char != '\n':
				time.sleep(0.00000000000000001)
		else:
				time.sleep(0.2)