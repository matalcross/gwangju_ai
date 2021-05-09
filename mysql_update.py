import pymysql

while True:
    c_show_id = input("수정할 키값을 입력하세요 : ")

    if c_show_id == '':
        print("키값이 입력되지 않았습니다. 다시 입력하세요.")
        continue
    else:
        break

# netflix_list 테이블에서 정보가 수정할 값이 존재하는지 확인한다.
conn = pymysql.connect(host='localhost', user='netflix', password='netflix1234',
        db='netflixdb', charset='utf8')
curs = conn.cursor()

sql = "select count(*) from netflix_list where show_id = (%s)"
curs.execute(sql, (c_show_id))
result = curs.fetchall()

cnt = int(result[0][0])

if cnt != 1:
    print(f"[키값:{c_show_id}]수정할 레코드가 존재하지 않습니다.")
    exit()

# 데이터를 수정한다.
# 입력확인
i_type = input("작품형태:")
i_title = input("작품이름:")
i_director = input("디렉터:")
i_cast = input("배우:")
i_country = input("제작국가:")
i_release_year = input("제작년도:")
i_duration = input("상영시간:")
i_description = input("작품설명:")

# 문자열 숫자로 변환
i_release_year = int(i_release_year)

# 입력값 출력
print("\n\n\n")
print(f"[{c_show_id} 수정내용확인]")
print("---------------------------------------------")
print("작품코드:", c_show_id)
print("작품형태:", i_type)
print("작품이름:", i_title)
print("디렉터:", i_director)
print("배우:", i_cast)
print("제작국가:", i_country)
print("제작년도:", i_release_year)
print("상영시간:", i_duration)
print("작품설명:", i_description)
print("---------------------------------------------")

choice_yn = input("입력하신 내용을 수정시겠습니까 ?[y/n]")

if choice_yn == 'y':
    # 가상데이터 입력해보기
    sql = """update netflix_list set
                type = %s,
                title = %s,
                director = %s, 
                cast = %s, 
                country = %s, 
                release_year = %s, 
                duration = %s, 
                description = %s
                where show_id = %s"""
    curs.execute(sql,(i_type, i_title, i_director, i_cast, 
                    i_country, i_release_year, i_duration, i_description, c_show_id))
    conn.commit()
    print(f"netflix_list 테이블에 {c_show_id} 코드번호를 수정하였습니다.")
else:
    print("수정이 취소하였습니다.")

conn.close()
