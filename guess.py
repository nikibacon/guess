import random
print('我們來玩猜數字!!')
start = input('請輸入範圍的開始值: ')
end = input('請輸入範圍的結束值: ')

start = int(start)
end = int(end)

r = random.randint(start, end)

count = 0

while True:
	count +=1 
	num = input('請猜數字: ')
	num = int(num)

	if num == r:
		print('你猜到的!!!!恭喜!!!!')
		print('你總共猜了', count,'次')
		break
	elif num > r:
		print('要在小一點喔')
	elif num < r:
		print('要在大一點喔')
	print('你猜第', count, '次了喔')	