
config = [
	# Window 1
	{
		"window_position_x_percent": 0,
		"window_position_y_percent": 0,
		"browser_width_percent": .5,
		"browser_height_percent": 1,
		"url": "https://www.google.com/",
	},
	# Window 2
	{
		"window_position_x_percent": .5,
		"window_position_y_percent": 0,
		"browser_width_percent": .5,
		"browser_height_percent": 1,
		"url": "https://www.google.com/",
	},
]

import os
import subprocess

def get_display_res():
	proc1 = subprocess.Popen(['xdpyinfo'], stdout=subprocess.PIPE)
	proc2 = subprocess.Popen(['grep', 'dimensions'], stdin=proc1.stdout, stdout=subprocess.PIPE)
	proc3 = subprocess.Popen(['awk', "{ print $2 }"], stdin=proc2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
	proc2.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
	dim_x, dim_y = proc3.communicate()[0].split('x')

	return int(dim_x.strip()), int(dim_y.strip())



def run_cmd(url, browser_width, browser_height, window_position_x, window_position_y):
	cmd = ('chromium --app="data:text/html,<html><body><script>window.moveTo(' + str(window_position_x) + ',' + str(window_position_y) +
		');window.resizeTo('+ str(browser_width) +',' + str(browser_height) + ');window.location=\''+ url +'\';</script></body></html>" &')
	print '... cmd: ' + cmd
	os.system(cmd)

width, height = get_display_res()



for website in config:
	print('Site --------------------------')

	print ('...Max Width:        ' + str(width))
	print ('...Max Height:       ' + str(height))

	browser_width     = website['browser_width_percent'] * width
	browser_height    = website['browser_height_percent'] * height

	window_position_x = website['window_position_x_percent'] * width
	window_position_y = website['window_position_y_percent'] * height

	# Debug info
	print ('...Browser Width:    ' + str(browser_width))
	print ('...Browser Height:   ' + str(browser_height))
	print ('...Window Postion x: ' + str(window_position_x))
	print ('...Window Postion y: ' + str(window_position_y))

	run_cmd(website['url'], browser_width, browser_height, window_position_x, window_position_y)
