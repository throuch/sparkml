import logging

from sparkml.jobs.wordcount import wordcount
from sparkml.utils.spark_session import get_spark_session
from src.main import create_df

# Configurer le logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def test_dummy():
    logger.info("Ceci est un log dans le test")
    assert 1 + 1 == 2

def test_create_df():
    df = create_df()

    df.show()
    logger.info("DataFrame créé avec %d lignes", df.count())
    assert df.count() == 2

def test_wordcount(spark):
    df =wordcount(spark, './resources/sample.txt')
    df.show()