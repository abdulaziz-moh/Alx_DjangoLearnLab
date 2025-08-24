from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners can edit/delete.
    """

    def has_object_permission(self, request, view, obj):
        # Anyone can read (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only owner can edit/delete
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # assuming `following = models.ManyToManyField("self", symmetrical=False, related_name="followers")`
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
    

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            # create notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already liked"}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(post=post, user=request.user).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        return Response({"message": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)