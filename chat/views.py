from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from modules import chat


def index(request):
    """Renderiza a página principal do chat."""
    return render(request, 'chat/index.html')


@csrf_exempt
@require_http_methods(["POST"])
def api_chat(request):
    """Endpoint da API para processar mensagens do chat."""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({
                'success': False,
                'error': 'Mensagem vazia. Por favor, digite algo.'
            }, status=400)
        
        # Gera resposta usando o módulo chat existente
        response = chat.generate_response(user_message)
        
        return JsonResponse({
            'success': True,
            'response': response
        })
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Erro ao processar a requisição JSON.'
        }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Erro ao gerar resposta: {str(e)}'
        }, status=500)

