# Copyright 2014 Jon Eyolfson
#
# This file is distributed under the GPLv3 license

import datetime
import logging
import markdown
import os
import pygit2

from django_blog.models import Post
from django_gitolite.utils import home_dir

logger = logging.getLogger('django_blog')

def update_blog(push):
    repo_path = push.repo.path
    if repo_path != 'jon/site-eyl-blog':
        return
    git_repo = pygit2.Repository(
        os.path.join(home_dir(), 'repositories', '{}.git'.format(repo_path))
    )
    # TODO: There is no diff if this is the first commit
    for patch in git_repo.diff(push.old_rev, push.new_rev):
        if patch.status == 'A':
            pass
        elif patch.status == 'M':
            if patch.old_file_path != patch.new_file_path:
                print("Old and new file paths do not match")
                continue
        elif patch.status == 'D':
            slug = patch.old_file_path.rstrip('.md')
            post = Post.objects.get(slug=slug)
            post.delete()
            continue
        else:
            print("Unhandled status '{}'".format(patch.status))
            continue
        file_path = patch.new_file_path
        slug = file_path.rstrip('.md')
        markdown_content = git_repo[patch.new_id].data.decode()
        md = markdown.Markdown(extensions=['headerid(level=2, forceid=False)',
                                           'meta',
                                           'tables'],
                               output_format='html5')
        content = md.convert(markdown_content)
        title = md.Meta['title'][0]
        post, created = Post.objects.get_or_create(
            slug=slug,
            defaults={'date': datetime.date.today(),}
        )
        post.content = content
        post.title = title
        post.save()
