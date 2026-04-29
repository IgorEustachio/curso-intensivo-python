# CLAUDE.md

Este arquivo fornece orientações ao Claude Code (claude.ai/code) ao trabalhar com o código deste repositório.

## Executando o jogo

O jogo deve ser iniciado a partir da raiz do repositório (dois níveis acima deste diretório), e não de dentro da pasta do projeto, pois os caminhos das imagens estão hardcoded em relação a essa raiz:

```bash
# A partir de python-crash-course/
python projetos/alien_invasion/alien_invasion.py
```

Executar diretamente de dentro de `alien_invasion/` causará `FileNotFoundError` no carregamento das imagens (ex.: `projetos/alien_invasion/images/ship.bmp`).

## Dependências

Requer Python 3 e `pygame`. Instale com:

```bash
pip install pygame
```

## Arquitetura

O jogo é organizado em torno de uma classe central `AlienInvasion` (`alien_invasion.py`) que detém todo o estado e conduz o loop principal. Todas as outras classes recebem `ai_game` (a instância de `AlienInvasion`) em seu construtor para acessar o estado compartilhado (`screen`, `settings`, `stats`).

Classes principais e seus papéis:

- **`Settings`** — configurações estáticas e dinâmicas. `initialize_dynamic_settings()` redefine os valores de velocidade a cada novo jogo; `increase_speed()` os aumenta toda vez que uma frota é eliminada.
- **`GameStats`** — estado mutável do jogo (pontuação, nível, naves restantes). `high_score` persiste entre redefinições dentro de uma sessão, mas não é salvo em disco.
- **`Scoreboard`** — renderiza pontuação, recorde, nível e ícones de naves na tela. Cada método `prep_*` re-renderiza a superfície correspondente e deve ser chamado sempre que a estatística subjacente mudar.
- **`Ship`**, **`Alien`**, **`Bullet`** — subclasses de `pygame.sprite.Sprite`. O movimento usa um atributo float (`self.x` / `self.y`) para precisão subpixel; o `rect` inteiro é atualizado a partir dele a cada frame.
- **`Powerup`** — aparece em um intervalo aleatório (60–180 frames) em uma posição x aleatória na parte inferior da tela. A colisão com a nave está parcialmente implementada (`_check_collision_ship_powerup` imprime `'aaa'` mas ainda não tem efeito).
- **`Button`** — renderiza o botão "Play"; exibido apenas quando `game_active` é `False`.

## Estado atual do desenvolvimento

O projeto base do livro "Curso Intensivo de Python" está concluído. 
A feature em desenvolvimento é o sistema de powerup (`Powerup`).

### O que está feito
- Powerup aparece na tela em intervalo aleatório (60–180 frames)
- Posição x aleatória na parte inferior da tela

### O que está incompleto
- `_check_collision_ship_powerup` detecta colisão mas não tem efeito ainda
  (atualmente só imprime `'aaa'`)
- Efeito do powerup na nave/jogo não foi definido

## Convenções do projeto

- Seguir o estilo do livro: métodos auxiliares prefixados com `_`
- Todas as classes recebem `ai_game` no construtor para acessar estado compartilhado
- Movimento usa float (`self.x` / `self.y`) para precisão subpixel
- Nunca salvar `high_score` em disco (comportamento intencional do projeto)

## Cuidados ao modificar

- Alterar `Settings` pode afetar o balanceamento do jogo — testar progressão de níveis após mudanças
- Métodos `prep_*` do `Scoreboard` devem ser chamados sempre que a estatística mudar
- O jogo deve ser executado a partir da raiz do repositório (ver seção "Executando o jogo")

### Fluxo do loop principal (`run_game`)

```
_check_events → (se ativo) ship.update / _update_bullets / _update_aliens / powerup.update → _update_screen → clock.tick(60)
```

`_update_bullets` trata colisão projétil-alienígena, atualização de pontuação, progressão de nível e recriação da frota. `_update_aliens` trata detecção de borda da frota, inversão de direção, colisão com a nave e alienígenas chegando à parte inferior.
