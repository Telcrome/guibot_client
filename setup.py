import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="guibot",
    version="0.0.1",
    author="Telcrome",
    author_email="raphaelschaefer1@outlook.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Telcrome/guibot_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        bot=guibot.cli:bot
    ''',
    python_requires='>=3.8',
    install_requires=[
        'click'
    ],
)
