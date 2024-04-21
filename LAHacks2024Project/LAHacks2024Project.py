from rxconfig import config
from .api.suggestions import SuggestionState
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

#foreach for every dialog box

class State(rx.State):
    """The app state."""

    city:str = 'Los Angeles'
    state:str = 'CA'
    form_data: dict = {'city': city, 'state': state}
    

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.city = form_data['city']
        self.state = form_data['state']
        print(self.form_data)
        print(self.city)
        print(self.state)



_GREEN = "#86FF9D"
_BLUE = "#3a53aa"
_ACTIVITIES = []
_ACTIVITY_TYPES = []
_ACTIVITY_DESCRIPTIONS = []

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
                size="4",
                on_click=rx.redirect("/explore/"),
            ),

            rx.box(),
            rx.box(),

            rx.button(
                "Credits",
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

                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(

                            rx.text(
                                "Recycling Center",
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),


                            border_radius="10px",
                            width="100%",
                            height="100%",
                            #on_click=SuggestionState.set_selected("recycling")
                        ),
                    ),
                    rx.dialog.content(

                        rx.dialog.title("Recycling Center"),
                        
                        rx.flex(

                            rx.form(
                                rx.hstack(
                                rx.input(
                                default_value=State.city,
                                placeholder="City Name",
                                name = "city",
                                ),

                                rx.select.root(
                                    rx.select.trigger(),
                                    rx.select.content(
                                        rx.select.item("AL", value="AL"),
                                        rx.select.item("AK", value="AK"),
                                        rx.select.item("AZ", value="AZ"),
                                        rx.select.item("AR", value="AR"),
                                        rx.select.item("CA", value="CA"),
                                        rx.select.item("CO", value="CO"),
                                        rx.select.item("CT", value="CT"),
                                        rx.select.item("DE", value="DE"),
                                        rx.select.item("DC", value="DC"),
                                        rx.select.item("FL", value="FL"),
                                        rx.select.item("GA", value="GA"),
                                        rx.select.item("HI", value="HI"),
                                        rx.select.item("ID", value="ID"),
                                        rx.select.item("IL", value="IL"),
                                        rx.select.item("IN", value="IN"),
                                        rx.select.item("IA", value="IA"),
                                        rx.select.item("KS", value="KS"),
                                        rx.select.item("KY", value="KY"),
                                        rx.select.item("LA", value="LA"),
                                        rx.select.item("ME", value="ME"),
                                        rx.select.item("MD", value="MD"),
                                        rx.select.item("MA", value="MA"),
                                        rx.select.item("MI", value="MI"),
                                        rx.select.item("MN", value="MN"),
                                        rx.select.item("MS", value="MS"),
                                        rx.select.item("MO", value="MO"),
                                        rx.select.item("MT", value="MT"),
                                        rx.select.item("NE", value="NE"),
                                        rx.select.item("NV", value="NV"),
                                        rx.select.item("NH", value="NH"),
                                        rx.select.item("NJ", value="NJ"),
                                        rx.select.item("NM", value="NM"),
                                        rx.select.item("NY", value="NY"),
                                        rx.select.item("NC", value="NC"),
                                        rx.select.item("ND", value="ND"),
                                        rx.select.item("OH", value="OH"),
                                        rx.select.item("OK", value="OK"),
                                        rx.select.item("OR", value="OR"),
                                        rx.select.item("PA", value="PA"),
                                        rx.select.item("RI", value="RI"),
                                        rx.select.item("SC", value="SC"),
                                        rx.select.item("SD", value="SD"),
                                        rx.select.item("TN", value="TN"),
                                        rx.select.item("TX", value="TX"),
                                        rx.select.item("UT", value="UT"),
                                        rx.select.item("VT", value="VT"),
                                        rx.select.item("VA", value="VA"),
                                        rx.select.item("WA", value="WA"),
                                        rx.select.item("WV", value="WV"),
                                        rx.select.item("WI", value="WI"),
                                        rx.select.item("WY", value="WY"),
                                    ),
                                    name="state",
                                    default_value=State.state,
                                ),
                                
                                rx.button("Submit", type="submit"),
                                ),
                                spacing="2",
                                direction="column",
                                margin_bottom = "10px",
                                on_submit=SuggestionState.handle_submit,
                                reset_on_submit=False,
                            ),
                        ),
                        


                        rx.dialog.description(
                            f"Please Enter Your City and State to Learn More",margin_bottom = "10px",
                        ),
                        rx.dialog.close(
                            rx.button("Close", size="3"),
                        ),

                        direction="column",
                        align="center",
                        spacing="3",
                        border_radius="10px",
                    ),
                ),

                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(

                            rx.text(
                                "Farmers Market",
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),

                            border_radius="10px",
                            width="100%",
                            height="100%",
                            on_click=SuggestionState.set_selected("market")
                        ),
                    ),
                    rx.dialog.content(

                        rx.dialog.title("Farmers Market"),
                        
                        rx.flex(

                            rx.form(
                                rx.hstack(
                                rx.input(
                                default_value=State.city,
                                placeholder="City Name",
                                name = "city",
                                ),

                                rx.select.root(
                                    rx.select.trigger(),
                                    rx.select.content(
                                        rx.select.item("AL", value="AL"),
                                        rx.select.item("AK", value="AK"),
                                        rx.select.item("AZ", value="AZ"),
                                        rx.select.item("AR", value="AR"),
                                        rx.select.item("CA", value="CA"),
                                        rx.select.item("CO", value="CO"),
                                        rx.select.item("CT", value="CT"),
                                        rx.select.item("DE", value="DE"),
                                        rx.select.item("DC", value="DC"),
                                        rx.select.item("FL", value="FL"),
                                        rx.select.item("GA", value="GA"),
                                        rx.select.item("HI", value="HI"),
                                        rx.select.item("ID", value="ID"),
                                        rx.select.item("IL", value="IL"),
                                        rx.select.item("IN", value="IN"),
                                        rx.select.item("IA", value="IA"),
                                        rx.select.item("KS", value="KS"),
                                        rx.select.item("KY", value="KY"),
                                        rx.select.item("LA", value="LA"),
                                        rx.select.item("ME", value="ME"),
                                        rx.select.item("MD", value="MD"),
                                        rx.select.item("MA", value="MA"),
                                        rx.select.item("MI", value="MI"),
                                        rx.select.item("MN", value="MN"),
                                        rx.select.item("MS", value="MS"),
                                        rx.select.item("MO", value="MO"),
                                        rx.select.item("MT", value="MT"),
                                        rx.select.item("NE", value="NE"),
                                        rx.select.item("NV", value="NV"),
                                        rx.select.item("NH", value="NH"),
                                        rx.select.item("NJ", value="NJ"),
                                        rx.select.item("NM", value="NM"),
                                        rx.select.item("NY", value="NY"),
                                        rx.select.item("NC", value="NC"),
                                        rx.select.item("ND", value="ND"),
                                        rx.select.item("OH", value="OH"),
                                        rx.select.item("OK", value="OK"),
                                        rx.select.item("OR", value="OR"),
                                        rx.select.item("PA", value="PA"),
                                        rx.select.item("RI", value="RI"),
                                        rx.select.item("SC", value="SC"),
                                        rx.select.item("SD", value="SD"),
                                        rx.select.item("TN", value="TN"),
                                        rx.select.item("TX", value="TX"),
                                        rx.select.item("UT", value="UT"),
                                        rx.select.item("VT", value="VT"),
                                        rx.select.item("VA", value="VA"),
                                        rx.select.item("WA", value="WA"),
                                        rx.select.item("WV", value="WV"),
                                        rx.select.item("WI", value="WI"),
                                        rx.select.item("WY", value="WY"),
                                    ),
                                    name="state",
                                    default_value=State.state,
                                ),
                                
                                rx.button("Submit", type="submit"),
                                ),
                                spacing="2",
                                direction="column",
                                margin_bottom = "10px",
                                on_submit=State.handle_submit,
                                reset_on_submit=False,
                            ),
                        ),
                        


                        rx.dialog.description(
                            f"Please Enter Your City and State to Learn More",margin_bottom = "10px",
                        ),
                        rx.dialog.close(
                            rx.button("Close", size="3"),
                        ),

                        direction="column",
                        align="center",
                        spacing="3",
                        border_radius="10px",
                    ),
                ),

                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(

                            rx.text(
                                "Metro Station",
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),
                            border_radius="10px",
                            width="100%",
                            height="100%",
                            on_click=SuggestionState.set_selected("metro"),
                        ),
                    ),
                    rx.dialog.content(

                        rx.dialog.title("Metro Station"),
                        
                        rx.flex(

                            rx.form(
                                rx.hstack(
                                rx.input(
                                default_value=State.city,
                                placeholder="City Name",
                                name = "city",
                                ),

                                rx.select.root(
                                    rx.select.trigger(),
                                    rx.select.content(
                                        rx.select.item("AL", value="AL"),
                                        rx.select.item("AK", value="AK"),
                                        rx.select.item("AZ", value="AZ"),
                                        rx.select.item("AR", value="AR"),
                                        rx.select.item("CA", value="CA"),
                                        rx.select.item("CO", value="CO"),
                                        rx.select.item("CT", value="CT"),
                                        rx.select.item("DE", value="DE"),
                                        rx.select.item("DC", value="DC"),
                                        rx.select.item("FL", value="FL"),
                                        rx.select.item("GA", value="GA"),
                                        rx.select.item("HI", value="HI"),
                                        rx.select.item("ID", value="ID"),
                                        rx.select.item("IL", value="IL"),
                                        rx.select.item("IN", value="IN"),
                                        rx.select.item("IA", value="IA"),
                                        rx.select.item("KS", value="KS"),
                                        rx.select.item("KY", value="KY"),
                                        rx.select.item("LA", value="LA"),
                                        rx.select.item("ME", value="ME"),
                                        rx.select.item("MD", value="MD"),
                                        rx.select.item("MA", value="MA"),
                                        rx.select.item("MI", value="MI"),
                                        rx.select.item("MN", value="MN"),
                                        rx.select.item("MS", value="MS"),
                                        rx.select.item("MO", value="MO"),
                                        rx.select.item("MT", value="MT"),
                                        rx.select.item("NE", value="NE"),
                                        rx.select.item("NV", value="NV"),
                                        rx.select.item("NH", value="NH"),
                                        rx.select.item("NJ", value="NJ"),
                                        rx.select.item("NM", value="NM"),
                                        rx.select.item("NY", value="NY"),
                                        rx.select.item("NC", value="NC"),
                                        rx.select.item("ND", value="ND"),
                                        rx.select.item("OH", value="OH"),
                                        rx.select.item("OK", value="OK"),
                                        rx.select.item("OR", value="OR"),
                                        rx.select.item("PA", value="PA"),
                                        rx.select.item("RI", value="RI"),
                                        rx.select.item("SC", value="SC"),
                                        rx.select.item("SD", value="SD"),
                                        rx.select.item("TN", value="TN"),
                                        rx.select.item("TX", value="TX"),
                                        rx.select.item("UT", value="UT"),
                                        rx.select.item("VT", value="VT"),
                                        rx.select.item("VA", value="VA"),
                                        rx.select.item("WA", value="WA"),
                                        rx.select.item("WV", value="WV"),
                                        rx.select.item("WI", value="WI"),
                                        rx.select.item("WY", value="WY"),
                                    ),
                                    name="state",
                                    default_value=State.state,
                                ),
                                
                                rx.button("Submit", type="submit"),
                                ),
                                spacing="2",
                                direction="column",
                                margin_bottom = "10px",
                                on_submit=State.handle_submit,
                                reset_on_submit=False,
                            ),
                        ),
                        


                        rx.dialog.description(
                            f"Please Enter Your City and State to Learn More",margin_bottom = "10px",
                        ),
                        rx.dialog.close(
                            rx.button("Close", size="3"),
                        ),

                        direction="column",
                        align="center",
                        spacing="3",
                        border_radius="10px",
                    ),
                ),

                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(

                            rx.text(
                                "Explore the Park",
                                size="8",
                                weight="bold",
                                align="center",
                                width = "90%",
                                height = "15%",
                            ),


                            border_radius="10px",
                            width="100%",
                            height="100%",
                            on_click=SuggestionState.set_selected("park")
                        ),
                    ),
                    rx.dialog.content(

                        rx.dialog.title("Explore the Park"),
                        
                        rx.flex(

                            rx.form(
                                rx.hstack(
                                rx.input(
                                default_value=State.city,
                                placeholder="City Name",
                                name = "city",
                                ),

                                rx.select.root(
                                    rx.select.trigger(),
                                    rx.select.content(
                                        rx.select.item("AL", value="AL"),
                                        rx.select.item("AK", value="AK"),
                                        rx.select.item("AZ", value="AZ"),
                                        rx.select.item("AR", value="AR"),
                                        rx.select.item("CA", value="CA"),
                                        rx.select.item("CO", value="CO"),
                                        rx.select.item("CT", value="CT"),
                                        rx.select.item("DE", value="DE"),
                                        rx.select.item("DC", value="DC"),
                                        rx.select.item("FL", value="FL"),
                                        rx.select.item("GA", value="GA"),
                                        rx.select.item("HI", value="HI"),
                                        rx.select.item("ID", value="ID"),
                                        rx.select.item("IL", value="IL"),
                                        rx.select.item("IN", value="IN"),
                                        rx.select.item("IA", value="IA"),
                                        rx.select.item("KS", value="KS"),
                                        rx.select.item("KY", value="KY"),
                                        rx.select.item("LA", value="LA"),
                                        rx.select.item("ME", value="ME"),
                                        rx.select.item("MD", value="MD"),
                                        rx.select.item("MA", value="MA"),
                                        rx.select.item("MI", value="MI"),
                                        rx.select.item("MN", value="MN"),
                                        rx.select.item("MS", value="MS"),
                                        rx.select.item("MO", value="MO"),
                                        rx.select.item("MT", value="MT"),
                                        rx.select.item("NE", value="NE"),
                                        rx.select.item("NV", value="NV"),
                                        rx.select.item("NH", value="NH"),
                                        rx.select.item("NJ", value="NJ"),
                                        rx.select.item("NM", value="NM"),
                                        rx.select.item("NY", value="NY"),
                                        rx.select.item("NC", value="NC"),
                                        rx.select.item("ND", value="ND"),
                                        rx.select.item("OH", value="OH"),
                                        rx.select.item("OK", value="OK"),
                                        rx.select.item("OR", value="OR"),
                                        rx.select.item("PA", value="PA"),
                                        rx.select.item("RI", value="RI"),
                                        rx.select.item("SC", value="SC"),
                                        rx.select.item("SD", value="SD"),
                                        rx.select.item("TN", value="TN"),
                                        rx.select.item("TX", value="TX"),
                                        rx.select.item("UT", value="UT"),
                                        rx.select.item("VT", value="VT"),
                                        rx.select.item("VA", value="VA"),
                                        rx.select.item("WA", value="WA"),
                                        rx.select.item("WV", value="WV"),
                                        rx.select.item("WI", value="WI"),
                                        rx.select.item("WY", value="WY"),
                                    ),
                                    name="state",
                                    default_value=State.state,
                                ),
                                
                                rx.button("Submit", type="submit"),
                                ),
                                spacing="2",
                                direction="column",
                                margin_bottom = "10px",
                                on_submit=State.handle_submit,
                                reset_on_submit=False,
                            ),
                        ),
                        


                        rx.dialog.description(
                            f"Please Enter Your City and State to Learn More",margin_bottom = "10px",
                        ),
                        rx.dialog.close(
                            rx.button("Close", size="3"),
                        ),

                        direction="column",
                        align="center",
                        spacing="3",
                        border_radius="10px",
                    ),
                ),

                columns="2",
                spacing="8",
                width="75%",
                height = "60%",
                align = "center",
            ),

            
            #An Interactive Experience About How We Can Be More Environmentally Proactive In Our Communities.

            rx.box(),
            rx.box(),

            rx.button(
                "Back to Home",
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
        accent_color="green",
    )
)

