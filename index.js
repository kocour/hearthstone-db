const allCards = require('./cards/all-cards.json');
const allCollectibles = require('./cards/all-collectibles.json');
const brm = require('./cards/brm.json');
const gadgetzan = require('./cards/gadgetzan.json')
const gvg = require('./cards/gvg.json');
const kar = require('./cards/kar.json');
const loe = require('./cards/loe.json');
const naxxramas = require('./cards/naxxramas.json');
const tgt = require('./cards/tgt.json');
const wtog = require('./cards/wtog.json');

module.exports = {
    meta: allCards.meta,
    allCards: allCards.cards,
    allCollectibles: allCollectibles.cards,
    brm: brm.cards,
    gadgetzan: gadgetzan.cards,
    gvg: gvg.cards,
    kar: kar.cards,
    loe: loe.cards,
    naxxramas: naxxramas.cards,
    tgt: tgt.cards,
    wtog: wtog.cards
};
