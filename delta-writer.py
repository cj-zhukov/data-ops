import boto3
import polars as pl
from deltalake import write_deltalake


if __name__ == "__main__":
    print("reading data")
    file = "s3://bucket/foo.parquet"
    df = pl.read_parquet(file)

    storage_options = {
        "aws_access_key_id": "",
        "aws_secret_access_key": "",
        "aws_session_token": "",
        "aws_region": "eu-central-1",
        "AWS_S3_ALLOW_UNSAFE_RENAME": "true",
    }

    print("writing data to delta")
    df.write_delta(
        "s3://bucket/dev/foo.parquet",
        mode="append",
        storage_options=storage_options,
    )
