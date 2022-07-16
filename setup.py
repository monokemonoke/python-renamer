from setuptools import setup

setup(
    name="renamer",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "renamer = src.app:main"
        ]
    }
)