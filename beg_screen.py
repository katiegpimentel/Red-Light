from effect_type import typewriter
#---------------------------------------------------------
#basically for the beginning of the game

#used https://fsymbols.com/generators/carty/ from lines 9-14 for the text
def title_screen():
	typewriter('Welcome to ... \n')
	print('\n\
██████╗░███████╗██████╗░  ██╗░░░░░██╗░██████╗░██╗░░██╗████████╗\n\
██╔══██╗██╔════╝██╔══██╗  ██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝\n\
██████╔╝█████╗░░██║░░██║  ██║░░░░░██║██║░░██╗░███████║░░░██║░░░\n\
██╔══██╗██╔══╝░░██║░░██║  ██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░\n\
██║░░██║███████╗██████╔╝  ███████╗██║╚██████╔╝██║░░██║░░░██║░░░\n\
╚═╝░░╚═╝╚══════╝╚═════╝░  ╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░ '
				)  #got this from https://fsymbols.com/generators/carty/
	
	typewriter ("\nTW: Mentions of suicide, tr*fficking ring and killing. Contains foul language.\n")
	input('\nPress ENTER to continue... ')

