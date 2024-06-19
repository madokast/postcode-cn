import json

PROVINCE_FULL_NAME = {'北京':'北京市', '天津':'天津市', '内蒙古':'内蒙古自治区', '上海':'上海市', 
                      '广西':'广西壮族自治区', '重庆':'重庆市', '西藏':'西藏自治区', '宁夏':'宁夏回族自治区',
                      '新疆':'新疆维吾尔自治区', '香港':'香港特别行政区', '澳门':'澳门特别行政区'}

postal2area = dict() # code -> (省,市,区) | (直辖市,'',区)

with open('data/xiaomi_zipcode.js', mode='r', encoding='utf-8') as src:
    js = src.readlines()[1][len('var data = '):] # 第二行，去除 var data = 
    data = json.loads(js)
    for provinces in data:
        province = provinces['name']
        province = PROVINCE_FULL_NAME.get(province, province + '省')
        print('process', province)
        for city in provinces['child']:
            if province.endswith('市'):
                for county in city['child']:
                    postal2area[county['zipcode']] = (province, '', county['name'])
            else:
                city_name = city['name']
                for county in city['child']:
                    if 'zipcode' in county:
                        postal2area[county['zipcode']] = (province, city_name, county['name'])
    

with open("data.json", mode="w+", encoding='utf-8') as f:
    print("dumps", "data.json")
    json.dump(postal2area, f, ensure_ascii=False)

with open("data_pretty.json", mode="w+", encoding='utf-8') as f:
    print("dumps", "data_pretty.json")
    json.dump(postal2area, f, ensure_ascii=False, indent=2)

