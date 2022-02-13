from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CommentSerializer, PostSerializer
from rest_framework.generics import get_object_or_404
from .models import Post


# Create your views here.
class IndexView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response({"data": post_serializer.data})

class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.validated_data["author"] = request.user
            post_serializer.save()
            return Response({"message": "post created."})
        else:
            return Response({"error": post_serializer.errors})

class ShowPostView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post_serializer = PostSerializer(instance=post)
        data = post_serializer.data
        return Response({"data": data})

class UpdatePostView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post_serializer = PostSerializer(
            instance=post,
            data = request.data,
            partial=True
            )
        if post_serializer.is_valid():
            post_serializer.save()
            return Response({"message": "post updated."})
        else:
            return Response({"error": post_serializer.errors})

class DeletePostView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return Response({"message": "post deleted."})

class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.validated_data['post'] = post
            comment_serializer.save()
            return Response({"message": "comment created."}) 
        else:
            return Response({"error": comment_serializer.errors})

