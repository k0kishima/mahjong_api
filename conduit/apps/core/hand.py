from mahjong.tile import TilesConverter
from mahjong.shanten import Shanten
from enum import Enum
from collections import namedtuple
from typing import List
import copy

Tile = namedtuple('Tile', ('tile_color', 'tile_number'))

class TileColor(Enum):
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

def calculate_shanten(sou=None, pin=None, man=None, honors=None) -> int:
    tiles = TilesConverter.string_to_34_array(sou=sou, pin=pin, man=man, honors=honors)
    shanten = Shanten()
    return shanten.calculate_shanten(tiles)

def one_line_string_tiles_to_color_indexed_strings(one_line_string_tiles: str):
    tiles_by_34_array = TilesConverter.one_line_string_to_34_array(one_line_string_tiles)
    return {
        'man': ''.join([str(index+1) * quantity for index, quantity in enumerate(tiles_by_34_array[0:9])]),
        'pin': ''.join([str(index+1) * quantity for index, quantity in enumerate(tiles_by_34_array[9:18])]),
        'sou': ''.join([str(index+1) * quantity for index, quantity in enumerate(tiles_by_34_array[18:27])]),
        'honors': ''.join([str(index+1) * quantity for index, quantity in enumerate(tiles_by_34_array[27:])]),
    }

def _tile_number_of(index_of_34_array: int) -> int:
    if index_of_34_array > 33:
        raise IndexError
    return (index_of_34_array % 9) + 1

def _tile_type_of(index_of_34_array: int) -> TileColor:
    if index_of_34_array >= 0 and index_of_34_array < 9:
        return TileColor.MAN
    elif index_of_34_array >= 9 and index_of_34_array < 18:
        return TileColor.PIN
    elif index_of_34_array >= 18 and index_of_34_array < 27:
        return TileColor.SOU
    elif index_of_34_array >= 27 and index_of_34_array < 34:
        return TileColor.HONORS
    else:
        raise IndexError
