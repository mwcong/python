# python
import random

secret = random.randint(1,10)

print('----开始----')
guess = 6
while guess != secret:
	temp = input("猜猜吧")
	guess = int(temp)
	if guess == 8:
		print("卧槽，对了")
		print("嗯，没用的")
	else:
		if guess > 8:
			print("大了")
		else:
			print("小了")
print("游戏结束")


