#  Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#  Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

START_CHAR_CODE = 32
END_CHAR_CODE = 127
char_code = START_CHAR_CODE

while char_code <= END_CHAR_CODE:
    if not (char_code - START_CHAR_CODE) % 10:
        print()
    print(f'{char_code:3d}-{chr(char_code)} ', end="")
    char_code += 1
