from setuptools import find_packages, setup

setup(
    name="statehelper",
    version="0.1.0",
    author="xiaowenz",
    author_email="xiaowen.z@outlook.com",
    description="High quality image generation by ideogram.ai. Reverse engineered API.",
    url="https://github.com/iamshaynez/service-state-helper",
    project_urls={
        "Bug Report": "https://github.com/iamshaynez/service-state-helper/issues/new",
    },
    install_requires=[
        "boto3",
    ],
    packages=find_packages(),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["statehelper = statehelper.statehelper:main"],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
