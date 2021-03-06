# Sala de Estudos Flask API

This is a backend API for 
[saladeestudos_COMP_UFF](https://github.com/GuilhermeSnts/saladeestudos_COMP_UFF).

It provides infos about **professors**, **subjects**, **lessons**
 and more for students of Tecnologia em Sistemas de Computação course of 
 Universidade Federal Fluminense.
 
## Installation
### Development mode

### Requirements

This Flask application requires a PostrgreSQL database running. 
 You can set the parameters to access the database in .secrets.toml
 and use .secrets.toml.example as example.
 
---  

For development mode it's recommended to use a virtual environment. 
Try to follow this tutorial on [realpython.com/intro-to-pyenv/
](https://realpython.com/intro-to-pyenv/).

Install [poetry](https://python-poetry.org/docs/cli/) to manage 
dependencies:

```shell script
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
``` 
You can use poetry [to manage virtual environments too](https://python-poetry.org/docs/managing-environments/).

Since you have a virtual environment installed, you can install
 this application for development using a single command:
 
```shell script
$ make install-dev
```

Update the database.

```shell script
$ flask db upgrade
```

Now you can run this application in development mode.
```shell script
$ make run-dev
```


## Usage

### Subjects

* `/api/v1/subjects/`
    
    Returns a list of all subjects on the database
    
    ```json
    [  
      {
        "code": "ead05006", 
        "id": 1, 
        "material_design_icon": null, 
        "name": "Álgebra Lienar"
      }, 
      {
        "code": "ead05018", 
        "id": 2, 
        "material_design_icon": null, 
        "name": "Análise de Sistemas"
      },
      ...
    ]
    ```
 
 * `/api/v1/subject/<id>/`

    Returns data referent for a subjects
    
    ```json
    {
      "amount_lessons": 15, 
      "code": "ead05006", 
      "drive_link": null, 
      "github_link": null, 
      "id": 1, 
      "name": "Álgebra Lienar", 
      "type": "OBRIGATÓRIA", 
      "workload": 80
    }
    ```
 
 * `/api/v1/subject/<subject_id>/lessons`
 
    Returns a list of lessons
    
    ```json
    [
      {
        "id": 1, 
        "lesson_index": "Aula 001", 
        "thumbnail": "http://va05-idc.rnp.br/riotransfer/cederj/sistemas_comp/ead05006/Aula_001/Aula_001_t.png", 
        "title": "Vetores"
      }, 
      {
        "id": 2, 
        "lesson_index": "Aula 002", 
        "thumbnail": "http://va05-idc.rnp.br/riotransfer/cederj/sistemas_comp/ead05006/Aula_002/02.png", 
        "title": "Espaços vetoriais"
      },
      ...
    ]
    ```