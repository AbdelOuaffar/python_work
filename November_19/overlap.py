class LineSegment:
    start = 0
    end = 0

    #constructor
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlap(self, line2):
        if self.start > line2.end or self.end < line2.start:
            return False

        return True

    def __str__(self):
        return f"({self.start}, {self.end})"

def print_line_segment(line_segment):
    print(f"start: {line_segment.start} end: {line_segment.end}")

def main():
    line1 = LineSegment(13, 22)
    line2 = LineSegment(13, 22)
    print_line_segment(line1)
    print_line_segment(line2)

    is_overlapping = line1.overlap(line2)
    if is_overlapping:
        print(f"{line1} overlaps with {line2}")
    else:
        print(f"{line1} doesnt ovelap with{line2}")

if __name__ == '__main__':
    main()


