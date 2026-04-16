### 分支和循环结构实战


# Example 1：100以内的素数

for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
"""
找出100以内的所有素数并打印。
使用双重循环实现：
- 外层循环遍历2到99的所有数字
- 内层循环检查当前数字是否能被2到√num之间的任何数整除
- 如果找到因数，标记为非素数并跳出内层循环
- if is_prime: 检查该数字是否为素数，如果是则打印
素数定义：只能被1和自身整除的大于1的自然数
"""

# Example 2：斐波那契数列

a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)

# Example 3：寻找水仙花数

for num in range(100, 1000):
    low = num % 10 # 取余
    mid = num // 10 % 10 # 取整除后再取余
    high = num // 100 # 取整除
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# Example 4：正整数的反转

num = int(input('num = '))
reversed_num = 0
while num > 0: # 当输入的数字大于0时继续循环
    reversed_num = reversed_num * 10 + num % 10 # 取余，得到最后一位数字，并将其添加到反转数的末尾
    num //= 10 # 取整除，去掉最后一位数字
print(reversed_num)
"""我来解释 Example 4（正整数反转）的逻辑：

**算法流程：**

假设输入 `num = 12345`，逐步执行：

| 循环次 | num | num%10 | reversed_num | num//=10 |
|--------|-----|--------|--------------|----------|
| 初始   | 12345 | - | 0 | - |
| 1 | 12345 | 5 | 0*10+5=5 | 1234 |
| 2 | 1234 | 4 | 5*10+4=54 | 123 |
| 3 | 123 | 3 | 54*10+3=543 | 12 |
| 4 | 12 | 2 | 543*10+2=5432 | 1 |
| 5 | 1 | 1 | 5432*10+1=54321 | 0 |

**核心思想：**
- `num % 10` 提取最后一位数字
- `reversed_num = reversed_num * 10 + num % 10` 将提取的数字逐个添加到反转数
- `num //= 10` 去掉最后一位数字，继续处理前面的数字
- 当 `num == 0` 时，所有数字都被反转完毕

**结果：** 12345 → 54321
"""

# Example 5：百钱百鸡问题

for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

"""
更精进一点的版本
"""

for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

# Example 6：CRAPS赌博游戏

import random

money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    # 下注金额必须大于0且小于等于玩家的总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家胜!\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'玩家摇出了{current_point}点')
            if current_point == 7:
                print('庄家胜!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜!\n')
                money += debt
                break
print('你破产了, 游戏结束!')