#!/usr/bin/python3

def print_stats(size, stats):
    """Function to print the dict containing data and file size
    Args:
        size -> is size of each file
        stats -> are the stats key/value for each input in dict
    """
    print(f"File size: {size}")
    for k in sorted(stats):
        print(f"{k}: {stats[k]}")

if __name__ == '__main__':
    from sys import stdin

    lineCount = 0
    fileSize = 0
    statsCollect = {}
    statsCodes = ['200', '301', '400', '401', '403', '404', '405', '500']
    try:
        for line in stdin:
            if lineCount == 10:
                print_stats(fileSize, statsCollect)
                lineCount = 1
            else:
                lineCount += 1

            line = line.split()
            try:
                fileSize += int(line[-1])
            except (IndexError, ValueError):
                pass

            key = line[-2]
            try:
                if key in statsCodes:
                    if key in statsCollect:
                        statsCollect[key] += 1
                    else:
                        statsCollect[key] = 1
            except IndexError:
                pass
        print_stats(fileSize, statsCollect)
    except KeyboardInterrupt:
        print_stats(fileSize, statsCollect)
