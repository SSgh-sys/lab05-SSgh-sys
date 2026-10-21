# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")
    parser.add_arguement(
        '-i', '--ignorecase',
        action='store_true',
        help ="Ignore case distinctions during processing."
    )

    args = parser.parse_args()

    if args.ignore_case:
        print("Case-insensitive mode is enabled")
    else:
        print("Case-sensitive mode is enabled.")


    a,b,c = (1,2,3)
    file = open(args.filename)
    pattern = args.pattern
    for lineNumber, line in enumerate (file, start=1):
        line = line.rstrip("\n")
        if pattern.lower() in line.lower():
            #print(f"{lineNumber}: {line}")
            print(str(lineNumber) + ": " + line)
    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).
    file.close()

if __name__ == "__main__":
    main()


#Finish find.py so that it prints every line of a file that contains a given pattern, 
#each prefixed with its line number (counting from 1). 
#Then add an optional -i / --ignore-case flag that makes the match ignore upper/lower case.