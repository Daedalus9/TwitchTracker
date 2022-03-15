import sys
from module.search import search
from module.store import store
from module.delete import delete

def main():
    args = sys.argv[1:]
    if len(args)>0:
        if args[0] == '--search':
            search()
        elif args[0] == '--store':
            store()
        elif args[0] == '--delete':
            delete()

if __name__ == '__main__':
    main()