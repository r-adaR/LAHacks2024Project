import google.generativeai as genai
from model import model

city = input("Please input a city near you: ")

response = model.generate_content(f'List the top three best public transit options in {city} along with where they are at. If the city does not exist just output N/A.')

print(response.text)
