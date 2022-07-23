import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt


if __name__ == '__main__':
    dataset_path = 'esb_0522.csv'
    column_names = ['serviceName', 'startTime', 'avg_time', 'num', 'succeed_num',
                    'succeed_rate']
    raw_dataset = pd.read_csv(dataset_path, names=column_names)
    raw_dataset = raw_dataset.drop(0)
    # na_values="?", comment='\t',
    # sep=" ", skipinitialspace=True)

    dataset = raw_dataset.copy()
    float_column = ['avg_time', 'num', 'succeed_rate']
    for column in float_column:
        try:
            # Cast to the correct type
            print(dataset[column])
            dataset[column] = dataset[column].astype(float)
        except:
            print("Error trying to set type of column: ", column)
            # Optional: raise the exception here to stop execution

    # dataset.apply(pd.to_numeric, errors='ignore')
    print(dataset.dtypes)
    # print(dataset.tail())
    #
    train_dataset = dataset.sample(frac=0.8, random_state=0)
    test_dataset = dataset.drop(train_dataset.index)

    sns.pairplot(train_dataset, vars=["avg_time", "num", "succeed_rate"], diag_kind="kde")
    plt.show()