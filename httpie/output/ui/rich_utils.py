import os

from rich.console import Console, RenderableType

from httpie.output.ui.rich_palette import _make_rich_color_theme


def render_as_string(renderable: RenderableType) -> str:
    """Render any `rich` object in a fake console and
    return a *style-less* version of it as a string."""

    with open(os.devnull, 'w') as null_stream:
        fake_console = Console(file=null_stream, record=True, theme=_make_rich_color_theme())
        fake_console.print(renderable)
        return fake_console.export_text()
