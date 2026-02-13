import streamlit as st
import asyncio
from googletrans import Translator, LANGUAGES

translator = Translator()

def get_lang_key(language_name):
    for key, value in LANGUAGES.items():
        if value == language_name:
            return key
    return None

async def translate_text(text, dest):
    result = await translator.translate(text, dest=dest)
    return result

st.set_page_config(page_title="Language Translator", page_icon="🌐")

st.title("🌍 AI Language Translator")
st.write("Translate text between multiple languages with auto language detection.")

col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("✍️ Enter Text", height=150)

with col2:
    target_language = st.selectbox(
        "🌐 Select Target Language",
        sorted(LANGUAGES.values())
    )

col_translate, col_clear = st.columns(2)

with col_translate:
    translate_btn = st.button("🔄 Translate")

with col_clear:
    clear_btn = st.button("🧹 Clear")

if translate_btn:
    if input_text.strip() == "":
        st.warning("⚠️ Please enter text to translate")
    else:
        try:
            lang_key = get_lang_key(target_language)
            result = asyncio.run(translate_text(input_text, lang_key))

            detected_lang = LANGUAGES.get(result.src, "Unknown")

            st.success("✅ Translation Successful")
            st.markdown(f"**Detected Language:** `{detected_lang}`")
            st.text_area(
                "📘 Translated Text",
                result.text,
                height=150
            )

        except Exception as e:
            st.error("❌ Translation failed. Please try again later.")
            st.exception(e)

if clear_btn:
    st.rerun()

##language Translator