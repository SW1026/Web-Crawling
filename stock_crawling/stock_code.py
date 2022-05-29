# stock_code.py

import csv


def output_info(key, values):
    print(f"번   호 : {key}")
    print(f"회 사 명 : {values['name']}")
    print(f"종목코드 : {values['code']}")
    print(f"업 종 : {values['line']}")
    print(f"회사주소 : {values['addr']}")


def search_code():
    company_list = {}
    key = 1
    for row in rows:
        if company_name in row[2]:
            company_list[key] = {"code": row[1], "name": row[2], "line": row[4], "addr": row[10]}
            key += 1

    for key, values in company_list.items():
        output_info(key, values)
        print("-" * 150)
        # print(values)

    while True:
        key = int(input("검색한 번호 : "))
        if key in company_list.keys():
            print(company_list[key]["code"])
            break
        print("없는 번호입니다.")
    return company_list[key]["code"]


company_name = input("회사명: ")
file = open("C:\\Users\\SW1026\\Desktop\\data.csv", "r", encoding="utf-8")
rows = csv.reader(file)