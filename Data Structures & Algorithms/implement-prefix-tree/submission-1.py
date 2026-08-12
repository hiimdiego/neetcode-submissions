#initialize Node class
class Node:
    def __init__(self):
        #initialize children and endOfWord
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        #initialize root
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        #traverse word
        for c in word:
            #check if character exists in curr.children
            if c not in curr.children:
                curr.children[c] = Node()
            #set curr to child
            curr = curr.children[c]
        #initialize endOfWord
        curr.endOfWord = True
    def search(self, word: str) -> bool:
        curr = self.root
        #traverse word
        for c in word:
            #check if character exists in curr.children
            if c not in curr.children:
                return False
            #set curr to child
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        #traverse word
        for c in prefix:
            #check if character exists in curr.children
            if c not in curr.children:
                return False
            #set curr to child
            curr = curr.children[c]
        return True

        