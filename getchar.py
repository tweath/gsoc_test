# Original code created by ActiveState Code, Danny Yoo
# Being modified
#
# getch()-like unbuffered character reading from stdin on 
# both Windows and Unix

# Gets a single character from standard input. 
# Does not echo to the screen.
class _Getch:

	def __init__(self):
		try:
			self.impl = _GetchWindows()
		except ImportError:
			self.impl = _GetchUnix()
 
	def __call__(self): return self.impl()

# Fetch and character using the termios module.   
class _GetchUnix:
	def __init__(self):
		import tty, sys

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

# Fetch a character using the Microsoft Visual C Runtime.	   
class _GetchWindows:
	def __init__(self):
		import msvcrt
 
	def __call__(self):
		import msvcrt
		return msvcrt.getch()
 
getch = _Getch()