# Convenções deste repositório

Site estático gerado por `build.py`. **Editar o conteúdo no `build.py`, nunca
nos ficheiros HTML** — correr o script reescreve-os todos.

```sh
python3 build.py
```

## Regras que não se negoceiam

Não são preferências de estilo. Cada uma existe por causa de uma política de
plataforma ou de uma cláusula do acordo com o vendedor.

| Regra | Porquê |
|---|---|
| Divulgação de afiliado no topo e no rodapé de todas as páginas | Exigência da FTC e do Google |
| Disclaimer da FDA no rodapé | Obrigatório para suplementos |
| `rel="nofollow sponsored"` e `data-hop` nos links de afiliado | Sinal de link pago; `data-hop` é o que o script de rastreamento procura |
| Script de rastreamento nas páginas com link de afiliado | Sem ele as vendas chegam à ClickBank sem origem — ver `RASTREAMENTO.md` na raiz do projecto |
| Secções "Skip it if" e "What we could not verify" em todos os reviews | São o que distingue um review real de uma página de venda disfarçada, e a melhor defesa numa revisão manual do Google |
| Sem testemunhos inventados, ratings não recolhidos ou alegações de doença | Violação de política e, no caso dos ratings, terreno de manual action |
| Sem logótipos de marca, sem nome de marca no cabeçalho ou rodapé | A Orbio World proíbe-o por escrito, com retenção de pagamentos como penalização |

## Guias vs reviews

Os ficheiros em `guides/` **não levam links de afiliado**. Existem para que o
domínio seja uma publicação e não uma montra — o Google reprova destinos
*"solely designed to send users elsewhere"* e avalia o domínio, não o URL.
Acrescentar um link de afiliado a um guia desfaz a razão de ele existir.

## Antes de publicar uma alteração

Clicar no anúncio → chegar à página → clicar no botão → confirmar na barra de
endereços que os parâmetros de rastreamento chegaram ao hoplink.

## Contexto

Operação documentada na pasta acima: relatórios em `01-relatorios/`,
especificação de rastreamento em `RASTREAMENTO.md`, regras do vendedor em
`06-derila/`.
