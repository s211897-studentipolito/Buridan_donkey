import random
import sys
import datetime

if __name__ == '__main__':
    args = list()
    start = datetime.datetime.now()
    if not sys.stdin.isatty():
        for line in sys.stdin:
            args.append(line)
    else:
        args = sys.argv[1:]
    argRange = len(args)
    for i in range(argRange):
        print(str(i+1) + '.', args.pop(random.randrange(0, len(args))))    
    end = datetime.datetime.now()
    print('\n', start, end)
