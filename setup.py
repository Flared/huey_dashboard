import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def rel(*xs: str) -> str:
    return os.path.join(here, *xs)


with open(rel("README.md")) as f:
    long_description = f.read()


with open(rel("src", "task_dashboard", "__init__.py"), "r") as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip('"')
            break
    else:
        raise RuntimeError("Version marker not found.")


dependencies = [
    "task-logs @ git+https://github.com/Flared/task-logs.git@master#egg=task-logs",
    "typing_extensions",
    "flask>=1.1.0",
]

extra_dependencies = {}

extra_dependencies["test"] = dependencies + [
    "pytest",
    "pytest-cov",
]

extra_dependencies["dev"] = dependencies + [
    # Linting
    "flake8",
    "flake8-bugbear",
    "flake8-quotes",
    "isort",
    "mypy",
    "black",
    # Testing
    "pytest",
    "pytest-cov",
    # Docs
    # "sphinx",
    # "sphinx-autodoc-typehints",
]

setup(
    name="task-dashboard",
    version=version,
    author="Flare Systems Inc.",
    author_email="oss@flare.systems",
    description="Generic dashboard for task managers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flared/task-dashboard",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=dependencies,
    python_requires=">=3.5",
    extras_require=extra_dependencies,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
