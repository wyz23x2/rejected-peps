import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rejected-peps",
    version="0.2.0a3",
    author="wyz23x2",
    author_email="wyz23x2@163.com",
    description="A python package that implements some rejected or withdrawn PEPs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/wyz23x2/rejected/",
    project_urls={
        "Bug Tracker": "https://gitee.com/wyz23x2/rejected-peps/issues",
        "Wiki": "https://gitee.com/wyz23x2/rejected-peps/wikis"
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "rejected_peps"},
    packages=[],
    python_requires=">=3.6",
)