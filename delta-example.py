import pandas as pd
from deltalake import DeltaTable, write_deltalake

# df = pd.DataFrame({"id": [1, 2, 3], "data": ["foo", "bar", "baz"]})
# write_deltalake("delta/my_super_delta", df)

# df = pd.DataFrame({"id": [14], "data": ["foofoo"]})
# df = pd.DataFrame({"id": [42], "data": ["new-data"]})
# write_deltalake("delta/my_super_delta", df, mode="append")

table = DeltaTable("delta/my_super_delta")
# table.vacuum(dry_run=True)
# table.delete(predicate='id = 5')
df = table.to_pandas()
print(df)

# to_delete = table.vacuum(dry_run=True, retention_hours=1, enforce_retention_duration=False)
# table.vacuum(dry_run=False, retention_hours=1, enforce_retention_duration=False)
# print(to_delete)
# opt = table.optimize.compact(min_commit_interval=1)
# table.create_checkpoint()

# print(opt)
# print(opt)
# print(table.version())
# history = table.history()
# print(history)
# table.restore(10)
# df = table.to_pandas()
# print(df)
