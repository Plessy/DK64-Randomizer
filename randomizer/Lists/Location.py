# fmt: off
"""Stores the Location class and a list of each location in the game."""

from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MoveTypes import MoveTypes
from randomizer.Enums.Types import Types
from randomizer.Lists.MapsAndExits import Maps, getLevelFromMap


class MapIDCombo:
    """A combination of a map and an associated item ID. If id == -1 and map == 0, has no model 2 item, ignore those."""

    def __init__(self, map=None, id=None, flag=None, kong=Kongs.any):
        """Initialize with given parameters."""
        self.map = map
        self.id = id
        self.flag = flag
        self.kong = kong


class Location:
    """A shufflable location at which a random item can be placed."""

    def __init__(self, name, default, type, data=None):
        """Initialize with given parameters."""
        if data is None:
            data = []
        self.name = name
        self.default = default
        self.type = type
        self.item = None
        self.delayedItem = None
        self.constant = False
        self.map_id_list = None
        helmmedal_locations = (
            "Helm Donkey Medal",
            "Helm Diddy Medal",
            "Helm Lanky Medal",
            "Helm Tiny Medal",
            "Helm Chunky Medal",
        )
        if type == Types.Shop:
            self.level = data[0]
            self.kong = data[1]
            self.movetype = data[2]
            self.index = data[3]
        elif type == Types.Blueprint:
            self.map = data[0]
            self.kong = data[1]
            level = getLevelFromMap(data[0])
            if level is None:
                level = 0
            elif level in (Levels.DKIsles, Levels.HideoutHelm):
                level = 7
            self.map_id_list = [MapIDCombo(0, -1, 469 + data[1] + (5 * level), data[1])]
        elif type == Types.Medal and name not in helmmedal_locations:
            level = data[0]
            if level is None:
                level = 0
            elif level in (Levels.DKIsles, Levels.HideoutHelm):
                level = 7
            self.map_id_list = [MapIDCombo(0, -1, 549 + data[1] + (5 * level), data[1])]
        elif type in (Types.Banana, Types.Key, Types.Coin, Types.Crown, Types.Medal):
            if "Turn In " not in name:
                if data is None:
                    self.map_id_list = []
                else:
                    self.map_id_list = data
        self.default_mapid_data = self.map_id_list

    def PlaceItem(self, item):
        """Place item at this location."""
        self.item = item

    def PlaceConstantItem(self, item):
        """Place item at this location, and set constant so it's ignored in the spoiler."""
        self.item = item
        self.constant = True

    def SetDelayedItem(self, item):
        """Set an item to be added back later."""
        self.delayedItem = item

    def PlaceDelayedItem(self):
        """Place the delayed item at this location."""
        self.item = self.delayedItem
        self.delayedItem = None

    def PlaceDefaultItem(self):
        """Place whatever this location's default (vanilla) item is at it."""
        self.item = self.default
        self.constant = True


LocationList = {
    # DK Isles locations
    Locations.IslesVinesTrainingBarrel: Location("Isles Vines Training Barrel", Items.Vines, Types.TrainingBarrel),
    Locations.IslesSwimTrainingBarrel: Location("Isles Swim Training Barrel", Items.Swim, Types.TrainingBarrel),
    Locations.IslesOrangesTrainingBarrel: Location("Isles Oranges Training Barrel", Items.Oranges, Types.TrainingBarrel),
    Locations.IslesBarrelsTrainingBarrel: Location("Isles Barrels Training Barrel", Items.Barrels, Types.TrainingBarrel),
    Locations.IslesDonkeyJapesRock: Location("Isles Donkey Japes Rock", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Isles, 0x4, 381, Kongs.donkey)]),
    Locations.IslesTinyCagedBanana: Location("Isles Tiny Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Isles, 0x2B, 420, Kongs.tiny)]),
    Locations.IslesTinyInstrumentPad: Location("Isles Tiny Instrument Pad", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 425, Kongs.tiny)]),
    Locations.IslesLankyCagedBanana: Location("Isles Lanky Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Isles, 0x2F, 421, Kongs.lanky)]),
    Locations.IslesChunkyCagedBanana: Location("Isles Chunky Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Isles, 0x2D, 422, Kongs.chunky)]),
    Locations.IslesChunkyInstrumentPad: Location("Isles Chunky Instrument Pad", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 424, Kongs.chunky)]),
    Locations.IslesChunkyPoundtheX: Location("Isles Chunky Pound the X", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Isles, 0x56, 431, Kongs.chunky)]),
    Locations.IslesBananaFairyIsland: Location("Isles Banana Fairy Island", Items.BananaFairy, Types.Fairy),
    Locations.IslesBananaFairyCrocodisleIsle: Location("Isles Banana Fairy Crocodisle Isle", Items.BananaFairy, Types.Fairy),
    Locations.IslesLankyPrisonOrangsprint: Location("Isles Lanky Prison Orangsprint", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.KLumsy, 0x3, 429, Kongs.lanky)]),
    Locations.CameraAndShockwave: Location("Camera and Shockwave", Items.CameraAndShockwave, Types.Shockwave),
    Locations.RarewareBanana: Location("Rareware Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.BananaFairyRoom, 0x1E, 301, Kongs.tiny)]),
    Locations.IslesLankyInstrumentPad: Location("Isles Lanky Instrument Pad", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 398, Kongs.lanky)]),
    Locations.IslesTinyAztecLobby: Location("Isles Tiny Aztec Lobby", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 402, Kongs.tiny)]),
    Locations.IslesDonkeyCagedBanana: Location("Isles Donkey Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Isles, 0x4D, 419, Kongs.donkey)]),
    Locations.IslesDiddySnidesLobby: Location("Isles Diddy Snides Lobby", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 416, Kongs.diddy)]),
    Locations.IslesBattleArena1: Location("Isles Battle Arena 1", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.SnidesCrown, -1, 615)]),
    Locations.IslesDonkeyInstrumentPad: Location("Isles Donkey Instrument Pad", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 404, Kongs.donkey)]),
    Locations.IslesKasplatFactoryLobby: Location("Isles Kasplat Frantic Factory Lobby", Items.DKIslesTinyBlueprint, Types.Blueprint, [Maps.FranticFactoryLobby, Kongs.tiny]),
    Locations.IslesBananaFairyFactoryLobby: Location("Isles Banana Fairy Factory Lobby", Items.BananaFairy, Types.Fairy),
    Locations.IslesTinyGalleonLobby: Location("Isles Tiny Galleon Lobby", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GloomyGalleonLobby, 0x9, 403)]),
    Locations.IslesKasplatGalleonLobby: Location("Isles Kasplat Gloomy Galleon Lobby", Items.DKIslesChunkyBlueprint, Types.Blueprint, [Maps.GloomyGalleonLobby, Kongs.chunky]),
    Locations.IslesDiddyCagedBanana: Location("Isles Diddy Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Isles, 0x2E, 423, Kongs.diddy)]),
    Locations.IslesDiddySummit: Location("Isles Diddy Summit", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 428, Kongs.diddy)]),
    Locations.IslesBattleArena2: Location("Isles Battle Arena 2", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.LobbyCrown, -1, 614)]),
    Locations.IslesBananaFairyForestLobby: Location("Isles Banana Fairy Forest Lobby", Items.BananaFairy, Types.Fairy),
    Locations.IslesDonkeyLavaBanana: Location("Isles Donkey Lava Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CrystalCavesLobby, 0x5, 411, Kongs.donkey)]),
    Locations.IslesDiddyInstrumentPad: Location("Isles Diddy Instrument Pad", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 410, Kongs.diddy)]),
    Locations.IslesKasplatCavesLobby: Location("Isles Kasplat Crystal Caves Lobby", Items.DKIslesLankyBlueprint, Types.Blueprint, [Maps.CrystalCavesLobby, Kongs.lanky]),
    Locations.IslesLankyCastleLobby: Location("Isles Lanky Castle Lobby", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 415, Kongs.lanky)]),
    Locations.IslesKasplatCastleLobby: Location("Isles Kasplat Creepy Castle Lobby", Items.DKIslesDiddyBlueprint, Types.Blueprint, [Maps.CreepyCastleLobby, Kongs.diddy]),
    Locations.IslesChunkyHelmLobby: Location("Isles Chunky Helm Lobby", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 406, Kongs.chunky)]),
    Locations.IslesKasplatHelmLobby: Location("Isles Kasplat Hideout Helm Lobby", Items.DKIslesDonkeyBlueprint, Types.Blueprint, [Maps.HideoutHelmLobby, Kongs.donkey]),
    Locations.BananaHoard: Location("Banana Hoard", Items.BananaHoard, Types.Constant),
    # Jungle Japes location
    Locations.JapesDonkeyMedal: Location("Japes Donkey Medal", Items.BananaMedal, Types.Medal, [Levels.JungleJapes, Kongs.donkey]),
    Locations.JapesDiddyMedal: Location("Japes Diddy Medal", Items.BananaMedal, Types.Medal, [Levels.JungleJapes, Kongs.diddy]),
    Locations.JapesLankyMedal: Location("Japes Lanky Medal", Items.BananaMedal, Types.Medal, [Levels.JungleJapes, Kongs.lanky]),
    Locations.JapesTinyMedal: Location("Japes Tiny Medal", Items.BananaMedal, Types.Medal, [Levels.JungleJapes, Kongs.tiny]),
    Locations.JapesChunkyMedal: Location("Japes Chunky Medal", Items.BananaMedal, Types.Medal, [Levels.JungleJapes, Kongs.chunky]),
    Locations.DiddyKong: Location("Diddy Kong", Items.Diddy, Types.Kong),
    Locations.JapesDonkeyFrontofCage: Location("Japes Donkey Front of Cage", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x69, 4, Kongs.donkey)]),
    Locations.JapesDonkeyFreeDiddy: Location("Japes Donkey Free Diddy", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x48, 5, Kongs.donkey)]),
    Locations.JapesDonkeyCagedBanana: Location("Japes Donkey Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x44, 20, Kongs.donkey)]),
    Locations.JapesDonkeyBaboonBlast: Location("Japes Donkey Baboon Blast", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JapesBaboonBlast, 1, 3, Kongs.donkey)]),
    Locations.JapesDiddyCagedBanana: Location("Japes Diddy Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x4D, 18, Kongs.diddy)]),
    Locations.JapesDiddyMountain: Location("Japes Diddy Mountain", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x52, 23, Kongs.diddy)]),
    Locations.JapesLankyCagedBanana: Location("Japes Lanky Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x4F, 19, Kongs.lanky)]),
    Locations.JapesTinyCagedBanana: Location("Japes Tiny Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x4C, 21, Kongs.tiny)]),
    Locations.JapesChunkyBoulder: Location("Japes Chunky Boulder", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 25, Kongs.chunky)]),
    Locations.JapesChunkyCagedBanana: Location("Japes Chunky Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x50, 22, Kongs.chunky)]),
    Locations.JapesBattleArena: Location("Japes Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.JapesCrown, -1, 609)]),
    Locations.JapesDiddyTunnel: Location("Japes Diddy Tunnel", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x1E, 31, Kongs.diddy)]),
    Locations.JapesLankyGrapeGate: Location("Japes Lanky Grape Gate", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 1, Kongs.lanky)]),
    Locations.JapesTinyFeatherGateBarrel: Location("Japes Tiny Feather Gate Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 2, Kongs.tiny)]),
    Locations.JapesKasplatLeftTunnelNear: Location("Japes Kasplat Left Tunnel (Near)", Items.JungleJapesDonkeyBlueprint, Types.Blueprint, [Maps.JungleJapes, Kongs.donkey]),
    Locations.JapesKasplatLeftTunnelFar: Location("Japes Kasplat Left Tunnel (Far)", Items.JungleJapesTinyBlueprint, Types.Blueprint, [Maps.JungleJapes, Kongs.tiny]),
    Locations.JapesTinyStump: Location("Japes Tiny Stump", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JungleJapes, 0x68, 8, Kongs.tiny)]),
    Locations.JapesChunkyGiantBonusBarrel: Location("Japes Chunky Giant Bonus Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 28, Kongs.chunky)]),
    Locations.JapesTinyBeehive: Location("Japes Tiny Beehive", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JapesTinyHive, 0x3F, 9, Kongs.tiny)]),
    Locations.JapesLankySlope: Location("Japes Lanky Slope", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 11, Kongs.lanky)]),
    Locations.JapesKasplatNearPaintingRoom: Location("Japes Kasplat Near Painting Room", Items.JungleJapesDiddyBlueprint, Types.Blueprint, [Maps.JungleJapes, Kongs.diddy]),
    Locations.JapesKasplatNearLab: Location("Japes Kasplat Near Cranky's Lab", Items.JungleJapesLankyBlueprint, Types.Blueprint, [Maps.JungleJapes, Kongs.lanky]),
    Locations.JapesBananaFairyRambiCave: Location("Japes Banana Fairy Rambi Cave", Items.BananaFairy, Types.Fairy),
    Locations.JapesLankyFairyCave: Location("Japes Lanky Fairy Cave", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JapesLankyCave, 0x4, 10, Kongs.lanky)]),
    Locations.JapesBananaFairyLankyCave: Location("Japes Banana Fairy Lanky Cave", Items.BananaFairy, Types.Fairy),
    Locations.JapesDiddyMinecarts: Location("Japes Diddy Minecarts", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 24, Kongs.diddy)]),
    Locations.JapesChunkyUnderground: Location("Japes Chunky Underground", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.JapesUnderGround, 0x3, 12, Kongs.chunky)]),
    Locations.JapesKasplatUnderground: Location("Japes Kasplat Underground", Items.JungleJapesChunkyBlueprint, Types.Blueprint, [Maps.JapesUnderGround, Kongs.chunky]),
    Locations.JapesKey: Location("Japes Key", Items.JungleJapesKey, Types.Key, [MapIDCombo(0, -1, 26)]),
    # Angry Aztec
    Locations.AztecDonkeyMedal: Location("Aztec Donkey Medal", Items.BananaMedal, Types.Medal, [Levels.AngryAztec, Kongs.donkey]),
    Locations.AztecDiddyMedal: Location("Aztec Diddy Medal", Items.BananaMedal, Types.Medal, [Levels.AngryAztec, Kongs.diddy]),
    Locations.AztecLankyMedal: Location("Aztec Lanky Medal", Items.BananaMedal, Types.Medal, [Levels.AngryAztec, Kongs.lanky]),
    Locations.AztecTinyMedal: Location("Aztec Tiny Medal", Items.BananaMedal, Types.Medal, [Levels.AngryAztec, Kongs.tiny]),
    Locations.AztecChunkyMedal: Location("Aztec Chunky Medal", Items.BananaMedal, Types.Medal, [Levels.AngryAztec, Kongs.chunky]),
    Locations.AztecDonkeyFreeLlama: Location("Aztec Donkey Free Llama", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AngryAztec, 0x26, 51, Kongs.donkey)]),
    Locations.AztecChunkyVases: Location("Aztec Chunky Vases", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AngryAztec, 0x23, 49, Kongs.chunky)]),
    Locations.AztecKasplatSandyBridge: Location("Aztec Kasplat Sandy Bridge", Items.AngryAztecDonkeyBlueprint, Types.Blueprint, [Maps.AngryAztec, Kongs.donkey]),
    Locations.AztecKasplatOnTinyTemple: Location("Aztec Kasplat On Tiny Temple", Items.AngryAztecDiddyBlueprint, Types.Blueprint, [Maps.AngryAztec, Kongs.diddy]),
    Locations.AztecTinyKlaptrapRoom: Location("Aztec Tiny Klaptrap Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecTinyTemple, 0x7E, 65, Kongs.tiny)]),
    Locations.AztecChunkyKlaptrapRoom: Location("Aztec Chunky Klaptrap Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecTinyTemple, 0x9, 64, Kongs.chunky)]),
    Locations.TinyKong: Location("Tiny Kong", Items.Tiny, Types.Kong),
    Locations.AztecDiddyFreeTiny: Location("Aztec Diddy Free Tiny", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecTinyTemple, 0x5B, 67, Kongs.diddy)]),
    Locations.AztecLankyVulture: Location("Aztec Lanky Vulture", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 68, Kongs.lanky)]),
    Locations.AztecBattleArena: Location("Aztec Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.AztecCrown, -1, 610)]),
    Locations.AztecDonkeyQuicksandCave: Location("Aztec Donkey Quicksand Cave", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 62, Kongs.donkey)]),
    Locations.AztecDiddyRamGongs: Location("Aztec Diddy Ram Gongs", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AngryAztec, 0xA3, 54, Kongs.diddy)]),
    Locations.AztecDiddyVultureRace: Location("Aztec Diddy Vulture Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AngryAztec, 0xEB, 63, Kongs.diddy)]),
    Locations.AztecChunkyCagedBarrel: Location("Aztec Chunky Caged Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 52, Kongs.chunky)]),
    Locations.AztecKasplatNearLab: Location("Aztec Kasplat Near Cranky's Lab", Items.AngryAztecTinyBlueprint, Types.Blueprint, [Maps.AngryAztec, Kongs.tiny]),
    Locations.AztecDonkey5DoorTemple: Location("Aztec Donkey 5 Door Temple", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecDonkey5DTemple, 0x6, 57, Kongs.donkey)]),
    Locations.AztecDiddy5DoorTemple: Location("Aztec Diddy 5 Door Temple", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecDiddy5DTemple, 0x6, 56, Kongs.diddy)]),
    Locations.AztecLanky5DoorTemple: Location("Aztec Lanky 5 Door Temple", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 60, Kongs.lanky)]),
    Locations.AztecTiny5DoorTemple: Location("Aztec Tiny 5 Door Temple", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecTiny5DTemple, 0x6, 58, Kongs.tiny)]),
    Locations.AztecBananaFairyTinyTemple: Location("Aztec Banana Fairy Tiny Temple", Items.BananaFairy, Types.Fairy),
    Locations.AztecChunky5DoorTemple: Location("Aztec Chunky 5 Door Temple", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 59, Kongs.chunky)]),
    Locations.AztecKasplatChunky5DT: Location("Aztec Kasplat Inside Chunky's 5-Door Temple", Items.AngryAztecChunkyBlueprint, Types.Blueprint, [Maps.AztecChunky5DTemple, Kongs.chunky]),
    Locations.AztecTinyBeetleRace: Location("Aztec Tiny Beetle Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecTinyRace, 0x48, 75, Kongs.tiny)]),
    Locations.LankyKong: Location("Lanky Kong", Items.Lanky, Types.Kong),
    Locations.AztecDonkeyFreeLanky: Location("Aztec Donkey Free Lanky", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecLlamaTemple, 0x6C, 77, Kongs.donkey)]),
    Locations.AztecLankyLlamaTempleBarrel: Location("Aztec Lanky Llama Temple Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 73, Kongs.lanky)]),
    Locations.AztecLankyMatchingGame: Location("Aztec Lanky Matching Game", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecLlamaTemple, 0x2B, 72, Kongs.lanky)]),
    Locations.AztecBananaFairyLlamaTemple: Location("Aztec Banana Fairy Llama Temple", Items.BananaFairy, Types.Fairy),
    Locations.AztecTinyLlamaTemple: Location("Aztec Tiny Llama Temple", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.AztecLlamaTemple, 0xAA, 71, Kongs.tiny)]),
    Locations.AztecKasplatLlamaTemple: Location("Aztec Kasplat Inside Llama Temple", Items.AngryAztecLankyBlueprint, Types.Blueprint, [Maps.AztecLlamaTemple, Kongs.lanky]),
    Locations.AztecKey: Location("Aztec Key", Items.AngryAztecKey, Types.Key, [MapIDCombo(0, -1, 74)]),
    # Frantic Factory locations
    Locations.FactoryDonkeyMedal: Location("Factory Donkey Medal", Items.BananaMedal, Types.Medal, [Levels.FranticFactory, Kongs.donkey]),
    Locations.FactoryDiddyMedal: Location("Factory Diddy Medal", Items.BananaMedal, Types.Medal, [Levels.FranticFactory, Kongs.diddy]),
    Locations.FactoryLankyMedal: Location("Factory Lanky Medal", Items.BananaMedal, Types.Medal, [Levels.FranticFactory, Kongs.lanky]),
    Locations.FactoryTinyMedal: Location("Factory Tiny Medal", Items.BananaMedal, Types.Medal, [Levels.FranticFactory, Kongs.tiny]),
    Locations.FactoryChunkyMedal: Location("Factory Chunky Medal", Items.BananaMedal, Types.Medal, [Levels.FranticFactory, Kongs.chunky]),
    Locations.FactoryDonkeyNumberGame: Location("Factory Donkey Number Game", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x7E, 122, Kongs.donkey)]),
    Locations.FactoryDiddyBlockTower: Location("Factory Diddy Block Tower", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 135, Kongs.diddy)]),
    Locations.FactoryLankyTestingRoomBarrel: Location("Factory Lanky Testing Room Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 137, Kongs.lanky)]),
    Locations.FactoryTinyDartboard: Location("Factory Tiny Dartboard", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x82, 124, Kongs.tiny)]),
    Locations.FactoryKasplatBlocks: Location("Factory Kasplat Block Tower Room", Items.FranticFactoryChunkyBlueprint, Types.Blueprint, [Maps.FranticFactory, Kongs.chunky]),
    Locations.FactoryBananaFairybyCounting: Location("Factory Banana Fairy by Counting", Items.BananaFairy, Types.Fairy),
    Locations.FactoryBananaFairybyFunky: Location("Factory Banana Fairy by Funky", Items.BananaFairy, Types.Fairy),
    Locations.FactoryDiddyRandD: Location("Factory Diddy R&D", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x60, 126, Kongs.diddy)]),
    Locations.FactoryLankyRandD: Location("Factory Lanky R&D", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x3E, 125, Kongs.lanky)]),
    Locations.FactoryChunkyRandD: Location("Factory Chunky R&D", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x7C, 127, Kongs.chunky)]),
    Locations.FactoryKasplatRandD: Location("Factory Kasplat Research and Development", Items.FranticFactoryLankyBlueprint, Types.Blueprint, [Maps.FranticFactory, Kongs.lanky]),
    Locations.FactoryBattleArena: Location("Factory Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.FactoryCrown, -1, 611)]),
    Locations.FactoryTinyCarRace: Location("Factory Tiny Car Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FactoryTinyRace, 0x62, 139, Kongs.tiny)]),
    Locations.FactoryDiddyChunkyRoomBarrel: Location("Factory Diddy Chunky Room Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 134, Kongs.diddy)]),
    Locations.FactoryDonkeyPowerHut: Location("Factory Donkey Power Hut", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FactoryPowerHut, 0x2, 112, Kongs.donkey)]),
    Locations.ChunkyKong: Location("Chunky Kong", Items.Chunky, Types.Kong),
    Locations.NintendoCoin: Location("Nintendo Coin", Items.NintendoCoin, Types.Coin, [MapIDCombo(Maps.FranticFactory, 0x13E, 132)]),
    Locations.FactoryDonkeyDKArcade: Location("Factory Donkey DK Arcade", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x108, 130, Kongs.donkey), MapIDCombo(Maps.FactoryBaboonBlast, 0, 130, Kongs.donkey)]),
    Locations.FactoryLankyFreeChunky: Location("Factory Lanky Free Chunky", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x78, 118, Kongs.lanky)]),
    Locations.FactoryTinybyArcade: Location("Factory Tiny by Arcade", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x23, 123, Kongs.tiny)]),
    Locations.FactoryChunkyDarkRoom: Location("Factory Chunky Dark Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x63, 121, Kongs.chunky)]),
    Locations.FactoryChunkybyArcade: Location("Factory Chunky by Arcade", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 136, Kongs.chunky)]),
    Locations.FactoryKasplatProductionBottom: Location("Factory Kasplat Bottom of Production Room", Items.FranticFactoryDiddyBlueprint, Types.Blueprint, [Maps.FranticFactory, Kongs.diddy]),
    Locations.FactoryKasplatStorage: Location("Factory Kasplat Storage Room", Items.FranticFactoryTinyBlueprint, Types.Blueprint, [Maps.FranticFactory, Kongs.tiny]),
    Locations.FactoryDonkeyCrusherRoom: Location("Factory Donkey Crusher Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FactoryCrusher, 0x7, 128, Kongs.donkey)]),
    Locations.FactoryDiddyProductionRoom: Location("Factory Diddy Production Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x2C, 113, Kongs.diddy)]),
    Locations.FactoryLankyProductionRoom: Location("Factory Lanky Production Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x2A, 115, Kongs.lanky)]),
    Locations.FactoryTinyProductionRoom: Location("Factory Tiny Production Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 116, Kongs.tiny)]),
    Locations.FactoryChunkyProductionRoom: Location("Factory Chunky Production Room", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FranticFactory, 0x29, 114, Kongs.chunky)]),
    Locations.FactoryKasplatProductionTop: Location("Factory Kasplat Top of Production Room", Items.FranticFactoryDonkeyBlueprint, Types.Blueprint, [Maps.FranticFactory, Kongs.donkey]),
    Locations.FactoryKey: Location("Factory Key", Items.FranticFactoryKey, Types.Key, [MapIDCombo(0, -1, 138)]),
    # Gloomy Galleon locations
    Locations.GalleonDonkeyMedal: Location("Galleon Donkey Medal", Items.BananaMedal, Types.Medal, [Levels.GloomyGalleon, Kongs.donkey]),
    Locations.GalleonDiddyMedal: Location("Galleon Diddy Medal", Items.BananaMedal, Types.Medal, [Levels.GloomyGalleon, Kongs.diddy]),
    Locations.GalleonLankyMedal: Location("Galleon Lanky Medal", Items.BananaMedal, Types.Medal, [Levels.GloomyGalleon, Kongs.lanky]),
    Locations.GalleonTinyMedal: Location("Galleon Tiny Medal", Items.BananaMedal, Types.Medal, [Levels.GloomyGalleon, Kongs.tiny]),
    Locations.GalleonChunkyMedal: Location("Galleon Chunky Medal", Items.BananaMedal, Types.Medal, [Levels.GloomyGalleon, Kongs.chunky]),
    Locations.GalleonChunkyChest: Location("Galleon Chunky Chest", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GloomyGalleon, 0xE, 182, Kongs.chunky)]),
    Locations.GalleonKasplatNearLab: Location("Galleon Kasplat Near Cranky's Lab", Items.GloomyGalleonTinyBlueprint, Types.Blueprint, [Maps.GloomyGalleon, Kongs.tiny]),
    Locations.GalleonBattleArena: Location("Galleon Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.GalleonCrown, -1, 612)]),
    Locations.GalleonBananaFairybyCranky: Location("Galleon Banana Fairy by Cranky", Items.BananaFairy, Types.Fairy),
    Locations.GalleonChunkyCannonGame: Location("Galleon Chunky Cannon Game", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GloomyGalleon, 0x32, 154, Kongs.chunky)]),
    Locations.GalleonKasplatCannons: Location("Galleon Kasplat Cannon Room", Items.GloomyGalleonLankyBlueprint, Types.Blueprint, [Maps.GloomyGalleon, Kongs.lanky]),
    Locations.GalleonDiddyShipSwitch: Location("Galleon Diddy Ship Switch", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GloomyGalleon, 0x2D, 204, Kongs.diddy)]),
    Locations.GalleonLankyEnguardeChest: Location("Galleon Lanky Enguarde Chest", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GloomyGalleon, 0x6B, 192, Kongs.lanky)]),
    Locations.GalleonKasplatLighthouseArea: Location("Galleon Kasplat Lighthouse Area", Items.GloomyGalleonDiddyBlueprint, Types.Blueprint, [Maps.GloomyGalleon, Kongs.diddy]),
    Locations.GalleonDonkeyLighthouse: Location("Galleon Donkey Lighthouse", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GalleonLighthouse, 0x2F, 157, Kongs.donkey)]),
    Locations.GalleonTinyPearls: Location("Galleon Tiny Pearls", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GalleonMermaidRoom, 0xE, 191, Kongs.tiny)]),
    Locations.GalleonChunkySeasick: Location("Galleon Chunky Seasick", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GalleonSickBay, 0x6, 166, Kongs.chunky)]),
    Locations.GalleonDonkeyFreetheSeal: Location("Galleon Donkey Free the Seal", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GloomyGalleon, 0x2E, 193, Kongs.donkey)]),
    Locations.GalleonKasplatNearSub: Location("Galleon Kasplat Near Submarine", Items.GloomyGalleonChunkyBlueprint, Types.Blueprint, [Maps.GloomyGalleon, Kongs.chunky]),
    Locations.GalleonDonkeySealRace: Location("Galleon Donkey Seal Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GalleonSealRace, 0x3B, 165, Kongs.donkey)]),
    Locations.GalleonDiddyGoldTower: Location("Galleon Diddy Gold Tower", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 163, Kongs.diddy)]),
    Locations.GalleonLankyGoldTower: Location("Galleon Lanky Gold Tower", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 164, Kongs.lanky)]),
    Locations.GalleonKasplatGoldTower: Location("Galleon Kasplat Gold Tower Room", Items.GloomyGalleonDonkeyBlueprint, Types.Blueprint, [Maps.GloomyGalleon, Kongs.donkey]),
    Locations.GalleonTinySubmarine: Location("Galleon Tiny Submarine", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 202, Kongs.tiny)]),
    Locations.GalleonDiddyMechafish: Location("Galleon Diddy Mechafish", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.GalleonMechafish, 0xF, 167, Kongs.diddy)]),
    Locations.GalleonLanky2DoorShip: Location("Galleon Lanky 2 Door Ship", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Galleon2DShip, 0x0, 183, Kongs.lanky)]),
    Locations.GalleonTiny2DoorShip: Location("Galleon Tiny 2 Door Ship", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 184, Kongs.tiny)]),
    Locations.GalleonDonkey5DoorShip: Location("Galleon Donkey 5 Door Ship", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 200, Kongs.donkey)]),
    Locations.GalleonDiddy5DoorShip: Location("Galleon Diddy 5 Door Ship", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 198, Kongs.diddy)]),
    Locations.GalleonLanky5DoorShip: Location("Galleon Lanky 5 Door Ship", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Galleon5DShipDiddyLankyChunky, 0xE, 199, Kongs.lanky)]),
    Locations.GalleonTiny5DoorShip: Location("Galleon Tiny 5 Door Ship", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.Galleon5DShipDKTiny, 0x21, 201, Kongs.tiny)]),
    Locations.GalleonBananaFairy5DoorShip: Location("Galleon Banana Fairy 5 Door Ship", Items.BananaFairy, Types.Fairy),
    Locations.GalleonChunky5DoorShip: Location("Galleon Chunky 5 Door Ship", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 197, Kongs.chunky)]),
    Locations.GalleonKey: Location("Galleon Key", Items.GloomyGalleonKey, Types.Key, [MapIDCombo(0, -1, 168)]),
    # Fungi Forest locations
    Locations.ForestDonkeyMedal: Location("Forest Donkey Medal", Items.BananaMedal, Types.Medal, [Levels.FungiForest, Kongs.donkey]),
    Locations.ForestDiddyMedal: Location("Forest Diddy Medal", Items.BananaMedal, Types.Medal, [Levels.FungiForest, Kongs.diddy]),
    Locations.ForestLankyMedal: Location("Forest Lanky Medal", Items.BananaMedal, Types.Medal, [Levels.FungiForest, Kongs.lanky]),
    Locations.ForestTinyMedal: Location("Forest Tiny Medal", Items.BananaMedal, Types.Medal, [Levels.FungiForest, Kongs.tiny]),
    Locations.ForestChunkyMedal: Location("Forest Chunky Medal", Items.BananaMedal, Types.Medal, [Levels.FungiForest, Kongs.chunky]),
    Locations.ForestChunkyMinecarts: Location("Forest Chunky Minecarts", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 215, Kongs.chunky)]),
    Locations.ForestDiddyTopofMushroom: Location("Forest Diddy Top of Mushroom", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 211, Kongs.diddy)]),
    Locations.ForestTinyMushroomBarrel: Location("Forest Tiny Mushroom Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 227, Kongs.tiny)]),
    Locations.ForestDonkeyBaboonBlast: Location("Forest Donkey Baboon Blast", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FungiForest, 0x39, 254, Kongs.donkey)]),
    Locations.ForestKasplatLowerMushroomExterior: Location("Forest Kasplat Lower Giant Mushroom Exterior", Items.FungiForestTinyBlueprint, Types.Blueprint, [Maps.FungiForest, Kongs.tiny]),
    Locations.ForestDonkeyMushroomCannons: Location("Forest Donkey Mushroom Cannons", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestGiantMushroom, 0x3, 228, Kongs.donkey)]),
    Locations.ForestKasplatInsideMushroom: Location("Forest Kasplat Inside Giant Mushroom", Items.FungiForestDiddyBlueprint, Types.Blueprint, [Maps.ForestGiantMushroom, Kongs.diddy]),
    Locations.ForestKasplatUpperMushroomExterior: Location("Forest Kasplat Upper Giant Mushroom Exterior", Items.FungiForestChunkyBlueprint, Types.Blueprint, [Maps.FungiForest, Kongs.chunky]),
    Locations.ForestBattleArena: Location("Forest Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.ForestCrown, -1, 613)]),
    Locations.ForestChunkyFacePuzzle: Location("Forest Chunky Face Puzzle", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestChunkyFaceRoom, 0x2, 225, Kongs.chunky)]),
    Locations.ForestLankyZingers: Location("Forest Lanky Zingers", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestLankyZingersRoom, 0x0, 226, Kongs.lanky)]),
    Locations.ForestLankyColoredMushrooms: Location("Forest Lanky Colored Mushrooms", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 224, Kongs.lanky)]),
    Locations.ForestDiddyOwlRace: Location("Forest Diddy Owl Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 250, Kongs.diddy)]),
    Locations.ForestLankyRabbitRace: Location("Forest Lanky Rabbit Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FungiForest, 0x57, 249)]),
    Locations.ForestKasplatOwlTree: Location("Forest Kasplat Owl Tree", Items.FungiForestLankyBlueprint, Types.Blueprint, [Maps.FungiForest, Kongs.lanky]),
    Locations.ForestTinyAnthill: Location("Forest Tiny Anthill", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestAnthill, 0x0, 205, Kongs.tiny)]),
    Locations.ForestDonkeyMill: Location("Forest Donkey Mill", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FungiForest, 0x2B, 219, Kongs.donkey), MapIDCombo(Maps.ForestMillFront, 0xA, 219, Kongs.donkey)]),
    Locations.ForestDiddyCagedBanana: Location("Forest Diddy Caged Banana", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FungiForest, 0x28, 214, Kongs.diddy)]),
    Locations.ForestTinySpiderBoss: Location("Forest Tiny Spider Boss", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestSpider, 0x1, 247, Kongs.tiny)]),
    Locations.ForestChunkyKegs: Location("Forest Chunky Kegs", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestMillFront, 0xD, 221, Kongs.chunky)]),
    Locations.ForestDiddyRafters: Location("Forest Diddy Rafters", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestRafters, 0x3, 216, Kongs.diddy)]),
    Locations.ForestBananaFairyRafters: Location("Forest Banana Fairy Rafters", Items.BananaFairy, Types.Fairy),
    Locations.ForestLankyAttic: Location("Forest Lanky Attic", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.ForestMillAttic, 0x2, 217, Kongs.lanky)]),
    Locations.ForestKasplatNearBarn: Location("Forest Kasplat Near Thorny Barn", Items.FungiForestDonkeyBlueprint, Types.Blueprint, [Maps.FungiForest, Kongs.donkey]),
    Locations.ForestDonkeyBarn: Location("Forest Donkey Barn", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 235, Kongs.donkey)]),
    Locations.ForestBananaFairyThornvines: Location("Forest Banana Fairy Thornvines", Items.BananaFairy, Types.Fairy),
    Locations.ForestTinyBeanstalk: Location("Forest Tiny Beanstalk", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FungiForest, 0x50, 209, Kongs.tiny)]),
    Locations.ForestChunkyApple: Location("Forest Chunky Apple", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.FungiForest, 0x3E, 253, Kongs.chunky)]),
    Locations.ForestKey: Location("Forest Key", Items.FungiForestKey, Types.Key, [MapIDCombo(0, -1, 236)]),
    # Crystal Caves locations
    Locations.CavesDonkeyMedal: Location("Caves Donkey Medal", Items.BananaMedal, Types.Medal, [Levels.CrystalCaves, Kongs.donkey]),
    Locations.CavesDiddyMedal: Location("Caves Diddy Medal", Items.BananaMedal, Types.Medal, [Levels.CrystalCaves, Kongs.diddy]),
    Locations.CavesLankyMedal: Location("Caves Lanky Medal", Items.BananaMedal, Types.Medal, [Levels.CrystalCaves, Kongs.lanky]),
    Locations.CavesTinyMedal: Location("Caves Tiny Medal", Items.BananaMedal, Types.Medal, [Levels.CrystalCaves, Kongs.tiny]),
    Locations.CavesChunkyMedal: Location("Caves Chunky Medal", Items.BananaMedal, Types.Medal, [Levels.CrystalCaves, Kongs.chunky]),
    Locations.CavesDonkeyBaboonBlast: Location("Caves Donkey Baboon Blast", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CrystalCaves, 0x32, 298, Kongs.donkey)]),
    Locations.CavesDiddyJetpackBarrel: Location("Caves Diddy Jetpack Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 294, Kongs.diddy)]),
    Locations.CavesTinyCaveBarrel: Location("Caves Tiny Cave Barrel", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 295, Kongs.tiny)]),
    Locations.CavesTinyMonkeyportIgloo: Location("Caves Tiny Monkeyport Igloo", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CrystalCaves, 0x29, 297, Kongs.tiny)]),
    Locations.CavesChunkyGorillaGone: Location("Caves Chunky Gorilla Gone", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CrystalCaves, 0x3E, 268, Kongs.chunky)]),
    Locations.CavesKasplatNearLab: Location("Caves Kasplat Near Cranky's Lab", Items.CrystalCavesDonkeyBlueprint, Types.Blueprint, [Maps.CrystalCaves, Kongs.donkey]),
    Locations.CavesKasplatNearFunky: Location("Caves Kasplat Near Funky's Hut", Items.CrystalCavesDiddyBlueprint, Types.Blueprint, [Maps.CrystalCaves, Kongs.diddy]),
    Locations.CavesKasplatPillar: Location("Caves Kasplat On Large Pillar", Items.CrystalCavesLankyBlueprint, Types.Blueprint, [Maps.CrystalCaves, Kongs.lanky]),
    Locations.CavesKasplatNearCandy: Location("Caves Kasplat Near Candy's Music Shop", Items.CrystalCavesTinyBlueprint, Types.Blueprint, [Maps.CrystalCaves, Kongs.tiny]),
    Locations.CavesLankyBeetleRace: Location("Caves Lanky Beetle Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesLankyRace, 0x1, 259, Kongs.lanky)]),
    Locations.CavesLankyCastle: Location("Caves Lanky Castle", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesFrozenCastle, 0x10, 271, Kongs.lanky)]),
    Locations.CavesChunkyTransparentIgloo: Location("Caves Chunky Transparent Igloo", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CrystalCaves, 0x28, 270, Kongs.chunky)]),
    Locations.CavesKasplatOn5DI: Location("Caves Kasplat On 5 Door Igloo", Items.CrystalCavesChunkyBlueprint, Types.Blueprint, [Maps.CrystalCaves, Kongs.chunky]),
    Locations.CavesDonkey5DoorIgloo: Location("Caves Donkey 5 Door Igloo", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesDonkeyIgloo, 0x1, 275, Kongs.donkey)]),
    Locations.CavesDiddy5DoorIgloo: Location("Caves Diddy 5 Door Igloo", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesDiddyIgloo, 0x1, 274, Kongs.diddy)]),
    Locations.CavesLanky5DoorIgloo: Location("Caves Lanky 5 Door Igloo", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesLankyIgloo, 0x3, 281, Kongs.lanky)]),
    Locations.CavesTiny5DoorIgloo: Location("Caves Tiny 5 Door Igloo", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesTinyIgloo, 0x2, 279, Kongs.tiny)]),
    Locations.CavesBananaFairyIgloo: Location("Caves Banana Fairy Igloo", Items.BananaFairy, Types.Fairy),
    Locations.CavesChunky5DoorIgloo: Location("Caves Chunky 5 Door Igloo", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesChunkyIgloo, 0x0, 278, Kongs.chunky)]),
    Locations.CavesDonkeyRotatingCabin: Location("Caves Donkey Rotating Cabin", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesRotatingCabin, 0x1, 276, Kongs.donkey)]),
    Locations.CavesBattleArena: Location("Caves Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.CavesCrown, -1, 616)]),
    Locations.CavesDonkey5DoorCabin: Location("Caves Donkey 5 Door Cabin", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesDonkeyCabin, 0x8, 261, Kongs.donkey)]),
    Locations.CavesDiddy5DoorCabinLower: Location("Caves Diddy 5 Door Cabin Lower", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesDiddyLowerCabin, 0x1, 262, Kongs.diddy)]),
    Locations.CavesDiddy5DoorCabinUpper: Location("Caves Diddy 5 Door Cabin Upper", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesDiddyUpperCabin, 0x4, 293, Kongs.diddy)]),
    Locations.CavesBananaFairyCabin: Location("Caves Banana Fairy Cabin", Items.BananaFairy, Types.Fairy),
    Locations.CavesLanky1DoorCabin: Location("Caves Lanky 1 Door Cabin", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesLankyCabin, 0x1, 264, Kongs.lanky)]),
    Locations.CavesTiny5DoorCabin: Location("Caves Tiny 5 Door Cabin", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CavesTinyCabin, 0x0, 260, Kongs.tiny)]),
    Locations.CavesChunky5DoorCabin: Location("Caves Chunky 5 Door Cabin", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 263, Kongs.chunky)]),
    Locations.CavesKey: Location("Caves Key", Items.CrystalCavesKey, Types.Key, [MapIDCombo(0, -1, 292)]),
    # Creepy Castle locations
    Locations.CastleDonkeyMedal: Location("Castle Donkey Medal", Items.BananaMedal, Types.Medal, [Levels.CreepyCastle, Kongs.donkey]),
    Locations.CastleDiddyMedal: Location("Castle Diddy Medal", Items.BananaMedal, Types.Medal, [Levels.CreepyCastle, Kongs.diddy]),
    Locations.CastleLankyMedal: Location("Castle Lanky Medal", Items.BananaMedal, Types.Medal, [Levels.CreepyCastle, Kongs.lanky]),
    Locations.CastleTinyMedal: Location("Castle Tiny Medal", Items.BananaMedal, Types.Medal, [Levels.CreepyCastle, Kongs.tiny]),
    Locations.CastleChunkyMedal: Location("Castle Chunky Medal", Items.BananaMedal, Types.Medal, [Levels.CreepyCastle, Kongs.chunky]),
    Locations.CastleDiddyAboveCastle: Location("Castle Diddy Above Castle", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 350, Kongs.diddy)]),
    Locations.CastleKasplatHalfway: Location("Castle Kasplat Half-way up Castle", Items.CreepyCastleLankyBlueprint, Types.Blueprint, [Maps.CreepyCastle, Kongs.lanky]),
    Locations.CastleKasplatLowerLedge: Location("Castle Kasplat Lower Ledge", Items.CreepyCastleTinyBlueprint, Types.Blueprint, [Maps.CreepyCastle, Kongs.tiny]),
    Locations.CastleDonkeyTree: Location("Castle Donkey Tree", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleTree, 0x8, 320, Kongs.donkey)]),
    Locations.CastleChunkyTree: Location("Castle Chunky Tree", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 319, Kongs.chunky)]),
    Locations.CastleKasplatTree: Location("Castle Kasplat Inside Tree", Items.CreepyCastleDonkeyBlueprint, Types.Blueprint, [Maps.CastleTree, Kongs.donkey]),
    Locations.CastleBananaFairyTree: Location("Castle Banana Fairy Tree", Items.BananaFairy, Types.Fairy),
    Locations.CastleDonkeyLibrary: Location("Castle Donkey Library", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleLibrary, 0x3, 313, Kongs.donkey)]),
    Locations.CastleDiddyBallroom: Location("Castle Diddy Ballroom", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 305, Kongs.diddy)]),
    Locations.CastleBananaFairyBallroom: Location("Castle Banana Fairy Ballroom", Items.BananaFairy, Types.Fairy),
    Locations.CastleTinyCarRace: Location("Castle Tiny Car Race", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleTinyRace, 0x1, 325, Kongs.tiny)]),
    Locations.CastleLankyTower: Location("Castle Lanky Tower", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 306, Kongs.lanky)]),
    Locations.CastleLankyGreenhouse: Location("Castle Lanky Greenhouse", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleGreenhouse, 0x1, 323, Kongs.lanky)]),
    Locations.CastleBattleArena: Location("Castle Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.CastleCrown, -1, 617)]),
    Locations.CastleTinyTrashCan: Location("Castle Tiny Trash Can", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleTrashCan, 0x4, 351, Kongs.tiny)]),
    Locations.CastleChunkyShed: Location("Castle Chunky Shed", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleShed, 0x6, 322, Kongs.chunky)]),
    Locations.CastleChunkyMuseum: Location("Castle Chunky Museum", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleMuseum, 0x7, 314, Kongs.chunky)]),
    Locations.CastleKasplatCrypt: Location("Castle Kasplat Inside Crypt", Items.CreepyCastleDiddyBlueprint, Types.Blueprint, [Maps.CastleLowerCave, Kongs.diddy]),
    Locations.CastleDiddyCrypt: Location("Castle Diddy Crypt", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleCrypt, 0x8, 310, Kongs.diddy)]),
    Locations.CastleChunkyCrypt: Location("Castle Chunky Crypt", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 311, Kongs.chunky)]),
    Locations.CastleDonkeyMinecarts: Location("Castle Donkey Minecarts", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 318, Kongs.donkey)]),
    Locations.CastleLankyMausoleum: Location("Castle Lanky Mausoleum", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleMausoleum, 0x3, 308, Kongs.lanky)]),
    Locations.CastleTinyMausoleum: Location("Castle Tiny Mausoleum", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleMausoleum, 0xD, 309, Kongs.tiny)]),
    Locations.CastleTinyOverChasm: Location("Castle Tiny Over Chasm", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 315, Kongs.tiny)]),
    Locations.CastleKasplatNearCandy: Location("Castle Kasplat Near Candy's Music Shop", Items.CreepyCastleChunkyBlueprint, Types.Blueprint, [Maps.CastleUpperCave, Kongs.chunky]),
    Locations.CastleDonkeyDungeon: Location("Castle Donkey Dungeon", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleDungeon, 0xF, 326, Kongs.donkey)]),
    Locations.CastleDiddyDungeon: Location("Castle Diddy Dungeon", Items.GoldenBanana, Types.Banana, [MapIDCombo(Maps.CastleDungeon, 0xD, 353, Kongs.diddy)]),
    Locations.CastleLankyDungeon: Location("Castle Lanky Dungeon", Items.GoldenBanana, Types.Banana, [MapIDCombo(0, -1, 316, Kongs.lanky)]),
    Locations.CastleKey: Location("Castle Key", Items.CreepyCastleKey, Types.Key, [MapIDCombo(0, -1, 317)]),
    # Hideout Helm locations
    Locations.HelmDonkey1: Location("Helm Donkey Barrel 1", Items.HelmDonkey1, Types.Constant),
    Locations.HelmDonkey2: Location("Helm Donkey Barrel 2", Items.HelmDonkey2, Types.Constant),
    Locations.HelmDiddy1: Location("Helm Diddy Barrel 1", Items.HelmDiddy1, Types.Constant),
    Locations.HelmDiddy2: Location("Helm Diddy Barrel 2", Items.HelmDiddy2, Types.Constant),
    Locations.HelmLanky1: Location("Helm Lanky Barrel 1", Items.HelmLanky1, Types.Constant),
    Locations.HelmLanky2: Location("Helm Lanky Barrel 2", Items.HelmLanky2, Types.Constant),
    Locations.HelmTiny1: Location("Helm Tiny Barrel 1", Items.HelmTiny1, Types.Constant),
    Locations.HelmTiny2: Location("Helm Tiny Barrel 2", Items.HelmTiny2, Types.Constant),
    Locations.HelmChunky1: Location("Helm Chunky Barrel 1", Items.HelmChunky1, Types.Constant),
    Locations.HelmChunky2: Location("Helm Chunky Barrel 2", Items.HelmChunky2, Types.Constant),
    Locations.HelmBattleArena: Location("Helm Battle Arena", Items.BattleCrown, Types.Crown, [MapIDCombo(Maps.HelmCrown, -1, 618)]),
    Locations.HelmDonkeyMedal: Location("Helm Donkey Medal", Items.BananaMedal, Types.Medal, [MapIDCombo(Maps.HideoutHelm, 0x5D, 584, Kongs.donkey)]),
    Locations.HelmDiddyMedal: Location("Helm Diddy Medal", Items.BananaMedal, Types.Medal, [MapIDCombo(Maps.HideoutHelm, 0x61, 585, Kongs.diddy)]),
    Locations.HelmLankyMedal: Location("Helm Lanky Medal", Items.BananaMedal, Types.Medal, [MapIDCombo(Maps.HideoutHelm, 0x5F, 586, Kongs.lanky)]),
    Locations.HelmTinyMedal: Location("Helm Tiny Medal", Items.BananaMedal, Types.Medal, [MapIDCombo(Maps.HideoutHelm, 0x60, 587, Kongs.tiny)]),
    Locations.HelmChunkyMedal: Location("Helm Chunky Medal", Items.BananaMedal, Types.Medal, [MapIDCombo(Maps.HideoutHelm, 0x5E, 588, Kongs.chunky)]),
    Locations.HelmBananaFairy1: Location("Helm Banana Fairy 1", Items.BananaFairy, Types.Fairy),
    Locations.HelmBananaFairy2: Location("Helm Banana Fairy 2", Items.BananaFairy, Types.Fairy),
    Locations.HelmKey: Location("Helm Key", Items.HideoutHelmKey, Types.Key, [MapIDCombo(Maps.HideoutHelm, 0x5A, 380)]),

    # Normal shop locations
    Locations.SimianSlam: Location("DK Isles Cranky Shared", Items.NoItem, Types.Shop, [Levels.DKIsles, Kongs.any, MoveTypes.Slam, 1]),
    Locations.BaboonBlast: Location("Japes Cranky Donkey", Items.BaboonBlast, Types.Shop, [Levels.JungleJapes, Kongs.donkey, MoveTypes.Moves, 1]),
    Locations.ChimpyCharge: Location("Japes Cranky Diddy", Items.ChimpyCharge, Types.Shop, [Levels.JungleJapes, Kongs.diddy, MoveTypes.Moves, 1]),
    Locations.Orangstand: Location("Japes Cranky Lanky", Items.Orangstand, Types.Shop, [Levels.JungleJapes, Kongs.lanky, MoveTypes.Moves, 1]),
    Locations.MiniMonkey: Location("Japes Cranky Tiny", Items.MiniMonkey, Types.Shop, [Levels.JungleJapes, Kongs.tiny, MoveTypes.Moves, 1]),
    Locations.HunkyChunky: Location("Japes Cranky Chunky", Items.HunkyChunky, Types.Shop, [Levels.JungleJapes, Kongs.chunky, MoveTypes.Moves, 1]),
    Locations.CoconutGun: Location("Japes Funky Donkey", Items.Coconut, Types.Shop, [Levels.JungleJapes, Kongs.donkey, MoveTypes.Guns, 1]),
    Locations.PeanutGun: Location("Japes Funky Diddy", Items.Peanut, Types.Shop, [Levels.JungleJapes, Kongs.diddy, MoveTypes.Guns, 1]),
    Locations.GrapeGun: Location("Japes Funky Lanky", Items.Grape, Types.Shop, [Levels.JungleJapes, Kongs.lanky, MoveTypes.Guns, 1]),
    Locations.FeatherGun: Location("Japes Funky Tiny", Items.Feather, Types.Shop, [Levels.JungleJapes, Kongs.tiny, MoveTypes.Guns, 1]),
    Locations.PineappleGun: Location("Japes Funky Chunky", Items.Pineapple, Types.Shop, [Levels.JungleJapes, Kongs.chunky, MoveTypes.Guns, 1]),
    Locations.StrongKong: Location("Aztec Cranky Donkey", Items.StrongKong, Types.Shop, [Levels.AngryAztec, Kongs.donkey, MoveTypes.Moves, 2]),
    Locations.RocketbarrelBoost: Location("Aztec Cranky Diddy", Items.RocketbarrelBoost, Types.Shop, [Levels.AngryAztec, Kongs.diddy, MoveTypes.Moves, 2]),
    Locations.Bongos: Location("Aztec Candy Donkey", Items.Bongos, Types.Shop, [Levels.AngryAztec, Kongs.donkey, MoveTypes.Instruments, 1]),
    Locations.Guitar: Location("Aztec Candy Diddy", Items.Guitar, Types.Shop, [Levels.AngryAztec, Kongs.diddy, MoveTypes.Instruments, 1]),
    Locations.Trombone: Location("Aztec Candy Lanky", Items.Trombone, Types.Shop, [Levels.AngryAztec, Kongs.lanky, MoveTypes.Instruments, 1]),
    Locations.Saxophone: Location("Aztec Candy Tiny", Items.Saxophone, Types.Shop, [Levels.AngryAztec, Kongs.tiny, MoveTypes.Instruments, 1]),
    Locations.Triangle: Location("Aztec Candy Chunky", Items.Triangle, Types.Shop, [Levels.AngryAztec, Kongs.chunky, MoveTypes.Instruments, 1]),
    Locations.GorillaGrab: Location("Factory Cranky Donkey", Items.GorillaGrab, Types.Shop, [Levels.FranticFactory, Kongs.donkey, MoveTypes.Moves, 3]),
    Locations.SimianSpring: Location("Factory Cranky Diddy", Items.SimianSpring, Types.Shop, [Levels.FranticFactory, Kongs.diddy, MoveTypes.Moves, 3]),
    Locations.BaboonBalloon: Location("Factory Cranky Lanky", Items.BaboonBalloon, Types.Shop, [Levels.FranticFactory, Kongs.lanky, MoveTypes.Moves, 2]),
    Locations.PonyTailTwirl: Location("Factory Cranky Tiny", Items.PonyTailTwirl, Types.Shop, [Levels.FranticFactory, Kongs.tiny, MoveTypes.Moves, 2]),
    Locations.PrimatePunch: Location("Factory Cranky Chunky", Items.PrimatePunch, Types.Shop, [Levels.FranticFactory, Kongs.chunky, MoveTypes.Moves, 2]),
    Locations.AmmoBelt1: Location("Factory Funky Shared", Items.ProgressiveAmmoBelt, Types.Shop, [Levels.FranticFactory, Kongs.any, MoveTypes.AmmoBelt, 1]),
    Locations.MusicUpgrade1: Location("Galleon Candy Shared", Items.ProgressiveInstrumentUpgrade, Types.Shop, [Levels.GloomyGalleon, Kongs.any, MoveTypes.Instruments, 2]),
    Locations.SuperSimianSlam: Location("Forest Cranky Shared", Items.ProgressiveSlam, Types.Shop, [Levels.FungiForest, Kongs.any, MoveTypes.Slam, 2]),
    Locations.HomingAmmo: Location("Forest Funky Shared", Items.HomingAmmo, Types.Shop, [Levels.FungiForest, Kongs.any, MoveTypes.Guns, 2]),
    Locations.OrangstandSprint: Location("Caves Cranky Lanky", Items.OrangstandSprint, Types.Shop, [Levels.CrystalCaves, Kongs.lanky, MoveTypes.Moves, 3]),
    Locations.Monkeyport: Location("Caves Cranky Tiny", Items.Monkeyport, Types.Shop, [Levels.CrystalCaves, Kongs.tiny, MoveTypes.Moves, 3]),
    Locations.GorillaGone: Location("Caves Cranky Chunky", Items.GorillaGone, Types.Shop, [Levels.CrystalCaves, Kongs.chunky, MoveTypes.Moves, 3]),
    Locations.AmmoBelt2: Location("Caves Funky Shared", Items.ProgressiveAmmoBelt, Types.Shop, [Levels.CrystalCaves, Kongs.any, MoveTypes.AmmoBelt, 2]),
    Locations.ThirdMelon: Location("Caves Candy Shared", Items.ProgressiveInstrumentUpgrade, Types.Shop, [Levels.CrystalCaves, Kongs.any, MoveTypes.Instruments, 3]),
    Locations.SuperDuperSimianSlam: Location("Castle Cranky Shared", Items.ProgressiveSlam, Types.Shop, [Levels.CreepyCastle, Kongs.any, MoveTypes.Slam, 3]),
    Locations.SniperSight: Location("Castle Funky Shared", Items.SniperSight, Types.Shop, [Levels.CreepyCastle, Kongs.any, MoveTypes.Guns, 3]),
    Locations.MusicUpgrade2: Location("Castle Candy Shared", Items.ProgressiveInstrumentUpgrade, Types.Shop, [Levels.CreepyCastle, Kongs.any, MoveTypes.Instruments, 4]),
    Locations.RarewareCoin: Location("Rareware Coin", Items.RarewareCoin, Types.Coin, [MapIDCombo(Maps.Cranky, 0x2, 379)]),
    # Additional shop locations for randomized moves- Index doesn't really matter, just set to 0
    # Japes
    Locations.SharedJapesPotion: Location("Japes Cranky Shared", Items.NoItem, Types.Shop, [Levels.JungleJapes, Kongs.any, MoveTypes.Moves, 0]),
    Locations.SharedJapesGun: Location("Japes Funky Shared", Items.NoItem, Types.Shop, [Levels.JungleJapes, Kongs.any, MoveTypes.Guns, 0]),
    # Aztec
    Locations.SharedAztecPotion: Location("Aztec Cranky Shared", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.any, MoveTypes.Moves, 0]),
    Locations.LankyAztecPotion: Location("Aztec Cranky Lanky", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.lanky, MoveTypes.Moves, 0]),
    Locations.TinyAztecPotion: Location("Aztec Cranky Tiny", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.tiny, MoveTypes.Moves, 0]),
    Locations.ChunkyAztecPotion: Location("Aztec Cranky Chunky", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.chunky, MoveTypes.Moves, 0]),
    Locations.SharedAztecGun: Location("Aztec Funky Shared", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.any, MoveTypes.Guns, 0]),
    Locations.DonkeyAztecGun: Location("Aztec Funky Donkey", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.donkey, MoveTypes.Guns, 0]),
    Locations.DiddyAztecGun: Location("Aztec Funky Diddy", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.diddy, MoveTypes.Guns, 0]),
    Locations.LankyAztecGun: Location("Aztec Funky Lanky", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.lanky, MoveTypes.Guns, 0]),
    Locations.TinyAztecGun: Location("Aztec Funky Tiny", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.tiny, MoveTypes.Guns, 0]),
    Locations.ChunkyAztecGun: Location("Aztec Funky Chunky", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.chunky, MoveTypes.Guns, 0]),
    Locations.SharedAztecInstrument: Location("Aztec Candy Shared", Items.NoItem, Types.Shop, [Levels.AngryAztec, Kongs.any, MoveTypes.Instruments, 0]),
    # Factory
    Locations.SharedFactoryPotion: Location("Factory Cranky Shared", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.any, MoveTypes.Moves, 0]),
    Locations.DonkeyFactoryGun: Location("Factory Funky Donkey", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.donkey, MoveTypes.Guns, 0]),
    Locations.DiddyFactoryGun: Location("Factory Funky Diddy", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.diddy, MoveTypes.Guns, 0]),
    Locations.LankyFactoryGun: Location("Factory Funky Lanky", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.lanky, MoveTypes.Guns, 0]),
    Locations.TinyFactoryGun: Location("Factory Funky Tiny", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.tiny, MoveTypes.Guns, 0]),
    Locations.ChunkyFactoryGun: Location("Factory Funky Chunky", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.chunky, MoveTypes.Guns, 0]),
    Locations.SharedFactoryInstrument: Location("Factory Candy Shared", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.any, MoveTypes.Instruments, 0]),
    Locations.DonkeyFactoryInstrument: Location("Factory Candy Donkey", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.donkey, MoveTypes.Instruments, 0]),
    Locations.DiddyFactoryInstrument: Location("Factory Candy Diddy", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.diddy, MoveTypes.Instruments, 0]),
    Locations.LankyFactoryInstrument: Location("Factory Candy Lanky", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.lanky, MoveTypes.Instruments, 0]),
    Locations.TinyFactoryInstrument: Location("Factory Candy Tiny", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.tiny, MoveTypes.Instruments, 0]),
    Locations.ChunkyFactoryInstrument: Location("Factory Candy Chunky", Items.NoItem, Types.Shop, [Levels.FranticFactory, Kongs.chunky, MoveTypes.Instruments, 0]),
    # Galleon
    Locations.SharedGalleonPotion: Location("Galleon Cranky Shared", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.any, MoveTypes.Moves, 0]),
    Locations.DonkeyGalleonPotion: Location("Galleon Cranky Donkey", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.donkey, MoveTypes.Moves, 0]),
    Locations.DiddyGalleonPotion: Location("Galleon Cranky Diddy", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.diddy, MoveTypes.Moves, 0]),
    Locations.LankyGalleonPotion: Location("Galleon Cranky Lanky", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.lanky, MoveTypes.Moves, 0]),
    Locations.TinyGalleonPotion: Location("Galleon Cranky Tiny", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.tiny, MoveTypes.Moves, 0]),
    Locations.ChunkyGalleonPotion: Location("Galleon Cranky Chunky", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.chunky, MoveTypes.Moves, 0]),
    Locations.SharedGalleonGun: Location("Galleon Funky Shared", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.any, MoveTypes.Guns, 0]),
    Locations.DonkeyGalleonGun: Location("Galleon Funky Donkey", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.donkey, MoveTypes.Guns, 0]),
    Locations.DiddyGalleonGun: Location("Galleon Funky Diddy", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.diddy, MoveTypes.Guns, 0]),
    Locations.LankyGalleonGun: Location("Galleon Funky Lanky", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.lanky, MoveTypes.Guns, 0]),
    Locations.TinyGalleonGun: Location("Galleon Funky Tiny", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.tiny, MoveTypes.Guns, 0]),
    Locations.ChunkyGalleonGun: Location("Galleon Funky Chunky", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.chunky, MoveTypes.Guns, 0]),
    Locations.DonkeyGalleonInstrument: Location("Galleon Candy Donkey", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.donkey, MoveTypes.Instruments, 0]),
    Locations.DiddyGalleonInstrument: Location("Galleon Candy Diddy", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.diddy, MoveTypes.Instruments, 0]),
    Locations.LankyGalleonInstrument: Location("Galleon Candy Lanky", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.lanky, MoveTypes.Instruments, 0]),
    Locations.TinyGalleonInstrument: Location("Galleon Candy Tiny", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.tiny, MoveTypes.Instruments, 0]),
    Locations.ChunkyGalleonInstrument: Location("Galleon Candy Chunky", Items.NoItem, Types.Shop, [Levels.GloomyGalleon, Kongs.chunky, MoveTypes.Instruments, 0]),
    # Forest
    Locations.DonkeyForestPotion: Location("Forest Cranky Donkey", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.donkey, MoveTypes.Moves, 0]),
    Locations.DiddyForestPotion: Location("Forest Cranky Diddy", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.diddy, MoveTypes.Moves, 0]),
    Locations.LankyForestPotion: Location("Forest Cranky Lanky", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.lanky, MoveTypes.Moves, 0]),
    Locations.TinyForestPotion: Location("Forest Cranky Tiny", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.tiny, MoveTypes.Moves, 0]),
    Locations.ChunkyForestPotion: Location("Forest Cranky Chunky", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.chunky, MoveTypes.Moves, 0]),
    Locations.DonkeyForestGun: Location("Forest Funky Donkey", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.donkey, MoveTypes.Guns, 0]),
    Locations.DiddyForestGun: Location("Forest Funky Diddy", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.diddy, MoveTypes.Guns, 0]),
    Locations.LankyForestGun: Location("Forest Funky Lanky", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.lanky, MoveTypes.Guns, 0]),
    Locations.TinyForestGun: Location("Forest Funky Tiny", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.tiny, MoveTypes.Guns, 0]),
    Locations.ChunkyForestGun: Location("Forest Funky Chunky", Items.NoItem, Types.Shop, [Levels.FungiForest, Kongs.chunky, MoveTypes.Guns, 0]),
    # Caves
    Locations.SharedCavesPotion: Location("Caves Cranky Shared", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.any, MoveTypes.Moves, 0]),
    Locations.DonkeyCavesPotion: Location("Caves Cranky Donkey", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.donkey, MoveTypes.Moves, 0]),
    Locations.DiddyCavesPotion: Location("Caves Cranky Diddy", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.diddy, MoveTypes.Moves, 0]),
    Locations.DonkeyCavesGun: Location("Caves Funky Donkey", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.donkey, MoveTypes.Guns, 0]),
    Locations.DiddyCavesGun: Location("Caves Funky Diddy", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.diddy, MoveTypes.Guns, 0]),
    Locations.LankyCavesGun: Location("Caves Funky Lanky", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.lanky, MoveTypes.Guns, 0]),
    Locations.TinyCavesGun: Location("Caves Funky Tiny", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.tiny, MoveTypes.Guns, 0]),
    Locations.ChunkyCavesGun: Location("Caves Funky Chunky", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.chunky, MoveTypes.Guns, 0]),
    Locations.DonkeyCavesInstrument: Location("Caves Candy Donkey", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.donkey, MoveTypes.Instruments, 0]),
    Locations.DiddyCavesInstrument: Location("Caves Candy Diddy", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.diddy, MoveTypes.Instruments, 0]),
    Locations.LankyCavesInstrument: Location("Caves Candy Lanky", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.lanky, MoveTypes.Instruments, 0]),
    Locations.TinyCavesInstrument: Location("Caves Candy Tiny", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.tiny, MoveTypes.Instruments, 0]),
    Locations.ChunkyCavesInstrument: Location("Caves Candy Chunky", Items.NoItem, Types.Shop, [Levels.CrystalCaves, Kongs.chunky, MoveTypes.Instruments, 0]),
    # Castle
    Locations.DonkeyCastlePotion: Location("Castle Cranky Donkey", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.donkey, MoveTypes.Moves, 0]),
    Locations.DiddyCastlePotion: Location("Castle Cranky Diddy", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.diddy, MoveTypes.Moves, 0]),
    Locations.LankyCastlePotion: Location("Castle Cranky Lanky", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.lanky, MoveTypes.Moves, 0]),
    Locations.TinyCastlePotion: Location("Castle Cranky Tiny", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.tiny, MoveTypes.Moves, 0]),
    Locations.ChunkyCastlePotion: Location("Castle Cranky Chunky", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.chunky, MoveTypes.Moves, 0]),
    Locations.DonkeyCastleGun: Location("Castle Funky Donkey", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.donkey, MoveTypes.Guns, 0]),
    Locations.DiddyCastleGun: Location("Castle Funky Diddy", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.diddy, MoveTypes.Guns, 0]),
    Locations.LankyCastleGun: Location("Castle Funky Lanky", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.lanky, MoveTypes.Guns, 0]),
    Locations.TinyCastleGun: Location("Castle Funky Tiny", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.tiny, MoveTypes.Guns, 0]),
    Locations.ChunkyCastleGun: Location("Castle Funky Chunky", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.chunky, MoveTypes.Guns, 0]),
    Locations.DonkeyCastleInstrument: Location("Castle Candy Donkey", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.donkey, MoveTypes.Instruments, 0]),
    Locations.DiddyCastleInstrument: Location("Castle Candy Diddy", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.diddy, MoveTypes.Instruments, 0]),
    Locations.LankyCastleInstrument: Location("Castle Candy Lanky", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.lanky, MoveTypes.Instruments, 0]),
    Locations.TinyCastleInstrument: Location("Castle Candy Tiny", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.tiny, MoveTypes.Instruments, 0]),
    Locations.ChunkyCastleInstrument: Location("Castle Candy Chunky", Items.NoItem, Types.Shop, [Levels.CreepyCastle, Kongs.chunky, MoveTypes.Instruments, 0]),
    # Isles
    Locations.DonkeyIslesPotion: Location("DK Isles Cranky Donkey", Items.NoItem, Types.Shop, [Levels.DKIsles, Kongs.donkey, MoveTypes.Moves, 0]),
    Locations.DiddyIslesPotion: Location("DK Isles Cranky Diddy", Items.NoItem, Types.Shop, [Levels.DKIsles, Kongs.diddy, MoveTypes.Moves, 0]),
    Locations.LankyIslesPotion: Location("DK Isles Cranky Lanky", Items.NoItem, Types.Shop, [Levels.DKIsles, Kongs.lanky, MoveTypes.Moves, 0]),
    Locations.TinyIslesPotion: Location("DK Isles Cranky Tiny", Items.NoItem, Types.Shop, [Levels.DKIsles, Kongs.tiny, MoveTypes.Moves, 0]),
    Locations.ChunkyIslesPotion: Location("DK Isles Cranky Chunky", Items.NoItem, Types.Shop, [Levels.DKIsles, Kongs.chunky, MoveTypes.Moves, 0]),

    # Blueprints
    Locations.TurnInDKIslesDonkeyBlueprint: Location("Turn In DK Isles Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInDKIslesDiddyBlueprint: Location("Turn In DK Isles Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInDKIslesLankyBlueprint: Location("Turn In DK Isles Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInDKIslesTinyBlueprint: Location("Turn In DK Isles Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInDKIslesChunkyBlueprint: Location("Turn In DK Isles Chunky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInJungleJapesDonkeyBlueprint: Location("Turn In Jungle Japes Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInJungleJapesDiddyBlueprint: Location("Turn In Jungle Japes Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInJungleJapesLankyBlueprint: Location("Turn In Jungle Japes Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInJungleJapesTinyBlueprint: Location("Turn In Jungle Japes Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInJungleJapesChunkyBlueprint: Location("Turn In Jungle Japes Chunky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInAngryAztecDonkeyBlueprint: Location("Turn In Angry Aztec Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInAngryAztecDiddyBlueprint: Location("Turn In Angry Aztec Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInAngryAztecLankyBlueprint: Location("Turn In Angry Aztec Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInAngryAztecTinyBlueprint: Location("Turn In Angry Aztec Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInAngryAztecChunkyBlueprint: Location("Turn In Angry Aztec Chunky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFranticFactoryDonkeyBlueprint: Location("Turn In Frantic Factory Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFranticFactoryDiddyBlueprint: Location("Turn In Frantic Factory Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFranticFactoryLankyBlueprint: Location("Turn In Frantic Factory Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFranticFactoryTinyBlueprint: Location("Turn In Frantic Factory Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFranticFactoryChunkyBlueprint: Location("Turn In Frantic Factory Chunky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInGloomyGalleonDonkeyBlueprint: Location("Turn In Gloomy Galleon Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInGloomyGalleonDiddyBlueprint: Location("Turn In Gloomy Galleon Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInGloomyGalleonLankyBlueprint: Location("Turn In Gloomy Galleon Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInGloomyGalleonTinyBlueprint: Location("Turn In Gloomy Galleon Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInGloomyGalleonChunkyBlueprint: Location("Turn In Gloomy Galleon Chunky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFungiForestDonkeyBlueprint: Location("Turn In Fungi Forest Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFungiForestDiddyBlueprint: Location("Turn In Fungi Forest Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFungiForestLankyBlueprint: Location("Turn In Fungi Forest Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFungiForestTinyBlueprint: Location("Turn In Fungi Forest Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInFungiForestChunkyBlueprint: Location("Turn In Fungi Forest Chunky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCrystalCavesDonkeyBlueprint: Location("Turn In Crystal Caves Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCrystalCavesDiddyBlueprint: Location("Turn In Crystal Caves Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCrystalCavesLankyBlueprint: Location("Turn In Crystal Caves Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCrystalCavesTinyBlueprint: Location("Turn In Crystal Caves Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCrystalCavesChunkyBlueprint: Location("Turn In Crystal Caves Chunky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCreepyCastleDonkeyBlueprint: Location("Turn In Creepy Castle Donkey Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCreepyCastleDiddyBlueprint: Location("Turn In Creepy Castle Diddy Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCreepyCastleLankyBlueprint: Location("Turn In Creepy Castle Lanky Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCreepyCastleTinyBlueprint: Location("Turn In Creepy Castle Tiny Blueprint", Items.GoldenBanana, Types.Banana),
    Locations.TurnInCreepyCastleChunkyBlueprint: Location("Turn In Creepy Castle Chunky Blueprint", Items.GoldenBanana, Types.Banana),
}
