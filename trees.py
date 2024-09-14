from enum import Enum
from typing import Optional


class BinarySearchTree:

    def __init__(self, value: Optional[int] = None):
        if value:
            self.root = BinarySearchTreeNode(value)
        else:
            self.root = None

    def __repr__(self):
        return self.root.__repr__()

    def insert(self, node):
        x, y = self.root, None
        while x:
            y = x
            if z.value < x.value:
                x = x.left

            else:
                x = x.right

        z.parent = y
        if not y:
            self.root = z

        else:
            if z.value < y.value:
                y.left = z

            else:
                y.right = z

    def search(self, value):
        if self.root:
            node = self.root
            while node:
                if node.value == value:
                    return node
                elif value < node.value:
                    node = node.left
                else:
                    node = node.right

        return None

    def max(self, node=None):
        if self.root:
            if not node:
                node = self.root
            while node.right:
                node = node.right

            return node

        return None

    def min(self, node=None):
        if self.root:
            if not node:
                node = self.root
            while node.left:
                node = node.left

            return node

        return None

    def predecessor(self, node):
        if self.root:
            if node.left:
                return self.max(node.left)
            parent = node.parent()

            while parent:
                if node == parent.right:
                    return parent
                node = parent
                parent = parent.parent

    def successor(self, node):
        if self.root:
            if node.right:
                return self.min(node.right)
            parent = node.parent()

            while parent:
                if node == parent.left:
                    return parent
                node = parent
                parent = parent.parent

    def delete(self, node):
        if node == self.root:
            if self.root.left and self.root.right:
                succ = node.successor()
                if succ.left:
                    if succ == succ.parent.left:
                        succ.parent.left = succ.left

                    else:
                        succ.parent.right = succ.left

                    succ.left.parent = succ.parent

                elif succ.right:
                    if succ == succ.parent.left:
                        succ.parent.left = succ.right

                    else:
                        succ.parent.right = succ.right

                    succ.right.parent = succ.parent

            elif self.root.left:
                self.root = self.root.left
                self.root.parent = None
            elif self.root.right:
                self.root = self.root.right
                self.root.parent = None
            else:
                self.root = None

        else:
            if node.left and node.right:
                succ = node.successor()
                if succ.left:
                    if succ == succ.parent.left:
                        succ.parent.left = succ.left

                    else:
                        succ.parent.right = succ.left

                    succ.left.parent = succ.parent

                elif succ.right:
                    if succ == succ.parent.left:
                        succ.parent.left = succ.right

                    else:
                        succ.parent.right = succ.right

                    succ.right.parent = succ.parent

                else:
                    if succ == succ.parent.left:
                        succ.parent.left = None

                    else:
                        succ.parent.right = None

                node.value = succ.value

            elif node.left:
                node.left.parent = node.parent
                if node == node.parent.left:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

            elif node.right:
                node.right.parent = node.parent
                if node == node.parent.left:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

            else:
                if node == node.parent.left:
                    node.parent.left = None
                if node == node.parent.right:
                    node.parent.right = None

    def height(self, node=None):
        if not node:
            node = self.root
        if node.left and node.right:
            return max(self.height(node.left), self.height(node.right)) + 1
        elif node.left:
            return self.height(node.left) + 1
        elif node.right:
            return self.height(node.right) + 1
        else:
            return 1

    def left_rotate(self, node):
        if not node.right:
            return

        y = node.right
        node.right = y.left
        if y.left:
            y.left.parent = node

        y.parent = node.parent
        if node.parent:
            if node == node.parent.left:
                node.parent.left = y

            else:
                node.parent.right = y

        else:
            self.root = y

        y.left = node
        node.parent = y

    def right_rotate(self, node):
        if not node.left:
            return

        y = node.left
        node.left = y.right
        if y.right:
            y.right.parent = node

        y.parent = node.parent
        if node.parent:
            if node == node.parent.left:
                node.parent.left = y

            else:
                node.parent.right = y

        else:
            self.root = y

        y.right = node
        node.parent = y


class BinarySearchTreeNode:

    def __init__(self, value: int):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return self.to_string()

    def to_string(self, last=True, header="") -> str:
        elbow = "└─"
        pipe = "│ "
        tee = "├─"
        blank = "  "
        if header:
            node_str = header + (elbow if last else tee) + str(self.value) + "\n"

        else:
            node_str = blank + str(self.value) + "\n"

        if self.left and self.right:
            node_str += self.right.to_string(
                last=False, header=header + (blank if last else pipe)
            )
            node_str += self.left.to_string(
                last=True, header=header + (blank if last else pipe)
            )

        elif self.left:
            node_str += self.left.to_string(
                last=True, header=header + (blank if last else pipe)
            )

        elif self.right:
            node_str += self.right.to_string(
                last=True, header=header + (blank if last else pipe)
            )

        return node_str


class RadixTree:

    def __init__(self):
        self.root = RadixTreeNode()

    def add(self, binary_string: str):

        node = self.root

        for bit in binary_string:
            if bit == "1":
                if not node.right:
                    new_node = RadixTreeNode()
                    node.right = new_node
                    new_node.parent = node

                node = node.right

            else:
                if not node.left:
                    new_node = RadixTreeNode()
                    node.left = new_node
                    new_node.parent = node

                node = node.left

        node.enabled = True

    def sort(self, reversed=False):
        node_queue = [(self.root, "")]

        sorted_list = []

        while node_queue:
            node, binary = node_queue.pop()
            if node.enabled:
                sorted_list.append(binary)

            if node.right:
                node_queue.append((node.right, binary + "1"))

            if node.left:
                node_queue.append((node.left, binary + "0"))

        return sorted_list[::-1] if reversed else sorted_list

    def __str__(self):
        return self.root.to_string()


class RadixTreeNode:

    def __init__(self, enabled=False):
        self.left = None
        self.right = None
        self.parent = None
        self.enabled = enabled

    def to_string(self, last=True, header="", value="") -> str:
        elbow = "└─"
        pipe = "│ "
        tee = "├─"
        blank = "  "
        node_str = (
            header + (elbow if last else tee) + (value if self.enabled else "x") + "\n"
        )
        if self.left and self.right:
            node_str += self.right.to_string(
                last=False, header=header + (blank if last else pipe), value=value + "1"
            )
            node_str += self.left.to_string(
                last=True, header=header + (blank if last else pipe), value=value + "0"
            )
        elif self.left:
            node_str += self.left.to_string(
                last=True, header=header + (blank if last else pipe), value=value + "0"
            )
        elif self.right:
            node_str += self.right.to_string(
                last=True, header=header + (blank if last else pipe), value=value + "1"
            )
        return node_str


class ColorEnum(Enum):
    RED = 0
    BLACK = 1


class RedBlackTreeNode:

    def __init__(
        self,
        value: int,
        color: Optional["ColorEnum"] = ColorEnum.RED,
        left: Optional["RedBlackTreeNode"] = None,
        right: Optional["RedBlackTreeNode"] = None,
        parent: Optional["RedBlackTreeNode"] = None,
    ):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree(BinarySearchTree):

    def __init__(self):
        super(RedBlackTree, self).__init__()
        self.NIL = RedBlackTreeNode(None, ColorEnum.BLACK)
        self.root = self.NIL

    def search(self, value):
        if self.root:
            z = self.root
            while z != self.NIL:
                if z.value == value:
                    return z
                elif value < z.value:
                    z = z.left
                else:
                    z = z.right

        return self.NIL

    def left_rotate(self, z):
        y = z.right
        z.right = y.left
        if y.left != self.NIL:
            y.left.parent = z

        y.parent = z.parent
        if z.parent == self.NIL:
            self.root = y
        else:
            if z == z.parent.left:
                z.parent.left = y

            else:
                z.parent.right = y

        y.left = z
        z.parent = y

    def right_rotate(self, z):
        y = z.left
        z.left = y.right
        if y.right != self.NIL:
            y.right.parent = z

        y.parent = z.parent
        if z.parent == self.NIL:
            self.root = y

        else:
            if z == z.parent.left:
                z.parent.left = y

            else:
                z.parent.right = y

        y.right = z
        z.parent = y

    def insert(self, z: RedBlackTreeNode | int):
        if isinstance(z, int):
            z = RedBlackTreeNode(z)

        x, y = self.root, self.NIL
        while x != self.NIL:
            y = x
            if z.value < x.value:
                x = x.left

            else:
                x = x.right

        z.parent = y
        if y == self.NIL:
            self.root = z

        else:
            if z.value < y.value:
                y.left = z

            else:
                y.right = z

        z.color = ColorEnum.RED
        z.left = self.NIL
        z.right = self.NIL
        self._insert_fixup(z)

    def _insert_fixup(self, z: RedBlackTreeNode):
        while z.parent.color == ColorEnum.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == ColorEnum.RED:
                    z.parent.color = ColorEnum.BLACK
                    y.color = ColorEnum.BLACK
                    z.parent.parent.color = ColorEnum.RED
                    z = z.parent.parent

                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    z.parent.color = ColorEnum.BLACK
                    z.parent.parent.color = ColorEnum.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == ColorEnum.RED:
                    z.parent.color = ColorEnum.BLACK
                    y.color = ColorEnum.BLACK
                    z.parent.parent.color = ColorEnum.RED
                    z = z.parent.parent

                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = ColorEnum.BLACK
                    z.parent.parent.color = ColorEnum.RED
                    self.left_rotate(z.parent.parent)

        self.root.color = ColorEnum.BLACK

    def delete(self, z: RedBlackTreeNode):
        if z.left == self.NIL or z.right == self.NIL:
            y = z

        else:
            y = self.successor(z)

        if y.left != self.NIL:
            x = y.left

        else:
            x = y.right

        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x

            else:
                y.parent.right = x

        if y != z:
            z.value = y.value

        if y.color == ColorEnum.BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, x: RedBlackTreeNode):
        while x != self.root and x.color == ColorEnum.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == ColorEnum.RED:
                    w.color = ColorEnum.BLACK
                    x.parent.color = ColorEnum.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == ColorEnum.BLACK and w.right.color == ColorEnum.BLACK:
                    w.color = ColorEnum.RED
                    x = x.parent

                else:
                    if w.right.color == ColorEnum.BLACK:
                        w.left.color = ColorEnum.BLACK
                        w.color = ColorEnum.RED
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = ColorEnum.BLACK
                    w.right.color = ColorEnum.BLACK
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                w = x.aprent.left
                if w.color == ColorEnum.RED:
                    w.color = ColorEnum.BLACK
                    x.aprent.color = ColorEnum.RED
                    self.right_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == ColorEnum.BLACK and w.right.color == ColorEnum.BLACK:
                    w.color = ColorEnum.RED
                    x = x.parent

                else:
                    if w.left.color == ColorEnum.Black:
                        w.right.color = ColorEnum.BLACK
                        w.color = ColorEnum.RED
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = ColorEnum.BLACK
                    w.left.color = ColorEnum.BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = ColorEnum.BLACK

    def __repr__(self):
        return self.to_string(self.root)

    def to_string(self, node=None, last=True, header="") -> str:
        elbow = "└─"
        pipe = "│ "
        tee = "├─"
        blank = "  "

        if not node:
            node = self.root

        if header:
            node_str = (
                header
                + (elbow if last else tee)
                + (
                    str(node.value)
                    if node.color == ColorEnum.BLACK
                    else f"\033[1;31m {str(node.value)}\033[1;37m "
                )
                + "\n"
            )

        else:
            node_str = blank + str(node.value) + "\n"

        if node.left != self.NIL and node.right != self.NIL:
            node_str += self.to_string(
                node.right, last=False, header=header + (blank if last else pipe)
            )
            node_str += self.to_string(
                node.left, last=True, header=header + (blank if last else pipe)
            )

        elif node.left != self.NIL:
            node_str += self.to_string(
                node.left, last=True, header=header + (blank if last else pipe)
            )

        elif node.right != self.NIL:
            node_str += self.to_string(
                node.right, last=True, header=header + (blank if last else pipe)
            )

        return node_str
