from rest_framework import serializers

from address.models import Address
from address.serializers import AddressSerializer
from major.models import Major
from major.serializers import MajorSerializer

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    company_address = AddressSerializer(read_only=True)

    major = MajorSerializer(
        many=True, read_only=True
    )

    class Meta:             
        model = Company
        fields = '__all__'

    def create(self, validated_data):

        address_data = self.initial_data['company_address']

        # get/(create if not exists) address
        company_address, _ = Address.objects.get_or_create(
            street=address_data['street'],
            district=address_data['district'],
            city=address_data['city'],
            zipcode=address_data['zipcode']
        )

        major_datas = self.initial_data['major']
        list_major = []
        # get/(create if not exists) major
        for major_data in major_datas:
            major, _ = Major.objects.get_or_create(
                name=major_data['name']
            )
            list_major.append(major)

        # print(address_data) # OrderedDict([('name', 'adgg')])
        company = Company.objects.create(
            company_address=company_address, **validated_data)
        company.major.set(list_major)

        return company
