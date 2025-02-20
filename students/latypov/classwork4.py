kalc = input('введите нужную операцию над числами:'  )
one = int(input('введите первое число'))
two = int(input('введите второе число'))
# запросить все данные
# в зависимости от вида оператора сделать соответствующую операцию
if kalc == '*':
    print(one * two)
if kalc == "/":
    print(one / two)
if kalc == "-":
    print(one - two)
if kalc == "+":
    print(one + two)
