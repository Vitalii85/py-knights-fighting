from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion
from app.knight.knight import Knight


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knights_config: dict) -> dict[str, int]:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(
        knights_config.get("lancelot").get("name"),
        knights_config.get("lancelot").get("hp"),
        knights_config.get("lancelot").get("power"),
        [Armour(item.get("part"), item.get("protection"))
         for item in knights_config.get("lancelot").get("armour")],
        Weapon(
            knights_config.get("lancelot").get("weapon").get("name"),
            knights_config.get("lancelot").get("weapon").get("power"),
        ),
        Potion(
            knights_config.get("lancelot").get("potion").get("name"),
            knights_config.get("lancelot").get("potion").get("effect"),
        ) if
        knights_config.get("lancelot").get("potion") is not None else None,
    )

    # arthur
    arthur = Knight(
        knights_config.get("arthur").get("name"),
        knights_config.get("arthur").get("hp"),
        knights_config.get("arthur").get("power"),
        [Armour(item.get("part"), item.get("protection"))
         for item in knights_config.get("arthur").get("armour")],
        Weapon(
            knights_config.get("arthur").get("weapon").get("name"),
            knights_config.get("arthur").get("weapon").get("power"),
        ),
        Potion(
            knights_config.get("arthur").get("potion").get("name"),
            knights_config.get("arthur").get("potion").get("effect"),
        ) if knights_config.get("arthur").get("potion") is not None else None,
    )

    # mordred
    mordred = Knight(
        knights_config.get("mordred").get("name"),
        knights_config.get("mordred").get("hp"),
        knights_config.get("mordred").get("power"),
        [Armour(item.get("part"), item.get("protection"))
         for item in knights_config.get("mordred").get("armour")],
        Weapon(
            knights_config.get("mordred").get("weapon").get("name"),
            knights_config.get("mordred").get("weapon").get("power"),
        ),
        Potion(
            knights_config.get("mordred").get("potion").get("name"),
            knights_config.get("mordred").get("potion").get("effect"),
        ) if knights_config.get("mordred").get("potion") is not None else None,
    )

    # red_knight
    red_knight = Knight(
        knights_config.get("red_knight").get("name"),
        knights_config.get("red_knight").get("hp"),
        knights_config.get("red_knight").get("power"),
        [Armour(item.get("part"), item.get("protection"))
         for item in knights_config.get("red_knight").get("armour")],
        Weapon(
            knights_config.get("red_knight").get("weapon").get("name"),
            knights_config.get("red_knight").get("weapon").get("power"),
        ),
        Potion(
            knights_config.get("red_knight").get("potion").get("name"),
            knights_config.get("red_knight").get("potion").get("effect"),
        ) if
        knights_config.get("red_knight").get("potion") is not None else None,
    )

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle_with(mordred)

    # 2 Arthur vs Red Knight:
    arthur.battle_with(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
