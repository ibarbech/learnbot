import time, math
from __future__ import division, print_function

def turn_left(lbot, params=None, verbose=True):
	lbot.setRobotSpeed(lbot.adv, -math.pi/2)
	if verbose:
		print('~ Learnbot turning left ...')
	time.sleep(1)