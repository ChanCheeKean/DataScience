def from_files(spark, src_dir, file_pattern, file_format):
    df = spark. \
        read. \
        format(file_format). \
        load(f'{src_dir}/{file_pattern}')
    return df
