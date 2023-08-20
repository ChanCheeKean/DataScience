import os
from util import get_spark_session
from read import from_files
from write import to_files
from process import transform

def main():
    # env = os.environ.get('ENVIRON')
    # src_dir = os.environ.get('SRC_DIR')
    # file_pattern = f"{os.environ.get('SRC_FILE_PATTERN')}-*"
    # src_file_format = os.environ.get('SRC_FILE_FORMAT')
    # tgt_dir = os.environ.get('TGT_DIR')
    # tgt_file_format = os.environ.get('TGT_FILE_FORMAT')

    env = "PROD"
    src_dir = 's3://aigithub/landing/ghactivity'
    file_pattern = f"2021-01-15-*"
    src_file_format = 'json'
    tgt_dir = 's3://aigithub/emrraw/ghactivity'
    tgt_file_format = 'parquet'

    spark = get_spark_session(env, 'GitHub Activity - Reading and Writing Data')
    df = from_files(spark, src_dir, file_pattern, src_file_format)
    df_transformed = transform(df)
    to_files(df_transformed, tgt_dir, tgt_file_format)


if __name__ == '__main__':
    main()
