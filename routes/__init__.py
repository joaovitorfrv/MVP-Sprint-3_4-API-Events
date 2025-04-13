from .event_routes import init_event_routes
from .home_routes import init_home_routes
from .health_route import init_health_route

def init_routes(app):
    """Inicializa todas as rotas do aplicativo"""
    init_home_routes(app)
    init_event_routes(app)
    init_health_route(app)