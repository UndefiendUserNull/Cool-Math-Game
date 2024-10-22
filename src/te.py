from random import randint, choice

def generate(depth):
    nums = []
    exp = []
    result = 0
    for _ in range(depth):
        x = randint(1, 10)
        nums.append(x)
        y = randint(1, 10)
        nums.append(y)
    for i in nums:
        symbol = choice(["+", "-", "*"])
        print(f"{i} {symbol} ", end="")
        exp.append(i)
        exp.append(symbol)
    exp.pop()
    print("\n--------------------")
    eval_text = ""

    for i in exp:
        eval_text += str(i)

    print(eval_text, end="\n")
    result = eval(eval_text)
    print(result)


generate(5)
