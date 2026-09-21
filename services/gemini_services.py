from google import genai


def analyze_shape(api_key, image, prompt):
    client = genai.Client(api_key=api_key)

    try:
        return client.models.generate_content(
            model="gemini-3.6-flash",
            contents=[prompt, image]
        )

    except Exception as e:
        error_message = str(e)

    if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
        raise Exception(
            "⚠️ O limite de requisições da API do Gemini foi atingido. "
            "Aguarde alguns instantes e tente novamente."
        )

    if "503" in error_message or "UNAVAILABLE" in error_message:
        raise Exception(
            "⚠️ Os servidores do Gemini estão indisponíveis ou "
            "sobrecarregados no momento. Tente novamente em alguns instantes."
        )

    raise Exception(
        f"Erro ao chamar a API do Gemini: {error_message}"
    )