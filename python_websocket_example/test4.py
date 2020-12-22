import ipaddress
import json
import time

import websockets
import asyncio

consumer_id = '31111'


async def main_logic():
    async with websockets.connect('ws://127.0.0.1:8000/ws/v1.0/traceroute/' + str(consumer_id)) as websocket:
        await websocket.send(json.dumps(
            {
                "message": {
                    "target_node": '30.207.41.0/24',
                    "cdn_id_list": [1, 2, 3],
                    "did": 38,
                }
            }
        ))
        count = 1
        while True:
            # time.sleep(5)
            # 等待服务器下发信息
            quote = await websocket.recv()
            # print(quote)
            data = json.loads(quote)['message']
            # print(data)
            if data['consumer_id'] == str(consumer_id):
                formate_result = data['response']
                for item in formate_result:
                    count += 1
                    print(count, item)
                # print(count, data['response'])
                # count += 1
            # print(quote)


asyncio.get_event_loop().run_until_complete(main_logic())
