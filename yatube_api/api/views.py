from django.shortcuts import get_object_or_404

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import GroupSerializer, PostSerializer
from .serializers import CommentSerializer, FollowSerializer

from rest_framework import permissions
from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """This GroupViewSet is created for Groups."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PostViewSet(viewsets.ModelViewSet):
    """This PostViewSet is created for Posts."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """This CommentViewSet is created for Comments."""
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """This FollowViewSet is created for Followers"""
    serializer_class = FollowSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    filter_backends = (filters.SearchFilter,)

    search_fields = ['following__username', 'user__username']

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
