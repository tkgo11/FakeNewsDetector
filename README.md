# FakeNewsDetector
FakeNewsDetector는 웹에서 사실 확인 데이터를 수집하고 분류하는 프로젝트입니다. 이 프로젝트는 Selenium을 사용하여 특정 웹사이트에서 데이터를 크롤링하고, 크롤링한 데이터를 다양한 카테고리로 분류하여 텍스트 파일로 저장합니다.
## 기능
    웹 페이지에서 사실 확인 카드 정보를 수집
    카드의 제목과 레이블을 추출하여 카테고리별로 분류
    각 카테고리별로 텍스트 파일에 저장
## 사용 방법
```
git clone https://github.com/tkgo11/FakeNewsDetector
cd FakeNewsDetector
python -m pip install -r requirements.txt
python main.py
python model.py
```
## 참고한 코드
    [grab-selector](https://github.com/adam-kov/grab-selector)