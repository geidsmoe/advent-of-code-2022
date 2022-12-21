class FileTree:

    def __init__(self, name, is_directory = False, children = None, size=0):
        self.name = name
        self.is_directory = is_directory
        self.children = children
        self.size = size

    def __str__(self):
        return f"({self.name}, {self.size})"

def create_file_tree():
    f = open("data/day07.txt")

    head = FileTree("/", is_directory=True, children=[])

    queue = [head]

    current_node = None
    current_directory = []

    for line in f.readlines():
        line = line.split()
        if line[1] == "cd" and line[2] != "..":
            queue += current_directory
            current_directory = []
            current_node = queue.pop()
        elif line[0] == "dir":
            child = FileTree(line[1], is_directory=True, children=[])
            current_node.children.append(child)
            current_directory.insert(0, child)
        elif line[0].isnumeric():
            child = FileTree(line[1], is_directory=False, size=int(line[0]))
            current_node.children.append(child)

    return head

def part1():
    file_tree = create_file_tree()
    
    directory_list = []

    def helper(ft):
        for n in ft.children:
            if n.is_directory:
                ft.size += helper(n)
            else:
                ft.size += n.size
        
        if ft.size <= 100000:
            directory_list.append(ft)
        
        return ft.size

    helper(file_tree)

    print(sum([n.size for n in directory_list]))

def part2():
    file_tree = create_file_tree()

    directories = []

    def helper(ft):
        for n in ft.children:
            if n.is_directory:
                ft.size += helper(n)
            else:
                ft.size += n.size
        
        directories.append(ft)
        return ft.size

    helper(file_tree)

    free_space = 70000000 - file_tree.size
    update_size = 30000000
    space_to_free = update_size - free_space

    optimal_dir = file_tree

    for dir in directories:
        if dir.size < optimal_dir.size and dir.size >= space_to_free:
            optimal_dir = dir

    print(optimal_dir)


if __name__ == "__main__":
    part2()