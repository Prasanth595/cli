<h2 align="center">
    <a href="https://httpie.io" target="blank_">
        <img height="100" alt="HTTPie" src="https://raw.githubusercontent.com/httpie/cli/master/docs/httpie-logo.svg" />
    </a>
    <br>
    HTTPie CLI: human-friendly HTTP client for the API era
</h2>

<div align="center">

[![HTTPie for Desktop](https://img.shields.io/static/v1?label=HTTPie&message=Desktop&color=4B78E6)](https://httpie.io/product)
[![](https://img.shields.io/static/v1?label=HTTPie&message=Web%20%26%20Mobile&color=73DC8C)](https://httpie.io/app)
[![](https://img.shields.io/static/v1?label=HTTPie&message=CLI&color=FA9BFA)](https://httpie.io/cli)
[![Twitter](https://img.shields.io/twitter/follow/httpie?style=flat&color=%234B78E6&logoColor=%234B78E6)](https://twitter.com/httpie)
[![Chat](https://img.shields.io/discord/725351238698270761?style=flat&label=Chat%20on%20Discord&color=%23FA9BFA)](https://httpie.io/discord)

</div>


<div align="center">

[![Docs](https://img.shields.io/badge/stable%20docs-httpie.io%2Fdocs%2Fcli-brightgreen?style=flat&color=%2373DC8C&label=Docs)](https://httpie.org/docs/cli)
[![Latest version](https://img.shields.io/pypi/v/httpie.svg?style=flat&label=Latest&color=%234B78E6&logo=&logoColor=white)](https://pypi.python.org/pypi/httpie)
[![Build](https://img.shields.io/github/actions/workflow/status/httpie/cli/tests.yml?branch=master&color=%23FA9BFA&label=Build)](https://github.com/httpie/cli/actions)
[![Coverage](https://img.shields.io/codecov/c/github/httpie/cli?style=flat&label=Coverage&color=%2373DC8C)](https://codecov.io/gh/httpie/cli)
[![PyPi downloads](https://img.shields.io/pepy/dt/httpie?style=flat&label=Downloads%20from%20PyPi%20only&color=4B78E6)](https://www.pepy.tech/projects/httpie)

</div>

HTTPie (pronounced _aitch-tee-tee-pie_) is a command-line HTTP client.
Its goal is to make CLI interaction with web services as human-friendly as possible.
HTTPie is designed for testing, debugging, and generally interacting with APIs & HTTP servers.
The `http` & `https` commands allow for creating and sending arbitrary HTTP requests.
They use simple and natural syntax and provide formatted and colorized output.

<div align="center">

<img src="https://raw.githubusercontent.com/httpie/cli/master/docs/httpie-animation.gif" alt="HTTPie in action" width="100%"/>


</div>




## We lost 54k GitHub stars

Please note we recently accidentally made this repo private for a moment, and GitHub deleted our community that took a decade to build. Read the full story here: https://httpie.io/blog/stardust

![](docs/stardust.png)


## Getting started

- [Installation instructions →](https://httpie.io/docs#installation)
- [Full documentation →](https://httpie.io/docs)

## Features

- Expressive and intuitive syntax
- Formatted and colorized terminal output
- Built-in JSON support
- Forms and file uploads
- HTTPS, proxies, and authentication
- Arbitrary request data
- Custom headers
- Persistent sessions
- `wget`-like downloads

[See all features →](https://httpie.io/docs)

## Examples

Hello World:

```bash
https httpie.io/hello
```

Custom [HTTP method](https://httpie.io/docs#http-method), [HTTP headers](https://httpie.io/docs#http-headers) and [JSON](https://httpie.io/docs#json) data:

```bash
http PUT pie.dev/put X-API-Token:123 name=John
```

Build and print a request without sending it using [offline mode](https://httpie.io/docs/cli/offline-mode):

```bash
http --offline pie.dev/post hello=offline
```

Use [GitHub API](https://developer.github.com/v3/issues/comments/#create-a-comment) to post a comment on an [Issue](https://github.com/httpie/cli/issues/83) with [authentication](https://httpie.io/docs#authentication):

```bash
http -a USERNAME POST https://api.github.com/repos/httpie/cli/issues/83/comments body='HTTPie is awesome! :heart:'
```

[See more examples →](https://httpie.io/docs#examples)

## Community & support

- Visit the [HTTPie website](https://httpie.io) for full documentation and useful links.
- Join our [Discord server](https://httpie.io/discord) is to ask questions, discuss features, and for general API chat.
- Tweet at [@httpie](https://twitter.com/httpie) on Twitter.
- Use [StackOverflow](https://stackoverflow.com/questions/tagged/httpie) to ask questions and include a `httpie` tag.
- Create [GitHub Issues](https://github.com/httpie/cli/issues) for bug reports and feature requests.
- Subscribe to the [HTTPie newsletter](https://httpie.io) for occasional updates.

## Contributing

Have a look through existing [Issues](https://github.com/httpie/cli/issues) and [Pull Requests](https://github.com/httpie/cli/pulls) that you could help with. If you'd like to request a feature or report a bug, please [create a GitHub Issue](https://github.com/httpie/cli/issues) using one of the templates provided.

[See contribution guide →](https://github.com/httpie/cli/blob/master/CONTRIBUTING.md)


## 🌐 Web Resources & Interactive Index
- [CATEGORY RACING DRIVING 3](https://studyquests.github.io/category-racing-driving-3.html)
- [COLOR WAVEE](https://thelearnquesters.pages.dev/color-wavee.html)
- [UNSCREW WOOD PUZZLE](https://studyquests.github.io/unscrew-wood-puzzle.html)
- [GRANDFATHER ROAD CHASE REALISTIC SHOOTER GUNS](https://quizverses.github.io/grandfather-road-chase-realistic-shooter-guns.html)
- [TANKS RACE FOR SURVIVAL](https://studyquests.github.io/tanks-race-for-survival.html)
- [PET CONNECT MATCH](https://learnquester.github.io/pet-connect-match.html)
- [CAT PANCAKE DINER](https://studyplaying.github.io/cat-pancake-diner.html)
- [HELIX CRUSH](https://studyquests.github.io/helix-crush.html)
- [CATEGORY PUZZLE 4](https://studyquests.github.io/category-puzzle-4.html)
- [ULTIMATE SPORTS CAR DRIFT](https://studyquests.github.io/ultimate-sports-car-drift.html)
- [COLOR DODGE](https://studyquests.github.io/color-dodge.html)
- [COP RUN 3D](https://quizverses.pages.dev/cop-run-3d.html)
- [HAPPY BLOCKS](https://studyplaying.github.io/happy-blocks.html)
- [SID GINNY Y2K GLAM CLASH](https://studyplaying.github.io/sid-ginny-y2k-glam-clash.html)
- [SPACE SURVIVAL RAINBOW FRIENDS MONSTER](https://studyplayings.pages.dev/space-survival-rainbow-friends-monster.html)
- [MAIDO](https://studyplayings.pages.dev/maido.html)
- [BACK 2 SCHOOL MAKEOVER](https://studyplayings.pages.dev/back-2-school-makeover.html)
- [TRAFFIC JAM HOP ON](https://quizverses.github.io/traffic-jam-hop-on.html)
- [MONSTER TRUCK CRUSH](https://studyplayings.pages.dev/monster-truck-crush.html)
- [SHADOWMAN RUNNER](https://studyplayings.pages.dev/shadowman-runner.html)
- [MINI GAMES PUZZLE COLLECTION](https://studyplaying.github.io/mini-games-puzzle-collection.html)
- [FIND OBJECTS HIDDEN ITEM](https://quizverses.pages.dev/find-objects-hidden-item.html)
- [PARKING FURY 3D NIGHT CITY](https://quizverses.github.io/parking-fury-3d-night-city.html)
- [BUBBLE SHOOTER POP](https://quizverses.pages.dev/bubble-shooter-pop.html)
- [CATEGORY CASUAL 6](https://learnquester.github.io/category-casual-6.html)
- [PUZZLE FEVER](https://studyquests.pages.dev/puzzle-fever.html)
- [TYPING ADVENTURE](https://studyplaying.github.io/typing-adventure.html)
- [SAVE MY HERO](https://quizverses.pages.dev/save-my-hero.html)
- [3D FPS TARGET SHOOTING](https://studyquests.github.io/3d-fps-target-shooting.html)
- [PET CONNECT MATCH](https://studyplaying.github.io/pet-connect-match.html)
- [GEOMETRY VIBES X BALL](https://studyquests.github.io/geometry-vibes-x-ball.html)
- [CUNNING GINGER](https://studyplayings.pages.dev/cunning-ginger.html)
- [DARING JACK](https://studyplaying.github.io/daring-jack.html)
- [ARROW HIT](https://studyquests.github.io/arrow-hit.html)
- [CATEGORY BLOODY29](https://studyplaying.github.io/category-bloody29.html)
- [BLOCK BLAST 2048](https://studyplaying.github.io/block-blast-2048.html)
- [ARROW TAP PUZZLE](https://studyplaying.github.io/arrow-tap-puzzle.html)
- [TRUCK STACK COLORS](https://studyplaying.github.io/truck-stack-colors.html)
- [BLACKRIVER MYSTERY HIDDEN OBJECTS](https://studyplaying.github.io/blackriver-mystery-hidden-objects.html)
- [PULL THE THREAD PUZZLE](https://studyplayings.pages.dev/pull-the-thread-puzzle.html)
- [MILITARY CUBES 2048](https://studyplayings.pages.dev/military-cubes-2048.html)
- [SKIBIDI TOILET VS CAMERAMAN SNIPER GAME](https://studyplaying.github.io/skibidi-toilet-vs-cameraman-sniper-game.html)
- [SPACE SHOOTER SPEED TYPING CHALLENGE](https://studyplaying.github.io/space-shooter-speed-typing-challenge.html)
- [CHRISTMAS CANDY ESCAPE 3D](https://studyquests.github.io/christmas-candy-escape-3d.html)
- [SIGIL SEEKER](https://quizverses.github.io/sigil-seeker.html)
- [ASMR MAKEOVER MAKEUP STUDIO](https://quizverses.github.io/asmr-makeover-makeup-studio.html)
- [TUNNEL ROAD](https://studyquests.pages.dev/tunnel-road.html)
- [FUN IQ PUZZLE](https://studyplaying.github.io/fun-iq-puzzle.html)
- [PRSINO](https://studyplaying.github.io/prsino.html)
- [FRUIT SORT LOGIC](https://studyplayings.pages.dev/fruit-sort-logic.html)
- [MR DRIFTER CAR CHASE SIMULATOR](https://studyplayings.pages.dev/mr-drifter-car-chase-simulator.html)
- [FIGHT FOR THE TREE](https://studyplaying.github.io/fight-for-the-tree.html)
- [3 TILES](https://learnquester.github.io/3-tiles.html)
- [TAXI DRIVER SIMULATOR](https://studyquests.github.io/taxi-driver-simulator.html)
- [ZERO TO MILLIONAIRE](https://studyplaying.github.io/zero-to-millionaire.html)
- [CRIME THEFT GANGSTER PARADISE](https://studyplaying.github.io/crime-theft-gangster-paradise.html)
- [WONDERS OF EGYPT MATCH](https://quizverses.pages.dev/wonders-of-egypt-match.html)
- [SWORD LIFE](https://studyplaying.github.io/sword-life.html)
- [AIRPORT SECURITY](https://studyplaying.github.io/airport-security.html)
- [DRAW TO SMASH](https://studyplayings.pages.dev/draw-to-smash.html)
- [CUTE CRAFT LAB](https://quizverses.github.io/cute-craft-lab.html)
- [MERGE 2048 CAKE](https://quizverses.github.io/merge-2048-cake.html)
- [ITALIAN BRAINROT FIND THE STARS](https://quizverses.github.io/italian-brainrot-find-the-stars.html)
- [RANCH ADVENTURES](https://quizverses.github.io/ranch-adventures.html)
- [UNCLE HIT PUNCH THE DUMMY](https://quizverses.github.io/uncle-hit-punch-the-dummy.html)
- [INDEX24](https://studyplaying.github.io/index24.html)
- [MY ARCADE CENTER](https://studyplayings.pages.dev/my-arcade-center.html)
- [OM NOM RUN](https://studyplaying.github.io/om-nom-run.html)
- [HOTEL FEVER TYCOON](https://quizverses.pages.dev/hotel-fever-tycoon.html)
- [ELEMENTAL DRESSUP MAGIC](https://studyplayings.pages.dev/elemental-dressup-magic.html)
- [GEOMETRY VIBES MONSTER](https://quizverses.github.io/geometry-vibes-monster.html)
- [TIMEWARRIORS](https://studyplaying.github.io/timewarriors.html)
- [JUST MAHJONG](https://studyquests.pages.dev/just-mahjong.html)
- [STICK ROPE HERO](https://studyplaying.github.io/stick-rope-hero.html)
- [THE OFFICE ESCAPE](https://quizverses.pages.dev/the-office-escape.html)
- [BFF HAPPY SPRING](https://quizverses.github.io/bff-happy-spring.html)
- [OBBY PRISON RUN](https://studyquests.pages.dev/obby-prison-run.html)
- [PET SALON SIMULATOR](https://studyplaying.github.io/pet-salon-simulator.html)
- [JELLY MONSTERS LINK PUZZLE](https://quizverses.github.io/jelly-monsters-link-puzzle.html)
- [DINO HUNTER KING](https://quizverses.pages.dev/dino-hunter-king.html)
- [CATEGORY PLATFORM260](https://studyquests.pages.dev/category-platform260.html)
- [COIN MERGE](https://studyplaying.github.io/coin-merge.html)
- [DOMINO ADVENTURE](https://studyplaying.github.io/domino-adventure.html)
- [SOKOBAN PR](https://studyplaying.github.io/sokoban-pr.html)
- [CATEGORY GITHUB IO](https://studyquests.github.io/category-github-io.html)
- [PURRFECT SCOOPS](https://studyquests.github.io/purrfect-scoops.html)
- [CATEGORY CARE](https://studyquesthub.web.app/category-care.html)
- [SPRUNKI 3D SHOOTER](https://quizverses.pages.dev/sprunki-3d-shooter.html)
- [SORCERER MAHJONG MARVELS](https://studyquesthub.web.app/sorcerer-mahjong-marvels.html)
- [SUPERMARKET CASHIER SIMULATOR](https://studyquests.github.io/supermarket-cashier-simulator.html)
- [CHECKERS DELUXE EDITION](https://studyplaying.github.io/checkers-deluxe-edition.html)
- [SNIPER ASSASSIN GOVERNMENT AGENT](https://studyplayings.web.app/sniper-assassin-government-agent.html)
- [SCHOOLBOY RUNAWAY ROOM ESCAPE](https://quizverses.pages.dev/schoolboy-runaway-room-escape.html)
- [SPIDER ROPE HERO CITY FIGHT](https://studyplaying.github.io/spider-rope-hero-city-fight.html)
- [SHAPE TRANSFORM RACE](https://studyplayings.web.app/shape-transform-race.html)
- [MEME WARS](https://studyplayings.pages.dev/meme-wars.html)
- [PRINCESS RUN 3D](https://studyplaying.github.io/princess-run-3d.html)
- [SHELF SHIFT MATCH](https://quizverses.pages.dev/shelf-shift-match.html)
- [MATCHING PUZZLE](https://quizverses.pages.dev/matching-puzzle.html)
- [KAWAII CLAW MERGE](https://studyplayings.web.app/kawaii-claw-merge.html)
- [DIAMOND MOSAIC](https://studyquests.pages.dev/diamond-mosaic.html)
- [MAHJONG QUEST CANDYLAND ADVENTURES](https://studyplayings.pages.dev/mahjong-quest-candyland-adventures.html)
- [PYRAMIDZ2](https://studyplaying.github.io/pyramidz2.html)
- [CATEGORY SECURLY BYPASS](https://studyquests.github.io/category-securly-bypass.html)
- [CATEGORY SOCCER60](https://studyplaying.github.io/category-soccer60.html)
- [BALLISTIC BREAKTHROUGH](https://studyplaying.github.io/ballistic-breakthrough.html)
- [CATEGORY MOUSE1 697](https://studyplaying.github.io/category-mouse1-697.html)
- [ENCHANTED EASTER ADVENTURE](https://studyplayings.web.app/enchanted-easter-adventure.html)
- [GEOMETRY STARS](https://quizverses.pages.dev/geometry-stars.html)
- [CATEGORY PIXEL313](https://studyplaying.github.io/category-pixel313.html)
- [TILE SORT MATCH 3](https://studyplayings.web.app/tile-sort-match-3.html)
- [INDEX20](https://studyquests.github.io/index20.html)
- [FORTUNES DECK SOLITAIRE](https://studyplayings.pages.dev/fortunes-deck-solitaire.html)
- [BALL SORT](https://quizverses.pages.dev/ball-sort.html)
- [STRAWBERRY SHORTCAKE](https://studyplayings.web.app/strawberry-shortcake.html)
- [CATEGORY MEDIEVAL15](https://studyquests.github.io/category-medieval15.html)
- [WINTER SOLITAIRE TRIPEAKS](https://studyplayings.web.app/winter-solitaire-tripeaks.html)
- [IDLE MONEY FACTORY](https://studyplayings.pages.dev/idle-money-factory.html)
- [GOKARTS IO](https://studyplayings.pages.dev/gokarts-io.html)
- [CATEGORY PUZZLE 5](https://studyplaying.github.io/category-puzzle-5.html)
- [SHANGHAI CHEF](https://quizverses.pages.dev/shanghai-chef.html)
- [BUBBLE BALL](https://studyplayings.web.app/bubble-ball.html)
- [INDEX37](https://studyquests.github.io/index37.html)
- [SNIPER 3D ZOMBIE](https://studyplayings.web.app/sniper-3d-zombie.html)
- [BOARD KINGS BOARD DICE](https://studyplaying.github.io/board-kings-board-dice.html)
- [COFFEE CRAZE SORTING GAME](https://studyplayings.web.app/coffee-craze-sorting-game.html)
- [SEAFARING MEMORY CHALLENGE](https://studyplaying.github.io/seafaring-memory-challenge.html)
- [CRAZY BAR BRAWL](https://studyplaying.github.io/crazy-bar-brawl.html)
- [SUIKA WATERMELON DROP](https://studyquesthub.web.app/suika-watermelon-drop.html)
- [CONTACT](https://studyplaying.github.io/contact.html)
