import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os

st.title("6하원칙 기반 작문 생성기")

# API 키 입력
api_key = st.text_input("Google API Key를 입력하세요:", type="password")

if api_key:
    # API 키를 환경 변수로 설정
    os.environ["GOOGLE_API_KEY"] = api_key
    
    # 6하원칙 입력 필드
    who = st.text_input("누가:")
    when = st.text_input("언제:")
    where = st.text_input("어디서:")
    what = st.text_input("무엇을:")
    how = st.text_input("어떻게:")
    why = st.text_input("왜:")

    # 생성 버튼
    if st.button("작문 생성하기"):
        try:
            # API 설정에 환경 변수 사용
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            
            # 프롬프트 템플릿 설정
            template = """
            다음 6하원칙을 바탕으로 자연스러운 글을 작성해주세요:
            
            누가: {who}
            언제: {when}
            어디서: {where}
            무엇을: {what}
            어떻게: {how}
            왜: {why}
            
            위 정보를 바탕으로 자연스러운 한국어 문장으로 작성해주세요.
            """
            
            prompt = PromptTemplate(
                input_variables=["who", "when", "where", "what", "how", "why"],
                template=template
            )

            # LangChain과 Gemini 모델 설정에도 환경 변수 사용
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.0-pro",
                temperature=0.7,
                google_api_key=os.getenv("GOOGLE_API_KEY")
            )
            
            # 작문 생성
            result = llm.invoke(prompt.format(
                who=who,
                when=when,
                where=where,
                what=what,
                how=how,
                why=why
            ))

            # 결과 표시
            st.subheader("생성된 작문:")
            st.write(result.content)

        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
else:
    st.warning("API 키를 입력해주세요.")


