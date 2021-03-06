from django.urls import path, re_path
from . import views

app_name = "users_url"

urlpatterns = [
    path("explore", view=views.ExploreUsers.as_view(), name="explore_users"),
    path("<int:user_id>/follow/", view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow/", view=views.UnFollowUser.as_view(), name="unfollow_user"),
    path("search/", view=views.Search.as_view(), name="search"),
    re_path(r'^(?P<username>\w+)/$', view=views.UserProfile.as_view(), name="user_profile"),
    re_path(r'^(?P<username>\w+)/followers/$', view=views.UserFollowers.as_view(), name="user_followers"),
    re_path(r'^(?P<username>\w+)/following/$', view=views.UserFollowing.as_view(), name="user_following"),
    re_path(r'^(?P<username>\w+)/password/$', view=views.ChangePassword.as_view(), name="change_password"),
    path("login/facebook/", view=views.FacebookLogin.as_view(), name='fb_login'),
    #url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
]
