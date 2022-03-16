import re

from setuptools import setup

version = ''
with open('discord/ext/menus/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

setup(
    name='discord-ext-menus',
    author='Rapptz',
    url='https://github.com/hawk-tomy/discord-ext-menus',
    version=version,
    packages=['discord.ext.menus'],
    license='MIT',
    description='An extension module to make reaction based menus with discord.py',
    install_requires=['git+https://github.com/Rapptz/discord.py'],
    python_requires='>=3.9'
)
