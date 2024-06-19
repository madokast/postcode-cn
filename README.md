# postal-code-cn

中国邮编数据，来自小米 https://p.www.xiaomi.com/open/common/js/address_all.js。data 文件夹中持久化版本时间为 202406190303

使用 resolve(postcode) 获取邮政编码地址，返回 (省,市,区) 元组，如果是直辖市，则为 (直辖市,'',区)。

```
import postcode
print(postcode.resolve(100032)) # ('北京市', '', '西城区')
print(postcode.resolve(100000)) # ('北京市', '', '')
```