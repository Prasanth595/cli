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
- [PING PONG AIR](https://studyplaying.github.io/ping-pong-air.html)
- [DIGWORM IO](https://studyquesthub.web.app/digworm-io.html)
- [CATEGORY UNBLOCKERS](https://quizverses.pages.dev/category-unblockers.html)
- [CATEGORY CASUAL 3](https://studyquesthub.web.app/category-casual-3.html)
- [CATEGORY 3D1 371](https://quizverses-9d2f2.web.app/category-3d1-371.html)
- [CATEGORY MERGE224](https://quizverses.github.io/category-merge224.html)
- [QUIZ SQUID ROUND](https://quizverses-9d2f2.web.app/quiz-squid-round.html)
- [CATEGORY FPS 3](https://thequizzone.pages.dev/category-fps-3.html)
- [CRAZY AXE](https://quizverses.pages.dev/crazy-axe.html)
- [BUBBLE SHOOTER POP](https://quizverses.pages.dev/bubble-shooter-pop.html)
- [ARCHER DUNGEON HERO](https://quizverses.pages.dev/archer-dungeon-hero.html)
- [CHILL CLICKER](https://quizverses-9d2f2.web.app/chill-clicker.html)
- [GIN RUMMY](https://quizverses.github.io/gin-rummy.html)
- [CATEGORY MERGE GAMES](https://quizverses-9d2f2.web.app/category-merge-games.html)
- [DOGE MATCH](https://quizverses.github.io/doge-match.html)
- [CATEGORY MAHJONG 2](https://quizverses.github.io/category-mahjong-2.html)
- [CATEGORY ARENA255](https://studyquesthub.web.app/category-arena255.html)
- [CATEGORY BALL173](https://studyquesthub.web.app/category-ball173.html)
- [WORLD FLAGS TRIVIA](https://studyquests.github.io/world-flags-trivia.html)
- [TOKA BOKA HOME CLEAN UP DESIGN](https://studyquests.github.io/toka-boka-home-clean-up-design.html)
- [SHELF SHIFT MATCH](https://quizverses.github.io/shelf-shift-match.html)
- [CATEGORY SANDBOX](https://studyquests.github.io/category-sandbox.html)
- [CAR CRASH TEST ABANDONED CITY](https://quizverses.github.io/car-crash-test-abandoned-city.html)
- [MAGIC FINGER PUZZLE 3D](https://studyquests.github.io/magic-finger-puzzle-3d.html)
- [CATEGORY DRESS UP 3](https://quizverses.github.io/category-dress-up-3.html)
- [CAKE SORT](https://quizverses.github.io/cake-sort.html)
- [INDEX13](https://studyquesthub.web.app/index13.html)
- [BUBBLE SHOOTER FREE 3](https://studyquests.github.io/bubble-shooter-free-3.html)
- [OFFLINE FPS ROYALE](https://quizverses.github.io/offline-fps-royale.html)
- [LOOP GHOST](https://studyquests.github.io/loop-ghost.html)
- [HIDDEN OBJECT TIME TRAVEL](https://quizverses.github.io/hidden-object-time-travel.html)
- [CATEGORY AVOID](https://studyquesthub.web.app/category-avoid.html)
- [1010 ELIXIR ALCHEMY](https://quizverses.github.io/1010-elixir-alchemy.html)
- [CATEGORY MOBILE2 097](https://studyquests.github.io/category-mobile2-097.html)
- [CATEGORY DRESS UP 2](https://quizverses-9d2f2.web.app/category-dress-up-2.html)
- [CATEGORY CONTROLLER59](https://studyquests.github.io/category-controller59.html)
- [INDEX5](https://studyquesthub.web.app/index5.html)
- [BUBBLE MANIA SHOOTER](https://quizverses.github.io/bubble-mania-shooter.html)
- [SURVEV](https://studyquesthub.web.app/survev.html)
- [DELICIOUS EMILYS NEW BEGINNING VALENTINES EDITION](https://quizverses-9d2f2.web.app/delicious-emilys-new-beginning-valentines-edition.html)
- [PUZZLE FEVER](https://studyquests.pages.dev/puzzle-fever.html)
- [MIRRORS PUZZLE](https://studyquests.pages.dev/mirrors-puzzle.html)
- [JUST MAHJONG](https://studyquests.pages.dev/just-mahjong.html)
- [INDEX15](https://studyplaying.github.io/index15.html)
- [DR PARKING](https://studyquests.pages.dev/dr-parking.html)
- [URUS CITY DRIVER](https://studyquests.pages.dev/urus-city-driver.html)
- [KINGS AND QUEENS MATCH 3](https://studyquests.pages.dev/kings-and-queens-match-3.html)
- [CATEGORY MAHJONG](https://quizverses.github.io/category-mahjong.html)
- [SUPER ELIP ADVENTURE](https://studyquesthub.web.app/super-elip-adventure.html)
- [CATEGORY CASUAL 8](https://quizverses.github.io/category-casual-8.html)
- [AVATAR WORLD SECRETS](https://quizverses.github.io/avatar-world-secrets.html)
- [INDEX17](https://studyquesthub.web.app/index17.html)
- [INDEX18](https://studyplaying.github.io/index18.html)
- [KLONDIKE SOLITAIRE](https://quizverses-9d2f2.web.app/klondike-solitaire.html)
- [GOTHIC KNIFE](https://studyquests.pages.dev/gothic-knife.html)
- [CATEGORY BATTLE524](https://studyquesthub.web.app/category-battle524.html)
- [CATEGORY CASUAL 4](https://studyquests.pages.dev/category-casual-4.html)
- [CATEGORY BATTLE ROYALE25](https://studyquesthub.web.app/category-battle-royale25.html)
- [ROYAL COIN RUSH](https://studyquests.pages.dev/royal-coin-rush.html)
- [CRAZY BIKE STUNTS PVP](https://quizverses-9d2f2.web.app/crazy-bike-stunts-pvp.html)
- [GRILL IT ALL](https://studyquests.pages.dev/grill-it-all.html)
- [KABOOM MINER](https://quizverses-9d2f2.web.app/kaboom-miner.html)
- [CATEGORY CUTE62](https://studyquests.github.io/category-cute62.html)
- [MOJICON EMOJI CONNECT](https://studyquests.pages.dev/mojicon-emoji-connect.html)
- [CATEGORY JUMPING147](https://studyquests.pages.dev/category-jumping147.html)
- [CATEGORY FOOTBALL](https://studyplaying.github.io/category-football.html)
- [CATEGORY COLLECT](https://studyplaying.github.io/category-collect.html)
- [PIN PUZZLE SAVE THE SHEEP](https://studyquests.pages.dev/pin-puzzle-save-the-sheep.html)
- [CATEGORY FASHION105](https://quizverses-9d2f2.web.app/category-fashion105.html)
- [ARMY FIGHT 3D](https://studyquests.github.io/army-fight-3d.html)
- [3D ACRYLIC NAIL NAIL ART GAME](https://studyquests.pages.dev/3d-acrylic-nail-nail-art-game.html)
- [PASSENGER SORT](https://studyquests.pages.dev/passenger-sort.html)
- [CATEGORY BRAIN](https://studyquesthub.web.app/category-brain.html)
- [STICKMAN WARRIOR WAY](https://studyquesthub.web.app/stickman-warrior-way.html)
- [CATEGORY CONTROLLER59](https://quizverses.github.io/category-controller59.html)
- [DIY PHONE CASE SHOP](https://studyquests.pages.dev/diy-phone-case-shop.html)
- [CATEGORY FIGHTING124](https://studyquests.github.io/category-fighting124.html)
- [COOL MAN](https://studyquests.pages.dev/cool-man.html)
- [CLICKER HEROES](https://quizverses.pages.dev/clicker-heroes.html)
- [NONOGRAM DAILY](https://studyquesthub.web.app/nonogram-daily.html)
- [AGARIO](https://studyquests.pages.dev/agario.html)
- [CATEGORY IDLE448](https://quizverses.github.io/category-idle448.html)
- [TWO BLOCKS](https://studyquesthub.web.app/two-blocks.html)
- [CATEGORY UNBLOCKED GAMES](https://studyplayings.pages.dev/category-unblocked-games.html)
- [CATEGORY STICKMAN](https://studyquesthub.web.app/category-stickman.html)
- [DINO DIGG](https://studyquesthub.web.app/dino-digg.html)
- [STICKMAN SHOOTER BROS](https://studyplayings.pages.dev/stickman-shooter-bros.html)
- [BUBBLE ESCAPE](https://quizverses.pages.dev/bubble-escape.html)
- [CATEGORY RPG80](https://studyquests.pages.dev/category-rpg80.html)
- [CATEGORY PREMIUM PERKS71](https://learnquester.github.io/category-premium-perks71.html)
- [CATEGORY MANAGEMENT GAME](https://studyquesthub.web.app/category-management-game.html)
- [NONOGRAM MASTER](https://quizverses.github.io/nonogram-master.html)
- [CATEGORY COOKING](https://studyquests.pages.dev/category-cooking.html)
- [CATEGORY INTERSTELLAR](https://thelearnquester.web.app/category-interstellar.html)
- [MINI GRAND THEFT CITY](https://quizverses.github.io/mini-grand-theft-city.html)
- [TRIPEAKS SOLITAIRE ESCAPES](https://quizverses-9d2f2.web.app/tripeaks-solitaire-escapes.html)
- [CATEGORY ESCAPE 2](https://studyquests.github.io/category-escape-2.html)
- [HAPPY FLUFFY CUBES](https://studyquesthub.web.app/happy-fluffy-cubes.html)
- [CATEGORY LOVE12](https://studyquests.pages.dev/category-love12.html)
- [BASE JUMP WINGSUIT FLYING](https://studyquests.pages.dev/base-jump-wingsuit-flying.html)
- [SAFE MERGE](https://learnquester.github.io/safe-merge.html)
- [MAJESTIC DRAGONS MERGE](https://learnquester.github.io/majestic-dragons-merge.html)
- [ROBOT TRANSFORM RACE](https://learnquester.github.io/robot-transform-race.html)
- [CATEGORY MEME BLOXY24](https://studyquests.pages.dev/category-meme-bloxy24.html)
- [CATEGORY DRESS UP97](https://quizverses-9d2f2.web.app/category-dress-up97.html)
- [PLANET HOPPER](https://learnquester.github.io/planet-hopper.html)
- [GIRLS FUN NAIL SALON](https://studyplayings.web.app/girls-fun-nail-salon.html)
- [CATEGORY GROW GAMES](https://quizverses.github.io/category-grow-games.html)
- [IDLE BASEBALL TYCOON](https://studyquests.github.io/idle-baseball-tycoon.html)
- [CRASH THE ROBOT](https://studyquests.github.io/crash-the-robot.html)
- [CATEGORY HORDE SURVIVAL67](https://quizverses.github.io/category-horde-survival67.html)
- [JUMPERS QUEST](https://quizverses-9d2f2.web.app/jumpers-quest.html)
- [INDEX11](https://studyquesthub.web.app/index11.html)
- [GRUKKLE ONSLAUGHT](https://studyquests.github.io/grukkle-onslaught.html)
- [ONLINE PORTAL](https://studyquests.pages.dev/)
- [TATTOO MASTER](https://studyplayings.web.app/tattoo-master.html)
- [SHELL STRIKERS](https://quizverses.github.io/shell-strikers.html)
- [ESCAPE ROOM MYSTERY KEY](https://learnquester.github.io/escape-room-mystery-key.html)
- [FEED ME MONSTERS IDLE BATTLE](https://studyplayings.pages.dev/feed-me-monsters-idle-battle.html)
- [2248 BLAST](https://learnquester.github.io/2248-blast.html)
- [STRAWBERRY HERO](https://studyquests.pages.dev/strawberry-hero.html)
- [BUBBLE SKY](https://quizverses.github.io/bubble-sky.html)
- [CATEGORY BALL](https://studyquesthub.web.app/category-ball.html)
- [INSPECTOR CAT](https://quizverses-9d2f2.web.app/inspector-cat.html)
- [CATEGORY AGILITY 2](https://quizverses-9d2f2.web.app/category-agility-2.html)
- [CATEGORY FREE RAGDOLL GAMES](https://studyquests.github.io/category-free-ragdoll-games.html)
- [TRIPEAKS SOLITAIRE ESCAPES](https://studyquests.pages.dev/tripeaks-solitaire-escapes.html)
- [CATEGORY MOUSE1 707](https://learnquester.github.io/category-mouse1-707.html)
- [CATEGORY PUZZLE 3](https://studyquests.pages.dev/category-puzzle-3.html)
- [BLOCKAPOLYPSE ZOMBIE SHOOTER](https://learnquester.github.io/blockapolypse-zombie-shooter.html)
