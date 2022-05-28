# desafio-4linux

API para gerencialmento de salas de aula desenvolvida como resposta a um desafio da 4Linux

## Executando o projeto localmente

1. Abra o CMD ou Terminal, clone o repositório e acesse a pasta do projeto

   ```bash
   git clone https://github.com/br-adriel/desafio-4linux.git

   cd desafio-4linux
   ```

2. Crie e ative o ambiente virtual python

   ```bash
   # windows
   py -m venv .venv
   .venv\Scripts\activate

   # linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale os pacotes necessários para execução

   ```bash
   pip install -r requirements.txt
   ```

4. Faça uma cópia do arquivo `.env.example` e o renomeie para `.env`

5. Execute o comando abaixo para gerar uma chave de criptografia para o Django

   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

6. Copie a chave gerada e cole no arquivo `.env` no campo SECRET_KEY:

   ```bash
   SECRET_KEY=chave_gerada_no_passo_anterior
   ```

7. Caso queira executar o projeto em modo debug, altere o valor de `DEBUG` do
   arquivo `.env` para `True`

8. Execute as migracoes e inicie o servidor

   ```bash
   # windows
   py manage.py migrate
   py manage.py runserver

   # linux
   python3 manage.py migrate
   python3 manage.py runserver
   ```

9. Acesse o endereco `localhost:8000/api/salas`
