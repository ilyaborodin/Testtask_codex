class Checker:
    def __init__(self):
        self.width = None
        self.height = None

    def check_canvas(self, command):
        checker = None
        try:
            if len(command) == 3 and int(command[1]) > 0 and int(command[2]) > 0:
                self.width = int(command[1])
                self.height = int(command[2])
                checker = 1
            else:
                checker = 2
        except:
            checker = 2
        finally:
            return self.output(checker, command)

    def check_line_and_rect(self, command):
        checker = None
        try:
            if len(command) == 5 and self.check_width(command[1]) and self.check_height(command[2]) and \
                    self.check_width(command[3]) and self.check_height(command[4]):
                if command[0] == "R" or (command[1] == command[3] or command[2] == command[4]):
                    checker = 1
                else:
                    checker = 2
                if not self.canvas_is_created():
                    checker = 3
            else:
                checker = 2
        except:
            checker = 2
        finally:
            return self.output(checker, command)

    def check_bucket_fill(self, command):
        checker = None
        try:
            if len(command) == 4 and self.check_width(command[1]) and self.check_height(command[2]):
                checker = 1
            else:
                checker = 2
            if not self.canvas_is_created():
                checker = 3
            if len(command[3]) != 1:
                checker = 4
        except:
            checker = 2
        finally:
            return self.output(checker, command)

    def check_width(self, num):
        if 0 < int(num) < self.width + 1:
            return True
        else:
            return False

    def check_height(self, num):
        if 0 < int(num) < self.height + 1:
            return True
        else:
            return False

    def canvas_is_created(self):
        if self.height is not None and self.width is not None:
            return True
        else:
            return False

    def output(self, checker, command):
        if checker == 1:
            return True
        if checker == 2:
            print("invalid input: " + str(command))
            return False
        if checker == 3:
            print("canvas is not created")
            return False
        if checker == 4:
            print("Length of color must be 1")
            return False
