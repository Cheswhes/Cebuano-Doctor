from ollama import chat

GEMMA_MODEL = "gemma4:e4b"       # change to match your pulled tag
MEDGEMMA_MODEL = "medgemma1.5"   # change to match your pulled tag


def strip_thinking(text):
    """Remove any leaked reasoning/thinking content from a model response.
    Gemma-family reasoning models sometimes separate 'thought' and final
    answer with special channel tokens like <unused94>/<unused95>.
    If a final-answer marker is present, keep only what comes after it."""
    if "<unused95>" in text:
        text = text.split("<unused95>")[-1]
    return text.strip()


def translate_cebuano_to_english(text):
    prompt = (
        "You are a translation engine, not a conversational assistant. "
        "The following text is written in Cebuano (Bisaya). "
        "Translate it into natural, fluent English. "
        "Preserve the original meaning exactly. "
        "Do not add any medical information, advice, or interpretation. "
        "Do not answer the question or respond to it in any way. "
        "Output ONLY the English translation, with no preamble, "
        "no quotation marks, and no explanation.\n\n"
        f"Cebuano text: {text}"
    )

    response = chat(
        model=GEMMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
        think=False,
    )

    return strip_thinking(response.message.content)


def get_medical_response(english_query):
    prompt = (
        "You are an educational health information assistant, not a licensed doctor. "
        "Answer the user's healthcare question below clearly and in plain language. "
        "Be medically accurate and avoid inventing facts you are not confident about — "
        "state uncertainty when it exists rather than guessing. "
        "Do not claim to diagnose the user personally; speak in terms of general "
        "possibilities and common causes instead. "
        "If the symptoms described could indicate something urgent, clearly say so "
        "and recommend seeking in-person medical care. "
        "Keep the answer concise — a few short paragraphs at most, not an exhaustive essay. "
        "Do not add unnecessary disclaimers beyond what is medically relevant.\n\n"
        f"User's question: {english_query}"
    )

    response = chat(
        model=MEDGEMMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
        think=False,
    )

    return strip_thinking(response.message.content)


def translate_english_to_cebuano(text):
    prompt = (
        "You are a translation engine, not a conversational assistant. "
        "The following text is written in English. "
        "Translate it into natural, fluent Cebuano (Bisaya). "
        "Preserve the meaning exactly, especially any medical warnings "
        "or advice about seeking medical attention — do not soften, "
        "shorten, or omit them. "
        "Do not add any new medical advice that was not in the original text. "
        "Do not summarize; translate the full text. "
        "If the original text uses bullet points or formatting, keep the "
        "same structure in the translation. "
        "Output ONLY the Cebuano translation, with no preamble, "
        "no quotation marks, and no explanation.\n\n"
        f"English text: {text}"
    )

    response = chat(
        model=GEMMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
        think=False,
    )

    return strip_thinking(response.message.content)


def cebuano_doctor(user_query):
    english_query = translate_cebuano_to_english(user_query)
    medical_response = get_medical_response(english_query)
    cebuano_response = translate_english_to_cebuano(medical_response)
    return cebuano_response


def run_chat():
    print("=" * 33)
    print("THE CEBUANO DOCTOR")
    print("=" * 33)
    print()
    print("IMPORTANT: This chatbot provides general health information only.")
    print("It is not a replacement for a licensed medical professional.")
    print("For emergencies, seek immediate medical attention.")
    print()
    print("Type your healthcare question in Cebuano.")
    print("Type 'exit' to quit.")
    print()

    try:
        while True:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("Doctor: Salamat! Pag-atiman kanunay sa imong kaugalingon.")
                break

            if not user_input:
                print("Doctor: (Palihug pagsulat og pangutana.)")
                continue

            print("Doctor: (naghunahuna...)")
            response = cebuano_doctor(user_input)
            print()
            print("Doctor:", response)
            print()

    except KeyboardInterrupt:
        print()
        print("Doctor: Salamat! Pag-atiman kanunay sa imong kaugalingon.")


if __name__ == "__main__":
    run_chat()
