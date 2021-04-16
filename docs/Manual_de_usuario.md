# Manual de usuario

- [Antes de comenzar](#previo)
- [Componentes de la interfaz](#interfaz)
- [Funcionalidad TytusDB](#funcionalidad)

<a name="previo"></a>*Antes de comenzar asegurese de tener todo instalaado, para más información dirigirse al [Manual de Instalación](./Manual_de_Installacion.md).*

Una vez con todos los archivos instalados deberá ejecutar el servidor, dentro de la carpeta server encontrará un archivo llamado main.exe haga doble click sobre este archivo para levantar su servidor, una vez el servidor esté corriendo puede ejecutar la aplicación para ello dentro de la carpeta tytusDB-win32-x64 debera buscar el archivo tytusDB.exe, hacer doble click para ejecutar.


## Componentes de la Interfaz <a name="interfaz"></a>

La aplicación cuenta con una interfaz intuitiva, algunos de sus componentes listados a continuación:
 - **Barra superior de pestañas**: en la parte superior se tienen diversas pestañas con distintas funcionalidades que podrán ser de utilidad para el usuario.
 - **Archivo**: esta pestaña le permite crear una base de datos con mayor facilidad.
 - **Barra lateral**: en la barra izquierda podrá encontrar un esquema del servidor, las bases de datos creados sus tablas y campos. En esta barra encontrará un botón de actualización que le permitira visualizar  los cambios mas recientes sobre el esquema. 
 - **Botón para guardar archivo**: podra guardar el trabajo que haya realizado en el editor.
 - **Botón para cargar archivo**: podra importar al editor de código cualquier archio con extensión .sql que haya guardado previamente, o que desee probar.
 - **Botón para agregar pestaña**: puede agregar multiples pestañas de editor, para trabajar en distintos archivos, o simplemente consultarlos.
 - **Editor de lenguaje SQL**: espacio de trabajo para consultas, creaciones, actualizaciones, etc.
 - **Consola de Salida**: en este apartado podrá verificar los resultados de las acciones realizadas.

## Funcionalidad DBMS TytusDB <a name="funcionalidad"></a>

Con el fin de facilitar la interacción del usuario con el DBMS TytusDB a continuación se proporciona un listado especificado de las funciones del lenguaje SQL disponibles para el usuario, algunas funciones aún no se encuentran optimizadas o siguen en proceso de desarrollo para estar a disposición de los usuarios de interés.

| No. |      Función      | Sintaxis | Disponible | No Disponible | Observaciones |
|:---:|:-------------------:|:--------:|:----------:|:-------------:|:-------------:|
|  1  | Create Database     |          |            |               |               |
|  2  | Show Databases      |          |            |               |               |
|  3  | Alter Database      |          |            |               |               |
|  4  | Drop Database       |          |            |               |               |
|  5  | Create Table        |          |            |               |               |
|  6  | Show Tables         |          |            |               |               |
|  7  | Extract Table       |          |            |               |               |
|  8  | Extract Range Table |          |            |               |               |
|  9  | Alter Add PK        |          |            |               |               |
|  10 | Alter Drop PK       |          |            |               |               |
|  11 | Alter Add FK        |          |            |               |               |
|  12 | Alter Add Index     |          |            |               |               |
|  13 | Alter Table         |          |            |               |               |
|  14 | Alter Add Column    |          |            |               |               |
|  15 | Alter Drop Column   |          |            |               |               |
|  16 | Drop Table          |          |            |               |               |
|  17 | Insert              |          |            |               |               |
|  18 | Load CSV            |          |            |               |               |
|  19 | Extract Row         |          |            |               |               |
|  20 | Update              |          |            |               |               |
|  21 | Delete              |          |            |               |               |
|  22 | Truncate            |          |            |               |               |

*Nota: TytusDB Al igual que en otros DBMS es case-insensitive, las instrucciones en lenguaje SQL al igual que los identificadores pueden ser ingresados con mayúsculas y minúsculas sin afectar el resultado.*
