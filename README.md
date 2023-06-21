# korean Formal Converter Using Deep Learning
한국어에서 반말(informal)을 존댓말(formal)로 바꿔주는 변환기(converter) 입니다.
*존댓말 데이터셋에서는 "해요체"와 "합쇼체" 두 종류가 존재했습니다, 하지만 본 모델은 "해요체"로 통일하여 변환하는 모델입니다.

## 한국어 존댓말 변환기
- 이전에 존댓말과 반말을 구분하는 분류기(https://github.com/jongmin-oh/korean-formal-classifier)를 학습했습니다.
- 존댓말 변환기는 반말데이터를 변환하여 존댓말로 사용할 수 있습니다.
- 바로 사용하실 분들은 밑에 예제 코드 참고해서 모델('j5ng/') 다운받아 사용하실 수 있습니다.

## Base on PLM model(ET5)
 - ETRI(https://aiopen.etri.re.kr/et5Model)

## Base on Dataset
 - AI허브(https://www.aihub.or.kr/) : 한국어 어체 변환 코퍼스
    1. KETI 일상오피스 대화 1,254 문장
    2. 수동태깅 병렬데이터

 - 스마일게이트 말투 데이터 셋(korean SmileStyle Dataset)

### Preprocessing
 1. 반말/존댓말 데이터 분리("해요체"만 분리)
    - 스마일게이트(['formal','informal']) 칼럼만 사용
    - 수동태깅 병렬데이터에서 ".ban", ".yo" txt 파일만 사용
    - KETI 일상오피스 데이터에서("반말","해요체") 칼럼만 사용

 2. 데이터 셋 병합(3가지 데이터 셋 병합)
 3. 마침표(.)와 쉼표(,)제거 

### 최종 학습데이터 예시
|informal|formal|
|------|---|
|응 고마워|네 감사해요|
|나도 그 책 읽었어 굉장히 웃긴 책이였어|저도 그 책 읽었습니다 굉장히 웃긴 책이였어요|
|미세먼지가 많은 날이야|미세먼지가 많은 날이네요|
|괜찮겠어?|괜찮으실까요?|
|아니야 회의가 잠시 뒤에 있어 준비해줘|아니에요 회의가 잠시 뒤에 있어요 준비해주세요|

