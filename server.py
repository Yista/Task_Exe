from flask import Flask, request, jsonify

app = Flask(__name__)

# 默认数据字典
data = {'item1': 'value1', 'item2': 'value2'}

# 使用嵌套字典结构的数据字典，用于测试patch
data2 = {
    'item3': {'field3_0': 'value3_0', 'field3_1': 'value3_1'},
    'item4': {'field4_0': 'value4_0', 'field4_1': 'value4_1'}
}


# GET请求接口
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data)

# POST请求接口
@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # 从请求中获取JSON数据
        request_data = request.get_json()

        # 检查请求中是否包含'name'和'value'字段
        if 'name' in request_data and 'value' in request_data:
            name = request_data['name']
            value = request_data['value']

            # 将数据存储到字典中
            data[name] = value

            return jsonify({'message': 'Data added successfully'})
        else:
            return jsonify({'error': 'Invalid request data'}), 400 #为HTTP状态码
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# PUT请求接口
@app.route('/update_data/<name>', methods=['PUT'])
def update_data(name):
    try:
        # 检查数据是否存在
        if name in data:
            request_data = request.get_json()
            value = request_data.get('value')

            if value is not None:
                # 更新数据
                data[name] = value

                return jsonify({'message': 'Data updated successfully'})
            else:
                return jsonify({'error': 'Invalid request data'}),
        else:
            return jsonify({'error': f'Data with name {name} not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# DELETE请求接口
@app.route('/delete_item/<item_name>', methods=['DELETE'])
def delete_item(item_name):
    if item_name in data:
        del data[item_name]
        return jsonify({'message': f'{item_name} deleted successfully'})
    else:
        return jsonify({'error': f'{item_name} not found'}), 404
    
# OPTIONS请求接口
@app.route('/options_example', methods=['OPTIONS'])
def options_example():
    response = jsonify({'message': 'This is an OPTIONS response.'})
    response.headers['Allow'] = 'GET, POST, PUT'
    return response

# PATCH请求接口
@app.route('/update_item/<item_name>', methods=['PATCH'])
def update_item(item_name):
    print(f"Received item_name: {item_name}")
    
    if item_name in data2:
        request_data = request.get_json()
        for key, value in request_data.items():
            data2[item_name][key] = value
        return jsonify({'message': f'{item_name} updated successfully'})
    else:
        return jsonify({'error': f'{item_name} not found'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
    #0.0.0.0'应用程序会监听所有网络接口;端口号设置8000，通常在开发环境中使用;debug参数设置为True,Flask以调试模式运行
    #app.run() #app.run() 会监听 localhost（即 127.0.0.1），只有本地机器可以访问应用程序
