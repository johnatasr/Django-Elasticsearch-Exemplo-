from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from courses.documents import CourseDocument


class CourseDocumentSerializer(DocumentSerializer):
    class Meta:
        document = CourseDocument
        fields = (
            'id',
            'course_title',
            'url',
            'is_paid',
            'price',
            'num_subscribers',
            'num_reviews',
            'num_lectures',
            'level',
            'content_duration',
            'published_timestamp',
            'subject'
        )
