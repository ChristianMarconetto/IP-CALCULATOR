class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def readLinesWithFourDots(self):
        lines_with_four_dots = []
        with open(self.filename, 'r') as file:
            for line in file:
                if len(line.split(".")) == 4:
                    lines_with_four_dots.append(line.replace("\n","").strip())
        return lines_with_four_dots
