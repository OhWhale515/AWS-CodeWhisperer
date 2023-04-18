import pandas as pd
#Function to load a CSV file into a Pandas DataFrame
#Select colummn Name, Age, and Address
def load_csv(filename):
    df = pd.read_csv(filename, usecols=['Name', 'Age', 'Address'])
    return df

# Unit test for load_csv

def test_load_csv():
    df = load_csv('test.csv')
    assert (df.shape == (3, 3))
    assert (df.columns.tolist() == ['Name', 'Age', 'Address'])
    assert (df.loc[0, 'Name'] == 'John')
    assert (df.loc[0, 'Age'] == 30)
    assert (df.loc[0, 'Address'] == '123 Main St')
    assert (df.loc[1, 'Name'] == 'Jane')
    assert (df.loc[1, 'Age'] == 25)
    assert (df.loc[1, 'Address'] == '456 Main St')
    assert (df.loc[2, 'Name'] == 'Joe')
    assert (df.loc[2, 'Age'] == 28)
    assert (df.loc[2, 'Address'] == '789 Main St')
    print('load_csv passed!')





    