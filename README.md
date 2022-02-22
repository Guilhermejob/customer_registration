## Instalação

- Primeiro faça o fork deste [repositório](https://github.com/Guilhermejob/customer_registration).

- Em seguida faça um git clone para a sua maquina

- Crie o ambiente um ambiente [virtual em python](https://docs.python.org/pt-br/3/tutorial/venv.html)

```
$ python -m venv venv --upgrade-deps
```

- Entre no ambiente virtual

```
$ source venv/bin/activate
```

- Instale as dependencias no arquivo `requirements.txt`

```
$ pip install -r requirements.txt
```

- Configure suas variáveis segundo o arquivo `.env.example`

  - Não esqueça de criar o seu banco de dados e adicionar no .env

- Crie as tabelas no banco de dados através do comando

```
$ flask db upgrade
```

- Inicie a aplicação local através do comando

```
$ flask run
```

- A aplicação inicializará na rota http://127.0.0.1:5000/. Você deverá ver algo semelhante ao snippet logo abaixo no seu terminal:

```
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 112-925-941
```


## Após rodar a sua aplicação todas as requisiçõs podem ser feitas com base nos dois links abaixo
### URL Base deploy no heroku: https://customer-registration-test.herokuapp.com
### URL Base local : http://127.0.0.1:5000/

#

## Requisições

## Registro de cliente
- ### Post /customer

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/155180148-63a2b37c-1c40-4241-83da-5bff9eeb39c3.png" width="1000px" />
</div>

#

## Login de cliente
- ### Post /login


<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/155180881-cf6a6f16-a397-41a5-a7c4-21e03e59e1fc.png" width="1000px" />
</div>

#

## Listagem de todos os clientes
- ### Get /customer


<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/155181377-e0d06460-46d9-4f9a-a354-7f325cf1bf0f.png" width="1000px" />
</div>


> #### OBS : Para esta requisição você precisar se autenticar passando o token que obteu na rota de login nos headers da requisição desta forma 

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/155182032-f0168114-d912-48e2-876a-dfc2adee7be7.png" width="700px" />
</div>

#

## Está aplicação foi feita com finalidade de reforcar conhecimentos já obtidos, quaisquer dúvidas ou caso tenha vontade de trocar uma idéia comigo segue o link do meu linkedin

https://www.linkedin.com/in/guilherme-armesto-job/









