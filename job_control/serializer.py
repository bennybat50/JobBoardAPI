from rest_framework import serializers

from job_control.models import JobModel, JobTypeModel, JobApplicationModel, JobTypeJobModel
from user_control.models import OrganizationModel
from user_control.serializers import OrganizationModelSerializer, ApplicantModelSerializer


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = ('uuid', 'name',)


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = ('uuid', 'organization', 'title', 'description', 'department', 'location')

    def save(self, **kwargs):
        job = JobModel.objects.create(
            organization=self.validated_data['organization'],
            title=self.validated_data['title'],
            description=self.validated_data['description'],
            department=self.validated_data['department'],
            location=self.validated_data['location'],
        )
        return job


class JobDetailSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()

    class Meta:
        model = JobModel
        fields = ('uuid', 'organization', 'title', 'description', 'department', 'location')

    def get_organization(self, obj):
        print(obj.organization)
        return OrganizationModelSerializer(obj.organization).data


class JobTypeJobSerializer(serializers.ModelSerializer):
    job_type = serializers.SerializerMethodField()

    class Meta:
        model = JobTypeJobModel
        fields = ('uuid', 'job_type',)

    def get_job_type(self, obj):
        return JobTypeSerializer(obj.job_type).data


class JobApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationModel
        fields = ('uuid', 'job', 'applicant', 'cover_letter')

    def save(self, **kwargs):
        job = self.validated_data['job']
        applicant = self.validated_data['applicant']
        cover_letter = self.validated_data['cover_letter']

        job_application = JobApplicationModel.objects.create(
            job=job,
            applicant=applicant,
            cover_letter=cover_letter,
        )

        return job_application


class JobApplicationDetailSerializer(serializers.ModelSerializer):
    job = serializers.SerializerMethodField()
    applicant = serializers.SerializerMethodField()

    class Meta:
        model = JobApplicationModel
        fields = ('uuid', 'job', 'applicant', 'cover_letter', 'status')

    def get_job(self, obj):
        return JobDetailSerializer(obj.job).data

    def get_applicant(self, obj):
        return ApplicantModelSerializer(obj.applicant).data