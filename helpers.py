import os
import subprocess


def node_version_parser(version: str):
    return tuple(map(int, (version.split('v')[1].split('.'))))


def get_current_node_version():
    return subprocess.check_output('node -v').strip().decode('utf-8')


def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))
