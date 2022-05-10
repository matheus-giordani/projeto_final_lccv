# Backlog
> Portal de gerencimento de bens.


Esse backlog é responsavel pelo crud de notas fiscais, bens, despesas, fornecedores e fazendo o gerencimante das ligações entre cada item citado.


## :closed_book: back-end

![](https://github.com/matheus-giordani/projeto_final_lccv/blob/main/control.png)

## Modelo ER
![](https://github.com/matheus-giordani/projeto_final_lccv/blob/main/DER%20-%20Patrim%C3%B4nio_page-0001.jpg)

### Instalação

```sh
docker compose build
```
```sh
docker compose up
```

## :pushpin: Exemplo de uso

com esse back-end é possivel realizar todas a funções de post, get e afins de cada tabela criada 

## :red_circle: dificuldades encontradas
 
por ser um ambiente de desenvolvimento novo tive varias dificulades voltas a criação e mautenção do banco de dados atraves do django e 
não obstante a esse primeiro problema a configuração do django foi custosa tambem

## :closed_book: front-end

![](https://github.com/matheus-giordani/projeto_final_lccv/blob/main/portal_teste.png)

### startando aplicação

```sh
 ng serve
```

## :pushpin: Exemplo de uso

usado para interação com usuario

## :red_circle: dificuldades encontradas
 
tudo no desenvolvimento com o angular demandou muito esforço para ser feito.Tive muita dificuldade com a dinamica de modulos, serviços e exports.
nessa aplicação só há a integração com a API do django para listar os bens cadastrados pelo backend não consegui implementar o cadastro de edição e exclução pelo
portal 





## :telephone_receiver: informações pessoais

Matheus Giordani – [@giordani_matheus](https://www.instagram.com/giordani_matheus/) – matheus.giordanioliveira@gmail.com



## Contributing

1. Faça o _fork_ do projeto (<https://github.com/matheus-giordani/projeto_final_lccv/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_


