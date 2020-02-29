## Reto 03

`api_ecobici_paginacion.py`

Modifica el archivo del reto anterior para agregar paginación a tu API, de modo que la respuesta sea de la siguiente manera:

```json
{
    "page": 1,
    "per_page": 100,
    "total": 2276,
    "data": [
        {
            "Genero_Usuario": "M",
            "Edad_Usuario": 12,
            "Bici": 7639,
            ...
        },
        ...
    ]
}
```

Agrega el manejo de parámetros a tu API para que se puedan filtrar los resultados
