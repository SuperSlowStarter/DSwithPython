import openai

# OpenAI API 키 설정
openai.api_key = '발급받은_API_키'

# 메시지 설정
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "안녕하세요, 오늘 날씨는 어떤가요?"}
]

# ChatGPT API 호출
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 사용할 모델 지정
    messages=messages,
    max_tokens=150,         # 생성할 응답의 최대 토큰 수
    temperature=0.7         # 응답의 창의성 조절 (0.0 ~ 2.0)
)

# 응답 출력
print(response['choices'][0]['message']['content'])
