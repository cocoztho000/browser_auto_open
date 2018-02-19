from selenium.webdriver import Firefox

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

for website in config:
	print('Site --------------------------')
	driver = Firefox()
	driver.maximize_window()
	window_size = driver.get_window_size()

	width = window_size['width']
	height = window_size['height']

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

	driver.set_window_size(browser_width, browser_height)
	driver.set_window_position(window_position_x, window_position_y)
	driver.get(website['url'])
