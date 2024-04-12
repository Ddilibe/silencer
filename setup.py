import io
import re

from setuptools import setup


def read(path):
    with io.open(path, mode="r", encoding="utf-8") as fd:
        content = fd.read()
    # Convert Markdown links to reStructuredText links
    return re.sub(r"\[([^]]+)\]\(([^)]+)\)", r"`\1 <\2>`_", content)


setup(
    name = 'Silencer',
    version = '0.18',
    author = 'Fidelugwuowo Dilibe',
    author_email = 'franklinfidelugwuowo@gmail.com',
    packages = ['silencer', 'silencer.plugins'],
    url = 'https://github.com/aerkalov/ebooklib',
    license = 'MIT License',
    description = 'Audio Book Generator which converts a book to an audiobook',
    long_description = read('README.md'),
    long_description_content_type = 'text/markdown',
    keywords = ['audio', 'books', 'audiobook', 'reading'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires = [
       "lxml", "six"
    ]
)