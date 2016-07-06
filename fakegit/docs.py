HELP_DOCS = '''FakeGit is a great tool to fool yourself and others, it will modify your local git config file, deceive git to recognize the committer as somebody else.

Usage: fakegit <command> [--user] [--help|-h]

FakeGit passes all your arguments into original Git cli, except for the following:

    change	Change your local identity for ever
    recover	Quickly delete 'user' params in your local git config file
    --help, -h	This brief guide

FakeGit intercepts '--user' with exact one arg following, which is the committer's identity.

Identity format:

    for exact input, use 'name <email>' format, for example:
    	--user 'John Doe <johndoe@example.com>'
    or if you want to keep the email blank, just keep it blank:
    	--user 'No Email <>'

    I also provided a quick identity lookup for Github users, fill in name only:
    	--user 'example'
    then it will lookup user with this id in Github.

For more info, please check the README file.'''
