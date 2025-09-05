from setuptools import setup, find_packages

setup(
    name="sparkml",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyspark>=4.0.0"
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "run-wordcount = sparkml.jobs.wordcount:run_wordcount",
        ],
    },
)
