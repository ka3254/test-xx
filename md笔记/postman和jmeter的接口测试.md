#接口测试
### 接口的组成
>- 接口地址/url(requsturl)
>- 接口类型(requst method)
>1.post
>2.get
>3.put
>- 请求头(response headers)
>- 请求参数(data)
一般都是key:value格式
1.get类型接口的请求头在url或者params
2.post类型接口的在在body
>- 响应结果响应结果(preview)
状态码(status code)(postman的返回框体上的才是状态码)
200-ok-接口正常运行
404-无法找到-url错误
405-方法不被允许-请求类型错误
400-错误的请求-输入的参数有问题
500-内部服务器错误-服务器异常-到服务器tail-f查看日志寻找报错日志

#### 接口的作用:前后端的联系连接
#### 接口测试的目的:为了保证接口不出问题而测试后端
#### get和post的区别
>	get
		一般使用get来读数据库的数据
		get的参数在url中,是暴露出来的,不安全
		get型接口不支持数据很多的参数
	post
		一般用来向数据库写入/修改内容
		接口参数在body中,是隐藏的
		post接口数据无上限

### 接口测试工具
### postman
> ___
##### get接口
>- 选择接口类型,填入url:地址端口+接口地址,点击send访问当前接口
>- 请求头只能放到headers的key里
>- get的接口参数填到params里也可以在url后通过&连接填写多个参数
>- save保存当前接口
 ##### post接口
>- post的请求头写到body里,字符类型按照要求填写,json类型在raw里
>- 登陆类型的接口在登录后可从返回数据的body里找到token文件
 ##### put接口
#### postman的技巧
##### 局部变量
>在右上角齿轮处点添加,写入key然后将值填入CURRENT VALUE,创建一个token的参数,
>例:创建token变量让value等于实际token 然后在其他需要使用token的地方直接'{{token}}'引用,重新登陆之后更改局部变量token的值就可以了
##### 断言
>- 在tests处的代码是控制请求后的参数
>- 在Pre-request Script处的代码是控制请求前的参数
>1,根据右侧方法选择需要的基础句式(例为responsebody:Json value check)
>2.var jsonData,将返回值保存到jsonData中,pm为比较,将jsonData.value的value改为返回的状态码,同时将eql的值改为判断需要的状态码(value如果是多层json嵌套的内层,需要从第一层的key开始写,直到要的key)
 ##### 批量执行接口
> 将有联系的接口写好自动断言放到一个文件夹,然后再文件夹右侧的三角选出run,在弹出的页面调整好逻辑顺序即可按排序逻辑自动测试多个端口,每条对应一个用例,
 ### jmeter使用技巧
>___
#### 接口测试 (执行顺序为列表从上到下)
>- http请求设置 
>1.testplan下添加线程组
>2.右键添加 http请求等+信息头管理器(请求头,key:value模式填写)+察看结果树等,
>3.★在http请求中,方法为接口类型,路径为接口地址,content encoding为字符类型(uft8),get接口的接口参数写到 parameters里,post的参数写到body data
>- 请求头的设置
>1.添加请求头管理 线程组->配置元件->http信息头管理器
>2.key:value模式写入请求头
>- 查看测试结果
>1.添加察看结果树 http请求->监听器->察看结果树
>- 参数化(类似postman环境变量)
>1.线程组->配置元件->用户定义变量 
> 用户自定义变量的三列分别为key:value:备注
>2.使用写法不同于postman,为${变量key};
>- 自动获取结果(自动提取值设置环境变量)
>1.http请求->后置处理器->正则表达式提取器
>a.引用名称为设置的变量名
>b.正则表达式为"需要获取的key"."(.*?)",
>c.模板为 ($1$)
>2.引用自动的获取变量是直接在其他的http请求中设置http信息头管理器中直接引用即可,用法(key.${变量名})
>- 断言
>1.http请求->断言->json assertion(单个执行的断言需添加到对应请求,不然会层级生效)
>2.assert json中的$符号代表返回的所有内容,$.key加下方expected value框的对比值即可实现断言
>例如 path exists框的 $.status+下方expected value 200 可以检测返回值是否为200
#### 性能测试
>- 多线程模拟
>在线程组中的 线程数 写入需要模拟的操作人数,即可实现多线程模拟,
>- 聚合报告
>1.线程组->监听器->聚合报告
>2.从左到右标题分别为"http请求名 请求数 平均响应时间(毫秒) 响应中位数 90%时间 95时间 99时间 最小时间 最大时间  错误率 每分钟吞吐量(kb/min) 接收数据 发送数据" 
#### jmeter 配置
>1.基于java,所以需要配置好的java环境
>2.配置环境变量 复制jmeter根目录路径,新建 JMETER_HOME变量,
>3.在path变量中新增 %JMETER_HOME%\bin变量
>4cmd中 输入jmeter启动/bin目录下jmeter批处理文件启动