import pandas as pd

url='https://pokeapi.co/api/v2/pokemon/ditto'

data=pd.read_json(url)


print(data)