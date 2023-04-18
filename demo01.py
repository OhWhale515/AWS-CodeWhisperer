import pandas as pd
# Function to load a CSV file into a Pandas DataFrame
#Select column Name, Age, and Address
def load_csv(filename):
    df = pd.read_csv(filename, usecols=['Name', 'Age', 'Address'])
    return df

# Unit test for load_csv()

def test_load_csv():
    df = load_csv('test.csv')
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ['Name', 'Age', 'Address']
    assert df.iloc[0].tolist() == ['John', 30, '123 Main Street']
    assert df.iloc[1].tolist() == ['Jane', 25, '456 Main Street']
    assert df.iloc[2].tolist() == ['Mary', 35, '789 Main Street']
    print('test_load_csv passed!')
    
