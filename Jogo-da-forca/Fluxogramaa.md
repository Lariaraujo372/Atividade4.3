

```mermaid
flowchart TD
    A([Início]) --> B[Escolher palavra aleatória]
    B --> C[Definir 6 tentativas]
    C --> D[Inicializar lista de letras utilizadas]
    D --> E[Mostrar palavra escondida e tentativas]
    E --> F{Todas as letras foram descobertas?}
    F -->|Sim| G[Mostrar: Ganhou!]
    F -->|Não| H{Ainda há tentativas?}
    H -->|Não| I[Mostrar: Perdeu!]
    H -->|Sim| J[Solicitar uma letra]
    J --> K{Entrada contém apenas uma letra?}
    K -->|Não| L[Mostrar mensagem de erro]
    L --> J
    K -->|Sim| M{Letra já foi utilizada?}
    M -->|Sim| N[Informar que a letra já foi utilizada]
    N --> J
    M -->|Não| O[Adicionar letra à lista]
    O --> P{Letra existe na palavra?}
    P -->|Sim| Q[Mostrar: Acertou!]
    P -->|Não| R[Mostrar: Errou!]
    R --> S[Diminuir uma tentativa]
    Q --> E
    S --> E
    G --> T([Fim do jogo])
    I --> T
```
