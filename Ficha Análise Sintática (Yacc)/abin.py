class ABin:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val} [{self.left or ''}] [{self.right or ''}]"