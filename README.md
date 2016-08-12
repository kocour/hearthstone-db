# Hearthstone-DB

A collection of all Hearthstone cards in a JSON format for all purposes.

Updated to GVG

[Download](https://www.dropbox.com/s/l6je7qjjqeogkiz/hs-images.zip) all images here.

## How to install

Choose one of these methods

```
npm install hearthstone-db --save
bower install hearthstone-db --save
git clone git://github.com/pdyck/hearthstone-db.git
```

## How to use with npm

The module is an json object with this structure:

```
hearthstone-db:
	- allCards
	- allCollectibles
	- brm
	- gvg
	- kar
	- loe
	- naxxramas
	- tgt
	- wtog
```


## JSON object structure

```
id: integer,
name: string,
description: string,
image_url: string,
hero: string
	- "neutral"
	- "druid"
	- "hunter"
	- "mage",
	- "paladin"
	- "priest"
	- "rogue"
	- "shaman"
	- "warlock"
	- "warrior",
category: string
	- "minion"
	- "spell"
	- "secret"
	- "weapon",
quality: string
	- "free"
	- "common"
	- "rare"
	- "epic"
	- "legendary",
race: string
	- "none"
	- "beast"
	- "demon"
	- "dragon"
	- "pirate"
	- "murloc"
	- "totem"
	- "mech",
set: string
	- "basic"
	- "expert"
	- "naxxramas"
	- "gvg"
	- "brm"
	- "kar"
	- "loe"
	- "tgt"
	- "wtog",
mana: integer,
attack: integer,
health: integer,
collectible: boolean,
effect_list: array
	- effect: string
		- "battlecry"
		- "charge"
		- "deathrattle"
		- "divine_shield"
		- "enrage"
		- "secret"
		- "stealth"
		- "taunt"
		- "windfury"
	- extra: string
```

## Files

```
cards:
	- all-cards.json ([Almost] all cards in the game)
	- all-collectibles.json (All cards you can have in your collection)
	- brm.json (All Blackrock Mountain cards)
	- gvg.json (All GvG cards)
	- naxxramas.json (All Naxx cards)

```
