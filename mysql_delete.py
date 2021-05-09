import pymysql

while True:
    c_show_id = input("삭제할 키값을 입력하세요 : ")

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

choice_yn = input(f"{c_show_id} 레코드를 삭제시겠습니까 ?[y/n]")

# 해당 레코드를 삭제한다.
sql = "delete from netflix_list where show_id = %s"
curs.execute(sql, c_show_id)

print(f"{c_show_id} 레코드를 삭제하였습니다.")

conn.commit()
conn.close()