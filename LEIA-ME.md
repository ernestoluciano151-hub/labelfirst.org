# Site LabelFirst — estrutura e checklist de lançamento

**Construído a 11 de Outubro de 2026** · 12 páginas + folha de estilos

---

## Estrutura

```
/                                 homepage — lista artigos, explica o método
/reviews/                         índice de reviews
/reviews/prodentim/               ← a página que recebe os anúncios
/guides/                          índice de guias
/guides/clinically-studied-claims/    "clinically studied" não quer dizer o que parece
/guides/reading-supplement-labels/    como ler um rótulo em dois minutos
/guides/oral-microbiome-basics/       o microbioma oral sem marketing
/how-we-review/                   o método, escrito
/about/                           quem publica
/contact/                         contacto e correcções
/privacy/                         política de privacidade
/affiliate-disclosure/            divulgação completa
/assets/style.css
```

## Porque é que o site tem oito páginas que não vendem nada

O Google reprova destinos *"solely designed to send users elsewhere"*. O revisor olha para o **domínio**, não para o URL. Um domínio com um único review de afiliado tem a assinatura exacta do thin affiliate, por melhor que esteja escrito.

Os três guias não vendem nada e não têm links de afiliado. Existem para que o domínio seja uma publicação e não uma montra. São também os únicos que podem posicionar-se em pesquisa orgânica a médio prazo.

A página `/how-we-review/` é a mais importante das institucionais: declara por escrito o que o site se recusa a publicar — testemunhos inventados, ratings não recolhidos, alegações de doença. Numa revisão manual, é a página que responde à pergunta antes de ela ser feita.

## Porquê `.org`

Para uma publicação de reviews, `.org` lê-se como mais independente que `.com` — é a extensão das organizações de defesa do consumidor. Não há restrição ao registo e não implica estatuto sem fins lucrativos.

O risco é de percepção: um `.org` que ganha comissões tem de ser transparente, ou a independência que o domínio sugere vira-se contra o site. Está coberto pela divulgação no topo de todas as páginas e pela página `/affiliate-disclosure/`. **Não retirar nenhuma das duas.**

## Antes de publicar — obrigatório

- [x] **Domínio escolhido: `labelfirst.org`** — registar na Hostinger.
- [ ] **Criar a caixa `hello@labelfirst.org`** no painel da Hostinger. O endereço já está escrito em `/contact/` — falta existir.
- [ ] **Substituir `PRECOS_A_CONFIRMAR`** em `/reviews/prodentim/` pelos preços reais lidos na página oficial. Os ficheiros de imagem do vendedor chamam-se `69.png`, `59.png` e `49.png`, o que sugere $69/$59/$49 por frasco — **confirmar, não assumir**.
- [ ] **Confirmar os dados do editor** em `/about/` e `/contact/`.
- [ ] Instalar analytics (a política de privacidade já o declara).

## Teste obrigatório antes do primeiro dólar

Clicar no próprio anúncio → chegar ao review → clicar no botão → **confirmar na barra de endereços que os parâmetros de rastreamento chegaram ao hoplink**.

Trinta segundos. Evita semanas de vendas sem origem conhecida.

## Se mudares o nome do site

Editar as quatro variáveis no topo de `build.py` e correr `python3 build.py`. Reescreve as doze páginas.

```python
SITE   = "LabelFirst"
DOMAIN = "labelfirst.org"
EDITOR = "Ernesto Luciano"
HOP    = "https://c5b6c6yqqlf5rr69yar2rroic4.hop.clickbank.net"
```

## Campanha

Oferta: **ProDentim** · comissão $166,92 · CVR 0,84% · **CPC de equilíbrio $1,40**
Orçamento aprovado: **$10/dia durante 3 semanas (~$210)**
Canal: Microsoft Ads pesquisa primeiro, Google depois da palavra-chave provada
Destino: `https://labelfirst.org/reviews/prodentim/`

Sufixo de URL a configurar na plataforma — ver `RASTREAMENTO.md` na raiz do projecto.
