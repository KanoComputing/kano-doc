# init_docs.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# The main functionality of the init-docs script.


import os

from kano_doc.utils import confirm, colourise, COLOURS
from kano_doc.paths import DOCS_TEMPLATE_DIR


def main(args):
    """The main functionality of the init-docs script.

    Returns:
        int: The return code of the binary
    """

    repo_path = os.path.abspath(args['<repo-path>'])
    repo_name = os.path.basename(repo_path)
    repo_docs_path = os.path.join(repo_path, 'docs')

    print 'Please double check the following:'
    print ' 1) {} directory will be created if needed for the new docs'.format(
        colourise(repo_docs_path, COLOURS['value'])
    )
    print ' 2) Docs template files from {} will be copied to {}'.format(
        colourise(DOCS_TEMPLATE_DIR, COLOURS['value']),
        colourise(repo_docs_path, COLOURS['value'])
    )
    print ' 3) {} will be used as the repository name in the docs'.format(
        colourise(repo_name, COLOURS['value'])
    )

    if (not args['--no-confirm'] and
       not confirm('Are you sure you want to continue? [Y/N]: ')):
        print 'Exiting..'
        return 0

    # Ensure docs path.
    cmd = 'mkdir -p {repo_docs_path}'.format(repo_docs_path=repo_docs_path)
    print cmd
    if not args['--dry-run']:
        os.system(cmd)

    # Copy the template docs to the new repo.
    cmd = (
        'cp -r {docs_template}/* {repo_docs_path}'
        .format(docs_template=DOCS_TEMPLATE_DIR, repo_docs_path=repo_docs_path)
    )
    print cmd
    if not args['--dry-run']:
        os.system(cmd)

    # Ensure the name is appropriate for the repo.
    cmd = (
        'find {repo_docs_path} -type f -exec sed -i "" -e'
        ' "s/kano-peripherals/{repo_name}/g" {{}} \;'
        .format(repo_docs_path=repo_docs_path, repo_name=repo_name)
    )
    print cmd
    if not args['--dry-run']:
        os.system(cmd)

    return 0
