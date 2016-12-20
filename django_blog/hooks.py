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
        delta = patch.delta
        if delta.status == pygit2.GIT_DELTA_ADDED:
            pass
        elif delta.status == pygit2.GIT_DELTA_MODIFIED:
            if delta.old_file.path != delta.new_file.path:
                print("Old and new file paths do not match")
                continue
        elif delta.status == pygit2.GIT_DELTA_DELETED:
            slug = delta.old_file.path.rstrip('.md')
            post = Post.objects.get(slug=slug)
            post.delete()
            continue
        else:
            print("Unhandled status '{}'".format(delta.status))
            continue
        file_path = delta.new_file.path
        slug = file_path.rstrip('.md')
        markdown_content = git_repo[delta.new_file.id].data.decode()
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
