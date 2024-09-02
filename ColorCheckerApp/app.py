import streamlit as st

def generate_color_combinations(colors, text):
    """Renk kombinasyonları oluşturma fonksiyonu."""
    combinations = []
    for bg_color in colors:
        for text_color in colors:
            if bg_color != text_color:  # Arka plan ve yazı rengi aynı olmasın
                combinations.append((bg_color, text_color, text))
    return combinations

def display_color_combinations(combinations):
    """Her bir kombinasyonu gösteren fonksiyon."""
    for bg_color, text_color, text in combinations:
        st.markdown(
            f"<div style='background-color:{bg_color}; padding: 10px; margin-bottom: 10px;'>"
            f"<p style='color:{text_color};'>{text}</p>"
            f"<p style='color:{text_color};'>Background: {bg_color} - Text: {text_color}</p>"
            "</div>",
            unsafe_allow_html=True
        )

def main():
    st.title("Color Checker Uygulaması")

    # Kullanıcıdan görmek istediği yazıyı alma
    default_text = "Örnek Yazı"
    user_text = st.text_input("Görmek istediğiniz yazıyı girin (Boş bırakırsanız varsayılan yazı kullanılacak):", default_text)
    if not user_text:
        user_text = default_text

    # Renk sayısı belirleme
    color_count = st.number_input("Kaç tane renk girmek istiyorsunuz?", min_value=1, max_value=10, value=3)

    # Renk giriş alanları
    colors = []
    for i in range(int(color_count)):
        color = st.text_input(f"{i+1}. Renk (Hex Kod)", value="#000000")
        if color.startswith("#") and len(color) == 7:
            colors.append(color)
            # Renk göstergesi
            st.markdown(
                f"<div style='background-color:{color}; width: 50px; height: 50px;'></div>",
                unsafe_allow_html=True
            )
        else:
            st.warning("Geçerli bir Hex kodu giriniz. Örnek: #FFFFFF")

    # Renkleri deneme
    if st.button("Renkleri Dene"):
        if len(colors) < 2:
            st.error("En az iki farklı renk giriniz!")
        else:
            combinations = generate_color_combinations(colors, user_text)
            display_color_combinations(combinations)

if __name__ == "__main__":
    main()
