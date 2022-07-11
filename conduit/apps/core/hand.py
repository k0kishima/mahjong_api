from mahjong.tile import TilesConverter
from mahjong.shanten import Shanten
from enum import Enum
from collections import namedtuple
from typing import List
import copy

Tile = namedtuple('Tile', ('tile_type', 'tile_number'))

class TileType(Enum):
    MAN = 'MAN'
    PIN = 'PIN'
    SOU = 'SOU'
    HONORS = 'HONORS'

# TODO: 引数の型をちゃんとあてたい
def calculate_shanten_advanceable_tiles(sou=None, pin=None, man=None, honors=None) -> List[Tile]:
    tiles = TilesConverter.string_to_34_array(sou=sou, pin=pin, man=man, honors=honors)

    # FIXME: 槓の場合は待ちの状態でも13枚になるとは限らないのでは？
    if sum(tiles) != 13:
        raise ValueError('This method calculates for the hand tiles after drawing and discarding, please hand over 13 tiles without excess or deficiency.')

    shanten = Shanten()
    current_shanten = shanten.calculate_shanten(tiles)

    shanten_advanceable_tile_indexes = []
    for x in range(0, 34):
        new_tiles = copy.copy(tiles)

        # FIXME: これも槓の場合を想定すべき
        if new_tiles[x] == 4:
            raise NotImplemented

        new_tiles[x] += 1
        if shanten.calculate_shanten(new_tiles) < current_shanten:
            shanten_advanceable_tile_indexes.append(x)

    return [Tile(_tile_type_of(x), _tile_number_of(x)) for x in shanten_advanceable_tile_indexes]


def _tile_number_of(index_of_34_array: int) -> int:
    if index_of_34_array > 33:
        raise IndexError
    return (index_of_34_array % 9) + 1

def _tile_type_of(index_of_34_array: int) -> TileType:
    if index_of_34_array >= 0 and index_of_34_array < 9:
        return TileType.MAN
    elif index_of_34_array >= 9 and index_of_34_array < 18:
        return TileType.PIN
    elif index_of_34_array >= 18 and index_of_34_array < 27:
        return TileType.SOU
    elif index_of_34_array >= 28 and index_of_34_array < 34:
        return TileType.HONORS
    else:
        raise IndexError
