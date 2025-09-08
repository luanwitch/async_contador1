from django.http import HttpResponse
import asyncio

async def contador(request):
    for i in range(1, 6):
        print(f"Contando... {i}")
        await asyncio.sleep(1)
    return HttpResponse("Contagem finalizada ✅")

def home(request):
    return HttpResponse("Bem-vindo ao Async Contador 🚀")
