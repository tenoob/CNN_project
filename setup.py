import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_desc = f.read()


__version__ = "0.0.1"

REPO_NAME = 'CNN_project'
AUTHOR_USER_NAME = 'tenoob'
SRC_REPO = 'cnnProject'
AUTHOR_EMAIL = 'kanandmohan8@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A demo on how to develop a dl project as package",
    long_description=long_desc,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)