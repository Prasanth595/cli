<div class='hidden-website'>

# Documentación de HTTPie

</div>

HTTPie (se pronuncia _aitch-tee-tee-pie_) es un cliente HTTP de línea de comandos.
Su objetivo es hacer que la interacción desde la CLI con los servicios web sea lo más amigable posible.
HTTPie está diseñado para probar, depurar y, en general, interactuar con APIs y servidores HTTP.
Los comandos `http` y `https` permiten crear y enviar solicitudes HTTP arbitrarias.
Usan una sintaxis simple y natural, y proporcionan salida formateada y con colores.

<div class='hidden-website'>

## Acerca de este documento

Esta documentación se visualiza mejor en [httpie.io/docs](https://httpie.org/docs).

Puedes seleccionar tu versión correspondiente de HTTPie y también ejecutar ejemplos directamente desde el navegador utilizando un terminal incrustado de [termible.io](https://termible.io?utm_source=httpie-readme).

Si estás leyendo esto en GitHub, entonces este texto cubre la versión actual de *desarrollo*.
Estás invitado a enviar correcciones y mejoras a la documentación editando [este archivo](https://github.com/httpie/cli/blob/master/docs/README.md).

</div>

## Características principales


- Sintaxis expresiva e intuitiva


- Salida en terminal formateada y con colores


- Soporte JSON incorporado


- Formularios y carga de archivos


- HTTPS, proxies y autenticación


- Datos arbitrarios en la solicitud


- Encabezados personalizados


- Sesiones persistentes


- Descargas al estilo de Wget


- Soporte para Linux, macOS, Windows y FreeBSD


- Plugins


- Documentación


- Cobertura de pruebas


## Instalación

<div data-installation-instructions>

<!--
LA SECCIÓN DE INSTALACIÓN ES GENERADA

No la edites aquí, sino en docs/installation/.

-->


- [Universal](#universal)


- [macOS](#macos)


- [Windows](#windows)


- [Linux](#linux)


- [FreeBSD](#freebsd)


### Universal

#### PyPI

Por favor, asegúrate de tener Python 3.7 o superior (`python --version`).


```bash

# Actualizar httpie
$ python -m pip install --upgrade pip wheel
$ python -m pip install httpie

```



```bash

# Actualizar httpie
$ python -m pip install --upgrade pip wheel
$ python -m pip install --upgrade httpie

```


### macOS

#### Homebrew

Para instalar [Homebrew](https://brew.sh/), consulta [su instalación](https://docs.brew.sh/Installation).


```bash

# Instalar httpie
$ brew update
$ brew install httpie

```



```bash

# Actualizar httpie
$ brew update
$ brew upgrade httpie

```


#### MacPorts

Para instalar [MacPorts](https://www.macports.org/), consulta [su instalación](https://www.macports.org/install.php).


```bash

# Instalar httpie
$ port selfupdate
$ port install httpie

```



```bash

# Actualizar httpie
$ port selfupdate
$ port upgrade httpie

```


### Windows

#### Chocolatey

Para instalar [Chocolatey](https://chocolatey.org/), consulta [su instalación](https://chocolatey.org/install).


```bash

# Instalar httpie
$ choco install httpie

```



```bash

# Actualizar httpie
$ choco upgrade httpie

```


### Linux

#### Debian and Ubuntu

También funciona con otras distribuciones derivadas de Debian como MX Linux, Linux Mint, deepin, Pop!_OS, KDE neon, Zorin OS, elementary OS, Kubuntu, Devuan, Linux Lite, Peppermint OS, Lubuntu, antiX, Xubuntu, etc.


```bash

# Instalar httpie
$ curl -SsL https://packages.httpie.io/deb/KEY.gpg | sudo gpg --dearmor -o /usr/share/keyrings/httpie.gpg
$ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/httpie.gpg] https://packages.httpie.io/deb ./" | sudo tee /etc/apt/sources.list.d/httpie.list > /dev/null
$ sudo apt update
$ sudo apt install httpie

```



```bash

# Actualizar httpie
$ sudo apt update && sudo apt upgrade httpie

```


#### Fedora


```bash

# Instalar httpie
$ dnf install httpie

```



```bash

# Actualizar httpie
$ dnf upgrade httpie

```


#### CentOS and RHEL

También funciona con otras distribuciones derivadas de RHEL como ClearOS, Oracle Linux, etc.


```bash

# Instalar httpie
$ yum install epel-release
$ yum install httpie

```



```bash

# Actualizar httpie
$ yum upgrade httpie

```


#### Ejecutables binarios únicos (Single binary executables)

Obtén los ejecutables independientes de HTTPie para Linux si no deseas realizar el proceso completo de instalación.


```bash

# Instalar httpie

```bash`r`n$ https --download packages.httpie.io/binaries/linux/http-latest -o http

$ ln -ls ./http ./https
$ chmod +x ./http ./https

```



```bash

# Actualizar httpie

```bash`r`n$ https --download packages.httpie.io/binaries/linux/http-latest -o http


```


#### Snapcraft (Linux)

Para instalar [Snapcraft](https://snapcraft.io/), consulta [su instalación](https://snapcraft.io/docs/installing-snapd).


```bash

# Instalar httpie
$ snap install httpie

```



```bash

# Actualizar httpie
$ snap refresh httpie

```


#### Linuxbrew

Para instalar [Linuxbrew](https://docs.brew.sh/Homebrew-on-Linux), consulta [su instalación](https://docs.brew.sh/Homebrew-on-Linux#install).


```bash

# Instalar httpie
$ brew update
$ brew install httpie

```



```bash

# Actualizar httpie
$ brew update
$ brew upgrade httpie

```


#### Arch Linux

También funciona con otras distribuciones derivadas de Arch como ArcoLinux, EndeavourOS, Artix Linux, etc.


```bash

# Instalar httpie
$ pacman -Syu httpie

```



```bash

# Actualizar httpie
$ pacman -Syu

```


### FreeBSD

#### FreshPorts


```bash

# Instalar httpie
$ pkg install www/py-httpie

```



```bash

# Actualizar httpie
$ pkg upgrade www/py-httpie

```


<!-- /SECCIÓN GENERADA -->

</div>

### Versión inestable

Si deseas probar la última versión de HTTPie que aún no ha sido publicada oficialmente, puedes instalar la versión de desarrollo o inestable directamente desde la rama `master` en GitHub. Sin embargo, ten en cuenta que esta versión está en desarrollo y puede no ser tan confiable como la versión estable.

Puedes usar el siguiente comando para instalar la versión de desarrollo de HTTPie en sistemas operativos Linux, macOS, Windows o FreeBSD. Este comando descarga e instala el código presente en la rama `master` usando `pip`.


```bash

$ python -m pip install --upgrade https://github.com/httpie/cli/archive/master.tar.gz

```


También hay otras formas de instalar la versión de desarrollo de HTTPie en macOS y Linux.

Puedes instalarla usando Homebrew ejecutando los siguientes comandos:


```bash

$ brew uninstall --force httpie
$ brew install --HEAD httpie

```


Puedes instalarla usando Snapcraft ejecutando los siguientes comandos:


```bash

$ snap remove httpie
$ snap install httpie --edge

```


Para verificar la instalación, puedes comparar el [identificador de versión en GitHub](https://github.com/httpie/cli/blob/master/httpie/__init__.py#L6) con el que está disponible en tu máquina. Puedes comprobar la versión de HTTPie en tu máquina usando el comando `http --version`.


```bash


```bash`r`n$ http --version

# 3.X.X.dev0

```


Ten en cuenta que en tu máquina, el nombre de la versión tendrá el sufijo `.dev0`.

## Uso

Hola Mundo:


```bash


```bash`r`n$ https httpie.io/hello


```


Sinopsis:


```bash


```bash`r`n$ http [flags] [METHOD] URL [ITEM [ITEM]]


```


Consulta también `http --help` (y en sistemas donde hay páginas de manual disponibles, puedes usar `man http`).

### Ejemplos

[Método HTTP](#http-method), [HTTP headers](#http-headers) personalizados y datos [JSON](#json):


```bash


```bash`r`n$ http PUT pie.dev/put X-API-Token:123 name=John


```


Envío de [formularios](#forms):


```bash


```bash`r`n$ http -f POST pie.dev/post hello=World


```


Ver la solicitud que se está enviando usando una de las [opciones de salida](#output-options):


```bash


```bash`r`n$ http -v pie.dev/get


```


Construir e imprimir una solicitud sin enviarla usando el [modo offline](#offline-mode):


```bash


```bash`r`n$ http --offline pie.dev/post hello=offline


```


Use [API de GitHub](https://developer.github.com/v3/issues/comments/#create-a-comment) para publicar un comentario en un [issue](https://github.com/httpie/cli/issues/83) con [authentication](#authentication):


```bash


```bash`r`n$ http -a USERNAME POST https://api.github.com/repos/httpie/cli/issues/83/comments body='HTTPie is awesome! :heart:'


```


Subir un archivo usando [entrada redirigida](#redirected-input):


```bash


```bash`r`n$ http pie.dev/post < files/data.json


```


Descargar un archivo y guardarlo mediante [salida redirigida](#redirected-output):


```bash


```bash`r`n$ http pie.dev/image/png > image.png


```


Descargar un archivo al estilo `wget`:


```bash


```bash`r`n$ http --download pie.dev/image/png


```


Usar [sessions](#sessions) con nombre para hacer persistentes ciertos aspectos de la comunicación entre solicitudes al mismo host:


```bash


```bash`r`n$ http --session=logged-in -a username:password pie.dev/get API-Key:123


```



```bash


```bash`r`n$ http --session=logged-in pie.dev/headers


```


Establecer un encabezado `Host` personalizado para evitar problemas con registros DNS ausentes:


```bash


```bash`r`n$ http localhost:8000 Host:example.com


```


## Método HTTP

El nombre del método HTTP se coloca justo antes del argumento de la URL:


```bash


```bash`r`n$ http DELETE pie.dev/delete


```


Lo cual se parece a la  `Request-Line` real que se envía:


```http

DELETE /delete HTTP/1.1

```


Además de los métodos estándar (`GET`, `POST`, `HEAD`, `PUT`, `PATCH`, `DELETE`, etc.), puedes usar nombres de métodos personalizados. Por ejemplo:


```bash


```bash`r`n$ http AHOY pie.dev/post


```


No hay restricciones respecto a qué métodos de solicitud pueden incluir un cuerpo. Puedes enviar una solicitud `POST` vacía:


```bash


```bash`r`n$ http POST pie.dev/post


```


También puedes hacer solicitudes `GET` que incluyan un cuerpo:


```bash


```bash`r`n$ http GET pie.dev/get hello=world


```


### `GET` y `POST` opcionales

El argumento `METHOD` es opcional. Cuando no lo especificas, HTTPie usa por defecto:


- `GET` para solicitudes sin cuerpo


- `POST` para solicitudes con cuerpo


Aquí no especificamos ningún dato de solicitud, por lo tanto ambos comandos enviarán la misma solicitud `GET`:


```bash


```bash`r`n$ http GET pie.dev/get


```



```bash


```bash`r`n$ http pie.dev/get


```


Aquí, en cambio, sí incluimos datos, así que ambos comandos enviarán la misma solicitud `POST`:


```bash


```bash`r`n$ http POST pie.dev/post hello=world


```



```bash


```bash`r`n$ http pie.dev/post hello=world


```


## URL de solicitud

La única información que HTTPie necesita para realizar una solicitud es una URL.

El esquema predeterminado es `http://` y puede omitirse en el argumento:


```bash


```bash`r`n$ http example.org

# → http://example.org

```


HTTPie también instala un ejecutable llamado `https`, donde el esquema predeterminado es `https://`:


```bash


```bash`r`n$ https example.org

# → https://example.org

```


Cuando pegas una URL en la terminal, incluso puedes mantener la parte `://` en el argumento de la URL para convertirla rápidamente en una llamada de HTTPie simplemente agregando un espacio después del nombre del protocolo.


```bash


```bash`r`n$ https ://example.org

# → https://example.org

```



```bash


```bash`r`n$ http ://example.org

# → http://example.org

```


### Parámetros en la cadena de consulta (Querystring parameters)

Si te encuentras construyendo manualmente URLs con parámetros en la cadena de consulta desde la terminal, puedes utilizar la sintaxis `param==value` para agregar parámetros de URL.

Con esto, no tienes que preocuparte por escapar los separadores `&` en tu shell. Además, cualquier carácter especial en el nombre o valor del parámetro será escapado automáticamente en formato URL (a diferencia de los parámetros especificados directamente en la URL completa, que HTTPie no modifica).


```bash


```bash`r`n$ http https://api.github.com/search/repositories q==httpie per_page==1


```



```http

GET /search/repositories?q=httpie&per_page=1 HTTP/1.1

```


Incluso puedes obtener el `value` desde un archivo utilizando la sintaxis `param==@file`.Esto también eliminará los saltos de línea al final. Consulta [separadores basados en archivos](#file-based-separators) para más ejemplos.


```bash


```bash`r`n$ http pie.dev/get text==@files/text.txt


```


### Atajos de URL para `localhost`

También se admite una forma abreviada al estilo de curl para localhost.
Esto significa que, por ejemplo, `:3000` se expandirá a `http://localhost:3000`.
Si se omite el puerto, se asume el puerto 80.


```bash


```bash`r`n$ http :/foo


```



```http

GET /foo HTTP/1.1
Host: localhost

```



```bash


```bash`r`n$ http :3000/bar


```



```http

GET /bar HTTP/1.1
Host: localhost:3000

```



```bash


```bash`r`n$ http :


```



```http

GET / HTTP/1.1
Host: localhost

```


### Otros esquemas predeterminados

Cuando HTTPie se invoca como `https`, entonces el esquema predeterminado es `https://` (`$ https example.org` hará una solicitud a `https://example.org`).

También puedes usar la opción `--default-scheme <URL_SCHEME>` para crear atajos para otros protocolos distintos a HTTP (posiblemente habilitados mediante [plugins](https://pypi.org/search/?q=httpie)). Ejemplo con el plugin [httpie-unixsocket](https://github.com/httpie/httpie-unixsocket):


```bash

# Before

```bash`r`n$ http http+unix://%2Fvar%2Frun%2Fdocker.sock/info


```



```bash

# Create an alias
$ alias http-unix='http --default-scheme="http+unix"'

```



```bash

# Now the scheme can be omitted

```bash`r`n$ http-unix %2Fvar%2Frun%2Fdocker.sock/info


```


### `--path-as-is`

El comportamiento estándar de los clientes HTTP es normalizar la parte de la ruta de las URLs eliminando los segmentos con puntos como lo haría un sistema de archivos típico:


```bash


```bash`r`n$ http -v example.org/./../../etc/password


```



```http

GET /etc/password HTTP/1.1

```


La opción `--path-as-is` permite desactivar este comportamiento:


```bash


```bash`r`n$ http --path-as-is -v example.org/./../../etc/password


```



```http

GET /../../etc/password HTTP/1.1

```


## Elementos de solicitud (Request items)

Hay varios tipos de  *elementos de solicitud* que proporcionan un mecanismo conveniente
para especificar encabezados HTTP, datos JSON y de formularios, archivos,
y parámetros en la URL. Esta es una forma muy práctica de construir
solicitudes HTTP desde cero en la CLI.

Cada *elementos de solicitud* es simplemente un par clave/valor separado con los siguientes
caracteres: `:` (encabezados), `=` (campo de datos, por ejemplo, JSON o formulario), `:=` (Campo de datos sin procesar)
`==` (parámetros de URL), `@` (carga de archivos).


```bash


```bash`r`n$ http PUT pie.dev/put \

    X-Date:today \                     # Encabezado
    token==secret \                    # Parámetro en la URL
    name=John \                        # Campo de datos
    age:=29                            # JSON sin procesar

```


|                                                    Tipo de elemento | Descripción                                                                                                                                                                                                            |
|-------------------------------------------------------------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                    Encabezados HTTP `Name:Value` | Encabezado HTTP arbitrario, por ejemplo: `X-API-Token:123`                                                                                                                                                                          |
|                                 Parámetros de URL `name==value` | Agrega el par nombre/valor como parámetro de cadena de consulta (querystring) a la URL. Se usa el separador `==`.                                                                                                                   |
|                                    Campos de datos `field=value` | Campos de datos de la solicitud que se serializan como un objeto JSON (por defecto), como formulario codificado (`--form, -f`), o como `multipart/form-data` (`--multipart`)                                             |
|                                Campos JSON sin procesar `field:=json` | Útil al enviar JSON y uno o más campos necesitan ser un `Boolean`, `Number`, `Object` anidado, o un `Array`, por ejemplo, `meals:='["ham","spam"]'` o `pies:='[1,2,3]'` (nota las comillas)                                 |
| Campos de carga de archivos `field@/dir/file`, `field@file;type=mime` | Solo disponible con `--form`, `-f` y `--multipart`. Por ejemplo `screenshot@~/Pictures/img.png`, o `'cv@cv.txt;type=text/markdown'`. Con `--form`, la presencia de un campo de archivo da como resultado una solicitud `--multipart` |

Ten en cuenta que los campos de datos estructurados no son la única forma de especificar datos en una solicitud:
[uerpo de solicitud sin procesar](#raw-request-body) es un mecanismo para pasar datos de solicitud arbitrarios.

### Separadores basados en archivos (File based separators)

Usar el contenido de archivos como valores para campos específicos es un caso de uso muy común, el cual puede lograrse añadiendo el sufijo `@`
a los operadores anteriores. Por ejemplo, en lugar de usar una cadena estática como valor de un encabezado, puedes usar `:@`
para leerlo desde un archivo.


```bash


```bash`r`n$ http POST pie.dev/post \

    X-Data:@files/text.txt             # Leer un encabezado desde un archivo
    token==@files/text.txt             # Leer un parámetro de URL desde un archivo
    name=@files/text.txt               # Leer el valor de un campo desde un archivo
    bookmarks:=@files/data.json        # Incluir un objeto JSON desde un archivo

```


### Reglas de escape (Escaping rules)

Puedes usar `\` para escapar caracteres que no deberían usarse como separadores (o partes de ellos). Por ejemplo, `foo\==bar` será interpretado como un campo de datos (`foo=` y `bar`) en lugar de un parámetro de URL.

A menudo es necesario entrecomillar los valores, por ejemplo: `foo='bar baz'`.

Si alguno de los nombres de campo o encabezados comienza con un guion (por ejemplo: `-fieldname`), debes colocar todos esos elementos después del token especial `--` para evitar confusión con `--arguments`:


```bash


```bash`r`n$ http pie.dev/post -- -name-starting-with-dash=foo -Unusual-Header:bar


```



```http

POST /post HTTP/1.1
-Unusual-Header: bar
Content-Type: application/json

{
    "-name-starting-with-dash": "foo"
}

```


## JSON

JSON es la *lingua franca* de los servicios web modernos, y también es el **tipo de contenido implícito** que HTTPie usa por defecto.

Ejemplo simple:


```bash


```bash`r`n$ http PUT pie.dev/put name=John email=john@example.org


```



```http

PUT / HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Host: pie.dev

{
    "name": "John",
    "email": "john@example.org"
}

```


### Comportamiento por defecto (Default behavior)

Si tu comando incluye algunos [elementos de solicitud](#request-items), estos se serializan como un objeto JSON por defecto. HTTPie también establece automáticamente los siguientes encabezados, que puedes sobrescribir:

|     Encabezado | Valor                         |
|---------------:|-------------------------------|
| `Content-Type` | `application/json`            |
|       `Accept` | `application/json, */*;q=0.5` |

### JSON explícito

Puedes usar `--json` o `-j` para establecer explícitamente el encabezado `Accept` como  `application/json` sin importar si estás enviando datos (Es un atajo para configurar el encabezado a través de la notación de encabezado habitual: `http url Accept:'application/json, */*;q=0.5'`).
Además, HTTPie intentará detectar respuestas JSON incluso si el `Content-Type` es incorrecto `text/plain` o desconocido.

### Campos JSON que no son cadenas

Para campos que no son cadenas, usa el separador `:=`, que te permite incluir datos JSON arbitrarios dentro del objeto resultante.
También puedes incluir archivos de texto o JSON sin procesar usando `=@` y `:=@`:


```bash


```bash`r`n$ http PUT pie.dev/put \

    name=John \                        # Cadena (por defecto)
    age:=29 \                          # JSON sin procesar — Número
    married:=false \                   # JSON sin procesar — Booleano
    hobbies:='["http", "pies"]' \      # JSON sin procesar — Array
    favorite:='{"tool": "HTTPie"}' \   # JSON sin procesar — Objeto
    bookmarks:=@files/data.json \      # Incluir archivo JSON
    description=@files/text.txt        # Incluir archivo de texto

```



```http

PUT /person/1 HTTP/1.1
Accept: application/json, */*;q=0.5
Content-Type: application/json
Host: pie.dev

{
    "age": 29,
    "hobbies": [
        "http",
        "pies"
    ],
    "description": "John is a nice guy who likes pies.",
    "married": false,
    "name": "John",
    "favorite": {
        "tool": "HTTPie"
    },
    "bookmarks": {
        "HTTPie": "https://httpie.org",
    }
}

```


La sintaxis `:=`/`:=@` es específica para JSON. Puedes cambiar tu solicitud a `--form` o `--multipart`,
y los valores de tipo cadena, número o flotante se seguirán serializando (como valores de formulario).
Sin embargo, otros tipos JSON no están permitidos con `--form` o `--multipart`.

### JSON anidado

Si tu caso de uso implica enviar objetos JSON complejos como parte del cuerpo de la solicitud,
HTTPie puede ayudarte a construirlos directamente desde tu terminal. Aún utilizas los operadores
de campo existentes (`=`/`:=`), pero en lugar de especificar un nombre de campo de nivel superior (como `key=value`),
especificas una declaración de ruta. Esto le indica a HTTPie dónde y cómo ubicar el valor dentro de un objeto:


```bash

http pie.dev/post \
  platform[name]=HTTPie \
  platform[about][mission]='Make APIs simple and intuitive' \
  platform[about][homepage]=httpie.io \
  platform[about][homepage]=httpie.io \
  platform[about][stars]:=54000 \
  platform[apps][]=Terminal \
  platform[apps][]=Desktop \
  platform[apps][]=Web \
  platform[apps][]=Mobile

```



```json

{
    "platform": {
        "name": "HTTPie",
        "about": {
            "mission": "Make APIs simple and intuitive",
            "homepage": "httpie.io",
            "stars": 54000
        },
        "apps": [
            "Terminal",
            "Desktop",
            "Web",
            "Mobile"
        ]
    }
}

```


#### Introducción

Comencemos con un ejemplo simple para construir una consulta de búsqueda:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  category=tools \
  search[type]=id \
  search[id]:=1

```


En el ejemplo anterior, `search[type]` es una instrucción para crear un objeto llamado `search`, y asignar el campo `type` con el valor (`"id"`).

También ten en cuenta que, al igual que con la sintaxis regular, puedes usar el operador `:=` para pasar directamente valores JSON sin procesar (por ejemplo, números en el caso anterior).


```json

{
    "category": "tools",
    "search": {
        "id": 1,
        "type": "id"
    }
}

```


También es posible construir arreglos mediante el sufijo `[]` (an append operation). Esto le indica a HTTPie que cree un array en la ruta especificada (si aún no existe), y añada el valor dado a ese array.


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  category=tools \
  search[type]=keyword \
  search[keywords][]=APIs \
  search[keywords][]=CLI

```



```json

{
    "category": "tools",
    "search": {
        "keywords": [
            "APIs",
            "CLI"
        ],
        "type": "keyword"
    }
}

```


Si deseas especificar explícitamente la posición de los elementos dentro de un arreglo,
simplemente puedes pasar el índice deseado como parte de la ruta:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  category=tools \
  search[type]=keyword \
  search[keywords][1]=APIs \
  search[keywords][0]=CLI

```



```json

{
    "category": "tools",
    "search": {
        "keywords": [
            "CLIs",
            "API"
        ],
        "type": "keyword"
    }
}

```


Si hay índices faltantes, HTTPie los rellenará con null para crear un objeto concreto que pueda ser enviado:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  category=tools \
  search[type]=platforms \
  search[platforms][]=Terminal \
  search[platforms][1]=Desktop \
  search[platforms][3]=Mobile

```



```json

{
    "category": "tools",
    "search": {
        "platforms": [
            "Terminal",
            "Desktop",
            null,
            "Mobile"
        ],
        "type": "platforms"
    }
}

```


También es posible incrustar JSON sin procesar en una estructura anidada, por ejemplo:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  category=tools \
  search[type]=platforms \
  'search[platforms]:=["Terminal", "Desktop"]' \
  search[platforms][]=Web \
  search[platforms][]=Mobile

```



```json

{
    "category": "tools",
    "search": {
        "platforms": [
            "Terminal",
            "Desktop",
            "Web",
            "Mobile"
        ],
        "type": "platforms"
    }
}

```


Y solo para demostrar todas estas características juntas, vamos a crear un objeto JSON profundamente anidado:


```bash


```bash`r`n$ http PUT pie.dev/put \

    shallow=value \                                # Par clave-valor superficial
    object[key]=value \                            # Par clave-valor anidado
    array[]:=1 \                                   # Arreglo — primer ítem
    array[1]:=2 \                                  # Arreglo — segundo ítem
    array[2]:=3 \                                  # Arreglo — tercer ítem (agregado)
    very[nested][json][3][httpie][power][]=Amaze   # Objeto profundamente anidado

```


#### Uso avanzado

##### Arreglos de nivel superior

Si deseas enviar un arreglo en lugar de un objeto regular, puedes hacerlo
simplemente omitiendo la clave inicial:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

    []:=1 \
    []:=2 \
    []:=3

```



```json

[
    1,
    2,
    3
]

```



También puedes aplicar anidamiento a los elementos haciendo referencia a su índice:


```bash

http --offline --print=B pie.dev/post \
    [0][type]=platform [0][name]=terminal \
    [1][type]=platform [1][name]=desktop

```



```json

[
    {
        "type": "platform",
        "name": "terminal"
    },
    {
        "type": "platform",
        "name": "desktop"
    }
]

```


Enviar tipos JSON escalares (un único `null`, `true`, `false`,  una cadena o número) como objeto de nivel superior no es posible usando la sintaxis de clave/valor. Pero aún puedes pasarlo mediante [`--raw='<value>'`](#raw-request-body).

##### Comportamiento de escape

La sintaxis JSON anidada usa las mismas [reglas de escape](#escaping-rules) que
el terminal. Hay tres caracteres especiales y un token especial que puedes escapar.

Si quieres enviar un corchete tal cual, escápalo con una barra invertida (`\`):


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  'foo\[bar\]:=1' \
  'baz[\[]:=2' \
  'baz[\]]:=3'

```



```json

{
    "baz": {
        "[": 2,
        "]": 3
    },
    "foo[bar]": 1
}

```


Si quieres enviar el carácter barra invertida (`\`), escápalo con otra barra invertida:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  'backslash[\\]:=1'

```



```json

{
    "backslash": {
        "\\": 1
    }
}

```


Un entero regular en una ruta (por ejemplo `[10]`) significa un índice de arreglo; pero si quieres que se trate
como una cadena, puedes escaparlo con un prefijo de barra invertida (`\`).


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  'object[\1]=stringified' \
  'object[\100]=same' \
  'array[1]=indexified'

```



```json

{
    "array": [
        null,
        "indexified"
    ],
    "object": {
        "1": "stringified",
        "100": "same"
    }
}

```


##### Errores de sintaxis guiados

Si cometes un error tipográfico o se te olvida cerrar un corchete, los errores te guiarán para corregirlo. Por ejemplo:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  'foo[bar]=OK' \
  'foo[baz][quux=FAIL'

```



```console

HTTPie Syntax Error: Expecting ']'
foo[baz][quux
             ^

```


Puedes seguir la instrucción dada (agregar un `]`) y corregir tu expresión.

##### Seguridad de tipos

Cada ruta contenedora (por ejemplo, `x[y][z]` in `x[y][z][1]`) tiene un tipo determinado que se define con
el primer uso y no se puede cambiar después de eso. Si intentas hacer un acceso por clave a un arreglo, o
un acceso por índice a un objeto, HTTPie mostrará un error:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  'array[]:=1' \
  'array[]:=2' \
  'array[key]:=3'
HTTPie Type Error: Can't perform 'key' based access on 'array' which has a type of 'array' but this operation requires a type of 'object'.
array[key]
     ^^^^^

```


La seguridad de tipos no aplica a la sobrescritura de valores. Por ejemplo:


```bash


```bash`r`n$ http --offline --print=B pie.dev/post \

  user[name]:=411     # Definido como entero
  user[name]=string   # Sobrescrito con una cadena

```



```json

{
    "user": {
        "name": "string"
    }
}

```


### JSON sin procesar

Para estructuras JSON muy complejas, puede ser más conveniente [enviar el cuerpo de la solicitud sin procesar](#raw-request-body), por ejemplo:


```bash

$ echo -n '{"hello": "world"}' | http POST pie.dev/post

```



```bash


```bash`r`n$ http POST pie.dev/post < files/data.json


```


## Formularios

Enviar formularios es muy similar a enviar solicitudes en [JSON](#json).
A menudo, la única diferencia es usar la opción `--form` o `-f`, que asegura que los campos se serialicen como pares clave-valor separados por '&', con un '=' entre la clave y el valor. Además, se establece `Content-Type` como `application/x-www-form-urlencoded; charset=utf-8`.
Es posible hacer que los datos en formulario sean el tipo de contenido predeterminado en lugar de JSON mediante el archivo de [configuracion](#config).

### Formularios regulares


```bash


```bash`r`n$ http --form POST pie.dev/post name='John Smith'


```



```http

POST /post HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8

name=John+Smith

```


### Formularios con carga de archivos

Si hay uno o más campos de archivo, la serialización y el tipo de contenido será `multipart/form-data`:


```bash


```bash`r`n$ http -f POST pie.dev/post name='John Smith' cv@~/files/data.xml


```


La solicitud anterior es equivalente a enviar el siguiente formulario HTML:


```html

<form enctype="multipart/form-data" method="post" action="http://example.com/jobs">
    <input type="text" name="name" />
    <input type="file" name="cv" />
</form>

```


Nota: `@` se usa para simular un campo de archivo en un formulario, mientras que `=@` simplemente inserta el contenido del archivo como texto.

Al subir archivos, el tipo de contenido se infiere del nombre del archivo. Puedes sobrescribirlo manualmente:


```bash


```bash`r`n$ http -f POST pie.dev/post name='John Smith' cv@'~/files/data.bin;type=application/pdf'


```


Para realizar una solicitud `multipart/form-data` incluso sin archivos, usa `--multipart` en lugar de `--form`:


```bash


```bash`r`n$ http --multipart --offline example.org hello=world


```



```http

POST / HTTP/1.1
Content-Length: 129
Content-Type: multipart/form-data; boundary=c31279ab254f40aeb06df32b433cbccb
Host: example.org

--c31279ab254f40aeb06df32b433cbccb
Content-Disposition: form-data; name="hello"

world
--c31279ab254f40aeb06df32b433cbccb--

```


Las cargas de archivos siempre se transmiten para evitar problemas de memoria con archivos grandes.

Por defecto, HTTPie usa una cadena única aleatoria como delimitador (boundary) en multipart, pero puedes definir uno personalizado con `--boundary`:


```bash


```bash`r`n$ http --form --multipart --boundary=xoxo --offline example.org hello=world


```



```http

POST / HTTP/1.1
Content-Length: 129
Content-Type: multipart/form-data; boundary=xoxo
Host: example.org

--xoxo
Content-Disposition: form-data; name="hello"

world
--xoxo--

```


Si defines manualmente el encabezado `Content-Type` sin incluir el límite (boundary), HTTPie añadirá automáticamente el valor del límite (especificado explícitamente o autogenerado) al encabezado:


```bash


```bash`r`n$ http --form --multipart --offline example.org hello=world Content-Type:multipart/letter


```



```http

POST / HTTP/1.1
Content-Length: 129
Content-Type: multipart/letter; boundary=c31279ab254f40aeb06df32b433cbccb
Host: example.org

--c31279ab254f40aeb06df32b433cbccb
Content-Disposition: form-data; name="hello"

world
--c31279ab254f40aeb06df32b433cbccb--

```


## Encabezados HTTP

Para establecer encabezados personalizados, puedes usar la notación `Header:Value`:


```bash


```bash`r`n$ http pie.dev/headers User-Agent:Bacon/1.0 'Cookie:valued-visitor=yes;foo=bar' \

    X-Foo:Bar Referer:https://httpie.org/

```



```http

GET /headers HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Cookie: valued-visitor=yes;foo=bar
Host: pie.dev
Referer: https://httpie.org/
User-Agent: Bacon/1.0
X-Foo: Bar

```


### Encabezados de solicitud predeterminados

Hay algunos encabezados predeterminados que HTTPie establece:


```http

GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
User-Agent: HTTPie/<version>
Host: <taken-from-URL>

```


Todos estos pueden sobrescribirse o eliminarse (ver más abajo).

### Leer encabezados desde un archivo

Puedes leer encabezados desde un archivo usando el operador `:@` Esto también elimina automáticamente los saltos de línea al final. Ver [separadores basados en archivos](#file-based-separators) para más ejemplos.


```bash


```bash`r`n$ http pie.dev/headers X-Data:@files/text.txt


```


### Empty headers and header un-setting

Para eliminar un encabezado previamente especificado (como uno de los predeterminados), usa `Header:`:


```bash


```bash`r`n$ http pie.dev/headers Accept: User-Agent:


```


Para enviar un encabezado con un valor vacío, usa `Header;`, con un punto y coma:


```bash


```bash`r`n$ http pie.dev/headers 'Header;'


```


Ten en cuenta que algunos encabezados internos, como `Content-Length`, no pueden eliminarse si
son añadidos automáticamente por el cliente.

### Múltiples valores de encabezado con el mismo nombre

Si la solicitud se envía con múltiples encabezados con el mismo nombre,
HTTPie los enviará de forma individual:


```bash

http --offline example.org Cookie:one Cookie:two

```



```http

GET / HTTP/1.1
Cookie: one
Cookie: two

```


También se permite enviar un solo par de encabezado, cuyo valor consiste en una lista
de valores de encabezado separados por comas. El cliente lo transmitirá entonces como un único encabezado:


```bash

http --offline example.org Numbers:one,two

```



```http

GET / HTTP/1.1
Numbers: one,two

```


También ten en cuenta que si la sesión actual contiene encabezados, serán sobrescritos
por los comandos individuales al enviar una solicitud en lugar de combinarse.

### Limitar encabezados de respuesta

La opción `--max-headers=n` te permite controlar cuántos encabezados HTTPie leerá antes de detenerse (el valor predeterminado es `0`, es decir, sin límite).


```bash


```bash`r`n$ http --max-headers=100 pie.dev/get


```


## Modo sin conexión (Offline)

Usa `--offline` para construir solicitudes HTTP sin enviarlas a ningún lado.
Con `--offline`, HTTPie construye una solicitud basada en las opciones y argumentos especificados, la imprime en `stdout`, y luego termina. Funciona completamente sin conexión; nunca se realiza una conexión de red. Esto tiene múltiples usos, incluyendo:

Generar ejemplos para documentación de APIs que puedes copiar y pegar sin enviar una solicitud:


```bash


```bash`r`n$ http --offline POST server.chess/api/games API-Key:ZZZ w=magnus b=hikaru t=180 i=2


```



```bash


```bash`r`n$ http --offline MOVE server.chess/api/games/123 API-Key:ZZZ p=b a=R1a3 t=77


```


Generar solicitudes sin procesar que pueden ser enviadas con cualquier otro cliente:


```bash

# 1. guardar una solicitud sin procesar en un archivo:

```bash`r`n$ http --offline POST pie.dev/post hello=world > request.http


```



```bash

# 2. envialo por la red utilizando, por ejemplo, la magnífica herramienta netcat:
$ nc pie.dev 80 < request.http

```


También puedes usar `--offline` para depuración, exploración de HTTP y HTTPie, y para “simulacros”.

`--offline` tiene el efecto secundario de activar automáticamente `--print=HB`, es decir, se imprimen tanto los encabezados como el cuerpo de la solicitud. Puedes personalizar la salida con las [opciones de salida](#output-options), con la excepción de que
no hay respuesta que imprimir. Puedes usar `--offline` junto con todas las demás opciones (por ejemplo `--session`).

## Cookies

Los clientes HTTP envían cookies al servidor como [encabezados HTTP](#http-headers) regulares.
Eso significa que HTTPie no ofrece ninguna sintaxis especial para especificar cookies — se usa la notación normal `Header:Value`:

Enviar una sola cookie:


```bash


```bash`r`n$ http pie.dev/cookies Cookie:sessionid=foo


```



```http

GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: sessionid=foo
Host: pie.dev
User-Agent: HTTPie/0.9.9

```


Enviar múltiples cookies (nota: se usan comillas para evitar que el shell interprete el `;`):


```bash


```bash`r`n$ http pie.dev/cookies 'Cookie:sessionid=foo;another-cookie=bar'


```



```http

GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: sessionid=foo;another-cookie=bar
Host: pie.dev
User-Agent: HTTPie/0.9.9

```


Si a menudo trabajas con cookies en tus solicitudes, entonces apreciarás
la función de [sesiones](#sessions).

## Autenticación

Los esquemas de autenticación actualmente soportados son Basic y Digest (ver [plugins de autenticación](#auth-plugins) para más). Hay dos flags que controlan la autenticación:

|              Flag | Argumentos                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      `--auth, -a` | Pasa un par `usuario:contraseña` o un `token` como argumento. Si el método de autenticación seleccionado requiere combinación usuario/contraseña y solo especificas el usuario (`-a username`), se te pedirá la contraseña antes de enviar la solicitud. Para enviar una contraseña vacía, pasa `username:`. También se soporta la sintaxis URL `username:password@hostname` (pero las credenciales pasadas vía `-a` tienen mayor prioridad). |
| `--auth-type, -A` | Especifica el mecanismo de autenticación. Los valores posibles son `basic`, `digest`, `bearer` o el nombre de cualquier [plugin de autenticación](#auth-plugins) que tengas instalado. El valor por defecto es `basic`, por lo que a menudo puede omitirse.                                                                                                                                                                                                                                  |

### Autenticación basica


```bash


```bash`r`n$ http -a username:password pie.dev/basic-auth/username/password


```


### Autenticación Digest


```bash


```bash`r`n$ http -A digest -a username:password pie.dev/digest-auth/httpie/username/password


```


### Autenticación Bearer


```bash

https -A bearer -a token pie.dev/bearer

```


### Solicitud de contraseña

Si omites la parte de la contraseña en `--auth, -a`, HTTPie te pedirá la contraseña de forma segura:


```bash


```bash`r`n$ http -a username pie.dev/basic-auth/username/password


```


Ten en cuenta que cuando usas [`--session`](#sessions), las contraseñas ingresadas se guardan en los archivos de sesión.

### Contraseña vacía

Para enviar una contraseña vacía sin que se te pida, incluye dos puntos al final de las credenciales:


```bash


```bash`r`n$ http -a username: pie.dev/headers


```


### `.netrc`

La información de autenticación de tu archivo `~/.netrc` es respetada por defecto.

Por ejemplo:


```bash

$ cat ~/.netrc
machine pie.dev
login httpie
password test

```



```bash


```bash`r`n$ http pie.dev/basic-auth/httpie/test

HTTP/1.1 200 OK
[...]

```


Esto se puede desactivar con la opción `--ignore-netrc`:


```bash


```bash`r`n$ http --ignore-netrc pie.dev/basic-auth/httpie/test

HTTP/1.1 401 UNAUTHORIZED
[...]

```


### Plugins de autenticación

Mecanismos adicionales de autenticación pueden instalarse como plugins.
Se pueden encontrar en el [Python Package Index](https://pypi.python.org/pypi?%3Aaction=search&term=httpie&submit=search).
Aquí algunos ejemplos:


- [httpie-api-auth](https://github.com/pd/httpie-api-auth): ApiAuth


- [httpie-aws-auth](https://github.com/httpie/httpie-aws-auth): AWS / Amazon S3


- [httpie-edgegrid](https://github.com/akamai-open/httpie-edgegrid): EdgeGrid


- [httpie-hmac-auth](https://github.com/guardian/httpie-hmac-auth): HMAC


- [httpie-jwt-auth](https://github.com/teracyhq/httpie-jwt-auth): JWTAuth (JSON Web Tokens)


- [httpie-negotiate](https://github.com/ndzou/httpie-negotiate): SPNEGO (GSS Negotiate)


- [httpie-ntlm](https://github.com/httpie/httpie-ntlm): NTLM (NT LAN Manager)


- [httpie-oauth1](https://github.com/qcif/httpie-oauth1): OAuth 1.0a


- [requests-hawk](https://github.com/mozilla-services/requests-hawk): Hawk


Consulta [plugin manager](#plugin-manager) para más detalles.

## Redirecciones HTTP

Por defecto, las redirecciones HTTP no se siguen y solo se muestra
la primera respuesta:


```bash


```bash`r`n$ http pie.dev/redirect/3


```


### Seguir `Location`

Para indicar a HTTPie que siga la cabecera `Location` de las respuestas `30x`
y muestre la respuesta final, usa la opción `--follow, -F`:


```bash


```bash`r`n$ http --follow pie.dev/redirect/3


```


Con `307 Temporary Redirect` y `308 Permanent Redirect`, el método y el cuerpo de la solicitud original
se reutilizan para realizar la solicitud redirigida. En otros casos, se realiza una solicitud `GET` sin cuerpo.

### Mostrar respuestas intermedias de redirección

Si deseas ver las solicitudes/respuestas intermedias,
usa la opción `--all`:


```bash


```bash`r`n$ http --follow --all pie.dev/redirect/3


```


### Limitar el máximo de redirecciones seguidas

Para cambiar el límite predeterminado de máximo `30` redirecciones, usa la opción `--max-redirects=<limit>`:


```bash


```bash`r`n$ http --follow --all --max-redirects=2 pie.dev/redirect/3


```


## Proxies

Puedes especificar los proxies a utilizar mediante el argumento `--proxy` para cada protocolo (que se incluye en el valor en caso de redirecciones entre protocolos):


```bash


```bash`r`n$ http --proxy=http:http://10.10.1.10:3128 --proxy=https:https://10.10.1.10:1080 example.org


```


Con autenticación básica:


```bash


```bash`r`n$ http --proxy=http:http://user:pass@10.10.1.10:3128 example.org


```


### Variables de entorno

También puedes configurar proxies mediante las variables de entorno `ALL_PROXY`, `HTTP_PROXY` y `HTTPS_PROXY`, y la biblioteca subyacente
[Requests](https://requests.readthedocs.io/en/latest/) las detectará automáticamente.
Si deseas deshabilitar los proxies configurados a través de variables de entorno para ciertos hosts, puedes especificarlos en `NO_PROXY`.

En tu `~/.bash_profile`:


```bash

export HTTP_PROXY=http://10.10.1.10:3128
export HTTPS_PROXY=https://10.10.1.10:1080
export NO_PROXY=localhost,example.com

```


### SOCKS

El uso de SOCKS es igual que para otros tipos de [proxies](#proxies):


```bash


```bash`r`n$ http --proxy=http:socks5://user:pass@host:port --proxy=https:socks5://user:pass@host:port example.org


```


## HTTPS

### Verificación del certificado SSL del servidor

Para omitir la verificación del certificado SSL del host, puedes pasar `--verify=no` (el valor predeterminado es `yes`):


```bash


```bash`r`n$ http --verify=no https://pie.dev/get


```


### CA bundle personalizado

También puedes usar `--verify=<CA_BUNDLE_PATH>` para establecer una ruta personalizada al CA bundle:


```bash


```bash`r`n$ http --verify=/ssl/custom_ca_bundle https://example.org


```


### Certificado SSL del lado del cliente

Para usar un certificado del lado del cliente en la comunicación SSL, puedes pasar
la ruta del archivo de certificado con `--cert`:


```bash


```bash`r`n$ http --cert=client.pem https://example.org


```


Si la clave privada no está contenida en el archivo de certificado, puedes pasar la
ruta del archivo de clave con `--cert-key`:


```bash


```bash`r`n$ http --cert=client.crt --cert-key=client.key https://example.org


```


Si la clave privada proporcionada requiere una frase de contraseña, HTTPie la detectará automáticamente
y la solicitará mediante un prompt:


```bash


```bash`r`n$ http --cert=client.pem --cert-key=client.key https://example.org

http: passphrase for client.key: ****

```


Si no deseas ver un prompt, puedes suministrar la frase de contraseña con el argumento `--cert-key-pass`:


```bash


```bash`r`n$ http --cert=client.pem --cert-key=client.key --cert-key-pass=my_password https://example.org


```


### Versión de SSL

Usa la opción `--ssl=<PROTOCOL>` para especificar la versión de protocolo deseada.
Por defecto se usa SSL v2.3, que negociará el protocolo más alto que tanto el servidor como tu instalación de OpenSSL soporten.
Los protocolos disponibles son `ssl2.3`, `ssl3`, `tls1`, `tls1.1`, `tls1.2`, `tls1.3`.
(El conjunto real de protocolos disponibles puede variar según tu instalación de OpenSSL.)


```bash

# Especificar el protocolo SSL v3 vulnerable para comunicarte con un servidor desactualizado:

```bash`r`n$ http --ssl=ssl3 https://vulnerable.example.org


```


### Cifrados SSL

Puedes especificar los cifrados disponibles con `--ciphers`.
Debe ser una cadena en el [formato de lista de cifrados de OpenSSL](https://www.openssl.org/docs/man1.1.0/man1/ciphers.html).


```bash


```bash`r`n$ http --ciphers=ECDHE-RSA-AES128-GCM-SHA256 https://pie.dev/get


```


Nota: estas cadenas de cifrado no cambian la versión negociada de SSL o TLS, solo afectan la lista de suites de cifrado disponibles.

Para ver la cadena de cifrado predeterminada, ejecuta `http --help` y busca la sección `--ciphers` bajo SSL.

## Opciones de salida

Por defecto, HTTPie solo muestra la respuesta final y se imprime todo el mensaje de respuesta (cabeceras y cuerpo). Puedes controlar qué se debe imprimir mediante varias opciones:

|                     Opción | Qué se imprime                                                                                           |
|---------------------------:|----------------------------------------------------------------------------------------------------------|
|            `--headers, -h` | Solo se imprimen los encabezados de la respuesta                                                         |
|               `--body, -b` | Solo se imprime el cuerpo de la respuesta                                                                |
|               `--meta, -m` | Solo se imprime la [metainformación de la respuesta](#response-meta)                                     |
|            `--verbose, -v` | Imprime todo el intercambio HTTP (solicitud y respuesta). Esta opción también habilita `--all` (ver abajo)|
| `--verbose --verbose, -vv` | Igual que `-v`, pero también incluye la metainformación de la respuesta.                                 |
|              `--print, -p` | Selecciona partes del intercambio HTTP                                                                   |
|              `--quiet, -q` | No imprime nada en `stdout` ni en `stderr`                                                               |

### Qué partes del intercambio HTTP deben imprimirse

Todas las demás [opciones de salida](#output-options) son en realidad atajos para la opción más potente `--print, -p`.
Esta acepta una cadena de caracteres, cada uno de los cuales representa una parte específica del intercambio HTTP:

| Carácter | Representa                        |
|----------:|----------------------------------|
|       `H` | encabezados de la solicitud      |
|       `B` | cuerpo de la solicitud           |
|       `h` | encabezados de la respuesta      |
|       `b` | cuerpo de la respuesta           |
|       `m` | [meta de la respuesta](#response-meta) |

Imprimir encabezados de solicitud y respuesta:


```bash


```bash`r`n$ http --print=Hh PUT pie.dev/put hello=world


```


#### Meta de la respuesta

La sección de metadatos de la respuesta actualmente incluye el tiempo total transcurrido. Es el número de segundos entre la apertura de la conexión de red y la descarga del último byte del cuerpo de la respuesta.


Para _only_ la metainformación de la respuesta, usa `--meta, -m` (de manera análoga a `--headers, -h` y `--body, -b`):


```bash


```bash`r`n$ http --meta pie.dev/delay/1


```



```console

Elapsed time: 1.099171542s

```


La [salida extra verbosa con `-vv`](#extra-verbose-output) incluye la sección meta por defecto. También puedes mostrarla en combinación con otras partes del intercambio usando [`--print=m`](#what-parts-of-the-http-exchange-should-be-printed). Por ejemplo, aquí la imprimimos junto con los encabezados de la respuesta:


```bash


```bash`r`n$ http --print=hm pie.dev/get


```



```http

HTTP/1.1 200 OK
Content-Type: application/json

Elapsed time: 0.077538375s

```


Ten en cuenta que también incluye el tiempo dedicado a formatear la salida, lo que añade una pequeña penalización. Además, si el cuerpo no forma parte de la salida, [no se invierte tiempo en descargarlo](#conditional-body-download).

Si [usas `--style` con uno de los temas Pie](#colors-and-formatting), verás la información de tiempo resaltada en color (verde/amarillo/naranja/rojo) según cuánto haya tardado el intercambio.


### Salida detallada

`--verbose` suele ser útil para depurar la solicitud y generar ejemplos de documentación:


```bash


```bash`r`n$ http --verbose PUT pie.dev/put hello=world

PUT /put HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Host: pie.dev
User-Agent: HTTPie/0.2.7dev

{
    "hello": "world"
}

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 477
Content-Type: application/json
Date: Sun, 05 Aug 2012 00:25:23 GMT
Server: gunicorn/0.13.4

{
    […]
}


```


#### Salida extra verbosa

Si ejecutas HTTPie con `-vv` o `--verbose --verbose`, también mostrará la [metainformación de la respuesta](#response-meta).


```bash

# Igual que el anterior, pero con columnas adicionales como el tiempo total transcurrido

```bash`r`n$ http -vv pie.dev/get


```


### Salida silenciosa

`--quiet` redirige toda la salida que normalmente iría a `stdout` y `stderr` a `/dev/null` (excepto errores y advertencias).
Esto no afecta la salida a un archivo mediante `--output` o `--download`.


```bash

# No habrá salida:

```bash`r`n$ http --quiet pie.dev/post enjoy='the silence'


```


Si también deseas silenciar las advertencias, usa `-q` o `--quiet` dos veces:


```bash

# No habrá salida, incluso en caso de un código de estado de respuesta inesperado:

```bash`r`n$ http -qq --check-status pie.dev/post enjoy='the silence without warnings'


```


### Advertencias de actualización

Cuando hay una nueva versión disponible para tu plataforma (por ejemplo, si instalaste HTTPie mediante `pip`, verificará la última versión en `PyPI`), HTTPie te advertirá regularmente sobre la nueva actualización (una vez por semana). Si deseas desactivar este comportamiento, puedes establecer `disable_update_warnings` en `true` en tu archivo de [configuración](#config).

### Ver solicitudes/respuestas intermedias

Para ver toda la comunicación HTTP, es decir, la solicitud/respuesta final así como cualquier posible solicitud/respuesta intermedia, utiliza la opción `--all`.
La comunicación HTTP intermedia incluye redirecciones seguidas (con `--follow`), la primera solicitud no autorizada cuando se usa autenticación digest HTTP (`--auth=digest`), etc.


```bash

# Incluye todas las respuestas que llevan a la final:

```bash`r`n$ http --all --follow pie.dev/redirect/3


```


Las solicitudes/respuestas intermedias se formatean por defecto según `--print, -p` (y sus atajos descritos arriba).

### Descarga condicional del cuerpo

Como optimización, el cuerpo de la respuesta se descarga del servidor solo si forma parte de la salida.
Esto es similar a realizar una solicitud `HEAD`, excepto que se aplica a cualquier método HTTP que utilices.

Supongamos que existe una API que devuelve todo el recurso cuando se actualiza, pero solo te interesan los encabezados de la respuesta para ver el código de estado después de una actualización:


```bash


```bash`r`n$ http --headers PATCH pie.dev/patch name='New Name'


```


Como aquí solo se imprimen los encabezados HTTP, la conexión con el servidor se cierra tan pronto como se reciben todos los encabezados de la respuesta.
Por lo tanto, no se desperdicia ancho de banda ni tiempo descargando el cuerpo que no te interesa.
Los encabezados de la respuesta siempre se descargan, incluso si no forman parte de la salida.

## Cuerpo de solicitud sin procesar

Además de crear solicitudes estructuradas en [JSON](#json) y [formularios](#forms) usando la sintaxis de [elementos de solicitud](#request-items), puedes proporcionar un cuerpo de solicitud sin procesar que se enviará sin procesamiento adicional.
Estos dos enfoques para especificar datos de solicitud (estructurado y sin procesar) no pueden combinarse.

Existen tres métodos para pasar datos sin procesar en la solicitud: mediante pipe usando `stdin`,
`--raw='data'` y `@/ruta/del/archivo`.

### Entrada redirigida

El método universal para pasar datos de solicitud es a través de la redirección de `stdin`
(entrada estándar), es decir, mediante pipe.

Por defecto, los datos de `stdin` se almacenan en búfer y luego se usan como cuerpo de la solicitud sin procesamiento adicional.
Si proporcionas `Content-Length`, entonces el cuerpo de la solicitud se transmite sin almacenamiento en búfer.
También puedes usar `--chunked` para habilitar la transmisión mediante [codificación de transferencia por bloques](#chunked-transfer-encoding)
o `--compress, -x` para [comprimir el cuerpo de la solicitud](#compressed-request-body).

Existen varias formas útiles de usar pipes:

Redirigir desde un archivo:


```bash


```bash`r`n$ http PUT pie.dev/put X-API-Token:123 < files/data.json


```


O la salida de otro programa:


```bash

$ grep '401 Unauthorized' /var/log/httpd/error_log | http POST pie.dev/post

```


Puedes usar `echo` para datos simples:


```bash

$ echo -n '{"name": "John"}' | http PATCH pie.dev/patch X-API-Token:123

```


También puedes usar un *here string* de Bash:


```bash


```bash`r`n$ http pie.dev/post <<<'{"name": "John"}'


```


Incluso puedes encadenar servicios web usando HTTPie:


```bash


```bash`r`n$ http GET https://api.github.com/repos/httpie/cli | http POST pie.dev/post


```


Puedes usar `cat` para ingresar datos multilínea en la terminal:


```bash

$ cat | http POST pie.dev/post
<pega aquí>
^D

```



```bash

$ cat | http POST pie.dev/post Content-Type:text/plain

- comprar leche


- llamar a los padres

^D

```


En macOS, puedes enviar el contenido del portapapeles con `pbpaste`:


```bash

$ pbpaste | http PUT pie.dev/put

```


Pasar datos a través de `stdin` **no puede** combinarse con campos de datos especificados en la línea de comandos:


```bash

$ echo -n 'data' | http POST example.org more=data  # Esto es inválido

```


Para evitar que HTTPie lea datos de `stdin` puedes usar la opción `--ignore-stdin`.

### Datos de solicitud vía `--raw`

En situaciones donde no es conveniente canalizar datos a través de `stdin` (por ejemplo,
al generar ejemplos para documentación de APIs), puedes especificar el cuerpo sin procesar de la solicitud usando
la opción `--raw`.


```bash


```bash`r`n$ http --raw 'Hello, world!' pie.dev/post


```



```bash


```bash`r`n$ http --raw '{"name": "John"}' pie.dev/post


```


### Datos de solicitud desde un archivo

Una alternativa a la redirección de `stdin` es especificar un nombre de archivo (como `@/ruta/al/archivo`) cuyo contenido se utiliza como si proviniera de `stdin`.

Tiene la ventaja de que el encabezado `Content-Type` se establece automáticamente al valor apropiado según la extensión del archivo.
Por ejemplo, la siguiente solicitud envía el contenido literal de ese archivo XML con `Content-Type: application/xml`:


```bash


```bash`r`n$ http PUT pie.dev/put @files/data.xml


```


La carga de archivos siempre se transmite para evitar problemas de memoria con archivos grandes.

## Transferencia por bloques (Chunked transfer encoding)

Puedes usar la opción `--chunked` para indicar a HTTPie que utilice `Transfer-Encoding: chunked`:


```bash


```bash`r`n$ http --chunked PUT pie.dev/put hello=world


```



```bash


```bash`r`n$ http --chunked --multipart PUT pie.dev/put hello=world foo@files/data.xml


```



```bash


```bash`r`n$ http --chunked pie.dev/post @files/data.xml


```



```bash

$ cat files/data.xml | http --chunked pie.dev/post

```


## Cuerpo de solicitud comprimido

Puedes usar la opción `--compress, -x` para indicar a HTTPie que utilice `Content-Encoding: deflate` y comprima los datos de la solicitud:


```bash


```bash`r`n$ http --compress pie.dev/post @files/data.xml


```



```bash

$ cat files/data.xml | http --compress pie.dev/post

```


Si comprimir los datos no reduce el tamaño, HTTPie los envía sin cambios. Para forzar la compresión siempre, especifica `--compress, -x` dos veces:


```bash


```bash`r`n$ http -xx PUT pie.dev/put hello=world


```


## Salida en terminal

HTTPie realiza varias acciones por defecto para que la salida en la terminal sea fácil de leer.

### Colores y formato

Se aplica resaltado de sintaxis a los encabezados y cuerpos HTTP (cuando tiene sentido).
Puedes elegir tu esquema de color preferido usando la opción `--style` si no te gusta el predeterminado.
Hay docenas de estilos disponibles, aquí algunos de los más destacados:

|       Estilo | Descripción                                                                                                                                                                                                                                                |
|------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      `auto` | Sigue los estilos de color ANSI de tu terminal. Este es el estilo predeterminado que usa HTTPie                                                                                                                                                             |
|   `default` | Estilos predeterminados de la biblioteca subyacente Pygments. No es el estilo predeterminado de HTTPie. Puedes activarlo con `--style=default`                                                                                                              |
|  `pie-dark` | El estilo original de la marca HTTPie. También se usa en [HTTPie para Web y Desktop](https://httpie.io/product).                                                                                                                                            |
| `pie-light` | Igual que `pie-dark`, pero para terminales con fondos claros.                                                                                                                                                                                               |
|       `pie` | Una versión genérica de los temas `pie-dark` y `pie-light` que puede funcionar con cualquier fondo de terminal. Su universalidad requiere compromisos en cuanto a legibilidad, pero es útil si cambias frecuentemente entre fondos claros y oscuros.         |
|   `monokai` | Un esquema de colores popular. Actívalo con `--style=monokai`                                                                                                                                                                                               |
|    `fruity` | Un esquema colorido y llamativo. Actívalo con `--style=fruity`                                                                                                                                                                                              |
|           … | Consulta `$ http --help` para ver todos los posibles valores de `--style`                                                                                                                                            |

Usa una de estas opciones para controlar el procesamiento de la salida:

|            Opción | Descripción                                                        |
|------------------:|--------------------------------------------------------------------|
|    `--pretty=all` | Aplica tanto colores como formato. Predeterminado para salida en terminal |
| `--pretty=colors` | Aplica solo colores                                               |
| `--pretty=format` | Aplica solo formato                                               |
|   `--pretty=none` | Desactiva el procesamiento de la salida. Predeterminado para salida redirigida |

HTTPie revisa el `Content-Type` para seleccionar el resaltador de sintaxis y el formateador adecuado para cada cuerpo de mensaje. Si esto falla (por ejemplo, si el servidor proporciona un tipo incorrecto), o prefieres un tratamiento diferente, puedes sobrescribir manualmente el tipo mime de una respuesta con `--response-mime`:


```bash


```bash`r`n$ http --response-mime=text/yaml pie.dev/get


```



El formateo tiene los siguientes efectos:


- Los encabezados HTTP se ordenan por nombre.


- Los datos JSON se indentan, se ordenan por claves y los caracteres unicode escapados se convierten

en los caracteres que representan.

- Los datos XML y XHTML se indentan.



Ten en cuenta que a veces los formateadores pueden realizar cambios en el cuerpo real de la respuesta (por ejemplo,
colapsar etiquetas vacías en XML), pero el resultado final siempre será semánticamente indistinguible. Algunos de
estos cambios de formato pueden configurarse de manera más granular mediante las [opciones de formato](#format-options).

### Opciones de formato

La opción `--format-options=opt1:value,opt2:value` te permite controlar cómo debe formatearse la salida
cuando se aplica el formateo. Las siguientes opciones están disponibles:

|           Option | Default value | Shortcuts                |
|-----------------:|:-------------:|--------------------------|
|   `headers.sort` |    `true`     | `--sorted`, `--unsorted` |
|    `json.format` |    `true`     | N/A                      |
|    `json.indent` |      `4`      | N/A                      |
| `json.sort_keys` |    `true`     | `--sorted`, `--unsorted` |
|     `xml.format` |    `true`     | N/A                      |
|     `xml.indent` |      `2`      | N/A                      |

Por ejemplo, así es como deshabilitarías el ordenamiento predeterminado de encabezados y claves JSON, y especificarías un tamaño de indentación personalizado para JSON:


```bash


```bash`r`n$ http --format-options headers.sort:false,json.sort_keys:false,json.indent:2 pie.dev/get


```


También existen dos atajos que te permiten desactivar y volver a activar rápidamente las opciones de formato relacionadas con el ordenamiento (actualmente significa claves JSON y encabezados): `--unsorted` y `--sorted`.

Esto es algo que normalmente almacenarías como una de las opciones predeterminadas en tu archivo de [configuración](#config).

### Salida redirigida

HTTPie utiliza un conjunto diferente de valores predeterminados para la salida redirigida que para la [salida en terminal](#salida-en-terminal).
Las diferencias son:


- No se aplican formato ni colores (a menos que se especifique `--pretty`).


- Solo se imprime el cuerpo de la respuesta (a menos que se establezca una de las [opciones de salida](#opciones-de-salida)).


- Además, los datos binarios no se suprimen.


La razón es facilitar el uso de pipes para enviar la salida de HTTPie a otros programas y descargar archivos sin necesidad de flags adicionales.
La mayoría de las veces, solo interesa el cuerpo bruto de la respuesta cuando la salida es redirigida.

Descargar un archivo:


```bash


```bash`r`n$ http pie.dev/image/png > image.png


```


Descarga una imagen de un [Octocat](https://octodex.github.com/images/original.jpg), redimensiónala usando [ImageMagick](https://imagemagick.org/) y súbela a otro lugar:


```bash


```bash`r`n$ http octodex.github.com/images/original.jpg | convert - -resize 25% - | http example.org/Octocats


```


Fuerza el coloreado y el formato, y muestra tanto la solicitud como la respuesta en el paginador `less`:


```bash


```bash`r`n$ http --pretty=all --verbose pie.dev/get | less -R


```


La opción `-R` le indica a `less` que interprete las secuencias de escape de color incluidas en la salida de HTTPie.

Puedes crear un atajo para invocar HTTPie con salida coloreada y paginada agregando lo siguiente a tu `~/.bash_profile`:


```bash

function httpless {
    # `httpless example.org'
    http --pretty=all --print=hb "$@" | less -R;
}

```


### Datos binarios

Los datos binarios se suprimen en la salida de terminal, lo que hace seguro realizar solicitudes a URLs que devuelven datos binarios.
Los datos binarios también se suprimen en la salida redirigida pero formateada.
La conexión se cierra tan pronto como se detecta que el cuerpo de la respuesta es binario,


```bash


```bash`r`n$ http pie.dev/bytes/2000


```


Casi de inmediato verás algo como esto:


```http

HTTP/1.1 200 OK
Content-Type: application/octet-stream

+--------------------------------------------------+
| NOTA: datos binarios no mostrados en la terminal |
+--------------------------------------------------+

```


### Codificación de visualización

HTTPie intenta decodificar correctamente los cuerpos de los mensajes al imprimirlos en la terminal. Utiliza la codificación especificada en el atributo `charset` de `Content-Type`. Si un mensaje no define su charset, lo detectamos automáticamente. Para mensajes muy cortos (1–32B), donde la autodetección sería poco confiable, usamos UTF-8 por defecto. En los casos en que la codificación de la respuesta siga siendo incorrecta, puedes sobrescribir manualmente el charset de la respuesta con `--response-charset`:


```bash


```bash`r`n$ http --response-charset=big5 pie.dev/get


```


## Modo de descarga

HTTPie incluye un modo de descarga en el que actúa de manera similar a `wget`.

Cuando se habilita usando la opción `--download, -d`, los encabezados de la respuesta se imprimen en la terminal (`stderr`) y se muestra una barra de progreso mientras el cuerpo de la respuesta se guarda en un archivo.


```bash


```bash`r`n$ http --download https://github.com/httpie/cli/archive/master.tar.gz


```



```http

HTTP/1.1 200 OK
Content-Disposition: attachment; filename=httpie-master.tar.gz
Content-Length: 257336
Content-Type: application/x-gzip

Downloading 251.30 kB to "httpie-master.tar.gz"
Done. 251.30 kB in 2.73862s (91.76 kB/s)

```


### Nombre del archivo descargado

Hay tres formas mutuamente excluyentes mediante las cuales HTTPie determina
el nombre del archivo de salida (en orden de prioridad descendente):

1. Puedes proporcionarlo explícitamente usando `--output, -o`. El archivo se sobrescribe si ya existe (o se añade al final con `--continue, -c`).
2. El servidor puede especificar el nombre del archivo en el encabezado de respuesta opcional `Content-Disposition`. Cualquier punto inicial se elimina del nombre de archivo proporcionado por el servidor.
3. Como último recurso, HTTPie genera el nombre del archivo a partir de una combinación de la URL de la solicitud y el `Content-Type` de la respuesta. Siempre se utiliza la URL inicial como base para el nombre de archivo generado, incluso si ha habido una o más redirecciones.

Para evitar la pérdida de datos por sobrescritura, HTTPie añade un sufijo numérico único al nombre del archivo cuando es necesario (a menos que se especifique con `--output, -o`).

### Redirección durante la descarga

También puedes redirigir el cuerpo de la respuesta a otro programa mientras los encabezados de la respuesta y el progreso aún se muestran en la terminal:


```bash


```bash`r`n$ http -d https://github.com/httpie/cli/archive/master.tar.gz | tar zxf -


```


### Reanudar descargas

Si se especifica `--output, -o`, puedes reanudar una descarga parcial usando la opción `--continue, -c`.
Esto solo funciona con servidores que soportan solicitudes `Range` y respuestas `206 Partial Content`.
Si el servidor no lo soporta, simplemente se descargará el archivo completo:


```bash


```bash`r`n$ http -dco file.zip example.org/file


```


`-dco` es un atajo para `--download` `--continue` `--output`.

### Otras notas


- La opción `--download` solo cambia cómo se trata el cuerpo de la respuesta.


- Aún puedes establecer encabezados personalizados, usar sesiones, `--verbose, -v`, etc.


- `--download` siempre implica `--follow` (las redirecciones se siguen).


- `--download` también implica `--check-status` (un estado HTTP de error resultará en un código de salida distinto de cero).


- HTTPie sale con código de estado `1` (error) si el cuerpo no se ha descargado completamente.


- `Accept-Encoding` no puede establecerse con `--download`.


## Respuestas transmitidas (streamed)

Las respuestas se descargan e imprimen en fragmentos.
Esto permite la transmisión y la descarga de archivos grandes sin usar demasiada memoria.
Sin embargo, cuando se aplican [colores y formato](#colors-and-formatting), toda la respuesta se almacena en búfer y solo entonces se procesa de una vez.

### Desactivando el almacenamiento en búfer

Puedes usar la opción `--stream, -S` para lograr dos cosas:

1. La salida se vacía en fragmentos mucho más pequeños sin ningún almacenamiento en búfer, lo que hace que HTTPie se comporte como `tail -f` para URLs.
2. El streaming se habilita incluso cuando la salida está embellecida: se aplicará a cada línea de la respuesta y se vaciará inmediatamente. Esto permite tener una salida agradable para solicitudes de larga duración, como una a la [API de streaming de Twitter](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data).

La opción `--stream` se habilita automáticamente cuando los encabezados de la respuesta incluyen `Content-Type: text/event-stream`.

### Ejemplos de uso

Respuesta embellecida en streaming:


```bash


```bash`r`n$ http --stream pie.dev/stream/3


```


Salida transmitida en pequeños fragmentos al estilo de `tail -f`:


```bash

# Envía cada nueva línea (objeto JSON) a otra URL tan pronto como llega desde una API de streaming:

```bash`r`n$ http --stream pie.dev/stream/3 | while read line; do echo "$line" | http pie.dev/post ; done


```


## Sesiones

Por defecto, cada solicitud que realiza HTTPie es completamente independiente de cualquier otra previa al mismo host.

Sin embargo, HTTPie también soporta sesiones persistentes mediante la opción `--session=SESSION_NAME_OR_PATH`.
En una sesión, los [encabezados HTTP](#http-headers) personalizados (excepto los que comienzan con `Content-` o `If-`), la [autenticación](#authentication) y las [cookies](#cookies) (especificadas manualmente o enviadas por el servidor) persisten entre solicitudes al mismo host.


```bash

# Crear una nueva sesión:

```bash`r`n$ http --session=./session.json pie.dev/headers API-Token:123


```



```bash

# Inspeccionar / editar el archivo de sesión generado:
$ cat session.json

```



```bash

# Reutilizar la sesión existente — el encabezado API-Token se establecerá:

```bash`r`n$ http --session=./session.json pie.dev/headers


```


Todos los datos de la sesión, incluidas credenciales, contraseñas solicitadas, datos de cookies y encabezados personalizados, se almacenan en texto plano.
Esto significa que los archivos de sesión también pueden crearse y editarse manualmente en un editor de texto—son archivos JSON regulares.
También significa que pueden ser leídos por cualquier persona que tenga acceso al archivo de sesión.

### Sesiones con nombre

Puedes crear una o más sesiones con nombre por host. Por ejemplo, así es como puedes crear una nueva sesión llamada `user1` para `pie.dev`:


```bash


```bash`r`n$ http --session=user1 -a user1:password pie.dev/get X-Foo:Bar


```


A partir de ahora, puedes referirte a la sesión por su nombre (`user1`).
Cuando decidas usar la sesión nuevamente, toda la autenticación o encabezados HTTP previamente especificados se establecerán automáticamente:


```bash


```bash`r`n$ http --session=user1 pie.dev/get


```


Para crear o reutilizar una sesión diferente, simplemente especifica un nombre distinto:


```bash


```bash`r`n$ http --session=user2 -a user2:password pie.dev/get X-Bar:Foo


```


Los datos de las sesiones con nombre se almacenan en archivos JSON dentro del subdirectorio `sessions` del directorio de [configuración](#config), típicamente en `~/.config/httpie/sessions/<host>/<name>.json` (`%APPDATA%\httpie\sessions\<host>\<name>.json` en Windows).

Si ejecutaste los comandos anteriores en una máquina Unix, deberías poder listar los archivos de sesión generados usando:


```bash

$ ls -l ~/.config/httpie/sessions/pie.dev

```


### Sesiones anónimas

En lugar de darle un nombre, también puedes especificar directamente una ruta a un archivo de sesión.
Esto permite que las sesiones se reutilicen entre múltiples hosts:


```bash

# Crear una sesión:

```bash`r`n$ http --session=/tmp/session.json example.org


```



```bash

# Usar la sesión para hacer una solicitud a otro host:

```bash`r`n$ http --session=/tmp/session.json admin.example.org


```



```bash

# También puedes referirte a una sesión con nombre creada previamente:

```bash`r`n$ http --session=~/.config/httpie/sessions/another.example.org/test.json example.org


```


Al crear sesiones anónimas, recuerda siempre incluir al menos una `/`, incluso si el archivo de sesión está en el directorio actual (es decir, `--session=./session.json` en lugar de solo `--session=session.json`), de lo contrario HTTPie asumirá que es una sesión con nombre.

### Sesión de solo lectura

Para usar el archivo de sesión original sin actualizarlo a partir del intercambio de solicitud/respuesta después de haber sido creado, especifica el nombre de la sesión mediante `--session-read-only=SESSION_NAME_OR_PATH`:


```bash

# Si el archivo de sesión no existe, se crea:

```bash`r`n$ http --session-read-only=./ro-session.json pie.dev/headers Custom-Header:orig-value


```



```bash

# Pero no se actualiza:

```bash`r`n$ http --session-read-only=./ro-session.json pie.dev/headers Custom-Header:new-value


```


### Política de cookies basada en host

Las cookies persistidas en archivos de sesión tienen un campo `domain`. Esto las _vincula_ a un nombre de host específico. Por ejemplo:


```json

{
    "cookies": [
        {
            "domain": "pie.dev",
            "name": "pie",
            "value": "apple"
        },
        {
            "domain": "httpbin.org",
            "name": "bin",
            "value": "http"
        }
    ]
}

```


Usando este archivo de sesión, incluimos `Cookie: pie=apple` solo en solicitudes contra `pie.dev` y sus subdominios (por ejemplo, `foo.pie.dev` o `foo.bar.pie.dev`):


```bash


```bash`r`n$ http --session=./session.json pie.dev/cookies


```



```json

{
    "cookies": {
        "pie": "apple"
    }
}

```


Para hacer que el dominio de una cookie sea _no vinculado_ (es decir, que esté disponible para todos los hosts, incluso a través de una cadena de redirección entre dominios), puedes establecer el campo `domain` en `null` en el archivo de sesión:


```json

{
    "cookies": [
        {
            "domain": null,
            "name": "unbound-cookie",
            "value": "send-me-to-any-host"
        }
    ]
}

```



```bash


```bash`r`n$ http --session=./session.json pie.dev/cookies


```



```json

{
    "cookies": {
        "unbound-cookie": "send-me-to-any-host"
    }
}

```



### Comportamiento de almacenamiento de cookies

Existen tres posibles fuentes de cookies persistidas dentro de una sesión. Tienen la siguiente prioridad de almacenamiento: 1—respuesta; 2—línea de comandos; 3—archivo de sesión.

1. Recibir una respuesta con un encabezado `Set-Cookie`:


    ```bash

    $ http --session=./session.json pie.dev/cookie/set?foo=bar

    ```


2. Enviar una cookie especificada en la línea de comandos como se muestra en [cookies](#cookies):


    ```bash

    $ http --session=./session.json pie.dev/headers Cookie:foo=bar

    ```


3. Establecer manualmente los parámetros de la cookie en el archivo de sesión:


    ```json

    {
       "cookies": {
           "foo": {
               "expires": null,
               "path": "/",
               "secure": false,
               "value": "bar"
               }
       }
    }

    ```


En resumen:


- Las cookies establecidas mediante la CLI sobrescriben las cookies con el mismo nombre dentro de los archivos de sesión.


- Las cookies enviadas por el servidor a través del encabezado `Set-Cookie` sobrescriben cualquier cookie preexistente con el mismo nombre.


Manejo de expiración de cookies:


- Cuando el servidor expira una cookie existente, HTTPie la elimina del archivo de sesión.


- Cuando una cookie en un archivo de sesión expira, HTTPie la elimina antes de enviar una nueva solicitud.


### Actualización de sesiones

HTTPie puede introducir cambios en el formato del archivo de sesión. Cuando HTTPie detecta un formato obsoleto, muestra una advertencia. Puedes actualizar tus archivos de sesión usando los siguientes comandos:

Actualiza todas las [sesiones con nombre](#sesiones-con-nombre) existentes dentro de la subcarpeta `sessions` de tu [directorio de configuración](https://httpie.io/docs/cli/config-file-directory):


```bash


```bash`r`n$ httpie cli sessions upgrade-all

Upgraded 'api_auth' @ 'pie.dev' to v3.1.0
Upgraded 'login_cookies' @ 'httpie.io' to v3.1.0

```


Para actualizar sesiones individuales, debes especificar el nombre de host de la sesión. Esto permite que HTTPie encuentre el archivo correcto en el caso de sesiones con nombre. Además, permite vincular correctamente las cookies al actualizar con [`--bind-cookies`](#session-upgrade-options).

Actualiza una sola [sesión con nombre](#sesiones-con-nombre):


```bash


```bash`r`n$ httpie cli sessions upgrade pie.dev api_auth

Upgraded 'api_auth' @ 'pie.dev' to v3.1.0

```


Actualiza una sola [sesión anónima](#sesiones-anonimas) usando una ruta de archivo:


```bash


```bash`r`n$ httpie cli sessions upgrade pie.dev ./session.json

Upgraded 'session.json' @ 'pie.dev' to v3.1.0

```


#### Opciones de actualización de sesión

Estos flags están disponibles tanto para `sessions upgrade` como para `sessions upgrade-all`:

| Opción            | Descripción                                                                                                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--bind-cookies`  | Vincula todas las [cookies no vinculadas](#host-based-cookie-policy) previamente a el host de la sesión ([contexto](https://github.com/httpie/cli/security/advisories/GHSA-9w4w-cpc8-h2fq)). |


## Configuración

HTTPie utiliza un archivo simple `config.json`.
El archivo no existe por defecto, pero puedes crearlo manualmente.

### Directorio del archivo de configuración

Para ver la ubicación exacta para tu instalación, ejecuta `http --debug` y busca `config_dir` en la salida.

La ubicación predeterminada del archivo de configuración en la mayoría de las plataformas es `$XDG_CONFIG_HOME/httpie/config.json` (por defecto `~/.config/httpie/config.json`).

Por compatibilidad con versiones anteriores, si existe el directorio `~/.httpie`, se usará el archivo de configuración allí.

En Windows, el archivo de configuración se encuentra en `%APPDATA%\httpie\config.json`.

El directorio de configuración puede cambiarse estableciendo la variable de entorno `$HTTPIE_CONFIG_DIR`:


```bash

$ export HTTPIE_CONFIG_DIR=/tmp/httpie

```bash`r`n$ http pie.dev/get


```


### Opciones configurables

Actualmente, HTTPie ofrece una sola opción configurable:

#### `default_options`

Un `Array` (por defecto vacío) de opciones predeterminadas que deben aplicarse a cada invocación de HTTPie.

Por ejemplo, puedes usar esta opción de configuración para cambiar tu tema de color predeterminado:


```bash

$ cat ~/.config/httpie/config.json

```



```json

{
    "default_options": [
        "--style=fruity"
    ]
}

```


Técnicamente, es posible incluir cualquier opción de HTTPie allí.
Sin embargo, no se recomienda modificar el comportamiento predeterminado de una manera que rompa la compatibilidad con el resto del mundo, ya que podría resultar confuso.

#### `plugins_dir`

El directorio donde se instalarán los plugins. HTTPie necesita tener acceso de lectura/escritura en ese directorio, ya que
`httpie cli plugins install` descargará nuevos plugins allí. Consulta [plugin manager](#plugin-manager) para más información.

### Desactivar opciones previamente especificadas

Las opciones predeterminadas del archivo de configuración, o especificadas de cualquier otra manera, pueden desactivarse para una invocación particular mediante argumentos `--no-OPTION` pasados por la línea de comandos (por ejemplo, `--no-style` o `--no-session`).

## Scripting

Cuando uses HTTPie desde scripts de shell, puede ser útil establecer el flag `--check-status`.
Esto le indica a HTTPie que salga con un error si el estado HTTP es uno de `3xx`, `4xx` o `5xx`.
El código de salida será `3` (a menos que se use `--follow`), `4` o `5`, respectivamente.


```bash

#!/bin/bash

if http --check-status --ignore-stdin --timeout=2.5 HEAD pie.dev/get &> /dev/null; then
    echo 'OK!'
else
    case $? in
        2) echo '¡La solicitud excedió el tiempo de espera!' ;;
        3) echo '¡Redirección HTTP 3xx inesperada!' ;;
        4) echo '¡Error HTTP 4xx del cliente!' ;;
        5) echo '¡Error HTTP 5xx del servidor!' ;;
        6) echo '¡Se excedió el número de redirecciones --max-redirects=<n>!' ;;
        *) echo '¡Otro error!' ;;
    esac
fi

```


### Buenas prácticas

El comportamiento predeterminado de leer automáticamente desde `stdin` normalmente no es deseable durante invocaciones no interactivas.
Lo más probable es que quieras usar la opción `--ignore-stdin` para desactivarlo.

Es importante notar que, sin la opción `--ignore-stdin`, HTTPie puede parecer que ha dejado de funcionar (se queda esperando). Esto sucede porque, en situaciones donde HTTPie se invoca fuera de una sesión interactiva, como desde un trabajo de cron, `stdin` no está conectado a una terminal. Esto significa que se seguirán las reglas para la [entrada redirigida](#redirected-input). Cuando `stdin` está redirigido, HTTPie asume que la entrada contendrá el cuerpo de la solicitud y espera a que se proporcione la entrada. Pero, como no hay datos de entrada ni una señal de fin de archivo (`EOF`), HTTPie se queda esperando. Para evitar este problema, se debe usar el flag `--ignore-stdin` en los scripts, a menos que se estén canalizando datos hacia HTTPie.

Para evitar que tu programa quede sin respuesta cuando el servidor no responde, es recomendable usar la opción `--timeout` para establecer un límite de tiempo de espera de conexión.

## Gestor de plugins

HTTPie ofrece extensibilidad a través de una [API de plugins](https://github.com/httpie/cli/blob/master/httpie/plugins/base.py),
¡y hay docenas de plugins disponibles para probar!
Estos agregan cosas como nuevos métodos de autenticación ([akamai/httpie-edgegrid](https://github.com/akamai/httpie-edgegrid)),
mecanismos de transporte ([httpie/httpie-unixsocket](https://github.com/httpie/httpie-unixsocket)),
convertidores de mensajes ([banteg/httpie-image](https://github.com/banteg/httpie-image)), o simplemente
cambian cómo se formatea una respuesta.

> Nota: Los plugins suelen ser creados por miembros de la comunidad y, por lo tanto, no tienen relación directa con
> el proyecto HTTPie. No los controlamos ni revisamos actualmente, así que úsalos bajo tu propio criterio.

Para gestionar estos plugins, a partir de la versión 3.0, ofrecemos un nuevo gestor de plugins.

Este comando está actualmente en beta.

### `httpie cli`

#### `httpie cli check-updates`

Puedes comprobar si hay una nueva actualización disponible para tu sistema ejecutando `httpie cli check-updates`:


```bash-termible


```bash`r`n$ httpie cli check-updates


```


#### `httpie cli export-args`

El comando `httpie cli export-args` puede exponer la especificación del parser de los comandos `http`/`https`
(como una definición de API) para que herramientas externas puedan usarla y construir mejores interacciones
sobre ellos (por ejemplo, ofrecer autocompletado).

Los formatos disponibles para exportar incluyen:

| Formato | Descripción                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `json`  | Exporta la especificación del parser en formato JSON. El esquema incluye un parámetro de nivel superior `version` que debe interpretarse según [semver](https://semver.org/). |

Puedes usar cualquiera de estos formatos con el parámetro `--format`, pero el predeterminado es `json`.


```bash


```bash`r`n$ httpie cli export-args | jq '"Program: " + .spec.name + ", Version: " +  .version'

"Program: http, Version: 0.0.1a0"

```


#### `httpie cli plugins`

La interfaz `plugins` es un gestor de plugins muy simple para instalar, listar y desinstalar plugins de HTTPie.

En el pasado se usaba `pip` para instalar/desinstalar plugins, pero en algunos entornos (por ejemplo, paquetes instalados con brew) no funcionaba correctamente. La nueva interfaz es una superposición muy simple sobre `pip` que permite la instalación de plugins en cualquier método de instalación.

Por defecto, los plugins (y sus dependencias faltantes) se almacenarán bajo el directorio de configuración,
pero esto puede modificarse mediante la variable `plugins_dir` en la configuración.

##### `httpie cli plugins install`

Para instalar plugins desde [PyPI](https://pypi.org/) o desde rutas locales, se puede usar `httpie cli plugins install`.


```bash


```bash`r`n$ httpie cli plugins install httpie-plugin

Installing httpie-plugin...
Successfully installed httpie-plugin-1.0.2

```


> Consejo: Generalmente los plugins de HTTPie comienzan con el prefijo `httpie-`. Intenta buscarlo en [PyPI](https://pypi.org/search/?q=httpie-)
> para encontrar todos los plugins de la comunidad.

##### `httpie cli plugins list`

Lista todos los plugins instalados.


```bash


```bash`r`n$ httpie cli plugins list

httpie_plugin (1.0.2)
    httpie_plugin (httpie.plugins.auth.v1)
httpie_plugin_2 (1.0.6)
    httpie_plugin_2 (httpie.plugins.auth.v1)
httpie_converter (1.0.0)
    httpie_iterm_converter (httpie.plugins.converter.v1)
    httpie_konsole_konverter (httpie.plugins.converter.v1)

```


##### `httpie cli plugins upgrade`

Para actualizar plugins ya instalados, usa `httpie plugins upgrade`.


```bash


```bash`r`n$ httpie cli plugins upgrade httpie-plugin


```


##### `httpie cli plugins uninstall`

Desinstala plugins del directorio aislado de plugins. Si el plugin no fue instalado
a través de `httpie cli plugins install`, no lo desinstalará.


```bash


```bash`r`n$ httpie cli plugins uninstall httpie-plugin


```


## Meta

### Diseño de la interfaz

La sintaxis de los argumentos del comando corresponde estrechamente a las solicitudes HTTP reales enviadas por la red.
Esto tiene la ventaja de que es fácil de recordar y leer.
A menudo puedes traducir una solicitud HTTP a una lista de argumentos de HTTPie simplemente colocando en línea los elementos de la solicitud.
Por ejemplo, compara esta solicitud HTTP:


```http

POST /post HTTP/1.1
Host: pie.dev
X-API-Key: 123
User-Agent: Bacon/1.0
Content-Type: application/x-www-form-urlencoded

name=value&name2=value2

```


con el comando HTTPie que la envía:


```bash


```bash`r`n$ http -f POST pie.dev/post \

    X-API-Key:123 \
    User-Agent:Bacon/1.0 \
    name=value \
    name2=value2

```


Observa que tanto el orden de los elementos como la sintaxis son muy similares, y que solo una pequeña parte del comando se utiliza para controlar HTTPie y no corresponde directamente a ninguna parte de la solicitud (aquí, solo `-f` le indica a HTTPie que envíe una solicitud de formulario).

Los dos modos, `--pretty=all` (predeterminado para terminal) y `--pretty=none` (predeterminado para [salida redirigida](#redirected-output)), permiten tanto un uso interactivo y amigable para el usuario como el uso desde scripts, donde HTTPie funciona como un cliente HTTP genérico.

En el futuro, la sintaxis de la línea de comandos y algunas de las `--OPTIONS` pueden cambiar ligeramente, a medida que HTTPie mejora y se agregan nuevas funciones.
Todos los cambios se registran en el [registro de cambios](#change-log).

### Comunidad y soporte

HTTPie cuenta con los siguientes canales comunitarios:


- [GitHub Issues](https://github.com/httpie/cli/issues) para reportar errores y solicitar nuevas funciones


- [Servidor de Discord](https://httpie.io/discord) para hacer preguntas, discutir características y conversar sobre desarrollo de APIs en general


- [StackOverflow](https://stackoverflow.com) para hacer preguntas (asegúrate de usar la etiqueta [httpie](https://stackoverflow.com/questions/tagged/httpie))


### Proyectos relacionados

#### Dependencias

Internamente, HTTPie utiliza estas dos increíbles bibliotecas:


- [Requests](https://requests.readthedocs.io/en/latest/) — biblioteca HTTP de Python para humanos


- [Pygments](https://pygments.org/) — resaltador de sintaxis para Python


#### Amigos de HTTPie

HTTPie funciona excepcionalmente bien con las siguientes herramientas:


- [http-prompt](https://github.com/httpie/http-prompt) — una shell interactiva para HTTPie con autocompletado y resaltado de sintaxis de comandos


- [jq](https://stedolan.github.io/jq/) — procesador de JSON en la línea de comandos que funciona muy bien junto con HTTPie


Ayudantes para convertir desde otras herramientas de cliente:


- [CurliPie](https://curlipie.open-api.vn) — biblioteca para convertir comandos cURL a HTTPie


#### Alternativas


- [httpcat](https://github.com/httpie/httpcat) — una utilidad hermana de bajo nivel de HTTPie para construir solicitudes HTTP sin procesar desde la línea de comandos


- [curl](https://curl.haxx.se) — una herramienta de línea de comandos "navaja suiza" y una biblioteca excepcional para transferir datos mediante URLs.


### Contribuir

Consulta [CONTRIBUTING](https://github.com/httpie/cli/blob/master/CONTRIBUTING.md).

### Política de seguridad

Consulta [github.com/httpie/cli/security/policy](https://github.com/httpie/cli/security/policy).

### Registro de cambios

Consulta el [REGISTRO DE CAMBIOS](https://github.com/httpie/cli/blob/master/CHANGELOG.md).

### Arte


- [Animación del README](https://github.com/httpie/cli/blob/master/docs/httpie-animation.gif) por [Allen Smith](https://github.com/loranallensmith).


### Licencia

BSD-3-Clause: [LICENSE](https://github.com/httpie/cli/blob/master/LICENSE).

### Autores

[Jakub Roztocil](https://roztocil.co) ([@jakubroztocil](https://twitter.com/jakubroztocil)) creó HTTPie y [these fine people](https://github.com/httpie/cli/blob/master/AUTHORS.md) han contribuido.
