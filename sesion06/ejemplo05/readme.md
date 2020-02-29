## Ejemplo 05

### Utilizando MongoDB con Python

Para conectarse a una base de datos desde Python se debe tener un cliente instalado.

En el caso de MongoDB el cliente más utilizado es pymongo.

Éste lo podemos instalar fácilmente con pip, y nos permitirá realizar todas las operaciones CRUD sobre MongoDB.

`pip install pymongo`

```python

In [1]: client = MongoClient('mongodb://bedu:holacrayola@mariohd.com:27017/')

In [2]: client.list_database_names()   
Out[2]: ['admin', 'config', 'local', 'stocks']

In [3]: db.list_collection_names()    
Out[3]: ['nasdaq']

In [4]: doc = collection.find({},limit=1)

In [5]: doc[0]                                                           
Out[5]: 
    {'_id': ObjectId('4d094f58c96767d7a0099d49'),
    'exchange': 'NASDAQ',
    'stock_symbol': 'AACC',
    'date': '2008-03-07',
    'open': 8.4,
    'high': 8.75,
    'low': 8.08,
    'close': 8.55,
    'volume': 275800,
    'adj close': 8.55}

In [6]: test_collection = db.test_collection                                

In [7]: test_collection.insert_one({'hola': 'mundo'})              
Out[7]: <pymongo.results.InsertOneResult at 0x7f65c03d0a80>

In [8]: test_collection.find()[0]                                           
Out[8]: {'_id': ObjectId('5e5a196fcbd91673c22c06b1'), 'hola': 'mundo'}

```

