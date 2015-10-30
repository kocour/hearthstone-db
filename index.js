var allCards = require('./cards/all-cards.json');
var allCollectibles = require('./cards/all-collectibles.json');
var brm = require('./cards/brm.json');
var gvg = require('./cards/gvg.json');
var naxxramas = require('./cards/naxxramas.json');
var tgt = require('./cards/tgt.json');

module.exports = {
    meta: allCards.meta,
    allCards: allCards.cards,
    allCollectibles: allCollectibles.cards,
    brm: brm.cards,
    gvg: gvg.cards,
    naxxramas: naxxramas.cards,
    tgt: tgt.cards
};