class TrieNode:

    def __init__(self):
        self.isEndOfWord = False
        self.children = [None]*26

    def isEmpty(self):
        currNode = self
        for node in currNode.children:
            if node != None:
                return False
        return not currNode.isEndOfWord

    def delete(self, word, depth=0):
        currNode = self
        if currNode == None:
            return None
        if depth == len(word):
            currNode.isEndOfWord = False
        else:
            index = ord(word[depth])-ord('a')
            if currNode.children[index] == None:
                return currNode
            currNode.children[index] = currNode.children[index].delete(
                word, depth+1)
        if currNode.isEmpty():
            currNode = None
        return currNode


class Trie:

    @staticmethod
    def info():
        print("Trie class")

    def __init__(self):
        self.root = self._getNode()

    def _getNode(self):
        return TrieNode()

    def insert(self, word):
        currNode = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            if not currNode.children[index]:
                currNode.children[index] = self._getNode()
            currNode = currNode.children[index]
        if currNode != None:
            currNode.isEndOfWord = True

    def search(self, word):
        currNode = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            if not currNode.children[index]:
                return False
            currNode = currNode.children[index]
        return currNode != None and currNode.isEndOfWord

    def delete(self, word):
        self.root.delete(word)


def main():
    T = Trie()
    # T.insert("word")
    # print(T.search("word"))
    # print(T.delete("word"))
    # print(T.search("word"))

    T.insert("Peter")

    # print(T.search("Peter"))
    # print(T.search("Pete"))
    # print(T.delete("Pete"))
    # print(T.search("Peter"))

    T.insert("piper")
    T.insert("picked")
    T.insert("peck")
    T.insert("pickled")
    T.insert("peppers")

    print(T.search("piper"))
    print(T.delete("picked"))
    print(T.search("picked"))
    print(T.delete("pickled"))


if __name__ == "__main__":
    main()
