import sys
import re

from fakegit.error import ArgumentError
from fakegit.github import GithubUser
from fakegit.gitconf import GitConf

def makeC(argx):
    ret = [repr(arg) if arg.count(' ') else arg for arg in argx]
    return ret

def procUser(argx):
    name = None
    email = ''
    if '--user' in argx:
        ind = argx.index('--user')
        argx.pop(ind)
        if ind >= len(argx):
            raise ArgumentError('Command excuted with inappropriate argument.')
        info = argx.pop(ind)
        name, email = re.findall(r'([\w -]+)(<.*@.*>|<>)?', info)[0] # such dirty regex
        name = name.strip()
        if name == '':
            raise ArgumentError('Username needed.')
        if email == '':
            print('Finding user %s...' % name)
            fake = GithubUser(name)
            name, email = fake.getIdentity()
            print('User found: %s <%s>' % (name, email))
        else:
            email = email[1:-1]
    return ' '.join(makeC(argx)), name, email, 'change' in argx

def showHelp(argx = []):
    print('''this is a help
text which ks nonsence''')
    exit(0)

def procArgs():
    if len(sys.argv) < 2:
        showHelp()
    cliArgs = sys.argv[1:]
    if '--help' in cliArgs or '-h' in cliArgs:
        showHelp(cliArgs)
    if 'recover' in cliArgs:
        GitConf().recover()
        print('Config file reset.')
        exit(0)
    return procUser(cliArgs)
