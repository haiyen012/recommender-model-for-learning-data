import os

import pandas as pd
import numpy as np

from my_config import conf


def load_raw_data(data_dir):
    return pd.read_csv(data_dir, header=0)


def processing_data(data):
    if "StudentID" in data.columns:
        data = data.rename(columns={"StudentID": "student_id"})
    data = pd.melt(
        data, id_vars=["student_id"], var_name="question_id", value_name="result"
    )
    data["question_id"] = data["question_id"].astype(int)
    return data


def process_df_with_question_level_df(data, level_dict):
    level_df = pd.DataFrame(level_dict)
    return data.merge(level_df, on="question_id", how="inner")


def get_random_data_by_level(data):
    """
    With each student and each level, get randomly a question to test
    :param data: data
    :return: sub data
    """
    np.random.seed(112)
    retrieve_random_test_df = (
        data.groupby(by=["student_id", "level_id"])["question_id"]
        .apply(lambda x: np.random.choice(x))
        .reset_index()
    )
    return retrieve_random_test_df.merge(
        data, on=conf.KEY_COLUMNS, how="inner"
    )


def anti_join(df1, df2, on_columns):
    df1 = df1[on_columns]
    df2 = df2[on_columns]
    merged_df = df1.merge(df2, on=on_columns, how="outer", indicator=True)
    return merged_df[merged_df["_merge"] == "left_only"]


def split_data(data):
    test_data = get_random_data_by_level(data=data)
    train_and_validation_data = anti_join(data, test_data, on_columns=conf.KEY_COLUMNS)
    validate_data = get_random_data_by_level(data=train_and_validation_data)
    train_data = anti_join(
        train_and_validation_data, validate_data, on_columns=conf.KEY_COLUMNS
    )
    return train_data, validate_data, test_data


def save_data(save_data_dir, data, data_name):
    if not os.path.exists(save_data_dir):
        os.makedirs(save_data_dir)
    data.to_csv(os.path.join(save_data_dir, f"{data_name}.csv"), index=False)


def save_split_data(save_data_dir, train_data, validate_data, test_data):
    save_data(save_data_dir=save_data_dir, data=train_data, data_name="train")
    save_data(save_data_dir=save_data_dir, data=validate_data, data_name="validate")
    save_data(save_data_dir=save_data_dir, data=test_data, data_name="test")


def process_data():
    df = load_raw_data(data_dir=conf.FULL_DATA_DIR)
    df = processing_data(data=df)
    df = process_df_with_question_level_df(data=df, level_dict=conf.QUESTION_LEVEL_DICT)
    train_df, validation_df, test_df = split_data(data=df)
    save_split_data(
        save_data_dir=conf.SAVE_DATA_DIR,
        train_data=train_df,
        validate_data=validation_df,
        test_data=test_df,
    )


if __name__ == "__main__":
    process_data()
