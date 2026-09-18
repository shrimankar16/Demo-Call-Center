from setuptools import find_packages, setup

project_name = "call-center-analytics"
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=project_name,
    packages=[project_name],
    package_dir={project_name: "src"},
    version="1.0.0",
    description="AI-powered call center analytics platform using LLMs and MLRun for automated call transcription, analysis, and insights generation",
    author="Shrijay Mankar",
    author_email="shrimankar16@example.com",
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    url="https://github.com/shrimankar16/Demo-Call-Center",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
