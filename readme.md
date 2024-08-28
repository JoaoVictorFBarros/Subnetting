# Subnetting e Geração de Sub-redes
**Subnetting** é o processo de dividir uma rede maior em sub-redes menores, permitindo uma gestão mais eficiente dos endereços IP. Nesta documentação, abordaremos os conceitos de subnetting, mostrando como ele funciona na prática e como implementá-lo em Python.

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/Subnetting.git
```

### Instalação das Dependências

Todas as bibliotecas usadas são padrão do python.

### Executando o Projeto

Para iniciar o simulador, execute:

```
python3 main.py
```

## Revisão Rápida: Endereço IP e Máscara de Rede

- **Endereço IP**: Um número de 32 bits dividido em quatro partes de 8 bits (octetos). Exemplo: `192.168.1.3`.
- **Máscara de Rede**: Define qual parte do endereço IP é usada para identificar a rede e qual parte é usada para identificar os hosts dentro da rede. Exemplo: `/24` ou `255.255.255.0`.

Em uma máscara `/24`, os primeiros 24 bits são para a rede e os últimos 8 bits são para os hosts. Isso significa que essa rede pode acomodar até 256 endereços IP (254 utilizáveis, excluindo o endereço de rede e o endereço de broadcast).

## Subnetting: Dividindo a Rede

O processo de subnetting envolve "emprestar" bits da parte de host para criar sub-redes. Ao aumentar o prefixo da máscara de rede, estamos reduzindo o espaço para hosts e criando mais sub-redes.

## Exemplo Prático

Considere a rede `192.168.1.3/24`. Vamos dividi-la em 4 sub-redes.

A máscara original é `/24`, o que significa:
- 24 bits para a rede: `192.168.1.3`
- 8 bits para hosts, ou seja, `2^8 = 256` endereços possíveis.

Se quisermos criar 4 sub-redes, precisamos de 2 bits adicionais para identificar essas sub-redes (porque `2^2 = 4`). Então, a nova máscara se torna `/26` (24 + 2), o que deixa 6 bits para hosts em cada sub-rede.

<div align="center">
<img src=print.png >
</div>

Cada sub-rede contém 64 endereços (62 utilizáveis). Com a máscara `/26`, as divisões são feitas em blocos fixos de 64 endereços.

## Como o Código Implementa Isso

No código Python, isso é feito da seguinte maneira:

1. **Calcular o Novo Prefixo**: O código determina o novo prefixo da máscara (por exemplo, `/26`) com base no número de sub-redes desejadas.

    ```python
    novo_prefixo = rede.prefixlen + (num_subredes - 1).bit_length()
    ```

    A função `.bit_length()` retorna o número de bits necessários para representar o número de sub-redes desejadas.

2. **Gerar as Sub-redes**: A função `subnets(new_prefix=novo_prefixo)` divide a rede original em sub-redes menores com a máscara especificada.

    ```python
    subredes = list(rede.subnets(new_prefix=novo_prefixo))
    ```

3. **Exibir os Resultados**: O código percorre cada sub-rede e exibe informações como o endereço de rede, IPs utilizáveis e o endereço de broadcast.

## Visualizando em Binário

Para entender melhor como funciona, aqui está a rede `192.168.1.3/24` em binário:
```
192.168.1.3/24: 11000000.10101000.00000001.00000000
```

Dividindo em 4 sub-redes, precisamos de 2 bits adicionais:

- **Sub-rede 1 (192.168.1.3/26)**: `11000000.10101000.00000001.00000000`
- **Sub-rede 2 (192.168.1.64/26)**: `11000000.10101000.00000001.01000000`
- **Sub-rede 3 (192.168.1.128/26)**: `11000000.10101000.00000001.10000000`
- **Sub-rede 4 (192.168.1.192/26)**: `11000000.10101000.00000001.11000000`

Os dois bits adicionais determinam a sub-rede, e os 6 bits restantes identificam os hosts dentro de cada sub-rede.

## Conclusão

A geração de sub-redes envolve modificar a máscara de rede para alocar mais bits para identificar as sub-redes, resultando em blocos menores de endereços. A lógica se baseia na manipulação dos bits do endereço IP para dividir o espaço de endereçamento original em partes menores, conforme o número de sub-redes desejado.


