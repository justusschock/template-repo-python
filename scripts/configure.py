import os
import shutil


def get_root_path():
    return os.path.dirname(os.path.dirname(__file__))


def set_repo_name(name: str):
    base_path = get_root_path()
    new_path = os.path.join(os.path.dirname(base_path), name)
    shutil.move(base_path, new_path)

    files = ['setup.cfg'
             ]

    for file in files:
        replace_file_content(os.path.join(base_path, file), 'REPONAME', name)

    return new_path


def read_file(file: str):
    with open(file) as f:
        content = f.readlines()
    return content


def remove_script(new_path: str):
    os.remove(os.path.join(new_path,
                           os.path.basename(os.path.dirname(__file__)),
                           os.path.basename(__file__)))


def replace_file_content(file: str, original_content: str, new_content: str):
    curr_content = read_file(file)

    for idx, line in enumerate(curr_content):
        curr_content[idx] = line.replace(original_content, new_content)

    with open(file, 'w') as f:
        f.writelines(curr_content)


def remove_starting_string(file: str, start_str: str):
    curr_content = read_file(file)

    for idx, line in enumerate(curr_content):
        if line.startswith(start_str):
            curr_content[idx] = line[len(start_str):]

    with open(file, 'w') as f:
        f.writelines(curr_content)


def remove_lines_with_starting_string(file: str, start_str: str):
    curr_content = read_file(file)

    new_content = []
    for line in curr_content:
        if line.startswith(start_str):
            continue

        new_content.append(line)

    with open(file, 'w') as f:
        f.writelines(new_content)


def set_package_name(name: str):
    files = ['setup.cfg',
             'setup.py',
             '.gitattributes',
             'MANIFEST.in',
             os.path.join('.github', 'workflows', 'unittests.yml')
             ]

    base_path = get_root_path()

    for file in files:
        replace_file_content(os.path.join(base_path, file), 'REPONAME', name)

    shutil.move(os.path.join(base_path, 'REPONAME'),
                os.path.join(base_path, name))


def set_github_name(name: str):
    files = ['setup.py',
             '.readthedocs.yml',
             'LICENSE',
             '.mergify.yml'
             ]

    base_path = get_root_path()

    for file in files:
        replace_file_content(
            os.path.join(
                base_path,
                file),
            'GITHUB_NAME',
            name)

    shutil.move(os.path.join(base_path, 'GITHUB_NAME'),
                os.path.join(base_path, name))

def set_author_name(name: str):
    files = ['setup.py',
             '.readthedocs.yml',
             'LICENSE',
             '.mergify.yml'
             ]

    base_path = get_root_path()

    for file in files:
        replace_file_content(
            os.path.join(
                base_path,
                file),
            'AUTHOR_NAME',
            name)

    shutil.move(os.path.join(base_path, 'AUTHOR_NAME'),
                os.path.join(base_path, name))


def set_author_email(name: str):
    files = ['setup.py']

    base_path = get_root_path()

    for file in files:
        replace_file_content(
            os.path.join(
                base_path,
                file),
            'AUTHOR_EMAIL',
            name)

    shutil.move(os.path.join(base_path, 'AUTHOR_EMAIL'),
                os.path.join(base_path, name))


def set_maintainer_name(name: str):
    files = ['setup.py']

    base_path = get_root_path()

    for file in files:
        replace_file_content(
            os.path.join(
                base_path,
                file),
            'MAINTAINER_NAME',
            name)

    shutil.move(os.path.join(base_path, 'MAINTAINER_NAME'),
                os.path.join(base_path, name))


def set_maintainer_email(name: str):
    files = ['setup.py']

    base_path = get_root_path()

    for file in files:
        replace_file_content(
            os.path.join(
                base_path,
                file),
            'MAINTAINER_EMAIL',
            name)

    shutil.move(os.path.join(base_path, 'MAINTAINER_EMAIL'),
                os.path.join(base_path, name))


def configure_coverage_upload(enable: bool):
    file = os.path.join(get_root_path(),
                        '.github', 'workflows', 'unittests.yml')
    start_str = '#COVERAGE_UPLOAD_CONFIG'

    if enable:
        remove_starting_string(file, start_str=start_str)
    else:
        remove_lines_with_starting_string(file, start_str=start_str)


def exec_fn_with_exception_guard(fn, *args, **kwargs):
    ret_val = None
    try:
        ret_val = fn(*args, **kwargs)
        return True, ret_val
    except Exception as e:
        print(e)
        return False, ret_val


def successfull(*args, **kwargs):
    return True

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo_name', type=str,
                        help='The new folder name for the repository',
                        default=None)
    parser.add_argument(
        '--package_name', type=str,
        help='The new name of the python package included in this directory',
        default=None)

    parser.add_argument(
        '--github_name',
        type=str,
        help='The name of the github accont of the python package included in this directory',
        default=None)
    parser.add_argument(
        '--author_name',
        type=str,
        help='The name of the author of the python package included in this directory',
        default=None)
    parser.add_argument(
        '--author_email',
        type=str,
        help='The email address of the author of the python package included in this directory',
        default=None)
    parser.add_argument(
        '--maintainer_name',
        type=str,
        help='The name of the maintainer of the python package included in this directory',
        default=None)
    parser.add_argument(
        '--maintainer_email',
        type=str,
        help='The email address of the maintainer of the python package included in this directory',
        default=None)

    parser.add_argument('--enable_coverage_upload', action='store_true',
                        help='Whether to enable or disable the coverage '
                             'reports for this repository')

    return parser.parse_args()

def main():
    parser_args = parse_args()

    returns, successes = {}, {}
    functions = OrderedDict()

    if parser_args.repo_name is None:
        repo_name_fn = successfull
    else:
        repo_name_fn = partial(set_repo_name, name=parser_args.repo_name)

    if parser_args.package_name is None:
        package_name_fn = successfull
    else:
        package_name_fn = partial(set_package_name,
                                  name=parser_args.package_name)

    if parser_args.github_name is None:
        github_name_fn = successfull
    else:
        github_name_fn = partial(set_github_name,
                                 name=parser_args.github_name)

    if parser_args.author_name is None:
        author_name_fn = successfull
    else:
        author_name_fn = partial(set_author_name,
                                 name=parser_args.author_name)

    if parser_args.author_email is None:
        author_email_fn = successfull
    else:
        author_email_fn = partial(set_author_email,
                                  name=parser_args.author_email)

    if parser_args.maintainer_name is None:
        maintainer_name_fn = successfull
    else:
        maintainer_name_fn = partial(set_maintainer_name,
                                     name=parser_args.maintainer_name)

    if parser_args.maintainer_email is None:
        maintainer_email_fn = successfull
    else:
        maintainer_email_fn = partial(set_maintainer_email,
                                      name=parser_args.maintainer_email)

    functions['coverage_upload'] = partial(
        configure_coverage_upload,
        enable=parser_args.enable_coverage_upload)

    functions['package_name'] = package_name_fn
    functions['repo_name'] = repo_name_fn
    functions['author_name'] = author_name_fn
    functions['author_email'] = author_email_fn
    functions['maintainer_name'] = maintainer_name_fn
    functions['maintainer_email'] = maintainer_email_fn

    for name, func in functions.items():
        success, ret_val = exec_fn_with_exception_guard(func)

        returns[name] = ret_val
        successes[name] = success


if __name__ == '__main__':
    from functools import partial
    import argparse
    from collections import OrderedDict

    main()
