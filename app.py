import streamlit as st

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

# 1. 動作モードの選択（ラジオボタン）
selected_item = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI値の計算"]
)

st.divider() # 区切り線を表示

# 2. 選択されたモードに応じて入力フォームを切り替える
if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
    text_count = len(input_message)
else:
    height = st.text_input(label="身長（cm）を入力してください。")
    weight = st.text_input(label="体重（kg）を入力してください。")

# 3. 実行ボタンが押された時の処理
if st.button("実行"):
    st.divider()
    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数: **{text_count}**")
        else:
            st.error("テキストを入力してください。")
    else:
        if height and weight:
            try:
                # BMI = 体重(kg) / 身長(m)^2
                bmi = round(float(weight) / ((float(height)/100) ** 2), 1)
                st.write(f"BMI値: **{bmi}**")
            except ValueError:
                st.error("身長と体重は数値で入力してください。")
        else:
            st.error("身長と体重をどちらも入力してください。")