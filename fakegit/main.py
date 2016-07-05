import os

from fakegit.args import procArgs
from fakegit.error import ArgumentError
from fakegit.gitconf import GitConf

def main():
    addition, name, email, forever = procArgs()
    cfg = GitConf()
    if forever and not name:
        raise ArgumentError('No user specified.')
    if name:
        cfg.change(name, email)
    if not forever:
        print('git ' + addition)
        os.system('git ' + addition)
        if name:
            cfg.recover()

if __name__ == '__main__':
    main()
