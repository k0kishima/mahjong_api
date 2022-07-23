from conduit.apps.core.hand import (
    Tile,
    TileColor,
    calculate_shanten_advanceable_tiles,
    one_line_string_tiles_to_color_indexed_strings,
)
from django.test import TestCase


class calculateShantenAdvanceableTilesFunctionTests(TestCase):
    def test_raise_exception_for_too_many_tiles(self):
        with self.assertRaises(ValueError):
            calculate_shanten_advanceable_tiles(man="23677", pin="2399", sou="23456")

    def test_raise_exception_for_too_little_tiles(self):
        with self.assertRaises(ValueError):
            calculate_shanten_advanceable_tiles(man="236", pin="2399", sou="23456")

    def test_calculation_for_just_13_tiles(self):
        self.assertEqual(
            calculate_shanten_advanceable_tiles(man="2367", pin="2399", sou="23456"),
            [
                Tile(TileColor.MAN, 1),
                Tile(TileColor.MAN, 4),
                Tile(TileColor.MAN, 5),
                Tile(TileColor.MAN, 8),
                Tile(TileColor.PIN, 1),
                Tile(TileColor.PIN, 4),
                Tile(TileColor.SOU, 1),
                Tile(TileColor.SOU, 4),
                Tile(TileColor.SOU, 7),
            ],
        )

    def test_one_line_string_tiles_to_color_indexed_strings(self):
        self.assertEqual(
            one_line_string_tiles_to_color_indexed_strings("123s456p789m11222z"),
            {
                "man": "789",
                "pin": "456",
                "sou": "123",
                "honors": "11222",
            },
        )
