import reflex as rx
from .model import model

_types: list = ["recycling", "market", "metro", "park", "none"]

class SuggestionState(rx.State):
    selected: str = "metro"
    form_data: dict = ()

    def handle_submit(self, form_data: dict):
        self.form_data = form_data


    def generate_suggestions(self):
        match self.selected:
            case "recycling":
                response = model.generate_content(f'List the top three best recycling centers in {self.form_data["city"]} {self.form_data["state"]} along with where they are at. If the city does not exist just output N/A.')
                print(response.text)
                return None
            case "market":
                response = model.generate_content(f'List the top three best farmers markets in {self.form_data["city"]} {self.form_data["state"]} along with where they are at. If the city does not exist just output N/A.')
                print(response.text)
                return None
            case "metro":
                response = model.generate_content(f'List the top three best public transit options in {self.form_data["city"]} {self.form_data["state"]} along with where they are at. If the city does not exist just output N/A.')
                print(response.text)
                return None
            case "park":
                response = model.generate_content(f'List the top three best outdoor parks in {self.form_data["city"]} {self.form_data["state"]} along with where they are at. If the city does not exist just output N/A.')
                print(response.text)
                return None
            case _:
                print("N/A")
                return None
