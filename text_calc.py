def checker(line_for_check):
    try:
        if not int_check(line_for_check[0]) or not int_check(line_for_check[2]):
            raise ValueError('Операнды не целые числа.')
        if not operand_check(line_for_check[1]):
            raise BaseException('Не верный оператор.')
    except (ValueError, BaseException) as exc:
        # print(" ".join(line_for_check), exc)#debug
        line_for_check = reinput(line_for_check)
        if line_for_check:
            return checker(line_for_check)
        else:
            return False
    else:
        return line_for_check


def int_check(number):
    return number.isdigit()


def operand_check(oper):
    oper_list = ['+', '-', '*', '/', '**', '//', '%']
    if oper in oper_list:
        return True


def reinput(bad_line):
    anser = input(f'Обнаружена ошибка в строке: {" ".join(bad_line)}   Хотите исправить? ')
    if anser.lower() != 'да':
        return False
    return input('Введите исправленную строку: ').split()


def calculator(input_list):
    input_line = ' '.join(input_list)
    return eval(input_line)


listed_line = checker(input('Введите строку выражения: ').split())
print(calculator(listed_line))
