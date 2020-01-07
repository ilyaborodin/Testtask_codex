from Checker import Checker
from Canvas import Canvas


if __name__ == "__main__":
    file = open("output.txt", "w")
    Canvas1 = Canvas(file)
    Checker1 = Checker()
    try:
        with open("input.txt", "r") as f:
            commands = f.read().splitlines()
    except:
        print("create input.txt")
        exit()
    for command in commands:
        split_command = command.split()
        used = False
        if split_command[0] == "C":
            if Checker1.check_canvas(split_command):
                Canvas1.make_canvas(int(split_command[1]), int(split_command[2]))
                used = True
        if split_command[0] == "L":
            if Checker1.check_line_and_rect(split_command):
                Canvas1.make_line(int(split_command[1]), int(split_command[2]),
                                  int(split_command[3]), int(split_command[4]),)
                used = True

        if split_command[0] == "R":
            if Checker1.check_line_and_rect(split_command):
                Canvas1.make_rect(int(split_command[1]), int(split_command[2]),
                                  int(split_command[3]), int(split_command[4]),)
                used = True

        if split_command[0] == "B":
            if Checker1.check_bucket_fill(split_command):
                Canvas1.bucket_fill(int(split_command[1]), int(split_command[2]), split_command[3])
                used = True

        if Canvas1.canvas is not None and used == True:
            Canvas1.print()
    file.close()
