from app.knight.knight import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


def knights_builder(knights_config: dict, knight: str) -> Knight:
    return Knight(
        knights_config.get(knight).get("name"),
        knights_config.get(knight).get("hp"),
        knights_config.get(knight).get("power"),
        [Armour(item.get("part"), item.get("protection"))
         for item in knights_config.get(knight).get("armour")],
        Weapon(
            knights_config.get(knight).get("weapon").get("name"),
            knights_config.get(knight).get("weapon").get("power"),
        ),
        Potion(
            knights_config.get(knight).get("potion").get("name"),
            knights_config.get(knight).get("potion").get("effect"),
        ) if knights_config.get(knight).get("potion") is not None else None,
    )
