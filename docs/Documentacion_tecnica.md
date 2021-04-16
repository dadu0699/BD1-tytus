# Documentación técnica
> TytusDB es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos; El administrador de la base de datos, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser.  — [Documentación Oficial](https://github.com/tytusdb/tytus)

## Contenido
- [Administrador de almacenamiento](#adminStorage)
- [Administrador de la base de datos](#adminDB)
    - [Servidor](#server)
    - [Cliente](#client)
- [SQL Parser](#parser)


## Administrador de almacenamiento<a name="adminStorage"></a>
Este componente es el encargado de gestionar, archivar, organizar y compartir los bytes de informacion del almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.

### Modo de almacenamiento
- [Árbol AVL]
- [Árbol B]
- [Árbol B+]
- [ISAM]
- [Tablas Hash]
- [Archivos JSON]

## Administrador de la base de datos<a name="adminDB"></a>
### Servidor<a name="server"></a>
Es un servidor http. Se debe seleccionar un puerto adecuado que no tenga conflictos con otros servidores. Se tiene un usuario admin y su contraseña. Además, se puede crear n usuarios configurando el acceso a las bases de datos.
### Cliente<a name="client"></a>
Es un cliente que para algunos equipos será web y para otros será una aplicación de escritorio. Este cliente se conectará al servidor y podrá hacer la mayoría de las operaciones que hace pgadmin de PostgreSQL. Dentro del cliente, cuando se navegue dentro de las diferentes bases de datos que existen se puede invocar un editor de queries.

## SQL Parser<a name="parser"></a>
Este componente proporciona al servidor una función encargada de interpretar sentencias del subconjunto del lenguaje SQL especificado.
