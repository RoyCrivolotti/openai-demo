import openai

def summarise(api_key: str,
    max_tokens: float,
    prompt: str = "",
    engine: str = 'text-davinci-003'):

    openai.api_key = api_key

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=int(max_tokens),
        n=1,
        stop=None,
        temperature=0.3,
    )

    return response.choices[0].text
