from setuptools import setup, find_packages

setup(
    name="sparkml",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # ici, uniquement les dépendances obligatoires pour que le package tourne
    ],
    extras_require={
        "dev": ["pandas==1.5.*", "numpy>=1.26",
                "pytest",  # tests unitaires
                ],
        "spark": ["pyspark>=3.5"],
    },

    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "run-wordcount = sparkml.jobs.wordcount:run_wordcount",
        ],
    },
)
