"""
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in
this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The
given directory path does not exist. If the middle directories in the path do
not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at
filePath.
"""

class Node:
    def __init__(self, content=None):
        self.children = {}
        self.content = content

    def add_child(self, name):
        if name not in self.children:
            self.children[name] = Node()
        return self.children[name]
    
    def read(self, path):
        node = self
        for s in path[1:].split('/'):
            if s == '': continue
            node = node.children[s]
        return node, s
    
    
    def mkpath(self, path):
        # makes directories and returns final node
        node = self
        for s in path[1:].split('/'):
            if s == '': continue
            node = node.add_child(s)
        return node
    
    
class FileSystem:

    def __init__(self):
        self.root = Node()
        

    def ls(self, path: str) -> List[str]:
        node, name = self.root.read(path)
        if node.content is not None:
            return [name]
        else:
            return list(sorted(node.children.keys()))
        

    def mkdir(self, path: str) -> None:
        self.root.mkpath(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root.mkpath(filePath)
        if node.content is None:
            node.content = content
        else:
            node.content += content
            

    def readContentFromFile(self, filePath: str) -> str:
        node, name = self.root.read(filePath)
        return node.content
    
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

"""
Solved in 28 minutes.  This isn't really 'hard'.  But, it is tricky and requires careful attention.

I mistakenly thought that a str.split('/') on an empty string would return an empty array, but 
it doesn't.  This seems inconsistent.


"""
