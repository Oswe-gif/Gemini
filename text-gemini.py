import google.generativeai as genai


genai.configure(api_key="AIzaSyDMywIL8s5o_OpHfUD4wbL6cwndpD4azsY")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a lol player")
print(response.text)