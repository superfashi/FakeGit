For more efficent Golang version, please check it here: `https://github.com/hanbang-wang/FakeGit-Go <https://github.com/hanbang-wang/FakeGit-Go>`_

-----

=======
FakeGit
=======
|pypi|

FakeGit is a great tool to fool yourself and others. It will modify your local git config file, deceive git to recognize the committer as somebody else.

You can use it on your own project or any repository, if you have push privilege.

Example
=======
.. image:: https://superfashi.b0.upaiyun.com/wp-content/uploads/2016/07/fakegitdemo.png
    :alt: FakeGit Demo
    :align: center

Those are real commits and will be recognized by Github and almost any git hosting websites as a user of one, if such a user exists.

Installation
============
.. code-block:: bash

    git clone https://github.com/hanbang-wang/FakeGit
    cd FakeGit
    python setup.py install

Or use pip:

.. code-block:: bash

    pip install fakegit

Usage
=====
.. code-block:: bash

    fakegit <command> [--user] [--help|-h]

FakeGit passes all your arguments into the original Git cli, except for the following:

.. code-block:: bash

    change       Change your local identity for ever
    recover      Quickly delete 'user' params in your local git config file
    --help, -h   A brief guide

FakeGit intercepts ``--user`` with exact one arg following, which should be the committer's identity.

Identity Format
---------------
For exact input, use ``name <email>`` format, for example:

.. code-block:: bash

    --user 'John Doe <johndoe@example.com>'

or if you want to keep the email blank, just keep it blank:

.. code-block:: bash

    --user 'No Email <>'

I also provided a quick identity lookup for Github users, fill in name only:

.. code-block:: bash

    --user 'example'

Examples
--------

.. code-block:: bash

    fakegit commit -a -m "An example." --user hanbang-wang

It will use Github API with the id `hanbang_wang`, which is me, lookup my commits history and my commit email, generating a format like `SuperFashi <admin@superfashi.com>` , use it to make commit messages.

But I recommend to specify a user info:

.. code-block:: bash

    fakegit commit -a -m "An example." --user "SuperFashi <admin@superfashi.com>"

of course you can use any git command by FakeGit:

.. code-block:: bash

    fakegit push --user "whateveryoulike <>"
    # same as `git push`

But it would not make any difference, since only the ``commit`` command will use `user` params.

Additions
---------

``fakegit change`` will change your local identity forever, therefore it must followed by ``--user``, or it will throw an error.

``fakegit recover`` is a quick tool for you to delete `user` params in your local git config file, in case of tired being someone else, or need a reset after a force quit.

License & Something
===================
This little project is unlicensed, check `LICENSE <https://github.com/hanbang-wang/FakeGit/blob/master/LICENSE>`_ file for more information. But you should read the following carefully:

**This project has something to do with others identity, so you may end up becoming an identity thief or harm the reputation of others or anything illegal may happen.**

I do not take any responsibility, as I hope this project will only use for harmless jokes, educational or research purpose.

.. |pypi| image:: https://badge.fury.io/py/fakegit.svg
    :target: https://pypi.python.org/pypi/fakegit
