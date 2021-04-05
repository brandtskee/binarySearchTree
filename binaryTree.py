class BinarySearchTree :
    class _Node :
        def __init__(self, value, left = None, right = None) :
            self._value = value
            self._left = left
            self._right = right
            self.amount = 1
            self.depth = 0
    
    def __init__(self) :
        self._root = None
        
    def isEmpty(self) :
        return self._root == None
    
    # Purpose: insert new value into binary tree
    # Parameter: new value
    # Return: None
    def insert(self, value) :
        if self.isEmpty() :
            self._root = self._Node(value)
            return
        parent = None
        probe = self._root
        while (probe != None) :
            if value <= probe._value :
                parent = probe
                probe = probe._left
            else :
                parent = probe
                probe = probe._right
        if (value <= parent._value) :
            parent._left = self._Node(value)
        else :
            parent._right = self._Node(value)

    # Purpose: Searches tree and returns value if found
    # Parameter: value
    # Return: Found value          
    def search(self, value) :
        probe = self._root
        while (probe != None) :
            if value == probe._value :
                probe.amount += 1
                return probe
            if value <= probe._value :
                probe = probe._left
            else :
                probe = probe._right
        return None 

    # Purpose: Searches tree for value and deletes if found
    # Parameter: value to search for
    # Return: deleted value
    def searchDelete(self, value):
        probe = self._root
        while (probe != None) :
            if value == probe._value :
                probe.amount -= 1
                return probe
            if value <= probe._value :
                probe = probe._left
            else :
                probe = probe._right
        return None
    
    # Purpose: searches value and deletes amount
    # Parameter: value to search for
    # Return: reduced value
    def reduce(self, value):
        probe = self._root
        while (probe != None) :
            if value == probe._value :
                probe.amount -= 2
                return probe
            if value <= probe._value :
                probe = probe._left
            else :
                probe = probe._right
        return None

    # Purpose: Deletes exisiting value
    # Parameter: value to delete
    # Return: None
    def delete(self, value) :
        parent = None
        probe = self._root
        while(probe != None) :
            if value == probe._value :
                break
            if value < probe._value :
                parent = probe
                probe = probe._left
            else :
                parent = probe
                probe = probe._right
        if probe == None :
            raise NotPresent("Attempt to delete nonexistent value.")
        # At this point, probe points at the node to be deleted and 
        # parent to the parent of this node.
        if (probe._left != None and probe._right != None):
            # Two children present; find the successor
            parentSu = probe
            su = probe._right
            amount = su.amount
            while (su._left != None) :
                parentSu = su
                su = su._left
            # At this point, su points to the successor of probe
            # Copy su to probe and delete su
            probe._value = su._value
            probe.amount = amount
            if parentSu == probe :
                parentSu._right = su._right
            else :
                parentSu._left = su._right
            return
        # We are in the case 0 or 1 child
        newChild = probe._left
        if newChild == None : newChild = probe._right
        if parent == None :
            # We are deleting the root
            self._root = newChild
        else:
            if probe == parent._left:
                parent._left = newChild
            else:
                parent._right = newChild
                
    def inOrder(self) :
        self.recInOrder(self._root)
        
    def recInOrder(self,node) :
        if node == None : return
        self.recInOrder(node._left)
        print(node._value)
        self.recInOrder(node._right)


    # Purpose: prints the tree recursively with certain added values if specified by user, and returns lists of values when specified
    # Parameter: parameters specified by user (command)
    # Return: lists of values
    def print_tree(self, command):
        if self._root != None:
            self._print_tree(self._root, -1, command)
        elif self._root == None:
            print('The tree is empty')
    def _print_tree(self, node, depth, command, parent=None, list=[]):
        
        if node != None:
            depth += 1
            self._print_tree(node._left, depth, command)
            if node._value not in list:
                list.append(node._value)
            parent = node._value
            if command == 'print':
                print(str(node._value) + ', count =', str(node.amount))
            if command == 'printd':
                print(str(node._value) + ', count =', str(node.amount) + ', depth =', str(depth))
            if command == 'printdp':
                if self.searchParent(node._value) != None:
                    parent = self.searchParent(node._value)
                    print(str(node._value) + ', count =', str(node.amount) + ', depth =', str(depth) + ', parent =', str(parent._value))
                else:
                    print(str(node._value) + ', count =', str(node.amount) + ', depth =', str(depth) + ', parent = None')
            self._print_tree(node._right, depth, command)
            if command == 'first':
                if node._value not in list:
                    list.append(node._value)
                return list
            if command == 'most':
                node.depth = depth
                if node not in list:
                    list.append(node)
                return list
    
    # Purpose: searches for the parent of a node by keeping track of the previous node
    # Parameter: value to search parent for
    # Return: parent node (previous)
    def searchParent(self, value):
        probe = self._root
        previous = None
        while (probe != None) :
            if value == probe._value :
                return previous
            if value <= probe._value :
                previous = probe
                probe = probe._left
            else :
                previous = probe
                probe = probe._right
        return None 
    
    # Purpose: returns first value alphabetically and by size
    # Parameter: None
    # Return: First word
    def first(self):
        word_list = self._print_tree(self._root, -1, 'first')
        return word_list[0]

    # Purpose: determines the amount of distinct words in the tree (not duplicates)
    # Parameter: list of already deleted words (deleted)
    # Return: lsit of distinct words (new_list)
    def distinct(self, deleted):
        word_list = self._print_tree(self._root, -1, 'first')
        new_list = []
        for i in deleted:
            if i in word_list:
                word_list.remove(i)
        for i in word_list:
            if i not in new_list:
                try:
                    if i.isalpha() == True:
                        new_list.append(i)
                except:
                    continue
        return len(new_list)
    
    # Purpose: returns last letter alphabetically
    # Parameter: None
    # Return: last word
    def last(self):
        old_list = self._print_tree(self._root, -1, 'first')
        word_list = []
        for i in old_list:
            if i not in word_list:
                word_list.append(i)
        for i in 'zyxwvutsrqponmlkjihgfedcba':
            for word in reversed(word_list):
                try:
                    if word[0] == i:
                        return word
                except:
                    continue
    
    # Purpose: Determines what word has the most instances
    # Parameter: list of already deleted words (deleted)
    # Return: most common word (most_word), and the amount it occurred (highest)
    def most(self, deleted):
        word_list = self._print_tree(self._root, -1, 'most', [])
        highest = 0
        most_word = None
        for i in deleted:
            for n in word_list:
                try:
                    if n._value == i:
                        word_list.remove(n)
                except:
                    continue
        for i in word_list:
            try:
                if i.amount > highest:
                    highest = i.amount
                    most_word = i._value
            except:
                continue
        
        return most_word, highest

    # Purpose: Determines height of the binary tree recursively
    # Parameter: None
    # Return: integer of height
    def height(self):
        if self._root != None:
            return self._height(self._root, -1)
        else:
            return None
    
    # Helper function for height()
    def _height(self, node, current_height):
        if node == None:
            return current_height
        left = self._height(node._left, current_height+1)
        right = self._height(node._right, current_height+1)
        return max(left, right)

    # Purpose: List the words in rows corresponding to depth
    # Parameter: None
    # Return: None
    def breadthfirst(self):
        word_list = self._print_tree(self._root, -1, 'most')
        height = self.height()
        for num in range(0, height+1):
            depth_range = []
            for i in word_list:
                try:
                    if i.depth == num:
                        depth_range.append(i._value)
                except:
                    continue
            print(f'Depth = {num}: ', end='')
            for i in depth_range[0:-1]:
                print(f'{i}, ', end='')
            print(depth_range[-1])

# Raises error if value is searched for and does not exist
class NotPresent(Exception) :
    pass