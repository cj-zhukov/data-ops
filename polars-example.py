import polars as pl


def get_df():
    df = pl.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["foo", "bar", "baz"],
        }
    )
    return df


def foo(x):
    return len(x)


if __name__ == "__main__":
    df = get_df()
    print(df)

    df = df.with_columns(pl.col("name").map_elements(
        foo, return_dtype=pl.Int32).alias('pkey'))
    print(df)
