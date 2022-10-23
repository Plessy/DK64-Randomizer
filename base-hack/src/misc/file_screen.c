#include "../../include/common.h"

static char balanced_igt[20] = "";
static char perc_str[7] = "";

#define LINE_GAP 0x8C
static char updated_tracker = 0;

typedef struct menu_controller_paad {
	/* 0x000 */ float screen_transition_progress;
	/* 0x004 */ float unk_4;
	/* 0x008 */ char unk_8[0x12-0x8];
	/* 0x012 */ unsigned char current_screen;
	/* 0x013 */ unsigned char next_screen;
	/* 0x014 */ char unk_14[0x16-0x14];
	/* 0x016 */ char prevent_action;
	/* 0x017 */ char selected_action;
} menu_controller_paad;

typedef struct tracker_struct {
	/* 0x000 */ short min_x;
	/* 0x002 */ short max_x;
	/* 0x004 */ short min_y;
	/* 0x006 */ short max_y;
	/* 0x008 */ unsigned char enabled;
	/* 0x009 */ unsigned char type;
} tracker_struct;

#define TRACKER_TYPE_COCONUT 0
#define TRACKER_TYPE_BONGOS 1
#define TRACKER_TYPE_GRAB 2
#define TRACKER_TYPE_STRONG 3
#define TRACKER_TYPE_BLAST 4

#define TRACKER_TYPE_PEANUT 5
#define TRACKER_TYPE_GUITAR 6
#define TRACKER_TYPE_CHARGE 7
#define TRACKER_TYPE_ROCKET 8
#define TRACKER_TYPE_SPRING 9

#define TRACKER_TYPE_GRAPE 10
#define TRACKER_TYPE_TROMBONE 11
#define TRACKER_TYPE_OSTAND 12
#define TRACKER_TYPE_OSPRINT 13
#define TRACKER_TYPE_BALLOON 14

#define TRACKER_TYPE_FEATHER 15
#define TRACKER_TYPE_SAX 16
#define TRACKER_TYPE_PTT 17
#define TRACKER_TYPE_MINI 18
#define TRACKER_TYPE_MONKEYPORT 19

#define TRACKER_TYPE_PINEAPPLE 20
#define TRACKER_TYPE_TRIANGLE 21
#define TRACKER_TYPE_PUNCH 22
#define TRACKER_TYPE_HUNKY 23
#define TRACKER_TYPE_GONE 24

#define TRACKER_TYPE_SLAM 25
#define TRACKER_TYPE_HOMING 26
#define TRACKER_TYPE_SNIPER 27
#define TRACKER_TYPE_AMMOBELT 28
#define TRACKER_TYPE_INSTRUMENT_UPG 29

#define TRACKER_TYPE_DIVE 30
#define TRACKER_TYPE_ORANGE 31
#define TRACKER_TYPE_BARREL 32
#define TRACKER_TYPE_VINE 33

#define TRACKER_TYPE_CAMERA 34
#define TRACKER_TYPE_SHOCKWAVE 35

#define TRACKER_TYPE_KEY1 36
#define TRACKER_TYPE_KEY2 37
#define TRACKER_TYPE_KEY3 38
#define TRACKER_TYPE_KEY4 39
#define TRACKER_TYPE_KEY5 40
#define TRACKER_TYPE_KEY6 41
#define TRACKER_TYPE_KEY7 42
#define TRACKER_TYPE_KEY8 43

#define TRACKER_TYPE_MELON_2 44
#define TRACKER_TYPE_MELON_3 45
#define TRACKER_TYPE_INSUPG_1 46
#define TRACKER_TYPE_INSUPG_2 47
#define TRACKER_TYPE_BELT_1 48
#define TRACKER_TYPE_BELT_2 49

#define TRACKER_ENABLED_DEFAULT 1

static tracker_struct tracker_info[] = {
	{.min_x = 0, .max_x = 20, .min_y = 0, .max_y = 22, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_COCONUT}, // Coconut
	{.min_x = 0, .max_x = 20, .min_y = 22, .max_y = 42, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_BONGOS}, // Bongos
	{.min_x = 0, .max_x = 20, .min_y = 44, .max_y = 64, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_GRAB}, // Grab
	{.min_x = 0, .max_x = 20, .min_y = 66, .max_y = 86, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_BLAST}, // Blast
	{.min_x = 0, .max_x = 20, .min_y = 88, .max_y = 108, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_STRONG}, // Strong
	{.min_x = 22, .max_x = 42, .min_y = 0, .max_y = 22, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_PEANUT}, // Peanut
	{.min_x = 22, .max_x = 42, .min_y = 22, .max_y = 42, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_GUITAR}, // Guitar
	{.min_x = 22, .max_x = 42, .min_y = 44, .max_y = 64, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_CHARGE}, // Charge
	{.min_x = 22, .max_x = 42, .min_y = 66, .max_y = 86, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SPRING}, // Spring
	{.min_x = 22, .max_x = 42, .min_y = 88, .max_y = 108, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_ROCKET}, // Rocket
	{.min_x = 44, .max_x = 64, .min_y = 0, .max_y = 22, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_GRAPE}, // Grape
	{.min_x = 44, .max_x = 64, .min_y = 22, .max_y = 42, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_TROMBONE}, // Trombone
	{.min_x = 44, .max_x = 64, .min_y = 44, .max_y = 64, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_OSTAND}, // OStand
	{.min_x = 44, .max_x = 64, .min_y = 66, .max_y = 86, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_BALLOON}, // Balloon
	{.min_x = 44, .max_x = 64, .min_y = 88, .max_y = 108, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_OSPRINT}, // OSprint
	{.min_x = 66, .max_x = 86, .min_y = 0, .max_y = 22, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_FEATHER}, // Feather
	{.min_x = 66, .max_x = 86, .min_y = 22, .max_y = 42, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SAX}, // Sax
	{.min_x = 66, .max_x = 86, .min_y = 44, .max_y = 64, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_PTT}, // PTT
	{.min_x = 66, .max_x = 86, .min_y = 66, .max_y = 86, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_MONKEYPORT}, // Monkeyport
	{.min_x = 66, .max_x = 86, .min_y = 88, .max_y = 108, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_MINI}, // Mini
	{.min_x = 88, .max_x = 108, .min_y = 0, .max_y = 22, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_PINEAPPLE}, // Pineapple
	{.min_x = 88, .max_x = 108, .min_y = 22, .max_y = 42, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_TRIANGLE}, // Triangle
	{.min_x = 88, .max_x = 108, .min_y = 44, .max_y = 64, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_PUNCH}, // Punch
	{.min_x = 88, .max_x = 108, .min_y = 66, .max_y = 86, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_GONE}, // Gone
	{.min_x = 88, .max_x = 108, .min_y = 88, .max_y = 108, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_HUNKY}, // Hunky
	{.min_x = 125, .max_x = 138, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY1}, // Key1
	{.min_x = 141, .max_x = 157, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY2}, // Key2
	{.min_x = 156, .max_x = 171, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY3}, // Key3
	{.min_x = 173, .max_x = 189, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY4}, // Key4
	{.min_x = 189, .max_x = 204, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY5}, // Key5
	{.min_x = 205, .max_x = 220, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY6}, // Key6
	{.min_x = 221, .max_x = 236, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY7}, // Key7
	{.min_x = 237, .max_x = 252, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_KEY8}, // Key8
	{.min_x = 136, .max_x = 150, .min_y = 0, .max_y = 20, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_CAMERA}, // Camera
	{.min_x = 130, .max_x = 152, .min_y = 22, .max_y = 42, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SHOCKWAVE}, // Shockwave
	{.min_x = 132, .max_x = 138, .min_y = 54, .max_y = 64, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SLAM}, // Slam
	{.min_x = 138, .max_x = 141, .min_y = 52, .max_y = 55, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SLAM}, // Slam
	{.min_x = 138, .max_x = 146, .min_y = 60, .max_y = 63, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SLAM}, // Slam
	{.min_x = 146, .max_x = 152, .min_y = 54, .max_y = 63, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SLAM}, // Slam
	{.min_x = 144, .max_x = 146, .min_y = 52, .max_y = 55, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SLAM}, // Slam
	{.min_x = 134, .max_x = 149, .min_y = 66, .max_y = 79, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_HOMING}, // Homing
	{.min_x = 132, .max_x = 152, .min_y = 92, .max_y = 104, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_SNIPER}, // Sniper
	{.min_x = 0, .max_x = 20, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_DIVE}, // Dive
	{.min_x = 22, .max_x = 42, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_ORANGE}, // Orange
	{.min_x = 44, .max_x = 64, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_BARREL}, // Barrel
	{.min_x = 66, .max_x = 86, .min_y = 108, .max_y = 128, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_VINE}, // Vine
	{.min_x = 186, .max_x = 202, .min_y = 0, .max_y = 18, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_MELON_2}, // Melon_2
	{.min_x = 202, .max_x = 219, .min_y = 0, .max_y = 18, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_MELON_3}, // Melon_3
	{.min_x = 218, .max_x = 238, .min_y = 22, .max_y = 40, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_INSUPG_1}, // InsUpg_1
	{.min_x = 239, .max_x = 249, .min_y = 25, .max_y = 39, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_INSUPG_2}, // InsUpg_2
	{.min_x = 220, .max_x = 235, .min_y = 44, .max_y = 57, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_BELT_1}, // Belt_1
	{.min_x = 236, .max_x = 244, .min_y = 44, .max_y = 58, .enabled = TRACKER_ENABLED_DEFAULT, .type = TRACKER_TYPE_BELT_2}, // Belt_2
};

void wipeTrackerCache(void) {
	// Wipe image cache for image
	for (int i = 0; i < 32; i++) {
		if ((ImageCache[i].image_index == IMAGE_TRACKER) && (ImageCache[i].image_state != 0)) {
			ImageCache[i].image_state = 0;
			if (ImageCache[i].image_pointer) {
				complex_free(ImageCache[i].image_pointer);
			}
			return;
		}
	}
}

static const int tracker_move_0[] = {TRACKER_TYPE_BLAST, TRACKER_TYPE_CHARGE, TRACKER_TYPE_OSTAND, TRACKER_TYPE_MINI, TRACKER_TYPE_HUNKY};
static const int tracker_move_1[] = {TRACKER_TYPE_STRONG, TRACKER_TYPE_ROCKET, TRACKER_TYPE_BALLOON, TRACKER_TYPE_PTT, TRACKER_TYPE_PUNCH};
static const int tracker_move_2[] = {TRACKER_TYPE_GRAB, TRACKER_TYPE_SPRING, TRACKER_TYPE_OSPRINT, TRACKER_TYPE_MONKEYPORT, TRACKER_TYPE_GONE};
static const int tracker_instrument[] = {TRACKER_TYPE_BONGOS, TRACKER_TYPE_GUITAR, TRACKER_TYPE_TROMBONE, TRACKER_TYPE_SAX, TRACKER_TYPE_TRIANGLE};
static const int tracker_gun[] = {TRACKER_TYPE_COCONUT, TRACKER_TYPE_PEANUT, TRACKER_TYPE_GRAPE, TRACKER_TYPE_FEATHER, TRACKER_TYPE_PINEAPPLE};

int getInitFileMove(int index) {
	int found = 0;
	for (int i = 0; i < 4; i++) {
		int move_type = TrainingMoves_New[i].purchase_type;
		int move_value = TrainingMoves_New[i].purchase_value;
		int move_kong = TrainingMoves_New[i].move_kong;
		switch(move_type) {
			case PURCHASE_MOVES:
				if (move_value == 1) {
					found |= tracker_move_0[move_kong] == index;
				} else if (move_value == 2) {
					found |= tracker_move_1[move_kong] == index;
				} else if (move_value == 3) {
					found |= tracker_move_2[move_kong] == index;
				}
				break;
			case PURCHASE_SLAM:
				if (index == TRACKER_TYPE_SLAM) {
					if (move_value >= 2) {
						return move_value;
					}
				}
				break;
			case PURCHASE_GUN:
				if (move_value == 1) {
					found |= tracker_gun[move_kong] == index;
				} else if (move_value == 2) {
					found |= TRACKER_TYPE_HOMING == index;
				} else if (move_value == 3) {
					found |= TRACKER_TYPE_SNIPER == index;
				}
				break;
			case PURCHASE_AMMOBELT:
				if (move_value == 1) {
					found |= index == TRACKER_TYPE_BELT_1;
				} else if (move_value == 2) {
					found |= index == TRACKER_TYPE_BELT_2;
				}
				break;
			case PURCHASE_INSTRUMENT:
				if (move_value == 1) {
					found |= tracker_instrument[move_kong] == index;
				} else if (move_value == 2) {
					found |= index == TRACKER_TYPE_INSUPG_1;
				} else if (move_value == 4) {
					found |= index == TRACKER_TYPE_INSUPG_2;
				} else if (move_value == 3) {
					found |= index == TRACKER_TYPE_MELON_3;
				}
				found |= index == TRACKER_TYPE_MELON_2;
				break;
			case PURCHASE_FLAG:
				if (move_value == FLAG_TBARREL_DIVE) {
					found |= index == TRACKER_TYPE_DIVE;
				} else if (move_value == FLAG_TBARREL_BARREL) {
					found |= index == TRACKER_TYPE_BARREL;
				} else if (move_value == FLAG_TBARREL_ORANGE) {
					found |= index == TRACKER_TYPE_ORANGE;
				} else if (move_value == FLAG_TBARREL_VINE) {
					found |= index == TRACKER_TYPE_VINE;
				} else if (move_value == FLAG_ABILITY_CAMERA) {
					found |= index == TRACKER_TYPE_CAMERA;
				} else if (move_value == FLAG_ABILITY_SHOCKWAVE) {
					found |= index == TRACKER_TYPE_SHOCKWAVE;
				} else if (move_value == -2) {
					found |= (index == TRACKER_TYPE_CAMERA);
					found |= (index == TRACKER_TYPE_SHOCKWAVE);
				}
				break;
		}
	}
	return found;
}

int getEnabledState(int index) {
	/*
		0-24:
			0: Gun
			1: Instrument
			2: Move
			3: Barrel
			4: Pad
			Repeat for all 5 kongs
		25: Slam
		26: Homing
		27: Sniper
		28: Ammo Belt
		29: Instrument Upg
		30: Dive
		31: Orange
		32: Barrel
		33: Vine
		34: Camera
		35: Shockwave
	*/
	int is_pre_given = getInitFileMove(index);
	if (index == TRACKER_TYPE_SLAM) {
		if ((is_pre_given >= 2) && (MovesBase[0].simian_slam < 2)) {
			return is_pre_given;
		}
	} else {
		if (is_pre_given) {
			return 1;
		}
	}
	if (index < 25) {
		int kong = index / 5;
		int submove = index % 5;
		if (Rando.unlock_moves) {
			return 1;
		}
		if (submove == 0) {
			// Gun
			return MovesBase[kong].weapon_bitfield & 1;
		} else if (submove == 1) {
			// Instrument
			return MovesBase[kong].instrument_bitfield & 1;
		} else if (submove == 2) {
			// Move
			int move_placement = 2;
			if (kong == 2) {
				move_placement = 0;
			} else if (kong > 2) {
				move_placement = 1;
			}
			return (MovesBase[kong].special_moves & (1 << move_placement)) != 0;
		} else if (submove == 3) {
			// Barrel
			int barrel_placement = 0;
			if (kong < 2) {
				barrel_placement = 1;
			} else if (kong == 2) {
				barrel_placement = 2;
			}
			return (MovesBase[kong].special_moves & (1 << barrel_placement)) != 0;
		} else if (submove == 4) {
			// Pad
			int pad_placement = 2;
			if (kong == 0) {
				pad_placement = 0;
			} else if (kong == 2) {
				pad_placement = 1;
			}
			return (MovesBase[kong].special_moves & (1 << pad_placement)) != 0;
		}
	} else {
		if (index < 34) {
			if (Rando.unlock_moves) {
				if (index == TRACKER_TYPE_SLAM) {
					return 3;
				}
				if ((index == TRACKER_TYPE_AMMOBELT) || (index == TRACKER_TYPE_INSTRUMENT_UPG)) {
					return 2;
				}
				return 1;
			}
		} else if (index < 36) {
			if (Rando.camera_unlocked) {
				return 1;
			}
		}
		switch(index) {
			case TRACKER_TYPE_SLAM:
				{
					// Slam
					int slam_val = MovesBase[0].simian_slam;
					if (slam_val < 1) {
						return 1;
					} else if (slam_val > 3) {
						return 3;
					}
					return slam_val;
				}
			case TRACKER_TYPE_HOMING:
				// Homing
				return (MovesBase[0].weapon_bitfield & 2) != 0;
			case TRACKER_TYPE_SNIPER:
				// Sniper
				return (MovesBase[0].weapon_bitfield & 4) != 0;
			case TRACKER_TYPE_AMMOBELT:
				// Ammo Belt
				return MovesBase[0].ammo_belt;
			case TRACKER_TYPE_INSTRUMENT_UPG:
				// Instrument Upgrade
				if (MovesBase[0].instrument_bitfield & 8) {
					return 2;
				} else if (MovesBase[0].instrument_bitfield & 2) {
					return 1;
				}
				return 0;
			case TRACKER_TYPE_DIVE:
				// Dive
				return checkFlag(FLAG_TBARREL_DIVE,0);
			case TRACKER_TYPE_ORANGE:
				// Orange
				return checkFlag(FLAG_TBARREL_ORANGE,0);
			case TRACKER_TYPE_BARREL:
				// Barrel
				return checkFlag(FLAG_TBARREL_BARREL,0);
			case TRACKER_TYPE_VINE:
				// Vine
				return checkFlag(FLAG_TBARREL_VINE,0);
			case TRACKER_TYPE_CAMERA:
				// Camera
				return checkFlag(FLAG_ABILITY_CAMERA,0);
			case TRACKER_TYPE_SHOCKWAVE:
				// Shockwave
				return checkFlag(FLAG_ABILITY_SHOCKWAVE,0);
			case TRACKER_TYPE_KEY1:
			case TRACKER_TYPE_KEY2:
			case TRACKER_TYPE_KEY3:
			case TRACKER_TYPE_KEY4:
			case TRACKER_TYPE_KEY5:
			case TRACKER_TYPE_KEY6:
			case TRACKER_TYPE_KEY7:
			case TRACKER_TYPE_KEY8:
				{
					// Keys in
					int key_index = index - TRACKER_TYPE_KEY1;
					int key_there = checkFlag(FLAG_KEYIN_KEY1 + key_index, 0);
					if (!key_there) {
						if (Rando.keys_preturned & (1 << key_index)) {
							key_there = 1;
						}
					}
					return key_there;
				}
			case TRACKER_TYPE_MELON_2:
				if (Rando.unlock_moves) {
					return 1;
				}
				return CollectableBase.Melons >= 2;
			case TRACKER_TYPE_MELON_3:
				if (Rando.unlock_moves) {
					return 1;
				}
				return CollectableBase.Melons >= 3;
			case TRACKER_TYPE_INSUPG_1:
				if (Rando.unlock_moves) {
					return 1;
				}
				return (MovesBase[0].instrument_bitfield & 2) != 0;
			case TRACKER_TYPE_INSUPG_2:
				if (Rando.unlock_moves) {
					return 1;
				}
				return (MovesBase[0].instrument_bitfield & 8) != 0;
			case TRACKER_TYPE_BELT_1:
				if (Rando.unlock_moves) {
					return 1;
				}
				return MovesBase[0].ammo_belt >= 1;
			case TRACKER_TYPE_BELT_2:
				if (Rando.unlock_moves) {
					return 1;
				}
				return MovesBase[0].ammo_belt >= 2;
		}
	}
	return 0;
}

void updateEnabledStates(void) {
	for (int i = 0; i < (int)(sizeof(tracker_info) / sizeof(tracker_struct)); i++) {
		tracker_info[i].enabled = getEnabledState(tracker_info[i].type);
	}
}

#define TRACKER_INIT 2
#define TRACKER_WIDTH 254
#define TRACKER_HEIGHT 128

void initTracker(void) {
	updated_tracker = 0;
}

void resetTracker(void) {
	updated_tracker = 0;
	WipeImageCache();
}

void modifyTrackerImage(int dl_offset) {
	// Check if tracker needs updating
	if (updated_tracker == (TRACKER_INIT + 3)) {
		return;
	}
	updated_tracker += 1;
	if (updated_tracker == TRACKER_INIT) {
		// wipeTrackerCache();
		updateEnabledStates();
	}
	if (updated_tracker == (TRACKER_INIT + 3)) {
		// Load Tracker Image into cache
		short* image = getPtr14Texture(IMAGE_TRACKER);
		// Manipulate cached image
		int width = TRACKER_WIDTH;
		for (int i = 0; i < (int)(sizeof(tracker_info) / sizeof(tracker_struct)); i++) {
			int enabled = tracker_info[i].enabled;
			for (int x = tracker_info[i].min_x; x < tracker_info[i].max_x; x++) {
				for (int y = tracker_info[i].min_y; y < tracker_info[i].max_y; y++) {
					unsigned short init_rgba = *(short*)(image + (y * width) + x);
					if (init_rgba & 1) {
						// Has Alpha
						unsigned short new_rgba = 1;
						int update = 0;
						if (tracker_info[i].type == TRACKER_TYPE_SLAM) {
							if (!enabled) {
								new_rgba = 0;
								update = 1;
							} else {
								int subdue[] = {0,0,0};
								if (enabled == 1) {
									subdue[0] = 1; // B
									subdue[1] = 3; // G
									subdue[2] = 1; // R
									update = 1;
								} else if (enabled == 2) {
									subdue[0] = 3; // B
									subdue[1] = 2; // G
									subdue[2] = 0; // R
									update = 1;
								} else if (enabled == 3) {
									subdue[0] = 0; // B
									subdue[1] = 0; // G
									subdue[2] = 3; // R
									update = 1;
								}
								for (int c = 0; c < 3; c++) {
									int shift = (5 * c) + 1;
									float channel = (init_rgba >> shift) & 31;
									if (subdue[c] == 0) {
										channel = 0;
									} else if (subdue[c] == 1) {
										channel *= 0.19f;
									} else if (subdue[c] == 2) {
										channel *= 0.5f;
									}
									new_rgba |= (((int)(channel) & 31) << shift);
								}
							}
						} else if ((tracker_info[i].type == TRACKER_TYPE_INSUPG_2) || (tracker_info[i].type == TRACKER_TYPE_BELT_2)) {
							if (!enabled) {
								update = 1;
								new_rgba = 0;
							}
						} else {
							if (!enabled) {
								for (int c = 0; c < 3; c++) {
									int shift = (5 * c) + 1;
									float channel = (init_rgba >> shift) & 31;
									channel *= 0.3f; // Depreciation
									new_rgba |= (((int)(channel) & 31) << shift);
								}
								update = 1;
							}
						}
						if (update) {
							*(short*)(image + (y * width) + x) = new_rgba;
						}
					}
				}
			}
		}
	}
}

int* display_images(int* dl) {
	int y_offset = FileScreenDLOffset - 720;
	dl = drawImage(dl, IMAGE_TRACKER, RGBA16, TRACKER_WIDTH, TRACKER_HEIGHT, 160, y_offset + 150,1.0f, 1.0f,0xFF);
	modifyTrackerImage(y_offset);
	return dl;
}

int* display_text(int* dl) {
	int y = FileScreenDLOffset - 320;
	// Balanced IGT
	// y += LINE_GAP;
	int secs = IGT % 60;
	float secsf = secs;
	secsf /= 60;
	int hm = IGT / 60;
	int minutes = hm % 60;
	int hours = hm / 60;
	dk_strFormat((char*)balanced_igt, "%03d:%02d:%02d",hours,minutes,secs);
	dl = drawText(dl, 1, 410, y + 80, (char*)balanced_igt, 0xFF, 0xFF, 0xFF, 0xFF);
	// Percentage Counter
	dk_strFormat((char*)perc_str, "%d%%", FilePercentage);
	dl = drawText(dl, 1, 410, y + 50, (char*)perc_str, 0xFF, 0xFF, 0xFF, 0xFF);
	dl = display_images(dl);
	return dl;
}

static unsigned char hash_textures[] = {48,49,50,51,55,62,63,64,65,76};
int* displayHash(int* dl, int y_offset) {
	for (int i = 0; i < 5; i++) {
		int hash_index = Rando.hash[i] % 10;
		dl = drawImage(dl, hash_textures[hash_index], RGBA16, 32, 32, 440 + (100 * i), 920 - y_offset, 3.0f, 3.0f, 0xFF);
	}
	return dl;
}

static const short kong_flags[] = {FLAG_KONG_DK,FLAG_KONG_DIDDY,FLAG_KONG_LANKY,FLAG_KONG_TINY,FLAG_KONG_CHUNKY};
void correctKongFaces(void) {
	if (Rando.unlock_kongs) {
		for (int i = 0; i < 5; i++) {
			int flag = checkFlag(kong_flags[i],0);
			KongUnlockedMenuArray[i] = flag;
			if (!flag) {
				KongUnlockedMenuArray[i] = (Rando.unlock_kongs & (1 << i)) != 0;
			}
		}
		if (!checkFlag(FLAG_KONG_DK,0)) {
			if ((Rando.unlock_kongs & 1) == 0) {
				KongUnlockedMenuArray[0] = 0;
			}
		}
	} else {
		for (int i = 0; i < 5; i++) {
			KongUnlockedMenuArray[i] = checkFlag(kong_flags[i],0);
		}
		KongUnlockedMenuArray[(int)Rando.starting_kong] = 1;
		if (Rando.starting_kong != 0) {
			if (!checkFlag(FLAG_KONG_DK,0)) {
				KongUnlockedMenuArray[0] = 0;
			}
		}
	}
}

void wipeFileMod(int file, int will_save) {
	resetTracker();
	WipeFile(file, will_save);
}

void enterFileProgress(int sfx) {
	resetTracker();
	playSFX(sfx);
}

void giveCollectables(void) {
	int mult = 1;
	if (MovesBase[0].ammo_belt > 0) {
		mult = 2 * MovesBase[0].ammo_belt;
	}
	CollectableBase.StandardAmmo = 25 * mult;
	CollectableBase.Oranges = 10;
	CollectableBase.Crystals = 1500;
	CollectableBase.Film = 5;
}

void file_progress_screen_code(actorData* actor, int buttons) {
	/*
		Buttons:
			0001 0000 0000 - Z Button
			0000 1000 0000 - C Down
			0000 0100 0000 - C Up
			0000 0010 0000 - Default
			0000 0001 0000 - Down
			0000 0000 1000 - Right
			0000 0000 0100 - Default
			0000 0000 0010 - B Button
			0000 0000 0001 - A Button
	*/
	menu_controller_paad* paad = actor->paad;
	if (paad->screen_transition_progress == 0.0f) {
		if (paad->unk_4 == 0.0f) {
			if (buttons & 1) { // A
				lockInput(1);
				int file_empty = isFileEmpty(0);
				fileStart(0);
				if (file_empty) {
					// New File
					unlockMoves();
					applyFastStart();
					openCrownDoor();
					giveCollectables();
					activateBananaports();
					if(Rando.fast_gbs) {
						setPermFlag(FLAG_RABBIT_ROUND1); //Start race at round 2
					}
					if (Rando.helm_hurry_mode) {
						QueueHelmTimer = 1;
					}
					setPermFlag(FLAG_ESCAPE);
					Character = Rando.starting_kong;
					StoredSettings.file_extra.location_sss_purchased = 0;
					StoredSettings.file_extra.location_ab1_purchased = 0;
					StoredSettings.file_extra.location_ug1_purchased = 0;
					StoredSettings.file_extra.location_mln_purchased = 0;
					for (int i = 0; i < 9; i++) {
						StoredSettings.file_extra.level_igt[i] = 0;
					}
					SaveToGlobal();
				} else {
					// Dirty File
					Character = Rando.starting_kong;
					determineStartKong_PermaLossMode();
					giveCollectables();
					if (Rando.helm_hurry_mode) {
						setFlag(FLAG_LOADED_GAME_OVER,1,0);
					}
				}
				ForceStandardAmmo = 0;
			} else if (buttons & 2) { // B
				playSFX(0x2C9);
				paad->prevent_action = 0;
				paad->next_screen = 1;
			} else if (buttons & 0x100) { // Z
				if (!isFileEmpty(0)) {
					playSFX(0x2C9);
					paad->prevent_action = 0;
					paad->next_screen = 5;
				} else {
					playSFX(Wrong);
				}
			}
		}
		initMenuBackground(paad,4);
	}
	updateMenuController(actor,paad,1);
}

static char* inverted_controls_str[] = {
	"INVERTED",
	"NON-INVERTED"
};

int* displayInverted(int* dl, int style, int x, int y, char* str, int unk0) {
	return displayText(dl, style, x, y, inverted_controls_str[(int)InvertedControls], unk0);
}

void initOptionScreen(void) {
	*(char*)(0x800338FC) = 5; // 5 Options
	*(short*)(0x8002DA86) = 1; // Cap to 1
	*(short*)(0x8002DA46) = getHi(&InvertedControls); // Up/Down Edit
	*(short*)(0x8002DA4E) = getLo(&InvertedControls); // Up/Down Edit
	*(short*)(0x8002DA1E) = getHi(&InvertedControls); // Up/Down Edit
	*(short*)(0x8002DA22) = getLo(&InvertedControls); // Up/Down Edit
	*(short*)(0x8002DADE) = getHi(&InvertedControls); // Save to global
	*(short*)(0x8002DAE2) = getLo(&InvertedControls); // Save to global
	*(short*)(0x8002DA88) = 0x1000; // Prevent Language Update
	*(int*)(0x8002DEC4) = 0x0C000000 | (((int)&displayInverted & 0xFFFFFF) >> 2); // Modify Function Call
}

static unsigned char previous_map_save = 0x22;

int updateLevelIGT(void) {
	int new_igt = getNewSaveTime();
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		sum += StoredSettings.file_extra.level_igt[i];
	}
	int diff = new_igt - sum;
	int world = getWorld(previous_map_save, 1);
	if (world < 9) {
		StoredSettings.file_extra.level_igt[world] += diff;
	}
	previous_map_save = CurrentMap;
	return new_igt;
}