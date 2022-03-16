import sys
from module.search import search
from module.store import store
from module.delete import delete
from module.plots import plots
from module.help import help

def main():
    args = sys.argv[1:]
    if len(args)>0:
        if args[0] == '--search':
            search()
        elif args[0] == '--store':
            store()
        elif args[0] == '--delete':
            delete()
        elif args[0] == '--plots':
            plots()
        elif args[0] == '--help':
            help()
        else:
            help()
    else:
        help()

if __name__ == '__main__':
    main()