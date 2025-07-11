"""Reflex custom component Mathjax."""

import reflex as rx
from reflex.components.component import NoSSRComponent

class MathJaxContext(NoSSRComponent):
    """Mathjax component."""

    library = "better-react-mathjax"
    tag = "MathJaxContext"
    # is_default = True

mathjax_context = MathJaxContext.create()

class MathJaxComponent(NoSSRComponent):
    library = "better-react-mathjax"
    # is_default = True

    @staticmethod
    def _get_app_wrap_components() -> dict[tuple[int, str], rx.Component]:
        return {
            (500, "MathJaxContext"): mathjax_context,
        }
    
class MathJax(MathJaxComponent):
    """Mathjax component for rendering LaTeX math expressions."""

    tag = "MathJax"
    # is_default = True

mathjax = MathJax.create

# import reflex as rx
# from reflex.components.component import Component


# class MantineProvider(rx.Component):
#     library = "@mantine/core"
#     tag = "MantineProvider"


# mantine_provider = MantineProvider.create()
# mantine_provider.special_props.update({rx.Var.create("withGlobalStyles"), rx.Var.create("withNormalizeCSS")})


# class MantineComponent(rx.Component):
#     library = "@mantine/core"

#     @staticmethod
#     def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
#         return {
#             (10, "MantineProvider"): mantine_provider,
#         }


# class Collapse(MantineComponent):
#     tag = "Collapse"

#     # variables
#     in_: rx.Var[bool]  # type: ignore
#     animate_opacity: rx.Var[bool]  # type: ignore
#     transition_duration: rx.Var[int]  # type: ignore

#     def get_event_triggers(self):
#         """Get the event triggers for the component.

#         Returns:
#             The event triggers.
#         """
#         return super().get_event_triggers() | {
#             "on_transition_end": lambda: [],
#         }


# class Button(MantineComponent):
#     tag = "Button"


# class State(rx.State):
#     is_opened: bool = False


# def index():
#     return rx.vstack(
#         Button.create("Toggle", on_click=lambda: State.set_is_opened(~State.is_opened)),
#         Collapse.create("foo", in_=State.is_opened),
#     )


# # Add state and page to the app.
# app = rx.App()
# app.add_page(index)
# app.compile()