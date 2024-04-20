"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):


    def printTestMsg(self):
        print("Hello World")
        

    """The app state."""

_GREEN = "#86FF9D"#"#edfa8b"
_BLUE = "#3a53aa"#"#5664D6"#"#1e425e"

@rx.page(route="/", title="Home Page")
def home() -> rx.Component:
    return \
    rx.aspect_ratio(
        rx.flex(

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            rx.flex(
                rx.flex(
                    rx.text("G",color=_BLUE,size="8",weight="regular",),
                    rx.text("O",color=_BLUE,size="6",weight="medium",),
                    align = "baseline"
                ),
                rx.flex(
                    rx.text("G",color=_BLUE,size="8",weight="regular",),
                    rx.text("REEN",color=_BLUE,size="6",weight="medium",),
                    align = "baseline"
                ),
                spacing="4",
                align = "baseline"
            ),
            
            rx.box(),
            rx.box(),

            rx.text(
                "with",
                color=_BLUE,
                size="7",
                weight="medium",
            ),
            
            rx.box(),
            rx.box(),
            
            rx.text(
                "G R E E N       G U I D E",
                color=_BLUE,
                size="9",
                weight="bold",
            ),

            rx.box(),
            rx.box(),
            
            rx.text(
                "An Interactive Experience About How",
                color=_BLUE,
                size="8",
                weight="regular",
                align="center",
            ),
            rx.text(
                "We Can Be More Environmentally",
                color=_BLUE,
                size="8",
                weight="regular",
                align="center",
            ),
            rx.text(
                "Proactive In Our Communities.",
                color=_BLUE,
                size="8",
                weight="regular",
                align="center",
            ),

            #An Interactive Experience About How We Can Be More Environmentally Proactive In Our Communities.
            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            rx.button(
                "Get Started",
                #color=_GREEN,
                #color_scheme="indigo",
                size="4",
                on_click=rx.redirect("/explore/"),
            ),

            rx.box(),
            rx.box(),

            rx.button(
                "Credits",
                #color=_GREEN,
                #color_scheme="indigo",
                size="4",
                on_click=rx.redirect("/credits/"),
            ),

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            spacing="3",
            direction="column",
            background=f"linear-gradient(45deg, #ffffff, {_GREEN})",
            #background=f"linear-gradient(45deg, {_GREEN}, #00ff33)",
            align="center",
            flex_wrap="wrap",
            width = "100%",
            height = "100%",
        ),
        justify="between",
    ratio = 16/9,
    )




@rx.page(route="/explore", title="Explore")
def explore() -> rx.Component:
    return \
    rx.aspect_ratio(
        rx.flex(

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            rx.text(
                "Here Is How You Can Help The Environment And Your Community",
                color=_BLUE,
                size="8",
                weight="bold",
            ),
            
            rx.box(),
            rx.box(),

            
            rx.grid(


                rx.popover.root(
                    rx.popover.trigger(
                        rx.button(

                            rx.text(
                                "Recycling Center",
                                #color=_BLUE,
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),


                            #background = "#00aa00",
                            border_radius="10px",
                            width="100%",
                            height="100%",
                        ),
                    ),
                    rx.popover.content(
                        rx.flex(
                            rx.text("Test"), #TODO put the content here
                            rx.popover.close(
                                rx.button(
                                    "Close",
                                    #background = _BLUE,
                                ),
                            ),
                            direction="column",
                            spacing="3",
                        ),
                    ),
                ),


                rx.popover.root(
                    rx.popover.trigger(
                        rx.button(

                            rx.text(
                                "Farmers Market",
                                #color=_BLUE,
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),


                            #background = "#00aa00",
                            border_radius="10px",
                            width="100%",
                            height="100%",
                        ),
                    ),
                    rx.popover.content(
                        rx.flex(
                            rx.text("Test"), #TODO put the content here
                            rx.popover.close(
                                rx.button(
                                    "Close",
                                    #background = _BLUE,
                                ),
                            ),
                            direction="column",
                            spacing="3",
                        ),
                    ),
                ),


                rx.popover.root(
                    rx.popover.trigger(
                        rx.button(

                            rx.text(
                                "Metro Station",
                                #color=_BLUE,
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),


                            #background = "#00aa00",
                            border_radius="10px",
                            width="100%",
                            height="100%",
                        ),
                    ),
                    rx.popover.content(
                        rx.flex(
                            rx.text("Test"), #TODO put the content here
                            rx.popover.close(
                                rx.button(
                                    "Close",
                                    #background = _BLUE,
                                ),
                            ),
                            direction="column",
                            spacing="3",
                        ),
                    ),
                ),

                rx.popover.root(
                    rx.popover.trigger(
                        rx.button(

                            rx.text(
                                "Explore the Park",
                                #color=_BLUE,
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),


                            #background = "#00aa00",
                            border_radius="10px",
                            width="100%",
                            height="100%",
                        ),
                    ),
                    rx.popover.content(
                        rx.flex(
                            rx.text("Test"), #TODO put the content here
                            rx.popover.close(
                                rx.button(
                                    "Close",
                                    #background = _BLUE,
                                ),
                            ),
                            direction="column",
                            spacing="3",
                        ),
                    ),
                ),








                # rx.flex(
                #     rx.box(),
                #     rx.text(
                #         "Recycling Center",
                #         color=_BLUE,
                #         size="8",
                #         weight="bold",
                #         align="center",
                #         width = "90%",
                #         height = "15%",
                #     ),
                #     rx.box(),
                #     # TODO put an image
                #     rx.box(),
                #     rx.popover.root(
                #         rx.popover.trigger(
                #             rx.button(
                #                 "Information",
                #                 background = _BLUE,
                #                 width = "90%",
                #                 height = "15%",
                #             ),
                #         ),
                #         rx.popover.content(
                #             rx.flex(
                #                 rx.text("Simple Example"), #TODO put the content here
                #                 rx.popover.close(
                #                     rx.button(
                #                         "Close",
                #                         background = _BLUE,
                #                     ),
                #                 ),
                #                 direction="column",
                #                 spacing="3",
                #             ),
                #         ),
                #     ),
                #     rx.box(),

                #     background="lime",
                #     align="center",
                #     width = "100%",
                #     height = "100%",
                #     border_radius = "10px",
                #     spacing = "2",
                #     direction="column"
                # ),






                # rx.card(
                #     background="lime",
                #     align="center",
                #     width = "100%",
                #     height = "100%",
                #     border_radius = "10px",
                #     on_click=State.printTestMsg
                # ),
                # rx.card(
                #     background="lime",
                #     align="center",
                #     width = "100%",
                #     height = "100%",
                #     border_radius = "10px",
                #     on_click=State.printTestMsg
                # ),
                # rx.card(
                #     background="lime",
                #     align="center",
                #     width = "100%",
                #     height = "100%",
                #     border_radius = "10px",
                #     on_click=State.printTestMsg
                # ),

                columns="2",
                spacing="8",
                width="75%",
                height = "65%",
                align = "center",
            ),

            
            #An Interactive Experience About How We Can Be More Environmentally Proactive In Our Communities.

            rx.box(),
            rx.box(),

            rx.button(
                "Back to Home",
                #color=_GREEN,
                #color_scheme="indigo",
                size="4",
                on_click=rx.redirect("/"),
            ),

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            spacing="3",
            direction="column",
            background=f"linear-gradient(45deg, #ffffff, {_GREEN})",
            #background=f"linear-gradient(45deg, {_GREEN}, #00ff33)",
            align="center",
            flex_wrap="wrap",
            width = "100%",
            height = "100%",
        ),
        justify = "between",
        ratio = 16/9,
    )



@rx.page(route="/credits", title="Credits")
def credits() -> rx.Component:
    return \
    rx.aspect_ratio(
        rx.flex(

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            rx.text(
                "A Project For LAHacks 2024",
                color=_BLUE,
                size="9",
                weight="bold",
            ),

            rx.text(
                "Done at the University of California, Los Angeles.",
                color=_BLUE,
                size="7",
                weight="medium",
            ),

            rx.text(
                "Los Angeles, California. 19 - 21 April 2024.",
                color=_BLUE,
                size="7",
                weight="medium",
            ),

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            rx.text(
                "Authors",
                color=_BLUE,
                size="7",
                weight="medium",
            ),

            rx.text(
                "Phillip Peterson (University of California, Irvine)",
                color=_BLUE,
                size="7",
                weight="bold",
            ),
            rx.text(
                "Nicholas Evangelos Georggin (University of California, Irvine)",
                color=_BLUE,
                size="7",
                weight="bold",
            ),

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            rx.text(
                "Resources and References TODO",
                color=_BLUE,
                size="7",
                weight="medium",
            ),

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),

            rx.button(
                "Back to Home",
                #color=_GREEN,
                #color_scheme="indigo",
                size="4",
                on_click=rx.redirect("/")
            ),

            rx.box(),
            rx.box(),
            rx.box(),
            rx.box(),
                
            
            

            spacing="2",
            direction="column",
            background=f"linear-gradient(45deg, #ffffff, {_GREEN})",
            #background=f"linear-gradient(45deg, {_GREEN}, #00ff33)",
            align="center",
            flex_wrap="wrap",
            width = "100%",
            height = "100%",
        ),
        justify="between",
    ratio = 16/9,
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
        accent_color="green",
    )
)
