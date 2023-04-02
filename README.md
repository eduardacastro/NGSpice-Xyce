# NGSpice

Scripts de circuitos feitos para simulação no NGSpice 

# Simulação

### Abrir o NGSpice: 
  - No terminal dentro da pasta do arquivo a ser testado digite `ngspice`. 
  - Em seguida digite `source nomeDoArquivo.cir`.
  - Após o arquivo ser carregado digite `run`.
  - `print <nome da nó>` para saber os dados desse nó. É possível dar o comando `print all` para printar todos os nós
  - `tran <tempo inicial> <tempo final>`para a analise transiente do ckt.
  - `plot <nome do nó> <nome do nó>` para printar um gráfico.
  
### Verificando a corrente em um ramo

O NGSpice não salva valores de correntes intermediarias, apenas de fontes independentes. Então, para poder analisar o valor de corrente de um ramo é possível adicionar uma fonte de tensão 0V.

ex: 

```
* Descrição do CKT

     vSignal vi  GND  1V 
     R1      vi  vo   1k 
     R2      vo  GND  2.2K 
     R3      vo  n01  890 
     vAmp    n01 GND  0V 
 ```
 
 Há também outro metódo usando o `.save`. Contudo, com esse método ele só mostra os parametros que são indicados no save, para mudar isso, basta colocar o `all`.
 
 ex:
 
 ```
    .save all @dev[parm]
    
    --------------------
    
    .save all @R2[i] @R3[i] @R1[i]
    .save all @R2[p] @R3[p] @R1[p]
 ```

Transformar o fundo preto em branco e aumentar o tamanho da linha:

```
    set color0=white
    set xbrushwidth=3
```



## Testes

1. Vo x Vi
```
    plot v(saida) v(entrada)
```
2. Frequencia
```
    fft v(saida)
    plot mag(v(saida))
```
