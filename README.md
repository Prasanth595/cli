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
- [DINOSAUR CARDS](https://quizverses.github.io/dinosaur-cards.html)
- [CUTE CATS ADVENTURES](https://themindzone.pages.dev/cute-cats-adventures.html)
- [CATEGORY MAHJONG 2](https://thelearnquester.web.app/category-mahjong-2.html)
- [ALCHEMY PUZZLE](https://studyplaying.github.io/alchemy-puzzle.html)
- [BLOXDHOP IO](https://studyquests.pages.dev/bloxdhop-io.html)
- [INDEX15](https://learnquester.github.io/index15.html)
- [POPPING PETS](https://learnquester.github.io/popping-pets.html)
- [SUPER ONION BOY 2](https://studyquests.github.io/super-onion-boy-2.html)
- [CATEGORY CONTROLLER](https://studyplaying.github.io/category-controller.html)
- [TREASURE HUNT PUZZLE](https://studyplayings.pages.dev/treasure-hunt-puzzle.html)
- [PING PONG BATTLE TABLE TENNIS](https://quizverses.pages.dev/ping-pong-battle-table-tennis.html)
- [CATEGORY MAKEUP51](https://quizverses.github.io/category-makeup51.html)
- [CATEGORY BASKETBALL](https://learnquester.github.io/category-basketball.html)
- [COIN MERGE MACHINE](https://quizverses.github.io/coin-merge-machine.html)
- [CATEGORY AVOID295](https://learnquester.github.io/category-avoid295.html)
- [TERMS](https://cryptotify.github.io/terms.html)
- [TERMS](https://cryptotify9.onrender.com/terms.html)
- [BLACK PINK STPATRICKS DAY CONCERT](https://studyplayings.pages.dev/black-pink-stpatricks-day-concert.html)
- [TROLLEY FUN](https://studyquests.github.io/trolley-fun.html)
- [CATEGORY EDUCATIONAL](https://studyquests.github.io/category-educational.html)
- [ACE CAR RACING](https://studyplayings.web.app/ace-car-racing.html)
- [HOME BLOCK STORY](https://studyplayings.pages.dev/home-block-story.html)
- [ROMANTIC MATCH TACTICS](https://quizverses.pages.dev/romantic-match-tactics.html)
- [CARD MASTER](https://studyplayings.pages.dev/card-master.html)
- [SITEMAP](https://learnquester.github.io/sitemap.html)
- [CATEGORY CASUAL 14](https://studyquests.github.io/category-casual-14.html)
- [CATEGORY SOCCER 3](https://quizverses.github.io/category-soccer-3.html)
- [CATEGORY AGILITY](https://learnquester.github.io/category-agility.html)
- [MERGE BLOCKS 2048 STYLE](https://studyquests.pages.dev/merge-blocks-2048-style.html)
- [GRANNYS CLASSROOM NIGHTMARE](https://studyplaying.github.io/grannys-classroom-nightmare.html)
- [KINGS AND QUEENS MATCH 3](https://studyquests.pages.dev/kings-and-queens-match-3.html)
- [COLOR BUMP DANCER](https://studyplayings.pages.dev/color-bump-dancer.html)
- [DESTRUCTION SIMULATOR](https://studyplayings.pages.dev/destruction-simulator.html)
- [TERMS](https://studyquests.github.io/terms.html)
- [CATEGORY BLOCK94](https://quizverses-9d2f2.web.app/category-block94.html)
- [PUZZLE TRAILS](https://learnquester.github.io/puzzle-trails.html)
- [CATEGORY RACING DRIVING](https://studyquests.github.io/category-racing-driving.html)
- [PUZZLE SOLITAIRE PICTURE MATCH](https://studyquests.github.io/puzzle-solitaire-picture-match.html)
- [CHRISTMAS MERGE](https://studyplaying.github.io/christmas-merge.html)
- [MATH QUEST](https://studyplayings.pages.dev/math-quest.html)
- [MY PERFECT MINE](https://studyquests.pages.dev/my-perfect-mine.html)
- [BUSY BEE HIVE](https://studyquests.pages.dev/busy-bee-hive.html)
- [CATEGORY MAKEUP CATEGORY](https://quizverses.pages.dev/category-makeup-category.html)
- [VALENTINE HIDDEN HEART](https://studyquests.pages.dev/valentine-hidden-heart.html)
- [GUN MATCH SCREW](https://studyplayings.pages.dev/gun-match-screw.html)
- [M5 CITY DRIVER](https://studyplayings.web.app/m5-city-driver.html)
- [KILLER ESCAPE HUGGY EXTREME](https://learnquester.github.io/killer-escape-huggy-extreme.html)
- [CATEGORY GUN241](https://quizverses-9d2f2.web.app/category-gun241.html)
- [STICKMAN ARCHERO FIGHT STICK SHADOW FIGHT WAR](https://studyplayings.web.app/stickman-archero-fight-stick-shadow-fight-war.html)
- [FLAPPY RUSH](https://studyquests.github.io/flappy-rush.html)
- [TERMS](https://quizverses-9d2f2.web.app/terms.html)
- [CRAZY SCREW KING](https://studyquests.github.io/crazy-screw-king.html)
- [BADLANDS HERO](https://studyplaying.github.io/badlands-hero.html)
- [MOON LEAGUE SPORTS SEASON](https://learnquester.github.io/moon-league-sports-season.html)
- [ITALIAN BRAINROT BABY CLICKER](https://studyplaying.github.io/italian-brainrot-baby-clicker.html)
- [STICKMAN THE FLASH](https://studyplaying.github.io/stickman-the-flash.html)
- [CATEGORY THINKY](https://studyplayings.web.app/category-thinky.html)
- [FUN IQ PUZZLE](https://studyplayings.web.app/fun-iq-puzzle.html)
- [BLOCK MINE FUSE TNT](https://studyquests.github.io/block-mine-fuse-tnt.html)
- [BASE JUMP WINGSUIT FLYING](https://studyquests.pages.dev/base-jump-wingsuit-flying.html)
- [KICK LOSER](https://quizverses-9d2f2.web.app/kick-loser.html)
- [GEOMETRY TOWER DEFENSE](https://quizverses.github.io/geometry-tower-defense.html)
- [ROOM SORT](https://studyplaying.github.io/room-sort.html)
- [SPRUNKI GETS SURGERY](https://studyplaying.github.io/sprunki-gets-surgery.html)
- [BUS JAM](https://studyquests.pages.dev/bus-jam.html)
- [CATEGORY SOCCER](https://studyplayings.web.app/category-soccer.html)
- [AROUND ELBRUS](https://studyquests.github.io/around-elbrus.html)
- [BALL MANIA](https://learnquester.github.io/ball-mania.html)
- [TRICKY CASTLE](https://studyquests.pages.dev/tricky-castle.html)
- [DELICIOUS EMILYS NEW BEGINNING VALENTINES EDITION](https://quizverses-9d2f2.web.app/delicious-emilys-new-beginning-valentines-edition.html)
- [SCREWDOM 3D](https://studyquests.github.io/screwdom-3d.html)
- [CATEGORY BIKE 2](https://studyquests.github.io/category-bike-2.html)
- [WIPE INSIGHT MASTER](https://studyquests.pages.dev/wipe-insight-master.html)
- [ROBYBOX SPACE STATION WAREHOUSE](https://quizverses.github.io/robybox-space-station-warehouse.html)
- [CATEGORY RACING DRIVING 2](https://studyplayings.web.app/category-racing-driving-2.html)
- [FUN TOWN PARKING](https://studyplayings.web.app/fun-town-parking.html)
- [CATEGORY BATTLE](https://quizverses.github.io/category-battle.html)
- [FIND OBJECTS HIDDEN ITEM](https://studyquests.pages.dev/find-objects-hidden-item.html)
- [KNOCK AND RUN 100 DOORS ESCAPE](https://studyquests.github.io/knock-and-run-100-doors-escape.html)
- [THE LAST TIGER TANK SIMULATOR](https://quizverses.pages.dev/the-last-tiger-tank-simulator.html)
- [ROYAL GARDEN MATCH](https://studyquests.pages.dev/royal-garden-match.html)
- [10K](https://studyquests.github.io/10k.html)
- [PRACTICE ON ME](https://quizverses.github.io/practice-on-me.html)
- [ICE FISHING 3D](https://studyplaying.github.io/ice-fishing-3d.html)
- [BFFS K POP FANGIRLS](https://studyplaying.github.io/bffs-k-pop-fangirls.html)
- [BALL JUMP SWITCH THE COLORS](https://learnquester.github.io/ball-jump-switch-the-colors.html)
- [SWAT PLANTS VS ZOMBIES](https://studyquests.pages.dev/swat-plants-vs-zombies.html)
- [SKATING PARK](https://quizverses-9d2f2.web.app/skating-park.html)
- [EGG ADVENTURE](https://studyquesthub.web.app/egg-adventure.html)
- [CATEGORY PHYSICS371](https://quizverses-9d2f2.web.app/category-physics371.html)
- [INDEX9](https://quizverses-9d2f2.web.app/index9.html)
- [PUSH PUSH CAT](https://studyquesthub.web.app/push-push-cat.html)
- [THE SURVEY](https://quizverses.github.io/the-survey.html)
- [CATEGORY SIMULATION 4](https://studyquests.github.io/category-simulation-4.html)
- [CATEGORY SHOOTER](https://studyquests.github.io/category-shooter.html)
- [TOW N GO](https://quizverses-9d2f2.web.app/tow-n-go.html)
- [WOOD BLOCK JAM](https://studyquests.github.io/wood-block-jam.html)
- [LEGEND OF FIREBALL](https://learnquester.github.io/legend-of-fireball.html)
- [CATEGORY BASKETBALL 2](https://studyquesthub.web.app/category-basketball-2.html)
- [RESIDENT EVIL PURGE OPERATION](https://quizverses.github.io/resident-evil-purge-operation.html)
- [SAFARI STORY MAHJONG](https://studyplaying.github.io/safari-story-mahjong.html)
- [CATEGORY STICKMAN 2](https://studyplayings.web.app/category-stickman-2.html)
- [INDEX22](https://studyplaying.github.io/index22.html)
- [SITEMAP](https://brainquests.onrender.com/sitemap.html)
- [CANDY MAKER DESSERT GAMES](https://studyplaying.github.io/candy-maker-dessert-games.html)
- [WATER SORT COLLECTIONS](https://studyquests.pages.dev/water-sort-collections.html)
- [SNAKE GO ESCAPE PUZZLE](https://studyplayings.pages.dev/snake-go-escape-puzzle.html)
- [BOW AND ARROW](https://learnquester.github.io/bow-and-arrow.html)
- [SPIDER EVOLUTION](https://studyplayings.pages.dev/spider-evolution.html)
- [INDEX5](https://quizverses-9d2f2.web.app/index5.html)
- [GOON BALL](https://quizverses-9d2f2.web.app/goon-ball.html)
- [CATEGORY BIKE63](https://studyquests.pages.dev/category-bike63.html)
- [CATEGORY ADVENTURE](https://studyquests.pages.dev/category-adventure.html)
- [INDEX5](https://studyquesthub.web.app/index5.html)
- [TANK SNIPER 3D](https://studyplayings.pages.dev/tank-sniper-3d.html)
- [OBBY PARKOUR RACING](https://studyplayings.pages.dev/obby-parkour-racing.html)
- [WAR LANDS](https://studyquests.pages.dev/war-lands.html)
- [THE FLOWERS MERGE AND SELL BOUQUETS](https://quizverses-9d2f2.web.app/the-flowers-merge-and-sell-bouquets.html)
- [CATEGORY SPEED158](https://studyplayings.web.app/category-speed158.html)
- [GUN BUILDER](https://quizverses.pages.dev/gun-builder.html)
- [WAR STATE IO CONQUER BATTLES](https://learnquester.github.io/war-state-io-conquer-battles.html)
- [BATTLE ISLAND 2](https://studyquests.github.io/battle-island-2.html)
- [GENFIRE](https://studyquests.github.io/genfire.html)
- [RUN FROM BABA YAGA](https://learnquester.github.io/run-from-baba-yaga.html)
- [BEAM DRIVE CAR CRASH TEST SIMULATOR](https://studyplayings.pages.dev/beam-drive-car-crash-test-simulator.html)
- [CATEGORY HORROR 2](https://studyplaying.github.io/category-horror-2.html)
- [ROPE COLOR SORT 3D](https://studyplayings.pages.dev/rope-color-sort-3d.html)
- [ACE CAR RACING](https://studyplaying.github.io/ace-car-racing.html)
- [PARKING DRIVER](https://studyplaying.github.io/parking-driver.html)
- [RUSSIAN TREASURE HUNTER](https://quizverses.pages.dev/russian-treasure-hunter.html)
