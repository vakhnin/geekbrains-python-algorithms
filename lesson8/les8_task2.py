# Закодируйте любую строку по алгоритму Хаффмана.
import collections


def huffman_encode(str_for_encode, code_table_):
    class Node:
        def __init__(self, frequency, char=None, left=None, right=None):
            self.frequency = frequency
            self.char = char
            self.left = left
            self.right = right

        def is_leaf(self):
            if self.left is None and self.left is None:
                return True
            return False

    def get_code_table(node, code_table_spam, path=""):
        if node.is_leaf():
            code_table_spam[node.char] = path
        else:
            get_code_table(node.left, code_table_spam, path + "0")
            get_code_table(node.right, code_table_spam, path + "1")

    def encode_str(code_table_spam, str_):
        result = ""
        for ch in str_:
            result += code_table_spam[ch]
        return result

    frequency_counter = {}
    for chr_spam in str_for_encode:
        if chr_spam in frequency_counter.keys():
            frequency_counter[chr_spam] += 1
        else:
            frequency_counter[chr_spam] = 1
    frequency_counter = dict(sorted(frequency_counter.items(), key=lambda idx: idx[0]))
    frequency_counter = sorted(frequency_counter.items(), key=lambda idx: idx[1], reverse=True)
    if len(frequency_counter) < 2:
        print("Недостаточно символов в строке для кодирования")
        return None

    trees_list = collections.deque()
    for item, value in frequency_counter:
        trees_list.appendleft(Node(value, item))

    item_left = Node(0)
    while trees_list:
        item_left = trees_list.popleft()
        if not trees_list:
            break
        item_right = trees_list.popleft()
        i = 0
        for i, item_spam in enumerate(trees_list):
            if item_spam.frequency >= item_left.frequency + item_right.frequency:
                break
        else:
            i += 1

        trees_list.insert(i, Node(item_left.frequency + item_right.frequency, None, item_left, item_right))

    code_table_ = {}
    get_code_table(item_left, code_table_)

    return encode_str(code_table_, str_for_encode)


code_table = {}
print(huffman_encode("beep boop beer!", code_table))
print("0011 1110 1011 0001 0010 1010 1100 1111 1000 1001" == "0011 1110 1011 0001 0010 1010 1100 1111 1000 1001")
