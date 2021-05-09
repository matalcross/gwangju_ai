import pymysql

# 데이터베이스 연결하기
conn = pymysql.connect(host='localhost', user='netflix', password='netflix1234',
        db='netflixdb', charset='utf8')
curs = conn.cursor()

# 입력확인
i_show_id = input("작품코드:")
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
print("[입력내용확인]")
print("---------------------------------------------")
print("작품코드:", i_show_id)
print("작품형태:", i_type)
print("작품이름:", i_title)
print("디렉터:", i_director)
print("배우:", i_cast)
print("제작국가:", i_country)
print("제작년도:", i_release_year)
print("상영시간:", i_duration)
print("작품설명:", i_description)
print("---------------------------------------------")

choice_yn = input("입력하신 내용을 저장하시겠습니까 ?[y/n]")

if choice_yn == 'y':
    # 가상데이터 입력해보기
    sql = """insert into netflix_list(show_id, type, title, director, cast, country, release_year, duration, description)
                            values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    curs.execute(sql,(i_show_id, i_type, i_title, i_director, i_cast, 
                    i_country, i_release_year, i_duration, i_description))
    conn.commit()
    print(f"netflix_list 테이블에 {i_show_id} 코드번호의 {i_title}을 저장하였습니다.")
else:
    print("입력을 취소하였습니다.")

conn.close()