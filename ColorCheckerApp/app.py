import streamlit as st

# Kontrast oranı hesaplama fonksiyonu
def calculate_contrast_ratio(hex1, hex2):
    """İki renk arasındaki kontrast oranını hesaplar."""
    def luminance(hex_code):
        hex_code = hex_code.lstrip('#')
        rgb = [int(hex_code[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
        rgb = [(v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4) for v in rgb]
        return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
    
    lum1 = luminance(hex1)
    lum2 = luminance(hex2)
    contrast = (lum1 + 0.05) / (lum2 + 0.05) if lum1 > lum2 else (lum2 + 0.05) / (lum1 + 0.05)
    return round(contrast, 2)

def generate_color_combinations(colors, text, font_family, font_size, font_style):
    """Renk kombinasyonları oluşturma fonksiyonu."""
    combinations = []
    for bg_color in colors:
        for text_color in colors:
            if bg_color != text_color:  # Arka plan ve yazı rengi aynı olmasın
                contrast_ratio = calculate_contrast_ratio(bg_color, text_color)
                combinations.append((bg_color, text_color, text, font_family, font_size, font_style, contrast_ratio))
    return combinations

def display_color_combinations(combinations):
    """Her bir kombinasyonu gösteren fonksiyon."""
    for bg_color, text_color, text, font_family, font_size, font_style, contrast_ratio in combinations:
        st.markdown(
            f"<div style='background-color:{bg_color}; padding: 10px; margin-bottom: 10px;'>"
            f"<p style='color:{text_color}; font-family:{font_family}; font-size:{font_size}px; {font_style}'>{text}</p>"
            f"<p style='color:{text_color};'>Background: {bg_color} - Text: {text_color} - Contrast Ratio: {contrast_ratio}</p>"
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

    # Yazı fontu ve boyut seçimi
    font_family = st.selectbox("Yazı Fontu Seçin", ["Arial", "Helvetica", "Times New Roman", "Courier New", "Verdana"])
    font_size = st.selectbox("Yazı Boyutu Seçin", [12, 14, 16, 18, 20, 24, 28, 32])
    font_weight = st.checkbox("Kalın", False)
    font_italic = st.checkbox("İtalik", False)
    font_underline = st.checkbox("Altı Çizili", False)

    # Yazı stilini belirleme
    font_style = "font-weight:bold;" if font_weight else ""
    font_style += "font-style:italic;" if font_italic else ""
    font_style += "text-decoration:underline;" if font_underline else ""

    # Renk sayısı belirleme
    color_count = st.number_input("Kaç tane renk girmek istiyorsunuz?", min_value=1, max_value=10, value=3)

    # Renk giriş alanları ve renk göstergesi
    colors = []
    for i in range(int(color_count)):
        col1, col2, col3 = st.columns([4, 1, 1])  # Sütunları oluştur ve genişliklerini ayarla
        with col1:
            color = st.text_input(f"{i+1}. Renk (Hex Kod)", value="#000000", key=f"color_input_{i}")
        with col2:
            if color.startswith("#") and len(color) == 7:
                st.markdown(
                    f"<div style='background-color:{color}; width: 30px; height: 30px; border: 1px solid #ddd; display: inline-block;'></div>",
                    unsafe_allow_html=True
                )
                colors.append(color)
        with col3:
            if st.button("🗑️", key=f"delete_button_{i}"):  # Çöp kutusu ikonu ile silme butonu
                st.experimental_rerun()  # Sayfayı yeniden yükleyerek rengi sil

    # Renkleri deneme
    if st.button("Renkleri Dene"):
        if len(colors) < 2:
            st.error("En az iki farklı renk giriniz!")
        else:
            combinations = generate_color_combinations(colors, user_text, font_family, font_size, font_style)
            display_color_combinations(combinations)

# CSS kullanarak stil ayarlamaları yapıyoruz
st.markdown(
    """
    <style>
    .stTextInput > div {
        display: flex;
        align-items: center;
    }
    .stTextInput div label {
        display: inline-block;
        width: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()

