from rxconfig import config
from .api.suggestions import SuggestionState
import reflex as rx

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
        rx.form(
            rx.input(
                placeholder="City",
                name="city",
            ),
            rx.input(
                placeholder="State",
                name="state",
            ),
            rx.button(
                "Generate",
                type="submit",
            ),
            on_submit=SuggestionState.handle_submit
        ),
        rx.button(
            "what",
            on_click=SuggestionState.generate_suggestions
        )
    )

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        accent_color="grass",
    )
)

"""rx.form(
        rx.vstack(
                rx.input(
                    placeholder="City",
                    name="city",
                ),
                rx.input(
                    placeholder="State",
                    name="state",
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=SuggestionState.handle_submission
        """
