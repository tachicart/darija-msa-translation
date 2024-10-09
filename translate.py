import openai

# Set your OpenAI API key, you should have already one
openai.api_key = 'your-api-key-here'

def translate_darija_to_msa(darija_text):
    response = openai.Completion.create(
        model="ft:gpt-4o-2024-08-06:personal:translate-darija-4o:AA0UYdZn",
        prompt=f"Translate the following Darija sentence into MSA: {darija_text}",
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    darija_sentence = input("Enter a Darija sentence: ")
    print("Translated MSA:", translate_darija_to_msa(darija_sentence))
