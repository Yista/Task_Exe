## 基于flask框架实现的简易HTTP Server
 * ### version

    python 3.10.6
    
    Flask 2.3.3
***

### Flask框架

用于构建 web 应用的微型 Web 框架，提供了处理 HTTP 请求和响应的工具和函数。

### HTTP 服务器（Hypertext Transfer Protocol Server）
用于处理和响应 HTTP 请求的软件或硬件系统。其主要功能是接收客户端（通常是浏览器）发送的 HTTP 请求，并返回相应的 HTTP 响应。

* #### 代表

    Apache HTTP Server

    Nginx

    Microsoft IIS

* #### 工作流程：

1. 监听端口：HTTP 服务器会在指定的网络端口上监听传入的 HTTP 请求。通常，HTTP 请求使用标准端口号 80（HTTP）或 443（HTTPS）。

2. 接收请求：一旦有客户端发起 HTTP 请求，HTTP 服务器会接收并解析该请求。请求中包括请求方法（GET、POST、PUT、DELETE 等）、请求的资源路径、HTTP 头部信息以及请求体（对于 POST 请求）等信息。

3. 处理请求：HTTP 服务器会根据请求的内容和配置执行相应的操作，这可能涉及到访问文件系统、数据库、运行应用程序或其他处理逻辑，以生成响应数据。

4. 生成响应：一旦服务器处理完请求，它会生成一个 HTTP 响应，包括 HTTP 状态码、响应头部和响应主体。响应主体通常包括请求的资源（如 HTML 文件、图像、JSON 数据等）。

5. 发送响应：服务器将响应发送回客户端，通常通过 TCP/IP 协议。客户端接收响应并处理它，以在浏览器中呈现网页或执行其他操作。


### 实现API


* ####  1. GET
    
     GET 方法请求一个指定资源的表示形式，使用 GET 的请求应该只被用于获取数据。

* #### 2. POST
    POST 方法用于将实体提交到指定的资源，通常导致在服务器上的状态变化或副作用。

* #### 3.PUT
    PUT 方法用有效载荷请求替换目标资源的所有当前表示。

* #### 4. DELETE
    DELETE 方法删除指定的资源。

* #### 5.OPTIONS
    OPTIONS 方法用于描述目标资源的通信选项。

* #### 6.PATCH
    PATCH 方法用于对资源应用部分修改，PATCH 请求通常用于更复杂的数据结构，而 PUT 请求适用于替换整个项目的情况。

****
### 使用命令
在后台运行一个python3服务器，并将输出（标准输出和标准错误）重定向到一个日志文件中

    python3 -m server &> log &

测试GET请求

    curl  http://127.0.0.1:8000/get_data

测试POST请求

    添加name为 x ,value为 y 的数据：

    curl -X POST -H "Content-Type: application/json" -d '{"name":"x","value":"y"}' http://127.0.0.1:8000/add_data
测试 PUT 请求：
    
    更新名为 x 的数据:

    curl -X PUT -H "Content-Type: application/json" -d '{"value": "z"}' http://127.0.0.1:8000/update_data/x
测试 DELETE 请求：

    删除名为 x 的数据:

    curl -X DELETE http://127.0.0.1:8000/delete_item/x
测试 OPTIONS 请求：

    用于查看服务器支持的 HTTP 方法:

    curl -X OPTIONS http://127.0.0.1:8000/options_example
测试 PATCH 请求：

    部分更新名为 x 的数据:

    curl -X PATCH -H "Content-Type: application/json" -d '{"feild3": "new_value"}' http://127.0.0.1:8000/update_item/item3

