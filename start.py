import streamlit as st

st.title("사칙연산 계산기")

a = st.number_input("첫번째 숫자를 입력하세요:", value=0.0, step=0.1)
b = st.number_input("두번째 숫자를 입력하세요:", value=0.0, step=0.1)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("더하기"):
        result = a + b
        # 0이 아닌 첫 번째 숫자까지만 표시
        if result == int(result):
            st.success(f"두 수의 합은 {int(result)}입니다.")
        else:
            st.success(f"두 수의 합은 {result:g}입니다.")

with col2:        
    if st.button("빼기"):
        result = a - b
        if result == int(result):
            st.success(f"두 수의 차는 {int(result)}입니다.")
        else:
            st.success(f"두 수의 차는 {result:g}입니다.")
        
with col3:
    if st.button("곱하기"):
        result = a * b
        if result == int(result):
            st.success(f"두 수의 곱은 {int(result)}입니다.")
        else:
            st.success(f"두 수의 곱은 {result:g}입니다.")
        
with col4:
    if st.button("나누기"):
        if b != 0:
            result = a / b
            if result == int(result):
                st.success(f"두 수를 나눈 값은 {int(result)}입니다.")
            else:
                st.success(f"두 수를 나눈 값은 {result:g}입니다.")
        else:
            st.error("0으로 나눌 수 없습니다.")
