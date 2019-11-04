from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.readlines()

with open("README.md") as f:
    readme = f.read()


setup(
    name="privacy.py",
    author="FasterSpeeding",
    url="https://github.com/FasterSpeeding/privacy.py",
    version="0.0.1",
    packages=find_packages(),
    license="BSD",
    description="A Python lib for Privacy.com",
    long_description=readme,
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
      ])