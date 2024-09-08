FULL_DATA_DIR = '/home/yenhai/projects/VAE/data/AEGlobal_data_package/A_province_data/scenario/full_data.csv'
SAVE_DATA_DIR = '/home/yenhai/projects/VAE/data/processed/'

QUESTION_LEVEL_DICT = {
        'level_id': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                  3, 3, 3, 3, 3, 3],
        'question_id': [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            30, 25, 28, 29, 26, 27,
        ]
    }

KEY_COLUMNS = ["student_id", "question_id", "level_id"]

P_DIMS = [200, 600]