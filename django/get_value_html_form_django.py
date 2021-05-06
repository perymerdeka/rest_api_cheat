# Templates
<form method="POST">
  {% for val in value_list %}
    <input type='text' value='{{ val }}' name='my_list'>{{ val }}</input>
  {% endfor %}
</form>

# Views
def view1(request):
    value_list = [1,2,3,4,5] # it will change every time view1 will get request
    if request.method == "POST":
        values_from_user = request.POST.getlist('my_list')
    return render ('ip_form.html', 'value_list': value_list)
"""
resources: https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.QueryDict.getlist
"""
