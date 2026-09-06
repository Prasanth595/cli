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
- [HIDE AND SEEK BLUE MONSTER](https://theskillquest.pages.dev/hide-and-seek-blue-monster.html)
- [LINKLINK](https://iskillquest.pages.dev/linklink.html)
- [MICROPLASTICS FEEDING](https://theskillquest.pages.dev/microplastics-feeding.html)
- [WINTER TETRIX TRAILS](https://themindplay.pages.dev/winter-tetrix-trails.html)
- [STELLAR FUSION](https://skillplay.github.io/stellar-fusion.html)
- [TICTOC URBAN OUTFITS](https://themindplay.pages.dev/tictoc-urban-outfits.html)
- [SUDOKU CLASSIC DAILY BRAIN PUZZLE](https://iskillplay.web.app/sudoku-classic-daily-brain-puzzle.html)
- [WORDS WITH PROF WISELY](https://skillplay.github.io/words-with-prof-wisely.html)
- [DRAW BRIGE PUZZLE](https://themindplay.pages.dev/draw-brige-puzzle.html)
- [CATEGORY LISTS](https://iskillquest.pages.dev/category-lists.html)
- [MYSTICAL BLADE 3D](https://themindplay.pages.dev/mystical-blade-3d.html)
- [JUST MAHJONG](https://themindskillplayplay.pages.dev/just-mahjong.html)
- [PURRFECT SCOOPS](https://theskillquest.pages.dev/purrfect-scoops.html)
- [REAL RACING 3D](https://iskillquest.pages.dev/real-racing-3d.html)
- [INDEX18](https://themindskillplayplay.pages.dev/index18.html)
- [FIGHT FOR THE TREE](https://themindplay.pages.dev/fight-for-the-tree.html)
- [ACADEMY ASSAULT](https://themindplay.github.io/academy-assault.html)
- [CATEGORY SOCCER 3](https://themindplay.pages.dev/category-soccer-3.html)
- [GROCERY SHOP SUPERMARKET GAME](https://theskillquest.pages.dev/grocery-shop-supermarket-game.html)
- [INDEX20](https://themindskillplayplay.pages.dev/index20.html)
- [PAINT POP 3D](https://themindplaying.web.app/paint-pop-3d.html)
- [JEWEL DRESS UP](https://iskillquest.pages.dev/jewel-dress-up.html)
- [MAGICAL DIARY PAPER DRESS UP](https://theskillquest.pages.dev/magical-diary-paper-dress-up.html)
- [KABOOM MINER](https://theskillquest.pages.dev/kaboom-miner.html)
- [SKATE HOOLIGANS](https://theskillquest.pages.dev/skate-hooligans.html)
- [GALACTIC CRUSADE CLICKER](https://themindplaying.web.app/galactic-crusade-clicker.html)
- [TANK BATTLEIO](https://skillplay.github.io/tank-battleio.html)
- [INDEX32](https://themindskillplayplay.pages.dev/index32.html)
- [NOSE HOSPITAL](https://skillplay.github.io/nose-hospital.html)
- [CATEGORY 3D1 371](https://themindskillplayplay.pages.dev/category-3d1-371.html)
- [CATEGORY ADVENTURE 4](https://themindskillplayplay.pages.dev/category-adventure-4.html)
- [CHICKEN BLAST](https://themindplaying.web.app/chicken-blast.html)
- [CATEGORY PUZZLE 3](https://themindplay.pages.dev/category-puzzle-3.html)
- [STICKHOLEIO](https://theskillquest.pages.dev/stickholeio.html)
- [INDEX21](https://themindskillplayplay.pages.dev/index21.html)
- [STICKMAN DUO ESCAPE THE TOMB](https://theskillquest.pages.dev/stickman-duo-escape-the-tomb.html)
- [SITEMAP](https://themindskillplayplay.pages.dev/sitemap.html)
- [LAVA LADDER LEAP](https://iskillquest.pages.dev/lava-ladder-leap.html)
- [GHOST ESCAPE 3D](https://themindplaying.web.app/ghost-escape-3d.html)
- [INDEX9](https://themindplay.github.io/index9.html)
- [ROYAL GARDEN MATCH](https://skillplay.github.io/royal-garden-match.html)
- [COOL GIRL AESTHETICS](https://themindplay.pages.dev/cool-girl-aesthetics.html)
- [INDEX2](https://themindskillplayplay.pages.dev/index2.html)
- [TRAFFIC LIGHT SIMULATOR 3D](https://theskillquest.pages.dev/traffic-light-simulator-3d.html)
- [PENTAWORD](https://iskillquest.pages.dev/pentaword.html)
- [INDEX41](https://themindskillplayplay.pages.dev/index41.html)
- [CHICKEN WARS MERGE GUNS](https://themindplay.pages.dev/chicken-wars-merge-guns.html)
- [IDLE BASEBALL TYCOON](https://themindplay.pages.dev/idle-baseball-tycoon.html)
- [2 CARS RUN](https://theskillquest.pages.dev/2-cars-run.html)
- [CRAZY BAR BRAWL](https://skillplay.github.io/crazy-bar-brawl.html)
- [NUTS BOLTS PUZZLE](https://themindplaying.web.app/nuts-bolts-puzzle.html)
- [COUNT MASTERS SUPERHERO](https://theskillquest.pages.dev/count-masters-superhero.html)
- [CATEGORY SECURLY](https://themindplay.pages.dev/category-securly.html)
- [PAPA BUZJA](https://themindplay.pages.dev/papa-buzja.html)
- [MAHJONG TOUR](https://themindplay.pages.dev/mahjong-tour.html)
- [POP THEM](https://skillplay.github.io/pop-them.html)
- [INDEX8](https://themindplaying.web.app/index8.html)
- [DEATH BALL](https://themindplay.pages.dev/death-ball.html)
- [ANIMAL MERGE BUBBLE SHOOTER](https://themindplay.pages.dev/animal-merge-bubble-shooter.html)
- [CATEGORY ALIEN34](https://themindskillplayplay.pages.dev/category-alien34.html)
- [WOODS OF NEVIA FOREST SURVIVAL](https://themindplay.pages.dev/woods-of-nevia-forest-survival.html)
- [MERMAIDS SPOT THE DIFFERENCES](https://skillplay.github.io/mermaids-spot-the-differences.html)
- [DOLPHIN COUPLE UNDERWATER DRESS UP](https://themindplay.pages.dev/dolphin-couple-underwater-dress-up.html)
- [DUNK CHALLENGE](https://themindplay.pages.dev/dunk-challenge.html)
- [SHELF SHIFT MATCH](https://themindplay.pages.dev/shelf-shift-match.html)
- [WOODY TAP BLOCK](https://themindplay.pages.dev/woody-tap-block.html)
- [CATEGORY TETRIS](https://themindplaying.web.app/category-tetris.html)
- [BROKEN CITY COMBAT](https://themindplaying.web.app/broken-city-combat.html)
- [FROGGA](https://skillplay.github.io/frogga.html)
- [RED LIGHT GREEN LIGHT](https://theskillquest.pages.dev/red-light-green-light.html)
- [MATCH TILE ROYAL FAMILY](https://themindplaying.web.app/match-tile-royal-family.html)
- [CATEGORY STICKMAN](https://themindplay.pages.dev/category-stickman.html)
- [PORTAL MASTER](https://theskillquest.pages.dev/portal-master.html)
- [TRY TO COUNT THE BOXES BRAIN TRAINING](https://theskillquest.pages.dev/try-to-count-the-boxes-brain-training.html)
- [TYPE SPRINT](https://theskillquest.pages.dev/type-sprint.html)
- [CAR JAM ESCAPE](https://theskillquest.pages.dev/car-jam-escape.html)
- [SPACE CRAFT SHIP WAR](https://theskillquest.pages.dev/space-craft-ship-war.html)
- [BLOCK TNT BLAST](https://themindplay.pages.dev/block-tnt-blast.html)
- [CATEGORY STUNT128](https://themindplay.pages.dev/category-stunt128.html)
- [BATTLE TANKS FIRESTORM](https://theskillquest.pages.dev/battle-tanks-firestorm.html)
- [THE OFFICE ESCAPE](https://theskillquest.pages.dev/the-office-escape.html)
- [CURSED TREASURE 11 2](https://themindplay.pages.dev/cursed-treasure-11-2.html)
- [CAT LIFE SIMULATOR](https://themindplaying.web.app/cat-life-simulator.html)
- [CATEGORY CARE](https://themindplay.pages.dev/category-care.html)
- [BACK 2 SCHOOL MAKEOVER](https://themindplay.pages.dev/back-2-school-makeover.html)
- [CATEGORY BATTLE 2](https://themindskillplayplay.pages.dev/category-battle-2.html)
- [SUDOKU GARDEN](https://themindzone.pages.dev/sudoku-garden.html)
- [DESIGN WITH ME SUPERHERO TUTU OUTFITS](https://themindplaying.web.app/design-with-me-superhero-tutu-outfits.html)
- [CHROMA TREK](https://skillplay.github.io/chroma-trek.html)
- [STOLEN HOUSE](https://skillplay.github.io/stolen-house.html)
- [CATEGORY BIKE 3](https://themindskillplayplay.pages.dev/category-bike-3.html)
- [CATEGORY BUBBLE SHOOTER27](https://themindplay.pages.dev/category-bubble-shooter27.html)
- [CATEGORY PUZZLE 5](https://themindplay.github.io/category-puzzle-5.html)
- [SKILLFITE IO](https://themindzone.pages.dev/skillfite-io.html)
- [CATEGORY CASUAL 2](https://themindplaying.web.app/category-casual-2.html)
- [INDEX14](https://themindskillplayplay.pages.dev/index14.html)
- [CATEGORY PUZZLE 2](https://themindskillplayplay.pages.dev/category-puzzle-2.html)
- [MARBLE SORT](https://themindplay.pages.dev/marble-sort.html)
- [UNTANGLE RINGS MASTER](https://thequizzone.pages.dev/untangle-rings-master.html)
- [BUBBLE SHOOTER ULTIMATE](https://theskillquest.pages.dev/bubble-shooter-ultimate.html)
- [CELEBRITY E GIRL VIBES](https://themindplay.pages.dev/celebrity-e-girl-vibes.html)
- [HIDE AND SEEK BLUE MONSTER](https://themindzone.pages.dev/hide-and-seek-blue-monster.html)
- [NUTS BOLTS WOOD PUZZLE GAME](https://themindplay.pages.dev/nuts-bolts-wood-puzzle-game.html)
- [CATEGORY FOOD95](https://themindskillplayplay.pages.dev/category-food95.html)
- [CUBICA](https://thequizzone.pages.dev/cubica.html)
- [GRAFFITI TAGS SPRAY PAINTING](https://theskillquest.pages.dev/graffiti-tags-spray-painting.html)
- [HEROES OF THE ARENA](https://themindzone.pages.dev/heroes-of-the-arena.html)
- [RESCUE SHARP TURN](https://theskillquest.pages.dev/rescue-sharp-turn.html)
- [MEGA RAMP BIKE RACING TRACKS](https://themindplay.github.io/mega-ramp-bike-racing-tracks.html)
- [WORD SEARCH UNIVERSE 2](https://theskillquest.pages.dev/word-search-universe-2.html)
- [TENNIS MASTERS 2026](https://themindplay.pages.dev/tennis-masters-2026.html)
- [CATEGORY GUN238](https://themindskillplayplay.pages.dev/category-gun238.html)
- [OBBY VS ZOMBIES](https://theskillquest.pages.dev/obby-vs-zombies.html)
- [COLOR MAZE](https://theskillquest.pages.dev/color-maze.html)
- [CAT LIFE MERGE MONEY](https://iskillquest.pages.dev/cat-life-merge-money.html)
- [SNAKE CLASH](https://skillplay.github.io/snake-clash.html)
- [EATING SIMULATOR](https://thequizzone.pages.dev/eating-simulator.html)
- [CELEBRITY SPRING FASHION TRENDS](https://themindzone.pages.dev/celebrity-spring-fashion-trends.html)
- [BEAUTY WORLD AND FASHION STYLIST](https://thequizzone.pages.dev/beauty-world-and-fashion-stylist.html)
- [OBBY ESCAPE BARRYS JAIL PARKOUR](https://themindplay.pages.dev/obby-escape-barrys-jail-parkour.html)
- [BELL MADNESS](https://themindplay.pages.dev/bell-madness.html)
- [CATEGORY CAN T STOP PLAYING215](https://themindskillplayplay.pages.dev/category-can-t-stop-playing215.html)
- [TAILOR STYLIST FASHION DIARY](https://thequizzone.pages.dev/tailor-stylist-fashion-diary.html)
- [DEEP FISHING](https://themindplay.pages.dev/deep-fishing.html)
- [CATEGORY OBBY56](https://themindskillplayplay.pages.dev/category-obby56.html)
- [RUN FROM BABA YAGA](https://themindplay.pages.dev/run-from-baba-yaga.html)
- [CHRONO DRIVE](https://themindplay.pages.dev/chrono-drive.html)
- [HOTGEAR](https://themindzone.pages.dev/hotgear.html)
- [MINI GAMES RELAX COLLECTION 2](https://themindzone.pages.dev/mini-games-relax-collection-2.html)
- [DOGS VS ALIENS](https://themindzone.pages.dev/dogs-vs-aliens.html)
