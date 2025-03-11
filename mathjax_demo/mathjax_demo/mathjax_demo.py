"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_mathjax import mathjax

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    pass

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to reflex-mathjax demo!", size="9"),
            rx.heading("Basic MathJax example with Latex"),
            mathjax("\\(\\frac{10}{4x} \\approx 2^{12}\\)"),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
