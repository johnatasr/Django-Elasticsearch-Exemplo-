from rest_framework.routers import SimpleRouter

from courses import views

app_name = 'courses'

router = SimpleRouter()
router.register(
    prefix=r'',
    base_name='courses',
    viewset=views.CoursesViewSet
)
urlpatterns = router.urls
