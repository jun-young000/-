import requests
import  json

def getsSiDo():
    url="https://www.starbucks.co.kr/store/getSidoList.do"
    resp=requests.post(url)
    #print(resp)
    #print(resp.json())
    #print(resp.json()['list'])
    sido_json=resp.json()['list']
    sido_code=list(map(lambda x:x['sido_cd'],sido_json))
    # print(sido_code)
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    # print(sido_name)
    sido_dict=dict(zip(sido_code,sido_name))  #zip: list끼리 묶어서 dict로 반환
    return sido_dict

def getGuGUN(sido_code):
    url="https://www.starbucks.co.kr/store/getGugunList.do"
    resp=requests.post(url,data={"sido_cd":sido_code})
    # print(resp.json())
    gugun_json=resp.json()['list']
    gugun_dict=dict(zip(list(map(lambda x: x['gugun_cd'],gugun_json)),list(map(lambda x: x['gugun_nm'],gugun_json))))
    return gugun_dict


def getStore(sido_code="",gugun_code=""):
    url="https://www.starbucks.co.kr/store/getStore.do"
    resp=requests.post(url,data={"ins_lat": "37.5682",
                                 "ins_lng": "126.9977",
                                 "p_sido_cd": sido_code,
	                             "p_gugun_cd": gugun_code,
                                 "in_biz_cd": "",
                                 "set_date": ""
                                 })
    # print(resp.json())
    store_json=resp.json()["list"]

    store_list=list()
    for store in store_json:

        store_dict=dict()
        store_dict["s_name"]=store["s_name"]
        store_dict["tel"]=store["tel"]
        store_dict["doro-address"]=store["doro_address"]
        store_dict['lat']=store['lat']
        store_dict['lot']=store['lot']
        store_list.append(store_dict)
    res_dict=dict()
    res_dict["list"]=store_list
    result =json.dumps(res_dict, ensure_ascii=False)
    return  result



if __name__ =='__main__':
    print(getsSiDo())
    sido=input("시도 코드를 입력해 주세요")
    if sido =="17":
        print(getStore(sido_code=sido))
    else:
        print(getGuGUN(sido))
        gugun=input("구군 코드를 입력해 주세요")
        print(getStore(sido_code=sido, gugun_code=gugun))