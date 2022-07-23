from conduit.apps.core.hand import (
    calculate_shanten,
    calculate_shanten_advanceable_tiles,
    one_line_string_tiles_to_color_indexed_strings,
)
from django.http import JsonResponse
from django.shortcuts import render


def shanten_advanceable_tiles(request, one_line_string_tiles):
    shanten_advanceable_tiles = calculate_shanten_advanceable_tiles(
        **one_line_string_tiles_to_color_indexed_strings(one_line_string_tiles)
    )
    return JsonResponse(
        {
            "shanten_advanceable_tiles": [
                [color.value, number] for color, number in shanten_advanceable_tiles
            ],
        }
    )


def shanten(request, one_line_string_tiles):
    return JsonResponse(
        {
            "shanten": calculate_shanten(
                **one_line_string_tiles_to_color_indexed_strings(one_line_string_tiles)
            ),
        }
    )
