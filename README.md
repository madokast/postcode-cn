# postal-code-cn

中国邮编数据，来自小米 https://p.www.xiaomi.com/open/common/js/address_all.js

已保存在 data 文件夹中，版本时间为 202406190303，保存时间为 2024年6月19日

使用 resolve(postcode) 获取邮政编码地址，返回 (省,市,区) 元组，如果是直辖市，则为 (直辖市,'',区)。

```
import postcode
print(postcode.resolve(100032)) # ('北京市', '', '西城区')
print(postcode.resolve(100000)) # ('北京市', '', '')

print(postcode.resolve(518109)) # ('广东省', '深圳市', '龙华区')
print(postcode.resolve(518110)) # ('广东省', '深圳市', '龙华区')
print(postcode.resolve(518000)) # ('广东省', '深圳市', '罗湖区')
print(postcode.resolve(518001)) # ('广东省', '深圳市', '罗湖区')
```
