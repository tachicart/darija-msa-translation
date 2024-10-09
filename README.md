# darija-msa-translation
# Darija to MSA Translation Using GPT-4o

This project provides a way to use the fine-tuned GPT-4o model (`ft:gpt-4o-2024-08-06:personal:translate-darija-4o:AA0UYdZn`) for translating Moroccan Darija into Modern Standard Arabic (MSA).

## How to Use

### Prerequisites
1. Python 3.7+
2. OpenAI Python package (`pip install openai`)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/darija-msa-translation.git
   cd darija-msa-translation
   ```

2. Install the dependencies:
   ```bash
   pip install openai
   ```

3. Use the model to translate:
   Create a Python script (`translate.py`) or use the one provided in this repository.

   ```python
   import openai

   # Set your OpenAI API key
   openai.api_key = 'your-api-key-here'

   # Translate a sentence from Darija to MSA
   response = openai.Completion.create(
       model="ft:gpt-4o-2024-08-06:personal:translate-darija-4o:AA0UYdZn",
       prompt="Translate the following Darija sentence into MSA: انا كانقرا باش نولي عالم.",
       max_tokens=100,
       temperature=0.7
   )

   print(response.choices[0].text.strip())
   ```

Replace `your-api-key-here` with your actual OpenAI API key.
## Authors
Ridouane Tachicart, Karim Bouzoubaa
## License
CC-BY
