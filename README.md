### TODO

verifier les libs python sur Databricks et Databricks for ML
en particulier Panda, Numpy et Pytorch

i
faire un POC avec Panda
faire un POC parallelisme Python+Spark
faire un POC dataclass/dataset




```bash 
conda init
conda --version
conda create -n sparkml python=3.12
conda activate sparkml
conda install pyspark
conda install pandas

# optionnel: conda list --export > requirements.txt

python -m pip install --upgrade build
python -m build


python sparkml/jobs/wordcount.py

ou

python -m sparkml.jobs.wordcount

# installe en mode snapshot le module (point sur son workspace)
pip install -e .[dev]
```

https://docs.databricks.com/aws/en/pandas/pandas-on-spark