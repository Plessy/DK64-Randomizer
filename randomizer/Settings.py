"""Settings class and functions."""
import json
import random

from randomizer.Enums.Kongs import Kongs
from randomizer.Prices import VanillaPrices, GetMaxForKong

class Settings:
    """Class used to store settings for seed generation."""

    def __init__(self, form_data: dict):
        """Init all the settings using the form data to set the flags.

        Args:
            form_data (dict): Post data from the html form.
        """
        self.algorithm = "forward"
        self.generate_main()
        self.generate_progression()
        self.generate_misc()
        for k, v in form_data.items():
            setattr(self, k, v)
        self.set_seed()
        # Store banana values in array
        self.EntryGBs = [
            self.blocker_0,
            self.blocker_1,
            self.blocker_2,
            self.blocker_3,
            self.blocker_4,
            self.blocker_5,
            self.blocker_6,
            self.blocker_7,
        ]
        self.BossBananas = [
            self.troff_0,
            self.troff_1,
            self.troff_2,
            self.troff_3,
            self.troff_4,
            self.troff_5,
            self.troff_6,
        ]

        # Settings which are not yet implemented on the web page

        # training_barrels: str
        # normal
        # shuffled
        # startwith
        self.training_barrels = "startwith"

        # bonus_barrels: str
        # skip
        # normal
        # random
        self.bonus_barrels = "random"

        # starting_kong: Kongs enum
        self.starting_kong = Kongs.donkey

        # shuffle_items: str
        # none
        # moves
        # all (currently only theoretical)
        self.shuffle_items = "none"

        # progressive_upgrades: bool
        self.progressive_upgrades = True

        # shuffle_loading_zones: str
        # none
        # levels
        # all
        self.shuffle_loading_zones = "none"

        # decoupled_loading_zones: bool
        self.decoupled_loading_zones = False

        self.prices = VanillaPrices.copy()
        self.resolve_settings()

    def generate_main(self):
        """Set Default items on main page."""
        self.seed = None
        self.download_json = None

    def set_seed(self):
        """Forcibly re-set the random seed to the seed set in the config."""
        random.seed(int(self.seed))

    def generate_progression(self):
        """Set default items on progression page."""
        self.blocker_selected = None
        self.troff_selected = None
        self.blocker_0 = None
        self.blocker_1 = None
        self.blocker_2 = None
        self.blocker_3 = None
        self.blocker_4 = None
        self.blocker_5 = None
        self.blocker_6 = None
        self.blocker_7 = None
        self.troff_0 = None
        self.troff_1 = None
        self.troff_2 = None
        self.troff_3 = None
        self.troff_4 = None
        self.troff_5 = None
        self.troff_6 = None

    def generate_misc(self):
        """Set default items on misc page."""
        #  Settings which affect logic
        # start_with_moves: bool
        self.unlock_all_moves = None
        # unlock_all_kongs: bool
        self.unlock_all_kongs = None
        # crown_door_open: bool
        self.crown_door_open = None
        # coin_door_open: bool
        self.coin_door_open = None
        # unlock_fairy_shockwave: bool
        self.unlock_fairy_shockwave = None
        # krool_phase_count: int, [1-5]
        self.krool_phase_count = 5

        #  Music
        self.music_bgm = None
        self.music_fanfares = None
        self.music_events = None

        #  Misc
        self.generate_spoilerlog = None
        self.fast_start_beginning_of_game = None
        self.fast_start_hideout_helm = None
        self.quality_of_life = None
        self.enable_tag_anywhere = None
        self.random_krool_phase_order = None

    def resolve_settings(self):
        """Resolve settings which are not directly set through the UI."""
        self.krool_donkey = False
        self.krool_diddy = False
        self.krool_lanky = False
        self.krool_tiny = False
        self.krool_chunky = True

        phases = ["donkey", "diddy", "lanky", "tiny"]
        phases = random.sample(phases, self.krool_phase_count - 1)
        orderedPhases = []
        if "donkey" in phases:
            self.krool_donkey = True
            orderedPhases.append("donkey")
        if "diddy" in phases:
            self.krool_diddy = True
            orderedPhases.append("diddy")
        if "lanky" in phases:
            self.krool_lanky = True
            orderedPhases.append("lanky")
        if "tiny" in phases:
            self.krool_tiny = True
            orderedPhases.append("tiny")

        if self.random_krool_phase_order:
            random.shuffle(orderedPhases)
        orderedPhases.append("chunky")
        self.krool_order = orderedPhases

    def __repr__(self):
        """Return printable version of the object as json.

        Returns:
            str: Json string of the dict.
        """
        return json.dumps(self.__dict__)
