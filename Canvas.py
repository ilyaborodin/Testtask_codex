from collections import deque


class Canvas:
    def __init__(self, file):
        self.canvas = None
        self.file = file

    def make_canvas(self, width, height):
        mid_str = ["|"] + [" "] * width + ["|"]
        top_str = ["-"] * (width + 2)
        self.canvas = [top_str[:]]
        i = 1
        while i < height + 1:
            self.canvas += [mid_str[:]]
            i += 1
        self.canvas += [top_str[:]]

    def make_line(self, width1, height1, width2, height2):
        if height1 == height2:
            if width1 > width2:
                (width1, width2) = (width2, width1)
            for w in range(width1, width2 + 1):
                self.canvas[height1][w] = "x"
        else:
            if height1 > height2:
                (height1, height2) = (height2, height1)
            for h in range(height1, height2 + 1):
                self.canvas[h][width1] = "x"

    def make_rect(self, width1, height1, width2, height2):
        if width1 > width2:
            (width1, width2) = (width2, width1)
        if height1 > height2:
            (height1, height2) = (height2, height1)
        for w in range(width1, width2 + 1):
            self.canvas[height1][w] = "x"
            self.canvas[height2][w] = "x"
        for h in range(height1+1, height2):
            self.canvas[h][width1] = "x"
            self.canvas[h][width2] = "x"

    def bucket_fill(self, x, y, color):
        stack = deque()
        first_color = self.canvas[y][x]
        stack.append((x, y))
        while len(stack) > 0:
            elem = stack.pop()
            self.canvas[elem[1]][elem[0]] = color
            if self.canvas[elem[1] + 1][elem[0]] == first_color:
                stack.append((elem[0], elem[1] + 1))
            if self.canvas[elem[1] - 1][elem[0]] == first_color:
                stack.append((elem[0], elem[1] - 1))
            if self.canvas[elem[1]][elem[0] + 1] == first_color:
                stack.append((elem[0] + 1, elem[1]))
            if self.canvas[elem[1]][elem[0] - 1] == first_color:
                stack.append((elem[0] - 1, elem[1]))

    def print(self):
        for i in self.canvas:
            for j in i:
                self.file.write(j)
            self.file.write("\n")
