import requests

from fakegit.error import UserError

class GithubUser():
    def __init__(self, name):
        self.findUser(name)

    def getIdentity(self):
        if not 'email' in dir(self):
            raise UserError('No email found for specific user.')
        return self.name, self.email

    def findUser(self, username):
        userInfo = requests.get('https://api.github.com/users/' + username)
        if userInfo.status_code == 404:
            raise UserError('No such user found.')
        elif userInfo.status_code == 403:
            raise UserError('You have reached Github API\'s rate limit, please wait for an hour.')
        self.name = userInfo.json()['name'] or userInfo.json()['login']
        self.getEmail(userInfo.json()['repos_url'])

    def getEmail(self, url):
        reposInfo = requests.get(url).json()
        reposInfo.sort(key = lambda repo: repo['id'], reverse = True)
        for repo in reposInfo:
            if self.getEmailFromRepo(repo['commits_url'][:-6]):
                break

    def getEmailFromRepo(self, url):
        commitsInfo = requests.get(url)
        for commit in commitsInfo.json():
            current = commit['commit']
            if current['author']['name'] == self.name:
                self.email = current['author']['email']
            elif current['committer']['name'] == self.name:
                self.email = current['committer']['email']
            else:
                continue
            return True
        return False
