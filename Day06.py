### for-in 循环

# Example 1

import time

print('hello, world')
time.sleep(1)

# Example 2_Version 1：每隔1秒输出一次“hello, world”，持续1小时

import time

for i in range(3600):
    print('hello, world')
    time.sleep(1)

# Example 2_Version 2：每隔1秒输出一次“hello, world”，持续1小时

import time

for _ in range(3600):
    print('hello, world')
    time.sleep(1)

# Example 3：从1到100的整数求和

total = 0
for i in range(1, 101):
    total += i
print(total)

# Example 4_Version 1：从1到100的偶数求和

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)

# Example 4_Version 2：从1到100的偶数求和

total = 0
for i in range(2, 101, 2):
    total += i
print(total)

# Example 4_Version 3：从1到100的偶数求和

print(sum(range(2, 101, 2)))



### While 循环

# Example 1：从1到100的整数求和

total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

# Example 2：从1到100的偶数求和

total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(total)



### break 和 continue

# Example 1_Version 1：从1到100的偶数求和

total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)

# Example 1_Version 2：从1到100的偶数求和

total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)



### 嵌套的循环语句

# Example 1：打印九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()

# Example 2：判断一个数是否是素数

num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

# Example 3_Version 1：输入两个正整数，计算它们的最大公约数和最小公倍数

x = int(input('x = '))
y = int(input('y = '))
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f'最大公约数: {i}')
        break

# Example 3_Version 2：输入两个正整数，计算它们的最大公约数和最小公倍数

x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')

# Example 4：猜数字游戏

import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('大一点.')
    elif num > answer:
        print('小一点.')
    else:
        print('猜对了.')
        break
print(f'你一共猜了{counter}次.')