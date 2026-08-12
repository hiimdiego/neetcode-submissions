class PrefixTree:

    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        return word in self.trie

    def startsWith(self, prefix: str) -> bool:
        for word in self.trie:
            if prefix in word:
                return True
        return False
        