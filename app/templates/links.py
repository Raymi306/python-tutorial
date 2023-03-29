"""Exports links for templating"""
from app import config

BASE_URL = config['TUTORIAL_BASE_URL']

# pylint: disable=line-too-long
links = {
        'ext_github_repo': 'https://github.com/Raymi306/python-tutorial',
        'ext_python_dl_page': 'https://www.python.org/downloads',
        'ext_python3_stdlib': 'https://docs.python.org/3/library/',
        'ext_python3_file_io': 'https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files',
        'ext_python3_context_managers': 'https://docs.python.org/3/reference/datamodel.html#context-managers',
        'ext_python3_venv_activate_commands': 'https://docs.python.org/3/library/venv.html#how-venvs-work',
        'ext_stdlib_random': 'https://docs.python.org/3/library/random.html',
        'ext_stdlib_sys': 'https://docs.python.org/3/library/sys.html',
        'ext_requests_docs': 'https://docs.python-requests.org/en/latest/index.html',
        'ext_beautifulsoup4_docs': 'https://beautiful-soup-4.readthedocs.io/en/latest/#',
        'ext_automate_the_boring_stuff': 'https://automatetheboringstuff.com/',
        'ext_invent_with_python': 'https://inventwithpython.com/',
        'ext_codewars': 'https://codewars.com',
        'int_home': config['HOMEPAGE_URL'],
        'int_index': f'{BASE_URL}/index.html',
        'int_misc': f'{BASE_URL}/misc.html',
        'int_misc_paths': f'{BASE_URL}/misc.html#path-variables',
        'int_misc_shells': f'{BASE_URL}/misc.html#command-prompts-shells-terminals',
        'int_misc_text_editors': f'{BASE_URL}/misc.html#common-text-editors',
        'int_misc_file_paths': f'{BASE_URL}/misc.html#files-and-file-paths',
        'int_resources': f'{BASE_URL}/resources.html',
        'int_installation': f'{BASE_URL}/00_installation.html',
        'int_running_code': f'{BASE_URL}/01_how_to_run_code.html',
        'int_programming_overview': f'{BASE_URL}/02_programming_overview.html',
        'int_first_steps': f'{BASE_URL}/10_first_steps.html',
        'int_first_projects': f'{BASE_URL}/11_first_projects.html',
        }
# pylint: enable=line-too-long
