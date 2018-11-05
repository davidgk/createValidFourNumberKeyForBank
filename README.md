## How to create a valid Four digit Key

### Rules
* No deberá contener más de tres caracteres numéricos iguales.

* No deberá contener más de tres números consecutivos (ascendentes o descendentes).

* No deberá contener los 4 primeros ni los 4 últimos dígitos del número de documento.

* No deberá contener fechas de nacimiento que comiencen con 19 o 20.
    * No deberá contener los siguientes dígitos de la fecha de nacimiento: 
    * Año de nacimiento (aaaa),
    * día y mes de nacimiento (dd/mm), 
    * mes y día de nacimiento (mm/dd), 
    * mes y año de nacimiento (mm/aa), 
    * año y mes de nacimiento (aa/mm).

* Además tomá en consideración que:

* No podrá ser la última clave utilizada.

### How to run it
En el path del proyecto
* 1.- export PYTHONPATH=$(pwd) 
* 2.- python src/valid_creator_four_number_key.py
    * Opciones:
        * Cargar los datos
        * agregar por parametro los primeros 4 y ultimos 4 valores del dni, la fecha de nacimiento (formato aaaa/mm/dd) y la ultima clave ( para uqe no la tenga en cuenta)
            ejemplo
            python ./src/valid_creator_four_number_key.py 2110 1122 1983/11/24 1111

        
        