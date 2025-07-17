import google.generativeai as genai

# 🔑 Set your Gemini API key
genai.configure(api_key="AIzaSyDu_AeXrB8O83J1Vq2p3xNrqAZ5wqtoqaw")

def get_gemini_response(prompt, character="jedi knight"):
    # Customize prompt based on character
    system_prompt = f"Reply like {character} from Star Wars. Use their speech style and tone."

    model = genai.GenerativeModel('gemini-2.0-flash')

    response = model.generate_content(
        [system_prompt, prompt],
        generation_config={"temperature": 0.7}
    )

    return response.text.strip()
