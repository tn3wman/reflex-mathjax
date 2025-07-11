"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx
from rxconfig import config
from reflex_mathjax import mathjax

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
            width="100%",
            align="center",
            spacing="7",
        ),
        width="100vw",
        height="100vh",
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
