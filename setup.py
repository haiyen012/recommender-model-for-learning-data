from pathlib import Path

from setuptools import find_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

style_packages = [
    "black==23.3.0",
    "flake8==6.0.0",
    "mypy==1.8.0",
    "isort==5.12.0",
    "pre-commit==3.3.2",
]

test_packages = ["pytest==7.3.2"]

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="recsys_for_learning_data",
    version="0.1",
    description="Master Recommendation System project for Learning data",
    long_description=readme,
    author="YenNguyenHai",
    author_email="yenhai.work@gmail.com",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.10",
    extras_require={
        "dev": required_packages + style_packages + test_packages,
        "test": required_packages + test_packages,
    },
)