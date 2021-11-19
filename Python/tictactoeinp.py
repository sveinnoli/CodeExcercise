def get_row_col(row_col):
    if row_col:
        return (ord(row_col[0].lower())-97, int(row_col[1])-1)

print(get_row_col("A1"))