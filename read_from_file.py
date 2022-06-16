import numpy as np
import pandas as pd


def add_to_set():
    pan = pd.read_excel('customers.xlsx')
    df = pd.DataFrame(pan, )
    df = df.replace({np.nan: None})
    customer = df['customer'].tolist()
    chance = df['chance'].tolist()
    customers = []
    chances = []
    for i in range(0, len(customer)):
        if chance[i] and customer[i]:
            customers.append(customer[i])
            chances.append(chance[i])

    info = zip(customers, chances)
    return list(info)

