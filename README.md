# Sorteo Python

App para generar un sorteo entre equipos de un bombo. 

### Ejecutar:

Antes de correr el script, se debe agregar la metadata necesaria.  

Agregar los datos en data/teams_metadata.json (crear el archivo en caso de no existir)  
Ejemplo:
```js
{
    "teams": [ /* lista de Strings con los equipos */ ],
    "metadata": {
        "cant_bombos": N,        // (int)
        "cant_teams_x_bombo": M  // (int)
    }
}
```
Ejemplo: Si se definen 4 bombos con 8 equipos c/u, generará 8 grupos con 4 equipos c/u.  
Se puede variar la cantidad de bombos y/o equipos por bombo.  
Ejemplo 2: Si se crean 4 bombos de 3 equipos c/u, se definirán 3 grupos de 4 equipos.  

Correr el sorteo por defecto:
```bash
./main.sh
```

Llamados importando el modulo:
```py
from main import Draw

# Se obtiene la metadata mediante un objeto:
groups_draw = Draw.main(True, True, None, metadata_info)

# Se obtiene la metadata mediante archivo:
groups_draw = Draw.main(True, True, "data/test.json")
```


### API
La API ejecuta el sorteo (en caso de existir sorteos generados en `data/` devuelve dicho sorteo)
Retorna un JSON con la información.

