
@csrf_exempt
def api_blog_list(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializers(blog, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializers(data=data)

        # validate the serializer
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def api_blog_detail(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = BlogSerializers(blog)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializers(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)
