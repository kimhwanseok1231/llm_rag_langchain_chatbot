# LLM Application 개발 (LangChain, RAG 활용)

프로젝트는 인프런 강의를 참고하여 LangChain, RAG(Retrieval-Augmented Generation), Upstage Embeddings를 활용한 LLM 기반 챗봇입니다.  
사용자의 질문을 받아 관련 문서를 검색하고, 문맥 기반 답변을 제공합니다.

## 🛠 주요 기능

- **질문 전처리 & 사전 참조**: 사용자 질문을 내부 사전에 맞게 변환  
- **문서 검색 기반 답변 생성**: Pinecone 벡터 DB와 UpstageEmbeddings 활용  
- **대화 기록 유지**: 채팅 세션별 문맥을 유지하며 답변 생성  
- **웹 UI 배포**: Streamlit Cloud 사용

## 서비스 배포 (Streamlit Cloud)

<img src="https://github.com/user-attachments/assets/ecc50250-3467-43f0-b7f8-2ac29f57ae81" 
     alt="서비스 화면" 
     width="600" 
     style="display: block; margin-left: 0;"/>
