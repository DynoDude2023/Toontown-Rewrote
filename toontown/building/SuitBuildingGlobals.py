from ElevatorConstants import *
SuitBuildingInfo = (((1, 1), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (1, 3), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (4, 4), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (8, 10), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1,) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 1 - 1
  ),
 ((1, 2), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (2, 4), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (5, 5), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (8, 10), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1.2) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 2 - 2
  ),
 ((1, 3), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (3, 5), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (6, 6),  # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (8, 10), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1.3, 1.6) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 3 - 3
  ),
 ((2, 3), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (4, 6), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (7, 7), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (8, 10), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1.4, 1.8) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 4 - 4
  ),
 ((3, 5), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (5, 7), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (8, 8), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (8, 10), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1.6, 1.8, 2, 2.2) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 5 - 5
  ),
 ((3, 6), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (6, 8), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (9, 9), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (10, 12), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1.6, 2, 2.4, 2.8, 3.2) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 6 - 6
  ),
 ((4, 7), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (7, 9), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (10, 10), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (10, 14), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1.6, 1.8, 2.2, 2.4, 2.8, 3) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 7 - 7
  ),
 ((5, 8), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (8, 10), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (11, 11), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (12, 16), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1.8, 2.4, 3, 3.2, 3.8, 4.4, 4.6) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 8 - 8
  ),
 ((6, 10), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (9, 11), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (12, 15), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (14, 20), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1.4, 1.8, 2.6, 3.4, 4, 4.4, 4.8, 5.8, 6.4, 7) # SUIT_BLDG_INFO_LVL_POOL_MULTS - lvlPoolMults [One value for each floor]
  # SUIT_BLDG_INFO_REVIVES [Cogs can have revives]

  # Cog Building Difficulty 9 - 9
  ),
 ((1, 1), # SUIT_BLDG_INFO_FLOORS - floorRange [minFloors, maxFloors]
  (1, 12), # SUIT_BLDG_INFO_SUIT_LVLS - lvlRange [lvlMin, lvlMax]
  (12, 12), # SUIT_BLDG_INFO_BOSS_LVLS - bossLvlRange [bossLvlMin, bossLvlMax]
  (67, 67), # SUIT_BLDG_INFO_LVL_POOL - lvlPoolRange [lvlPoolMin, lvlPoolMax]
  (1, 1, 1, 1, 1)),
 ((1, 12),
  (12, 12),
  (67, 67),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (8, 12),
  (12, 12),
  (100, 100),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (1, 12),
  (12, 12),
  (100, 100),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (8, 12),
  (12, 12),
  (150, 150),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (8, 12),
  (12, 12),
  (275, 275),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (9, 12),
  (12, 12),
  (206, 206),
  (1,
   1,
   1,
   1,
   1),
  (1,)),
 ((1, 1),
  (1, 5),
  (5, 5),
  (33, 33),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (4, 5),
  (5, 5),
  (50, 50),
  (1,
   1,
   1,
   1,
   1)),
  ((1, 1),
   (10, 15),
   (15, 15),
   (206, 206),
   (1,
    1,
    1,
    1,
    1),
    (2,)))
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
