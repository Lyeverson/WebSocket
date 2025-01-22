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

async def main():
    # Iniciar o servidor WebSocket
    print("Iniciando servidor WebSocket...")
    async with websockets.serve(handler, "0.0.0.0", 12345):
        await asyncio.Future()  # Mantém o servidor rodando indefinidamente

# Criação explícita do loop de eventos
if __name__ == "__main__":
    asyncio.run(main())
