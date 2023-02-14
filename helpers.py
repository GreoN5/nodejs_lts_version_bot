import os
import subprocess
import urllib.request


def node_version_parser(version: str):
    return tuple(map(int, (version.split('v')[1].split('.'))))


def get_current_node_version():
    output = run_shell_output(['node', '-v'])

    return output.stdout.decode('utf-8')


def check_nvm_usage():
    '''
        Returns False if there is no error during execution of the command "nvm -v", otherwise True.
    '''

    output = run_shell_output(['nvm', '-v'])

    # check if we get error when running the command
    return bool(output.stderr)


def run_shell_output(args):
    return subprocess.run(args, capture_output=True, shell=True)


def run_node_installer(node_version, download_link):
    current_path = get_current_path()
    file_extension = '.msi'
    file_appendix = 'node'
    file_windows_version = 'x64'

    filename = f'{file_appendix}-{node_version}-{file_windows_version}{file_extension}'
    url = f'{download_link}{filename}'

    urllib.request.urlretrieve(url, filename)
    node_exe_path = f'{current_path}\{filename}'

    # run the node installer
    os.system(node_exe_path)


def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))
