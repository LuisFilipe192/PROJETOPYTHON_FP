# Manual de uso

## Projeto: “Adoção+” – Sistema de Gestão de Centro de Adoção de Animais

>`Para os interessados em entender como funciona esse crud de adoção de animais, e também entender o jeito certo de como você poderá usa-lo e manuzea-lo`

Existem certas coisas que você como usuário pode fazer nesse programa para usa-lo da melhor maneira, dentre tais é ...

## Menu principal

> Ele irá aparecer assim para você

====== MENU PRINCIPAL ======

1. Adicionar Animal
2. Listar Animais
3. Editar Animal
4. Excluir Animal
5. Registrar Tarefa
6. Listar Tarefas
7. Editar Tarefa
8. Excluir Tarefa
9. Exibir Alertas
10. Mostrar Atrasos
11. Registrar Histórico Médico
12. Listar Histórico Médico
13. Sair

- É recomendado escolher numeros ***Interiros*** entre 1 e 13 como mostrado acima

## 1. Adicionar Animal (Cadastro)

- Você irá inserir as seguintes informações nessa parte

1. Nome
2. Espécie
3. Raça
4. Idade
5. Estado de saúde
6. Comportamento

- Não serão aceitos **numeros** nas seguintes partes

1. Nome❌
2. Espécie❌
3. Raça❌
4. Idade✅
5. Estado de saúde❌
6. Comportamento❌

- Em idade, só é aceito numeros do tipo **inteiro** sendo eles positivos
- Cada animal recebera um ID, gerado de forma automática
- A data de chegada também é gerada de maneira automática a partir do dia em que aconteceu o cadastro
- No final será perguntado se o usuário deseja voltar ao menu

## 2. Listar Animais (Lista dos cadastros)

- Aqui será mostrado todos os animais cadastrados
- Cada animal aparecera com todas as suas respectivas informações de cadastro
- O sistema alertará caso **nada** tenha sido cadastrado
- No final será perguntado se o usuário deseja voltar ao menu

## 3. Editar Animal (Alteração na lista)

- O sistema vai mostar os IDs dos animais cadastrados, junto ao nome e a espécie
- Digite o ID dos animal que você vai querer alterar, caso não digite o ID correto (ou deixe em branco, ou com qualquer tipo de letra), o sistema **Para** e pergunta se o usuário deseja retornar ao menu
- Caso não queira editar alguma linha de informação, apenas pressione Enter
- Caso ocorra alguma alteração nas informações do animal, após o ENTER, as alterações serão salvas automaticamente
- A *idade* ainda exigirá que você insira um numero inteiro positivo
- Caso o usuário digite algo fora dos padrões definidos aparecerá uma mensagem de aviso e será solicidado inserir a informação no formato requerido
- No final será perguntado se o usuário deseja voltar ao menu

## 4. Excluir animal (Deleta da lista)

- Digite o ID do animal que deseja excluir do cadastro, caso não digite o ID, aparecera a seguinte mensagem de aviso **"ID não encontrado. Tente novamente."**
- Após isso aparecerá um menu de ***confirmação***

1. (s) para confirmar✅
2. (n) para cancelar❌

- outros formatos além do (n) e do (s) ***não*** serão aceitos
- Após a exclusão, não é possível recuperar o que foi deletado, tome cuidado para não se arrepender
- No final será perguntado se o usuário deseja voltar ao menu

## 5. Registrar Tarefa (Atribuição do afazer na lista)

- Escolha o animal para atribuir uma tarefa à ser aplicada a ele ***(Isso é feito digitando o ID do animal cadastrado)***
- Será mostrado os animais cadastrados junto ao seu respectivo ID
- Depois selecione o tipo de tarefa (digitando um numero). Irá aparecer um menu assim

1. Vacina
2. Banho
3. Consulta veterinária
4. Treino
5. Outra

- É recomendado escolher numeros ***Interiros*** entre 1 e 5 como mostrado acima
- Informe a data prevista com *dia/mês/ano* e o ***responsável*** pela tarefa
- A data tem que ser obrigatoriamente nesse formato *dia/mês/ano*
- Caso o usuário escolha a opção 5, vai ser possível digitar a informação
- No final será perguntado se o usuário deseja voltar ao menu

## 6. Listar tarefas (Exibe a lista das terefas atribuídas)

- Mostra na tela todas as tarefas registradas até o momento com o:

>- Nome do animal
>- Tipo de tarefa
>- Data prevista
>- Responsável

- Caso não exista nenhuma tarefa o sistema irá avisar
- No final será perguntado se o usuário deseja voltar ao menu

## 7. Editar Tarefa (edição da lista com as tarefas)

- Exibe uma lista com todas as tarefas atribuídas
- Digite o dígito com o número da tarefa que deseja editar
- Você poderá alterar:

>- Data
>- Responsável
>- Tipo de tarefa

- Caso não queira editar, pressione Enter para continuar
- Após o ENTER as alterações são salvas altomaticamente
- No final será perguntado se o usuário deseja voltar ao menu

## 8. Excluir tarefa (deleta uma tarefa da lista)

- Escolha o número da tarefa, para ser excluida
- Após isso aparecerá um menu de ***confirmação***

1. (s) para confirmar✅
2. (n) para cancelar❌

- Outros formatos além do (n) e do (s) ***não*** serão aceitos
- Após a exclusão, não é possível recuperar o que foi deletado, tome cuidado para não se arrepender
- No final será perguntado se o usuário deseja voltar ao menu

## 9. Exibir alertas (Prazos a serem cumpridos)

- Mostra todas as tarefas com o:

>- Nome do animal
>- Tarefa
>- Responsável
>- Dias restantes ou atraso

- A mensagem poderá ser exibida na tela dessas maneira

>- “Faltam X dia(s)” → tarefa futura
>- “Atrasada há X dia(s)” → tarefa vencida
>- “Data inválida!” → formato incorreto

- No final será perguntado se o usuário deseja voltar ao menu


## 10. Mostrar Tarefas

- Isso exibirá, somente as tarefas que estão atrasadas
- Mostra as seguintes informações:

>- Nome do animal
>- Tipo de tarefa
>- O responsável
>- Quanto tempo de atraso (em dias)

## 11. Registrar Histórico Médico

- Aparecerá na tela os animais cadastrados assim como seus respectivos IDs
- Caso não exista, o sistema irá alertar
- Digite o ID corretamente para prosseguir, caso isso não ocorra o programa encerra e será perguntado se o usuário deseja voltar ao menu
- Digitando o Id correto, será pedido para o usuário inserir:
    >- Data (nesse formato, **dia/mês/ano**)
    >- Tipo de envento (com exemplificações)
    >- Descrição em detalhes do evento
- No final será perguntado se o usuário deseja voltar ao menu

## 12. Listar Histórico Médico

- Aparecerá na tela os Históricos Médicos cadastrados assim como seus respectivos IDs
- Caso não exista, o sistema irá alertar
- Caso queira ver o histórico médico completo do animal cadastrado, digite o ID do respectivo animal cadastrado, caso isso não ocorra o programa encerra e será perguntado se o usuário deseja voltar ao menu
- No final será perguntado se o usuário deseja voltar ao menu

## 13. Sair do sistema (encerrar o programa)

- Encerra o programa imediatamente
- Tudo é salvo automaticamente

## 👨‍💻Autores do trabalho👨‍💻

| Nome | E-mail |
|------|--------|
| **Marcus Vinícius Pereira Barbosa** | [mvpb@cesar.school](mailto:mvpb@cesar.school) |
| **Victor Rodrigues Tavares** | [vrt@cesar.school](mailto:vrt@cesar.school) |
| **Luís Filipe Alves Silva Santos** | [lfass@cesar.school](mailto:lfass@cesar.school) |
| **Vinícius Fernandes Mousinho Neves Souza** | [vfmns@cesar.school](mailto:vfmns@cesar.school) |
| **Matheus Costa da Rocha** | [mcr@cesar.school](mailto:mcr@cesar.school) |
| **Brenno Dornelas de Medeiros Filho** | [bdmf@cesar.school](mailto:bdmf@cesar.school) |
