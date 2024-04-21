import reflex as rx
from .model import model

_types: list = ["recycling", "market", "metro", "park", "none"]

class SuggestionState(rx.State):
    selected: str = "none"
    response = ""
    form_data: dict = ()


    # Takes in the submission data and generates suggestions given the selected city and state.
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.generate_suggestions()


    # Generate the top three activities with Gemini given the city and state in the form data.
    def generate_suggestions(self):
        match self.selected:
            case "recycling":
                response = model.generate_content(f'List the top three best recycling centers in {self.form_data["city"]} {self.form_data["state"]} along with where they are at.')
                self.response = response.text
                return None
            case "market":
                response = model.generate_content(f'List the top three best farmers markets in {self.form_data["city"]} {self.form_data["state"]} along with where they are at.')
                self.response = response.text
                return None
            case "metro":
                response = model.generate_content(f'List the top three best public transit options in {self.form_data["city"]} {self.form_data["state"]} along with where they are at.')
                self.response = response.text
                return None
            case "park":
                response = model.generate_content(f'List the top three best outdoor parks in {self.form_data["city"]} {self.form_data["state"]} along with where they are at.')
                self.response = response.text
                return None
            case _:
                print("N/A")
                return None
