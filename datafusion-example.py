import datafusion
import pyarrow as pa
# import pyarrow.parquet as pq
# import pandas as pd


def foo(x: str) -> str:
    return f"{x}-foo"


def add_col_example():
    batch = pa.RecordBatch.from_arrays(
        [pa.array([1, 2, 3]), pa.array(["foo", "bar", "baz"])],
        names=["id", "name"],
    )
    ctx = datafusion.SessionContext()
    df = ctx.create_dataframe([[batch]])
    table = df.to_arrow_table()
    table = table.append_column(
        'new-col', pa.array(['foo'] * len(table), pa.string()))
    print(table)


def get_columns_names(df) -> list[str]:
    cols = str(df.schema())
    cols = " ".join(cols.split())
    cols = cols.split(" ")
    cols = [col.replace(":", "") for col in cols if ":" in col]
    return cols


def select_all_exclude(df, to_exclude: list[str]):
    cols = get_columns_names(df)
    cols = [col for col in cols if col not in to_exclude]
    return df.select_columns(" ".join(cols))


if __name__ == "__main__":
    ctx = datafusion.SessionContext()

    batch = pa.RecordBatch.from_arrays(
        [pa.array([1, 2, 3]), pa.array(["foo", "bar", "baz"])],
        names=["id", "name"],
    )
    df = ctx.create_dataframe([[batch]])
    # print(df)
    table = df.to_arrow_table()
    # print(type(t))

    # new_col = [1, 2, 3]
    # t = t.append_column("new_col", [new_col])
    new_col = table.column("name").to_pylist()
    # print(type(new_col))
    print(new_col)
    new_col = [foo(x) for x in new_col]
    print(new_col)
    # table = table.append_column('new-col', pa.array(['foo'] * len(table), pa.string()))
    # table = table.append_column('new-col', [new_col])
    table = table.add_column(0, 'new-col', [new_col])
    # print(table)
    batches = table.to_batches()
    for i, batch in enumerate(batches):
        print(f"#{i} {batch}")
    # df = ctx.from_arrow_table(table)
    # print(df)
