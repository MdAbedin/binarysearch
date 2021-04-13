class VirtuallyCloneableStacks:
    def __init__(self):
        self.stacks = [0]

    def copyPush(self, i):
        self.stacks.append(self.stacks[i]+1)

    def copyPop(self, i):
        self.stacks.append(self.stacks[i]-1)

    def size(self, i):
        return self.stacks[i]
