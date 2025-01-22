import asyncio
import websockets

# Lista para manter as conexões ativas
connected_clients = set()

async def handler(websocket, path):
    # Adicionar o cliente conectado à lista
    connected_clients.add(websocket)
    print("Novo cliente conectado.")
    try:
        async for message in websocket:
            print(f"Mensagem recebida: {message}")
            # Reencaminhar a mensagem para todos os outros clientes conectados
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Conexão fechada: {e}")
    finally:
        # Remover o cliente desconectado da lista
        connected_clients.remove(websocket)

# Iniciar o servidor WebSocket
start_server = websockets.serve(handler, "0.0.0.0", 12345)

# Executar o servidor
asyncio.run(start_server)
