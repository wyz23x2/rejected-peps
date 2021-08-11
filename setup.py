import rejected_peps
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rejected-peps",
    version=rejected_peps.__version__,
    author="wyz23x2",
    author_email="wyz23x2@163.com",
    description="A Python package that implements some rejected or withdrawn PEPs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wyz23x2/rejected-peps/",
    project_urls={
        "Bug Tracker": "https://github.com/wyz23x2/rejected-peps/issues",
        "Changelog": "https://github.com/wyz23x2/rejected-peps/blob/main/CHANGELOG.md"
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Typing :: Typed",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)