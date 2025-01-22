import asyncio
import websockets

async def handler(websocket, path):
    print("Novo cliente conectado!")
    try:
        async for message in websocket:
            print(f"Mensagem recebida: {message}")
            await websocket.send(f"Mensagem ecoada: {message}")
    except websockets.ConnectionClosed:
        print("Cliente desconectado")

start_server = websockets.serve(handler, "0.0.0.0", 12345)

print("Servidor WebSocket rodando...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
