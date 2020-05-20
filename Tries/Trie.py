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

    def startsWith(self, word):
        currNode = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            if currNode.children[index] == None:
                return False
            currNode = currNode.children[index]
        return True

    def _display(self, node, word):
        if node.isEndOfWord:
            print(word)
        for i in range(26):
            if node.children[i] != None:
                self._display(node.children[i], word+chr(i+ord('a')))

    def display(self, word=""):
        self._display(self.root, "")

    def _get_recommendations(self, node, word):
        if node.isEndOfWord:
            print(word)

        for i in range(26):
            if node.children[i] != None:
                self._get_recommendations(
                    node.children[i], word+chr(i+ord('a')))

    def printAutoComplete(self, word):
        currNode = self.root

        for ch in word:
            index = ord(ch)-ord('a')
            if currNode.children[index] == None:
                print("No such prefix")
                return
            currNode = currNode.children[index]
        self._get_recommendations(currNode, word)


def main():
    T = Trie()
    # T.insert("word")
    # print(T.search("word"))
    # print(T.delete("word"))
    # print(T.search("word"))

    T.insert("peter")

    # print(T.search("Peter"))
    # print(T.search("Pete"))
    # print(T.delete("Pete"))
    # print(T.search("Peter"))

    T.insert("piper")
    T.insert("picked")
    T.insert("peck")
    T.insert("pickled")
    T.insert("peppers")

    # print(T.search("piper"))
    # print(T.delete("picked"))
    # print(T.search("picked"))
    # print(T.delete("pickled"))

    # T.insert('apple')
    # print(T.search('apple'))
    # print(T.search('app'))
    # print(T.startsWith('app'))
    # print(T.insert('app'))
    # print(T.search('app'))
    # print(T.startsWith('app'))

    # T.display()

    # T.printAutoComplete("pic")
    # T.printAutoComplete("pi")
    # T.printAutoComplete("pip")
    # T.printAutoComplete("pe")
    T.printAutoComplete("ep")
    T.printAutoComplete("peter")


if __name__ == "__main__":
    main()
