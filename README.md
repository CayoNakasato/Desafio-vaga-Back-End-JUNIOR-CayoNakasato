# Parse seu arquivo CNAB e veja renderizado na tela

Projeto no qual você pode dar upload de um arquivo CNAB e pode vê los em exibição na tela de maneira mais prática de entender cada linha do arquivo. Os dados ficam guardados no banco local SQLite3, e estão resguardados em tabela para melhor vizualização.

## Tecnologias Utilizadas

Neste projeto foram usados as seguintes tecnologias:
  - Python
  - Django
  - SQLite3

## Ao clonar este repositório instale no ambiente virtual(venv):
  #### Para utilizar o venv se estiver utilizando Linux use o comando:
    
        source venv/bin/activate
  #### Para utilizar o venv se estiver utilizando Windows use o comando:
    
        source venv/Scripts/activate
    
  ### Para instalar use o comando:
         pip install -r requirements.txt 
   ##### Dentro do arquivo requirements.txt está todos as denpendências que o projeto necessita para o código rodar normalmente.
 
## Após instalar pode se iniciar o projeto com
   ### Rodando as migrations com
        python manage.py migrate
#### Após rodar as migrations pode iniciar o projeto com:
        python manage.py runserver
