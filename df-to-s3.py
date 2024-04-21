import boto3
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import logging
import os


logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
if not logger.handlers:
    logger.addHandler(logging.StreamHandler())


def df_to_s3(df, bucket, key):
    client = boto3.client("s3")
    table = pa.Table.from_pandas(df)
    writer = pa.BufferOutputStream()
    pq.write_table(table, writer)

    try:
        client.put_object(Body=bytes(writer.getvalue()),
                          Bucket=bucket, Key=key)
        logger.info(f"file is written {key}")
    except Exception as e:
        logger.info(f"unable to s3 upload {key}: {e} ({type(e)})")


if __name__ == "__main__":
    d = {'id': [1, 2, 3], 'name': ["foo", "bar", "baz"]}
    df = pd.DataFrame(data=d)
    df_to_s3(df, "dmg-data-dev", "szhukov/data/foo.parquet")
