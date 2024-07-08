import pandas as pd
import random
import json

# How to display full Dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def concat_example():
    df1 = pd.DataFrame({"id": [1, 2], "data": ["foo", "bar"]})
    df2 = pd.DataFrame({"id": [3], "data": ["baz"]})
    res = pd.concat([df1, df2], ignore_index=True)
    print(res)


def merge_example():
    df1 = pd.DataFrame({"id": [1, 2], "data": ["foo", "bar"]})
    df2 = pd.DataFrame({"id": [1], "data": ["baz"]})
    df1.merge(df2, left_on="id", right_on="id")
    print(df1)


def filter_example():
    df = get_df()
    # df = df.query("id == 1")
    df = df[df["id"] == 1]
    print(df)


def get_df():
    data = {
        "id": [1, 2, 3],
        "name": ["foo", "bar", "baz"],
        "data": [42, 43, 44],
    }
    df = pd.DataFrame(data)
    return df


def get_df_rnd():
    data = [{"id": i, "value": random.randint(1, 100)} for i in range(1, 6)]
    df = pd.DataFrame(data)
    return df


def foo(x):
    return x+1


def iter_df(df):
    for idx, row in df.iterrows():
        idx += 1
        print(
            f"#{idx} id: {row['id']}, name: {row['name']}, data: {row['data']}")


def parse_json_example():
    df = pd.DataFrame({
        'bank_account': [101, 102, 201, 301],
        'data': [
            '{"uid": 100, "account_type": 1, "account_data": {"currency": {"current": 1000, "minimum": -500}, "fees": {"monthly": 13.5}}, "user_name": "Alice"}',
            '{"uid": 100, "account_type": 2, "account_data": {"currency": {"current": 2000, "minimum": 0},  "fees": {"monthly": 0}}, "user_name": "Alice"}',
            '{"uid": 200, "account_type": 1, "account_data": {"currency": {"current": 3000, "minimum": 0},  "fees": {"monthly": 13.5}}, "user_name": "Bob"}',
            '{"uid": 300, "account_type": 1, "account_data": {"currency": {"current": 4000, "minimum": 0},  "fees": {"monthly": 13.5}}, "user_name": "Carol"}'
        ]},
        index=['Alice', 'Alice', 'Bob', 'Carol']
    )

    parsed_df = pd.concat([pd.json_normalize(json.loads(js))
                          for js in df['data']])
    # parsed_df['bank_account'] = df['bank_account'].values
    # parsed_df.index = parsed_df['user_name']
    print(parsed_df)


if __name__ == "__main__":
    # df = get_df()
    # print(df)
    # df.insert(0, "id-new", [1, 2, 3], True)
    # image_df["pkey_new"] = image_df["data_val"].apply(calc_image_phash)
    # df.insert(0, "id-new", df["data"].apply(foo))
    # concat_example()
    # merge_example()
    df = get_df()
    iter_df(df)
