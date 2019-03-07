# Backend no Grupo Rovema
Somos uma empresa que atua em vários segmentos de mercado, com diferentes tecnologias, culturas e desafios. Por isso, gostamos de compor nossos times com profissionais multidisciplinares, que tenham alta capacidade de aprendizado, sejam detalhistas, resiliêntes, questionadores e curiosos. Você, como **Backend Developer**, será o responsável por implementar, dar manutenção, aplicar correções e propor soluções em arquiteturas de **microsserviços** e **RESTFul API**, baseadas em **Containers Docker** sempre buscando a melhor composição de tecnologias para cada cenário.

## Objetivo do desafio
O desafio para **Backend Developer**, tem o objetivo de analisar como você constrói uma **RESTFul API** e como a sua estrutura de aplicações pode ser **escalável** e **maleável as mudanças de escopo**.

## Orientações
Para executar o desafio de **Backend Developer**, você **poderá utilizar qualquer liguagem de programação, framework ou biblioteca e banco de dados** que for **confortável para você**, seguindo o [passo-a-passo](https://github.com/rovema/Backend-test#etapas) para a execução, atendendo aos [critérios de aceitação](https://github.com/rovema/Backend-test#crit%C3%A9rios-de-aceita%C3%A7%C3%A3o). 

## Desafio
Você é o responsável por construir uma **RESTFul API** que seja capaz de efetuar o **CRUD** de **produtos** e **categorias**. O produto deve conter obrigatoriamente os campos *id*, *nome* e *preço* e a categoria deve conter *id* e *nome*. Cada produto, pode estar relacionado a várias categorias e este não pode estar relacionado a mesma categoria mais de uma vez, bem como, cada categoria pode estar relacionada a vários produtos. A implementação deve iniciar com apenas o CRUD de produtos, **sem relação ao CRUD de categorias** e então, deve ser implementado o **CRUD de categorias após implementado o CRUD de produtos**.

É imprescindível que o **CRUD de categorias** seja implementado após o **CRUD de produtos**, pois analisaremos como você **executa e automatiza** as alterações na sua **base de dados**. 

**Dica:** Utilize **Migrations**.

## Etapas

#### 1 - Fazer um fork desse repositório
![https://i.imgur.com/HoIHtPU.png](https://i.imgur.com/HoIHtPU.png)


#### 2 - Criar um branch com o seu primeiro e último nome
```bash
git checkout -b joao-silva
```

#### 3 - Escreva a documentação da sua aplicação
Crie uma pasta na raíz da aplicação chamada **docs/** contendo o a **modelagem entidade-relacionamento** (em imagem ou pdf) da sua aplicação. Você deve também, substituir o conteúdo do arquivo **README.md** e escrever a documentação da sua aplicação, com os seguintes tópicos: 
- **Projeto**: Descreva o projeto e como você o executou. Seja objetivo.
- **Tecnologias**: Descreva quais tecnologias foram utilizadas, enumerando versões (se necessário) e os links para suas documentações, bem como, qual guia de estilos de código você utilizou com o link para a sua documentação.
- **Como rodar**: Descreva como iniciar a sua aplicação, utilizando **Docker** e **Docker Compose**.

**Observações:** Escreva a documentação em formato [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

#### 4 - Faça uma Pull Request
Após implementada a solução, crie uma [pull request](https://github.com/rovema/Backend-test/pulls) com o seu projeto para esse repositório.


## Critérios de Aceitação
Para que seu teste tenha o mínimo necessário que atenda aos requisitos esperados, ele deve:
- Atender ao que foi proposto no [Desafio](https://github.com/rovema/Backend-test#Desafio).
- Ter documentação de aplicação e modelos de banco de dados.
- Utilize o paradigma de orientação a objetos.
- Sua RESTFul API deve se comunicar em JSON e apenas nele.
- Utilize corretamente os códigos de retorno HTTP. Gostamos [dessa abordagem](https://developer.amazon.com/docs/amazon-drive/ad-restful-api-response-codes.html).
- Manter uma estrutura de aplicação concisa e coerente. (Simples é melhor que complexo)
- Sua aplicação e banco de dados devem conter uma implementação como container Docker.
- Código escrito com base em algum padrão de convenções (style guide) da linguagem que está utilizando. Ex: Em Python, temos o [pep8](https://www.python.org/dev/peps/pep-0008/), em PHP temos a [PSR2](https://www.php-fig.org/psr/psr-2/), em JavaScript temos [AirBnB Standards](https://github.com/airbnb/javascript) e o [Javascript Standards](https://standardjs.com/), etc.
- Utilizar padrões semânticos em mensagens de commit. (Gostamos do padrão de commits do repositório [AngularJS](http://karma-runner.github.io/3.0/dev/git-commit-msg.html))


## Dicas e Informações Valiosas

#### O que gostaríamos de ver em seu teste:
- Testar ele localmente com docker e validar os endpoints.
- Se possível, que seu teste estivesse hospedado em algum lugar. (Gostamos do [Heroku](https://www.heroku.com/)).
- Convenção de nome em classes, objetos, variáveis, métodos e etc.
- Um planejamento de entrega das tarefas do seu desafio. (Gostamos de [Kanban](https://blog.runrun.it/o-que-e-kanban/)).
- Que sua estrutura de linguagem e tecnologias seja compatível com ambiente Linux.
- Testes unitários.

**Observação:** Nenhum dos itens acima é obrigatório.

#### O que não gostaríamos de ver no seu teste:
- Saber que não foi você quem implementou.
- Processos manuais de inicialização da aplicação e banco de dados.
- Fraco relacionamento entre colunas nas tabelas (falta de Foreign Key e Constraints).
- Falta de organização de código.
- Falta de documentação.
- Histórico de commits desorganizado e despadronizado.
