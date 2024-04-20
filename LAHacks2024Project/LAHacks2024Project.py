"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

@rx.page(route="/", title="Home Page")
def home() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.button(
                "Get Started",
                color="#EDFA8B",
                size="4",
            ),
            rx.button(
                "More Info",
                color="#EDFA8B",
                size="4",
            ),
            spacing="2",
            align="center",
        ),
        background="linear-gradient(45deg, green, blue)",
    )


@rx.page(route="/test", title="Testing Page")
def test() -> rx.Component:
    return rx.vstack(
    rx.desktop_only(
        rx.text("Desktop View"),
    ),
    rx.tablet_only(
        rx.text("Tablet View"),
    ),
    rx.mobile_only(
        rx.text("Mobile View"),
    ),
    rx.mobile_and_tablet(
        rx.text("Visible on Mobile and Tablet"),
    ),
    rx.tablet_and_desktop(
        rx.text("Visible on Desktop and Tablet"),
    ),
)

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        accent_color="grass",
    )
)
