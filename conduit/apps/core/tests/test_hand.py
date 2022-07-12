from django.test import TestCase
from conduit.apps.core.hand import calculate_shanten_advanceable_tiles, Tile, TileColor

class calculateShantenAdvanceableTilesFunctionTests(TestCase):
    def test_raise_exception_for_too_many_tiles(self):
        with self.assertRaises(ValueError):
            calculate_shanten_advanceable_tiles(man='23677', pin='2399', sou='23456')

    def test_raise_exception_for_too_little_tiles(self):
        with self.assertRaises(ValueError):
            calculate_shanten_advanceable_tiles(man='236', pin='2399', sou='23456')

    def test_calculation_for_just_13_tiles(self):
        self.assertEqual(
            calculate_shanten_advanceable_tiles(man='2367', pin='2399', sou='23456'),
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
            ]
        )
