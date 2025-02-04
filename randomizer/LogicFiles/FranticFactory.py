# fmt: off
"""Logic file for Frantic Factory."""

from re import L

from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MinigameType import MinigameType
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.LogicClasses import (Event, LocationLogic, Region,
                                     TransitionFront)

LogicRegions = {
    Regions.FranticFactoryStart: Region("Frantic Factory Start", Levels.FranticFactory, False, None, [
        LocationLogic(Locations.FactoryDonkeyMedal, lambda l: l.ColoredBananas[Levels.FranticFactory][Kongs.donkey] >= 75),
        LocationLogic(Locations.FactoryDiddyMedal, lambda l: l.ColoredBananas[Levels.FranticFactory][Kongs.diddy] >= 75),
        LocationLogic(Locations.FactoryLankyMedal, lambda l: l.ColoredBananas[Levels.FranticFactory][Kongs.lanky] >= 75),
        LocationLogic(Locations.FactoryTinyMedal, lambda l: l.ColoredBananas[Levels.FranticFactory][Kongs.tiny] >= 75),
        LocationLogic(Locations.FactoryChunkyMedal, lambda l: l.ColoredBananas[Levels.FranticFactory][Kongs.chunky] >= 75),
    ], [
        Event(Events.FactoryEntered, lambda l: True),
        Event(Events.HatchOpened, lambda l: l.Slam),
    ], [
        TransitionFront(Regions.FranticFactoryLobby, lambda l: True, Transitions.FactoryToIsles),
        TransitionFront(Regions.Testing, lambda l: l.settings.open_levels or Events.TestingGateOpened in l.Events),
        # Hatch opened already in rando if loading zones randomized
        TransitionFront(Regions.BeyondHatch, lambda l: l.settings.shuffle_loading_zones == "all" or Events.HatchOpened in l.Events),
    ]),

    Regions.Testing: Region("Testing", Levels.FranticFactory, True, None, [
        LocationLogic(Locations.FactoryDonkeyNumberGame, lambda l: l.Slam and l.donkey),
        LocationLogic(Locations.FactoryDiddyBlockTower, lambda l: l.spring and l.isdiddy, MinigameType.BonusBarrel),
        LocationLogic(Locations.FactoryLankyTestingRoomBarrel, lambda l: l.balloon and l.islanky, MinigameType.BonusBarrel),
        LocationLogic(Locations.FactoryTinyDartboard, lambda l: Events.DartsPlayed in l.Events and l.tiny),
        LocationLogic(Locations.FactoryKasplatBlocks, lambda l: not l.settings.kasplat_location_rando),
        LocationLogic(Locations.FactoryBananaFairybyCounting, lambda l: l.camera),
        LocationLogic(Locations.FactoryBananaFairybyFunky, lambda l: l.camera and Events.DartsPlayed in l.Events),
    ], [
        Event(Events.DartsPlayed, lambda l: l.Slam and l.mini and l.feather and l.tiny),
    ], [
        TransitionFront(Regions.FranticFactoryStart, lambda l: Events.TestingGateOpened in l.Events),
        TransitionFront(Regions.RandD, lambda l: True),
        TransitionFront(Regions.Snide, lambda l: True),
        TransitionFront(Regions.FunkyFactory, lambda l: True),
        TransitionFront(Regions.FactoryBossLobby, lambda l: True),
    ]),

    Regions.RandD: Region("R&D", Levels.FranticFactory, True, -1, [
        LocationLogic(Locations.FactoryDiddyRandD, lambda l: l.guitar and l.charge and l.diddy),
        LocationLogic(Locations.FactoryLankyRandD, lambda l: l.trombone and l.Slam and l.lanky),
        LocationLogic(Locations.FactoryChunkyRandD, lambda l: l.triangle and l.punch and l.hunkyChunky and l.chunky),
        LocationLogic(Locations.FactoryKasplatRandD, lambda l: not l.settings.kasplat_location_rando),
        LocationLogic(Locations.FactoryBattleArena, lambda l: l.grab and l.donkey),
    ], [], [
        TransitionFront(Regions.Testing, lambda l: True),
        TransitionFront(Regions.FactoryTinyRaceLobby, lambda l: l.mini and l.istiny),
        TransitionFront(Regions.ChunkyRoomPlatform, lambda l: True),
        TransitionFront(Regions.FactoryBossLobby, lambda l: True),
    ]),

    Regions.FactoryTinyRaceLobby: Region("Factory Tiny Race Lobby", Levels.FranticFactory, False, None, [
        LocationLogic(Locations.FactoryTinyCarRace, lambda l: l.istiny),
    ], [], [
        TransitionFront(Regions.RandD, lambda l: l.mini and l.istiny),
        TransitionFront(Regions.FactoryTinyRace, lambda l: l.mini and l.istiny, Transitions.FactoryRandDToRace)
    ]),

    Regions.FactoryTinyRace: Region("Factory Tiny Race", Levels.FranticFactory, False, None, [
        LocationLogic(Locations.FactoryTinyCarRace, lambda l: l.istiny),
    ], [], [
        TransitionFront(Regions.FactoryTinyRaceLobby, lambda l: True, Transitions.FactoryRaceToRandD),
    ], Transitions.FactoryRandDToRace
    ),

    Regions.ChunkyRoomPlatform: Region("Chunky Room Platform", Levels.FranticFactory, False, -1, [
        LocationLogic(Locations.FactoryDiddyChunkyRoomBarrel, lambda l: l.Slam and l.isdiddy, MinigameType.BonusBarrel),
    ], [], [
        TransitionFront(Regions.PowerHut, lambda l: l.coconut and l.isdonkey, Transitions.FactoryChunkyRoomToPower),
        TransitionFront(Regions.BeyondHatch, lambda l: True),
    ]),

    Regions.PowerHut: Region("Power Hut", Levels.FranticFactory, False, None, [
        LocationLogic(Locations.FactoryDonkeyPowerHut, lambda l: Events.MainCoreActivated in l.Events and l.isdonkey),
    ], [
        Event(Events.MainCoreActivated, lambda l: l.settings.high_req or (l.coconut and l.grab and l.isdonkey)),
    ], [
        TransitionFront(Regions.ChunkyRoomPlatform, lambda l: True, Transitions.FactoryPowerToChunkyRoom),
    ]),

    Regions.BeyondHatch: Region("Beyond Hatch", Levels.FranticFactory, True, None, [
        LocationLogic(Locations.ChunkyKong, lambda l: l.CanFreeChunky()),
        LocationLogic(Locations.NintendoCoin, lambda l: Events.ArcadeLeverSpawned in l.Events and l.grab and l.donkey),
        LocationLogic(Locations.FactoryDonkeyDKArcade, lambda l: Events.ArcadeLeverSpawned in l.Events and l.grab and l.donkey),
        LocationLogic(Locations.FactoryLankyFreeChunky, lambda l: l.Slam and l.HasKong(l.settings.chunky_freeing_kong)),
        LocationLogic(Locations.FactoryTinybyArcade, lambda l: l.mini and l.tiny),
        LocationLogic(Locations.FactoryChunkyDarkRoom, lambda l: l.punch and l.Slam and l.chunky),
        LocationLogic(Locations.FactoryChunkybyArcade, lambda l: l.punch and l.ischunky, MinigameType.BonusBarrel),
        LocationLogic(Locations.FactoryKasplatProductionBottom, lambda l: not l.settings.kasplat_location_rando),
        LocationLogic(Locations.FactoryKasplatStorage, lambda l: not l.settings.kasplat_location_rando),
    ], [
        Event(Events.TestingGateOpened, lambda l: l.Slam),
        Event(Events.DiddyCoreSwitch, lambda l: l.Slam and l.diddy),
        Event(Events.LankyCoreSwitch, lambda l: l.Slam and l.lanky),
        Event(Events.TinyCoreSwitch, lambda l: l.Slam and l.tiny),
        Event(Events.ChunkyCoreSwitch, lambda l: l.Slam and l.chunky),
    ], [
        TransitionFront(Regions.FranticFactoryStart, lambda l: l.settings.shuffle_loading_zones == "all" or Events.HatchOpened in l.Events),
        TransitionFront(Regions.InsideCore, lambda l: Events.MainCoreActivated in l.Events, Transitions.FactoryBeyondHatchToInsideCore),
        TransitionFront(Regions.MiddleCore, lambda l: Events.MainCoreActivated in l.Events),
        TransitionFront(Regions.CrankyFactory, lambda l: True),
        TransitionFront(Regions.CandyFactory, lambda l: True),
        TransitionFront(Regions.FactoryBossLobby, lambda l: True),
        TransitionFront(Regions.FactoryBaboonBlast, lambda l: l.blast and l.isdonkey)  # , Transitions.FactoryMainToBBlast)
    ]),

    Regions.FactoryBaboonBlast: Region("Factory Baboon Blast", Levels.FranticFactory, False, None, [], [
        Event(Events.ArcadeLeverSpawned, lambda l: l.isdonkey)
    ], [
        TransitionFront(Regions.BeyondHatch, lambda l: True)
    ]),

    Regions.InsideCore: Region("Inside Core", Levels.FranticFactory, False, -1, [
        LocationLogic(Locations.FactoryDonkeyCrusherRoom, lambda l: l.strongKong and l.isdonkey),
    ], [], [
        TransitionFront(Regions.BeyondHatch, lambda l: True, Transitions.FactoryInsideCoreToBeyondHatch),
    ]),

    Regions.MiddleCore: Region("Middle Core", Levels.FranticFactory, True, -1, [
        LocationLogic(Locations.FactoryChunkyProductionRoom, lambda l: Events.ChunkyCoreSwitch in l.Events and Events.MainCoreActivated in l.Events and l.chunky),
    ], [], [
        TransitionFront(Regions.BeyondHatch, lambda l: True),
        TransitionFront(Regions.UpperCore, lambda l: Events.MainCoreActivated in l.Events),
    ]),

    Regions.UpperCore: Region("Upper Core", Levels.FranticFactory, False, -1, [
        LocationLogic(Locations.FactoryDiddyProductionRoom, lambda l: Events.DiddyCoreSwitch in l.Events and Events.MainCoreActivated in l.Events and l.spring and l.diddy),
        LocationLogic(Locations.FactoryLankyProductionRoom, lambda l: Events.LankyCoreSwitch in l.Events and Events.MainCoreActivated in l.Events and l.handstand and l.lanky),
        LocationLogic(Locations.FactoryTinyProductionRoom, lambda l: Events.TinyCoreSwitch in l.Events and Events.MainCoreActivated in l.Events and l.twirl and l.istiny, MinigameType.BonusBarrel),
        LocationLogic(Locations.FactoryKasplatProductionTop, lambda l: not l.settings.kasplat_location_rando)
    ], [], [
        TransitionFront(Regions.BeyondHatch, lambda l: True),
        TransitionFront(Regions.MiddleCore, lambda l: True),
    ]),

    Regions.FactoryBossLobby: Region("Factory Boss Lobby", Levels.FranticFactory, False, None, [], [], [
        TransitionFront(Regions.FactoryBoss, lambda l: l.IsBossReachable(Levels.FranticFactory)),
    ]),

    Regions.FactoryBoss: Region("Factory Boss", Levels.FranticFactory, False, None, [
        LocationLogic(Locations.FactoryKey, lambda l: l.IsBossBeatable(Levels.FranticFactory)),
    ], [], []),
}
