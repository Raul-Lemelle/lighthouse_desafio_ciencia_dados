# Contribuindo para o Projeto IMDb

Obrigado por considerar contribuir para o projeto IMDb! Este documento é um guia para ajudá-lo a começar.

## Como Contribuir

![Workflow de Contribuição](https://github.com/Raul-Lemelle/data/blob/main/docs/workflow_contri.jpg)


1. **Fork do Repositório**
   - Faça um fork deste repositório no GitHub para sua própria conta.

2. **Clone o Repositório**
   - Clone o repositório forkado para o seu ambiente local:
     ```bash
     git clone https://github.com/seu-usuario/imdb-project.git
     cd imdb-project
     ```

3. **Instale as Dependências**
   - Certifique-se de ter Python 3 instalado. Use um ambiente virtual se preferir:
     ```bash
     python -m venv venv
     source venv/bin/activate   # No Windows use 'venv\Scripts\activate'
     ```
   - Instale as dependências do projeto:
     ```bash
     pip install -r requirements.txt
     ```

4. **Desenvolvimento**
   - Faça suas alterações ou adições no código, scripts, ou notebooks de acordo com o que deseja contribuir.

5. **Teste**
   - Execute os testes locais para garantir que suas alterações não quebrem o código existente:
     ```bash
     pytest
     ```

6. **Envie suas Alterações**
   - Commit suas alterações e envie para seu repositório forkado:
     ```bash
     git add .
     git commit -m "Descrição concisa das alterações"
     git push origin master
     ```

7. **Abra um Pull Request**
   - Vá para o repositório no GitHub e abra um Pull Request (PR) com uma descrição clara do que foi feito nas suas alterações.

## Orientações Adicionais

- **Informações de Contato**
  - Para dúvidas ou discussões sobre o projeto, utilize as issues do GitHub.

- **Código de Conduta**
  - Este projeto segue o [Código de Conduta do Contribuidor](CODE_OF_CONDUCT.md). Ao participar deste projeto, você concorda em seguir suas diretrizes.

Obrigado por contribuir para o projeto IMDb! Sua participação é valiosa para nós.
