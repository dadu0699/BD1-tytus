# Documentación técnica
> TytusDB es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos; El administrador de la base de datos, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser.  — [Documentación Oficial](https://github.com/tytusdb/tytus)

## Contenido
- [Administrador de almacenamiento](#adminStorage)
    - [Modos de almacenamiento](#storageMode)
- [Administrador de la base de datos](#adminDB)
    - [Servidor](#server)
    - [Cliente](#client)
- [SQL Parser](#parser)


## Administrador de almacenamiento<a name="adminStorage"></a>
Este componente es el encargado de gestionar, archivar, organizar y compartir los bytes de informacion del almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.

### Modos de almacenamiento<a name="storageMode"></a>
- **Árbol AVL** *(Grupo 14)*
    - [Manual Técnico](../storage/AVL/docs/TechnicalManual.md)
    - [Manual de Usuario](../storage/AVL/docs/UserManual.md)
- **Árbol B** *(Grupo 15)*
    - [Manual Técnico](../storage/BTree/docs/Manual_de_Usuario.md)
    - [Manual de Usuario](../storage/BTree/docs/Manual_Tecnico.md)
- **Árbol B+** *(Grupo 16)*
    - [Manual Técnico](../storage/BPTree/doc/techManual_doc.md)
    - [Manual de Usuario](../storage/BPTree/doc/userManual_doc.md)
- **ISAM** *(Grupo 17)*
    - [Manual Técnico](../storage/ISAM/doc/Technical_guide.md)
    - [Manual de Usuario](../storage/ISAM/doc/user_guide.md)
- **Tablas Hash** *(Grupo 18)*
    - [Manual Técnico](../storage/Hash/docs/Manual_tecnico.md)
    - [Manual de Usuario](../storage/Hash/docs/Manual_de_usuario.md)
- Archivos JSON

## Administrador de la base de datos<a name="adminDB"></a>
### Servidor<a name="server"></a>
Es un servidor http. Se debe seleccionar un puerto adecuado que no tenga conflictos con otros servidores. Se tiene un usuario admin y su contraseña. Además, se puede crear n usuarios configurando el acceso a las bases de datos.

Componente utilizado *Grupo 5:*
- [Manual](../server/README.md)

### Cliente<a name="client"></a>
Es un cliente que para algunos equipos será web y para otros será una aplicación de escritorio. Este cliente se conectará al servidor y podrá hacer la mayoría de las operaciones que hace pgadmin de PostgreSQL. Dentro del cliente, cuando se navegue dentro de las diferentes bases de datos que existen se puede invocar un editor de queries.

Componente utilizado *Grupo 5:*
- [Manual Técnico](../client/team05/TECNICO.md)
- [Manual de Usuario](../client/team05/README.md)

## SQL Parser<a name="parser"></a>
Este componente proporciona al servidor una función encargada de interpretar sentencias del subconjunto del lenguaje SQL especificado.

Componente utilizado *Grupo 28:*
- [Manual Técnico](../parserT28/docs/Manual_Tecnico.md)
- [Manual de Usuario](../parserT28/docs/Manual_de_Usuario.md)
