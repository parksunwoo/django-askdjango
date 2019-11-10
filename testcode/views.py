from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import quote

# Create your views here.
# Excel 파일 다운로드 응답
def response_excel(request):
    filepath = '/other/path/excel.xls'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f,content_type='application/vnd.ms-excel')

        encoded_filenmae = quote(filename)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filenmae)

    return response


import pandas as pd
from io import StringIO
from django.http import HttpResponse

# Pandas를 통한 CSV 응답 생성
def response_csv(request):
    df = pd.DataFrame([
        [100, 110, 120],
        [200, 210, 220],
        [300, 310, 320],
    ])

    io = StringIO()
    df.to_csv(io)
    io.seek(0) # 끝에 있는 file cursor를 처음으로 이동

    response = HttpResponse(io, content_type='text/csv')
    response['Content-Disposition'] = "attachment; filenmae*=utf-8''{}".format(encoded_filename)
    return response

from io import BytesIO

# Pandas를 통한 엑셀 응답 생성
def response_excel(request):
    df = pd.DataFrame([
        [100, 110, 120],
        [200, 210, 220],
    ])

    io = BytesIO
    df.to_excel(io)
    io.seek(0)

    encoded_filename = quote('pandas.xlsx')
    response = HttpResponse(io, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename*=utf-8''{}'.format(encoded_filename)
    return response

from PIL import Image, ImageDraw, ImageFont
# Pillow를 통한 이미지 응답 생성 - 기본

ttf_path = 'Library/Fonts/AppleGothic.ttf'
image_url = 'http://www.flowermeaning.com/flow-pics/Calla-Lily-Meaning.jpg'

res = requests.get(image_url) # 서버로 HTTP GET 요청하여, 응답획득
io = BytesIO(res.content) # 응답의 Raw Body 메모리 파일 객체 BytesIO 인스턴스 생성
io.seek(0) # 파일의 처음으로 커서를 이동

canvas = Image.open(io).convert('RGBA') # 이미지 파일을 열고, RGBA 모드로 변환
font = ImageFont.truetype(ttf_path, 40) # 지정경로의 TrueType 폰트, 폰트크기40
draw = ImageDraw.Draw(canvas) # canvas에 대한 ImageDraw 객체 획득

text = 'Ask Company'
left, top = 10, 10
margin = 10
width, height = font.getsize(text)
right = left + width + margin
bottom = top + height + margin

draw.rectangle( (left, top, right, bottom), (255, 255, 224))
draw.text((15, 15), text, font=font, fill=(20,20,20))

draw.show()


# Pillow를 통한 이미지 응답 생성 - view
def response_pillow_image(request):
    ttf_path = 'Library/Fonts/AppleGothic.ttf'
    image_url = 'http://www.flowermeaning.com/flow-pics/Calla-Lily-Meaning.jpg'

    res = requests.get(image_url)  # 서버로 HTTP GET 요청하여, 응답획득
    io = BytesIO(res.content)  # 응답의 Raw Body 메모리 파일 객체 BytesIO 인스턴스 생성
    io.seek(0)  # 파일의 처음으로 커서를 이동

    canvas = Image.open(io).convert('RGBA')  # 이미지 파일을 열고, RGBA 모드로 변환
    font = ImageFont.truetype(ttf_path, 40)  # 지정경로의 TrueType 폰트, 폰트크기40
    draw = ImageDraw.Draw(canvas)  # canvas에 대한 ImageDraw 객체 획득

    text = 'Ask Company'
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin

    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15, 15), text, font=font, fill=(20, 20, 20))

    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG') # HttpResponse 의 file-Like 특성 활용
    return response





































