import os

from fakegit.error import GitConfigError

class GitConf():
    def __init__(self, path = '.git/config'):
        if not os.path.exists(path):
            raise GitConfigError('No git config file found, make sure you are under a git repository folder.')
        self.__basecommand = 'git config -f %s ' % path

    def change(self, name, email):
        os.system(self.__basecommand + 'user.name ' + name)
        os.system(self.__basecommand + 'user.email ' + email)

    def recover(self):
        os.system(self.__basecommand + '--remove-section user')
