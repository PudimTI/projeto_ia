# Projeto final IA

### Trabalho de conclusão da diciplina de Inteligencia Artificial

## Minecraft AI Assistant

Projeto de assistente virtual especializado em Minecraft, pronto para oferecer dicas, curiosidades, receitas e informações sobre mobs de forma amigável.

## Instalação
- Garanta que você possui Python 3.10+ instalado.
- Crie e ative um ambiente virtual.
- Instale as dependências com `pip install -r requirements.txt`.

## Execução

### Interface de Linha de Comando
- Configure as variáveis de ambiente conforme indicado abaixo.
- Inicie a aplicação com `python main.py`.

### Interface Web (Django)
- Configure as variáveis de ambiente conforme indicado abaixo.
- Execute as migrações: `python manage.py migrate`
- Inicie o servidor: `python manage.py runserver`
- Acesse `http://127.0.0.1:8000` no seu navegador

## Configuração da OpenAI
- Renomeie `.env.example` para `.env`.
- Informe o valor de `OPENAI_API_KEY` com a sua chave da OpenAI.
- Durante a execução, o script carregará automaticamente as variáveis definidas no `.env`.

