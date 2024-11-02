import PIL.Image
import google.generativeai as genai


genai.configure(api_key="AIzaSyDMywIL8s5o_OpHfUD4wbL6cwndpD4azsY")
model = genai.GenerativeModel("gemini-1.5-flash")
player = PIL.Image.open("img/Faker.jpg")
response = model.generate_content(["Tell me about this player", player])
print(response.text)