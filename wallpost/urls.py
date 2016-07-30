from django.conf.urls import url
from wallpost import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^update_profile/$',views.update_profile,name='update_profile'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^login/$',views.user_login,name='user_login'),
	url(r'^add_category/$',views.add_category,name='add_category'),
	url(r'^logout/$',views.user_logout,name='user_logout'),
	url(r'^(?P<category_slug>[-\w]+)/$',views.category,name='category'),
	url(r'^(?P<category_slug>[-\w]+)/create_post/$',views.create_post,name='create_post'),
	url(r'^(?P<category_slug>[-\w]+)/(?P<id>\d+)/$',views.post,name='post'),
	] 
