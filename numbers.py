def graphic_num(num_str):
	d=[('1','▀▀█ ',
		    '  █ ',
		    '  █ ',
		    '████'),
	('2','▀▀▀█',
		 '▄▄▄█',
		 '█   ',
		 '█▄▄▄'),

	('3','▀▀▀█',
		 '▄▄▄█',
		 '   █',
		 '▄▄▄█'),

	('4','█ █ ',
		 '█▄█▄',
		 '  █ '
		,'  ▀ '),
	('5','█▀▀▀',
		 '█▄▄▄',
		 '   █',
		 '▄▄▄█'),

	('6','█▀▀▀',
		 '█▄▄▄',
		 '█  █',
		 '█▄▄█'),

	('7','▀▀▀█',
		 '   █',
		 '   █',
		 '   █'),

	('8','█▀▀█',
		 '█▄▄█',
		 '█  █',
		 '█▄▄█'),

	('9','█▀▀█',
		 '█▄▄█',
		 '   █',
		 '▄▄▄█'),

	('0','█▀▀█',
		 '█  █',
		 '█  █',
		 '█▄▄█')

	]


	#n=0
	d2=[]
	import time
	for n in num_str:
		for i in d:
			for i2 in i:
				if n==i2:
					d2.append(i)
					break
	part=1
	#print(d2)
	for i in range(4):

		for x in d2:
			time.sleep(0.02)
			print(x[part],end=' ')
		print()
		part+=1
n=1000000000000000
for i in range(n,n+1000):
	graphic_num(str(i))
	print()
