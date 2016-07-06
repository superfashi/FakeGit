import requests

from fakegit.error import UserError

def Expectation(resp):
    ret = resp.json()
    if resp.status_code != 200:
        raise UserError(ret['message'])
    return ret

class GithubUser():
    def __init__(self, name):
        self.findUser(name)

    def getIdentity(self):
        if not 'email' in dir(self):
            raise UserError('No email found for specific user.')
        return self.name, self.email

    def findUser(self, username):
        userInfo = Expectation(requests.get('https://api.github.com/users/' + username))
        self.name = userInfo['name'] or userInfo['login']
        self.getEmail(userInfo['repos_url'])

    def getEmail(self, url):
        reposInfo = Expectation(requests.get(url))
        reposInfo.sort(key = lambda repo: repo['id'], reverse = True)
        for repo in reposInfo:
            if self.getEmailFromRepo(repo['commits_url'][:-6]):
                break

    def getEmailFromRepo(self, url):
        commitsInfo = Expectation(requests.get(url))
        for commit in commitsInfo:
            current = commit['commit']
            if current['author']['name'] == self.name:
                self.email = current['author']['email']
            elif current['committer']['name'] == self.name:
                self.email = current['committer']['email']
            else:
                continue
            return True
        return False
