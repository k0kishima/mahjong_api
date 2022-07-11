from django.test import TestCase
from conduit.apps.core.hand import calculate_shanten_advanceable_tiles, Tile, TileType

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
                Tile(TileType.MAN, 1),
                Tile(TileType.MAN, 4),
                Tile(TileType.MAN, 5),
                Tile(TileType.MAN, 8),
                Tile(TileType.PIN, 1),
                Tile(TileType.PIN, 4),
                Tile(TileType.SOU, 1),
                Tile(TileType.SOU, 4),
                Tile(TileType.SOU, 7),
            ]
        )
