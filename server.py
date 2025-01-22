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

async def main():
    async with websockets.serve(handler, "0.0.0.0", 12345):
        print("Servidor WebSocket rodando na porta 12345...")
        await asyncio.Future()  # Mantém o servidor rodando

# Inicializa o loop de eventos e executa o servidor
if __name__ == "__main__":
    asyncio.run(main())
