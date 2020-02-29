## Ejemplo 06

### Agregación con pymongo

Para conectarse a una base de datos desde Python se debe tener un cliente instalado.

En el caso de MongoDB el cliente más utilizado es pymongo.

Éste lo podemos instalar fácilmente con pip, y nos permitirá realizar todas las operaciones CRUD sobre MongoDB.

`pip install pymongo`

```python

In [1]: db = client.stocks
In [2]: collection = db.nasdaq
In [3]: collection.find().distinct('stock_symbol')                               
Out[3]: 
    ['AACC',
    'AAME',
    'AANB',
    'AAON',
        ...

In [4]: stage_1 = {'$group': {'_id': '$stock_symbol', 'avg_open': {'$avg': '$open'}, 'avg_close': {'$avg': '$close'}}}

In [5]: collection.aggregate([stage_1])                                   
Out[5]: <pymongo.command_cursor.CommandCursor at 0x7f65c0066c40>

In [6]: grouped = collection.aggregate([stage_1])

In [7]: list(grouped)[0]                                                  
Out[7]: 
{'_id': 'GXDX',
 'avg_open': 29.714494382022473,
 'avg_close': 29.643820224719104}

```

