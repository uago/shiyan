# -*- coding:utf-8 -*-

import git
from git import Repo

repo = git.Repo(path='E:/ni')
# assert repo.bare
# new_repo = repo.clone(path="E:/ni/nicai")
# remote = repo.create_remote(name='gitlab', url='git@gitlab.com:USER/REPO.git')
# repo.index.add(items=["txt.txt"])
# repo.index.commit('suibian')
# index = repo.index
# index.add([])
# index.commit()




# print repo
# remote = repo.remote()
git = repo.git
git.add(".")
# git.commit()
# remote.push()
#remote.push()
#remote.fetch()
# remote.pull()
#一键提交，包含add、commit、push操作
# def add_com_push():
