#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import git
import gitlab
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def pull(http_url_to_repo):
    path = http_url_to_repo.strip()
    path = path.replace(' ', '').replace('http://', '').replace('https://', '')
    path = path.replace('.git', '')
    path = os.path.join("code/" + path)
    if not os.path.isdir(path):
        try:
            print(f"Git clone to {path}")
            git.Repo.clone_from(http_url_to_repo, path)
        except Exception as e:
            print(e)


def get_users(gl):
    try:
        users = gl.users.list()
        print(users)
    except Exception as e:
        print(e)


def get_issues(gl):
    try:
        issues = gl.issues.list()
        print(issues)
    except Exception as e:
        print(e)


def get_project_members(project):
    try:
        print("Get members in project")
        members = project.members_all.list(all=True)
        print(members)
    except Exception as e:
        print(e)


def get_project_snippets(project):
    try:
        print("Get snippets in project")
        snippets = project.snippets.list()
        print(snippets)
    except Exception as e:
        print(e)


def get_projects(gl):
    try:
        projects = gl.projects.list(all=True)
        for project in projects:
            print(f"{project.name_with_namespace} | {project.http_url_to_repo}")
            pull(project.http_url_to_repo)
            print('----')
    except Exception as e:
        print(e)


def main():
    gitlab_url = sys.stdin.read().strip()
    if gitlab_url != None:
        # anonymous read-only access for public resources (GitLab.com)
        gl = gitlab.Gitlab()
        # anonymous read-only access for public resources (self-hosted GitLab instance)
        gl = gitlab.Gitlab(gitlab_url)
        gl.ssl_verify = False

        get_projects(gl)
    else:
        sys.exit(1)


main()
