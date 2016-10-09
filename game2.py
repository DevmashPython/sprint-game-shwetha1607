import msvcrt
import time

f=10
c1=c2=c3=0

print "press enter key to begin"
raw_input()
s_time=time.time()
while(1):
	k=msvcrt.getch()
	if k=='d':
		c1=c1+1
		print "-->",
		if c1==f:
			print "move downwards",
			break
	else:
		print "you lose"
if c1==f:
	while(1):
		k2=msvcrt.getch()
		if k2=='s':
			c2=c2+1
			print "                                                  |"
			print "                                                  |"
			print "                                                  v"
			if c2==f:
				print "                                                  move right",
				break
		else:
			print "you lose"
if c2==f:
	while(1):
		k3=msvcrt.getch()
		if k3=='d':
			c3=c3+1
			print "-->",
			if c3==f:
				print "Game completed"
				break
		else:
			print "you lose"
time_elapsed=time.time()-s_time
print "time taken is"+str(time_elapsed)


'''
1. Mention controls for the game.
2. The game should be lost on pressing the wrong key
'''
