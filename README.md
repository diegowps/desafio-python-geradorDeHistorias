# desafio-python-geradorDeHistorias
O desafio da turma EducafroTech é usar a biblioteca Random e criatividade para criar um gerador de histórias.


# Gerador de Histórias Python

Projeto simples e divertido para gerar histórias curtas e aleatórias, com diferentes temas e personagens. Ideal para praticar Python e mostrar criatividade!

## O que o projeto faz?
Gera histórias únicas a cada execução, combinando elementos aleatórios de temas como fantasia, ficção científica e mistério. O usuário escolhe o tema e recebe uma história pronta.

## Como usar
1. **Pré-requisitos:**
   - Python 3 instalado
2. **Execução rápida:**
   - Pelo terminal, execute:
     ```bash
     python script.py
     ```
   - Escolha entre gerar uma história ou rodar os testes automáticos.
3. **Gerar história diretamente:**
   - Execute:
     ```bash
     python gerador_historia.py
     ```
   - Escolha o tema e veja sua história.
4. **Rodar testes:**
   - Execute:
     ```bash
     python -m unittest test_gerador_historia.py
     ```

## Estrutura do projeto
- `gerador_historia.py`: Script principal, gera histórias e interage com o usuário.
- `test_gerador_historia.py`: Testes automáticos para garantir funcionamento.
- `script.py`: Menu para rodar o gerador ou os testes.
- `README.md`: Documentação do projeto.

## Tecnologias utilizadas
- Python 3
- Biblioteca padrão (random, unittest)

## Próximos passos e ideias de melhoria
- Interface gráfica com Tkinter ou PySimpleGUI
  - Já implementado: execute `python gerador_historia_gui.py` para usar a interface gráfica.
- Salvar histórias geradas em arquivos .txt
  - Sugestão: Adicione um botão ou opção para salvar a história exibida em um arquivo texto, usando `open('historias.txt', 'a')` e `write()`.
- Usar APIs para palavras aleatórias
  - Sugestão: Utilize APIs como Wordnik ou Datamuse para buscar palavras aleatórias e enriquecer as listas de elementos.
- Reestruturar usando classes e objetos
  - Sugestão: Crie classes como `Historia`, `Personagem`, `Tema` para organizar o código e facilitar expansões.
- Adicionar novos temas e elementos
  - Sugestão: Expanda o dicionário TEMAS com temas como aventura, terror, comédia, e adicione mais opções nas listas de personagens, lugares, ações, objetos e desfechos.

## Comentários e aprendizado
O código está comentado para facilitar o entendimento, ideal para quem está começando ou quer mostrar domínio de boas práticas no portfólio.

---

**Divirta-se criando histórias e evoluindo seu Python!**

