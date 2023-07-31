# IFome

Essa é uma de três apis que compõem o Ifome juntas realizam parte do comportamento de um aplicativo de entrega de 
comida online.

Com arquitetura em camadas, segue os princípios do SOLID.

Um de seus objetivos é mostrar como serviços diferentes pode se comunicar de forma resiliente por meio de mensageria.

Isso permite, por exemplo, a atualização do status do aplicativo em tempo real sem que seja preciso solicitar ao 
servidor que envie o novo status do pedido

## 🚀 Começando

Esse projeto é um microsserviço chamado ifome-client, é responsável por tudo que é relativo ao usuário que vai efetuar a 
compra, ou seja, os clientes (client) da loja. 

A seguir o link para download de todos os microsserviços e a documentação de consumo das apis

* [ifome-client](https://github.com/GuilhermeJimenes/ifome-client)
* [ifome-deliveryman](https://github.com/GuilhermeJimenes/ifome-deliveryman)
* [ifome-enterprise](https://github.com/GuilhermeJimenes/ifome-enterprise)
* [Documentação](https://documenter.getpostman.com/view/12799226/2s9XxtxFaQ#intro)

### 📋 Pré-requisitos

Antes de começa precisamos ter o [Python 3.8.10](https://www.python.org/downloads/release/python-3810/) instalado 
e uma ide de sua preferência por exemplo o [Pycharm](https://www.jetbrains.com/pt-br/pycharm/) que é a ide recomenda 
pelo python, também vamos também vamos precisar do [RabbitMQ](https://www.rabbitmq.com/) e do [MySQL](https://dev.mysql.com/doc/)

### 🔧 Instalação

No terminal é preciso baixar as dependências com o seguinte comando:

```
pip install - r requirements.txt
```

Se estiver usando outra ide que não seja o pycharm vai preciso ativar a venv e interpretador manualmente antes de 
rodar o comando a cima, consulte a documentação oficial do python se for o seu caso

## ⚙️ Começando

* Antes de começar a utilizar esse projeto precisamos entender como ele funciona e é bem simples
* Ao rodar o arquivo local.py você inicia o servidor flask, com isso todos os endpoints ficam disponíveis para serem 
consumidos.
* E ao rodar o arquivo index.py você inicia o consumer da fila, que é por onde ocorre a comunicação entre os 
microsserviços do ifome

## 🛠️ Construído com

* [Python 3.8.10](https://www.python.org/downloads/release/python-3810/) - Linguagem usada
* [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/) - O framework web usado
* [RabbitMQ](https://www.rabbitmq.com/) - Message Broker
* [MySQL](https://dev.mysql.com/doc/) - Banco de dados
* [SQLite](https://www.sqlite.org/docs.html) - Banco de dados

## ✒️ Autores

Eu, eu mesmo e eu denovo

* **Guilherme Jimenes** - [meu github](https://github.com/GuilhermeJimenes)

## 📄 Licença

Esse código é livre para você usar como quiser, então se puder dar uma conferida no meu [github](https://github.com/GuilhermeJimenes?tab=repositories) eu seria muito grato


## 🎁 Expressões de gratidão

* Agradeço a todas as empresa e pessoas com quem eu já trabalhei, tudo que eu sei hoje sobre tecnologia é devido aos que estavam comigo todo esse tempo 📢
* Agradeço também a minha coluna que não desistiu de mim todo esse tempo trabalhando sentado ao computador 🤣
* Um agradecimento especial para você que está vendo um pouquinho do meu trabalho 😁

---
⌨️ com ❤️ por [JimenesGM](https://www.linkedin.com/in/guilherme-moraes-jimenes/) 😊