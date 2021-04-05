from binaryTree import *
from openFile import *
from strip_punctuation import *

def main():
    tree = BinarySearchTree()
    deleted = []
    while True:
        input_text = input().lower()
        if input_text == 'quit':
            print('** BST Program Finished **')
            break
        if input_text[0:4] == 'read':
            deleted = []
            file = open_file_r(input_text[5:])
            words = strip_punctuation(file)
            for word in words:
                #print(word)
                if tree.search(word) == None:
                    tree.insert(word)
        if input_text == 'print':
            print('Printing the tree')
            tree.print_tree('print')
        if input_text == 'printd':
            print('Printing the tree')
            tree.print_tree('printd')
        if input_text == 'printdp':
            print('Printing the tree')
            tree.print_tree('printdp')
        if input_text == 'first':
            print(f'The first word is {tree.first()}')
        if input_text == 'last':
            print(f'The last word is {tree.last()}')
        if input_text == 'most':
            word, value = tree.most(deleted)
            print(f'most occurrences is {value}')
            print(f'{word}, Count = {value}')
        if input_text == 'height':
            print(tree.height())
        if input_text[0:6] == 'delete':
            if tree.search(input_text[7:]) != None:
                word_node = tree.searchDelete(input_text[7:])
                number = word_node.amount
                tree.delete(input_text[7:])
                print(f'Word deleted had {number} occurrences')
                deleted.append(word_node._value)
                for i in words:
                    if i == input_text[7:]:
                        words.remove(i)
        if input_text[0:6] == 'reduce':
            if tree.search(input_text[7:]) != None:
                word_node = tree.reduce(input_text[7:])
                number = word_node.amount
                if number != 0:
                    print(f'Word now has occurences of {number}.')
                if number == 0:
                    tree.delete(input_text[7:])
                    print("Word deleted as occurrences was 1.")
        if input_text[0:7] == 'summary':
            print('** Tree Statistics **')
            print(f'    Height of tree: {tree.height()}')
            print(f'    Total Words:  {len(words)}  Distinct Words:  {tree.distinct(deleted)}')
            print(f'    First word:  {tree.first()}')
            print(f'    Last word:  {tree.last()}')
        if input_text == 'breadthfirst':
            print('Breadth-first Traversal of the tree\n')
            tree.breadthfirst()


main()