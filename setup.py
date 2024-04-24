from setuptools import find_packages, setup

setup(
    name="r2config",
    version="0.1.0",
    author="xiaowenz",
    author_email="xiaowen.z@outlook.com",
    description="R2 Config Center.",
    url="https://github.com/iamshaynez/R2ConfigCenter",
    project_urls={
        "Bug Report": "https://github.com/iamshaynez/R2ConfigCenter/issues/new",
    },
    install_requires=[
        "boto3",
    ],
    packages=find_packages(),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["r2config = ConfigCenter.r2config:main"],
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
