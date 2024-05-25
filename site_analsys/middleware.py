from .models import Visitor
from django.utils.deprecation import MiddlewareMixin

class VisitorTrackingMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.method == 'GET':
            ip_address = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT', '<unknown>')
            page_visited = request.path
            session_key = request.session.session_key

            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            Visitor.objects.create(
                ip_address=ip_address,
                user_agent=user_agent,
                page_visited=page_visited,
                session_key=session_key
            )

        return None
