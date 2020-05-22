from django_elasticsearch_dsl import (
    DocType,
    fields,
    Index,
)

from courses.models import Course

course_index = Index('course')

course_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@course_index.doc_type
class CourseDocument(DocType):

    title = fields.StringField(
        attr='course_title',
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.Completion(),
        }
    )

    course_level = fields.StringField(
        attr='level',
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    class Meta:
        model = Course
        fields = [
            'id',
            'course_title',
            'level'
        ]

