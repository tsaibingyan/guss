import random

r = random.randint(1, 100)
while True:
	num = input('請猜1-100之間一個數')
	num = int(num)
	if num == r:
		print('答對! 答案是', num)
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
