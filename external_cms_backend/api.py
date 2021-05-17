from wagtail.api.v2.router import WagtailAPIRouter
from wagtail_spa_integration.views import SPAExtendedPagesAPIEndpoint, RedirectViewSet
from wagtail_spa_integration.headless_preview_api import PagePreviewAPIViewSet

api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint('pages', SPAExtendedPagesAPIEndpoint)
api_router.register_endpoint('page_preview', PagePreviewAPIViewSet)
api_router.register_endpoint('redirects', RedirectViewSet)
