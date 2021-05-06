# List serializers
class JobListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name="job-detail", lookup_field='slug')
    class Meta:
        model = Job
        fields = ['title', 'job_url', 'url', 'job_type', 'price', 'experience', 'posted', 'data_obtained']

class JobDetailSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'job_url', 'job_type', 'description', 'price', 'experience', 'posted', 'client_country',
                  'hire_rate', 'data_obtained']
        
        
"""
OUTPUT

 {
            "title": "test data clue",
            "job_url": "https://stackoverflow.com/questions/46195429/django-get-absolute-url-return-user-to-the-same-page-after-form-submission",
            "url": "http://localhost:8000/api/jobs/test-data-clue/",
            "job_type": "Fixed Price",
            "price": "$50",
            "experience": "Expert",
            "posted": "40 minutes ago",
            "data_obtained": "2021-05-05T15:43:21.525471Z"
        }
"""
