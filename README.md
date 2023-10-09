# Solo As A Service - Backend

Este é o repositório do **Solo As A Service - Backend**, parte do projeto Solo As A Service que fornece sugestões de programas para mulheres que viajam sozinhas. Este README fornecerá uma visão geral do projeto, instruções de instalação e uso, bem como detalhes sobre como contribuir.

## Visão Geral

O **Solo As A Service - Backend** é a parte do projeto que lida com as solicitações de sugestões de programas para mulheres que gostam da sua própria companhia. Ele é construído com o framework FastAPI e fornece uma API simples que retorna uma sugestão de programa aleatória quando solicitada. A API também possui configurações de CORS para permitir solicitações de origens específicas.

## Funcionalidades Principais

- Fornecimento de uma sugestão de programa aleatória para mulheres que viajam sozinhas.
- Configuração de CORS para permitir solicitações de origens específicas.
- Endpoint `/` para uma mensagem de boas-vindas.
- Endpoint `/solo_todo` para obter uma sugestão de programa solo aleatória.

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Framework web assíncrono para construção de APIs rápidas em Python.
- [Pydantic](https://pydantic-docs.helpmanual.io/): Biblioteca para validação de dados e definição de modelos.
- Python: Linguagem de programação utilizada para desenvolver a aplicação.

## Instalação e Uso

Para executar o **Solo As A Service - Backend** localmente, siga estas etapas:

1. Clone o repositório:

```bash
git clone https://github.com/Gabbyroba/Solo-aas.git
```

2. Navegue até o diretório do projeto:

```bash
cd Solo-aas
```

3. Instale as dependências usando o pip:

```bash
pip install fastapi[all]
```

4. Execute o aplicativo com o comando:

```bash
uvicorn main:app --reload
```

Isso iniciará o servidor FastAPI e estará pronto para receber solicitações.

## Uso da API

### Obtenha uma Sugestão de Programa Solo Aleatória

- **Endpoint:** `/solo_todo`
- **Método:** GET
- **Descrição:** Obtém uma sugestão de programa solo aleatória.
- **Exemplo de solicitação:** `https://soloaas.onrender.com/solo_todo`
- **Resposta de Exemplo:**

```json
{
    "program": "Visitar uma exposição de um artista que você gosta."
}
```

### Mensagem de Boas-Vindas

- **Endpoint:** `/`
- **Método:** GET
- **Descrição:** Exibe uma mensagem de boas-vindas.
- **Exemplo de solicitação:** `https://soloaas.onrender.com/`
- **Resposta de Exemplo:** `Boas vindas à API Solo as a Service!`

## Configuração de CORS

A API está configurada para permitir solicitações de origens específicas listadas na variável `origins` no código. Certifique-se de configurar essas origens de acordo com as necessidades do seu projeto.

## Contribuição

Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork deste repositório.

2. Clone o seu fork localmente:

```bash
git clone https://github.com/seu-usuario/Solo-aas.git
```

3. Crie uma branch para sua contribuição:

```bash
git checkout -b minha-contribuicao
```

4. Faça as alterações desejadas e adicione, comite e envie suas alterações:

```bash
git add .
git commit -m "Minha contribuição"
git push origin minha-contribuicao
```

5. Abra um pull request neste repositório. Sua contribuição será revisada e mesclada após aprovação.

## Autoria

Este projeto foi desenvolvido por [Gabbyroba](https://github.com/Gabbyroba).
