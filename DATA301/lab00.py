import dask.dataframe as df

Bombing_Operations_df = df.read_parquet("Bombing_Operations.parquet")
Bombing_Operations = Bombing_Operations_df.to_bag().persist()
column_indices = dict([(k, i) for i, k in enumerate(Bombing_Operations_df.columns)])
print(column_indices)
