from rest_framework import serializers
from .models import AllocationDetailsModel,LabModel,BoardAllocationDataModel,UtilizationSummaryModel,BroadcastModel
import json

class LabModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabModel
        fields = ('Name')

class LabModelDisplayAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabModel
        fields = '__all__'

class AllocationDetailSerializer(serializers.ModelSerializer):
    Program = serializers.CharField(source='Program')
    SKU = serializers.CharField(source='Sku')
    Vendor = serializers.CharField(source='Vendor')
    AllocatedTo = serializers.CharField(source='AllocatedTo')
    FromWW = serializers.CharField(source='FromWW')
    ToWW =  serializers.CharField(source='ToWW')
    NumberOfBenches = serializers.IntegerField(source='NumberOfBenches')
    Location = serializers.CharField(source='Location__Name')
    IsAllocated = serializers.BooleanField(source="IsAllocated")
    class Meta:
        model = AllocationDetailsModel
        fields = ('Program','SKU','Vendor','AllocatedTo','FromWW','ToWW','NumberOfBenches','Location','IsAllocated')


class ApproveViewSerializer(serializers.ModelSerializer):
    Program = serializers.CharField(source='Program')
    SKU = serializers.CharField(source='Sku')
    Vendor = serializers.CharField(source='vendor')
    AllocatedTo = serializers.CharField(source='allocatedTo')
    FromWW = serializers.CharField(source='FromWW')
    ToWW =  serializers.CharField(source='ToWW')
    NumberOfBenches = serializers.IntegerField(source='NumberOfBenches')
    Location = serializers.CharField(source='Location__Name')
    IsAllocated = serializers.BooleanField(source="IsAllocated")
    class Meta:
        model = AllocationDetailsModel
        fields = ('Program','SKU','Vendor','AllocatedTo','FromWW','ToWW','NumberOfBenches','Remarks','Location','IsAllocated')



class CustomJSONField(serializers.JSONField):
    def to_representation(self, obj):
        # Ensure that JSON strings are converted to dictionaries
        if isinstance(obj, str):
            return json.loads(obj)
        return obj

class BoardAllocationDataModelSerializer(serializers.ModelSerializer):
    # Use the custom serializer for the fields that store JSON data
    January = CustomJSONField()
    February = CustomJSONField()
    March = CustomJSONField()
    April = CustomJSONField()
    May = CustomJSONField()
    June = CustomJSONField()
    July = CustomJSONField()
    August = CustomJSONField()
    September = CustomJSONField()
    October = CustomJSONField()
    November = CustomJSONField()
    December = CustomJSONField()
    # Add the rest of your fields here

    class Meta:
        model = BoardAllocationDataModel
        fields = [
            "id","Program","Sku","Team","Vendor","TotalBoard","createdBy","createdDate","modifiedBy","modifiedDate","deletedBy","deletedDate",
            "isdeleted","year","January","February","March","April","May","June","July","August","September","October","November","December",
            ]
class BoardAllocationDataModelSerializers(serializers.ModelSerializer):
    # Use the custom serializer for the fields that store JSON data
    January = CustomJSONField()
    February = CustomJSONField()
    March = CustomJSONField()
    April = CustomJSONField()
    May = CustomJSONField()
    June = CustomJSONField()
    July = CustomJSONField()
    August = CustomJSONField()
    September = CustomJSONField()
    October = CustomJSONField()
    November = CustomJSONField()
    December = CustomJSONField()
    # Add the rest of your fields here

    class Meta:
        model = BoardAllocationDataModel
        fields = [
            "January","February","March","April","May","June","July","August","September","October","November","December",
            ]
    
class UtilizationSerializer2(serializers.ModelSerializer):
    AllocatedTo = serializers.JSONField(default=list)
    class Meta:
        model = UtilizationSummaryModel
        fields = '__all__'
    
class BroadcastSerializer(serializers.ModelSerializer):
    content_without_html = serializers.SerializerMethodField()

    def get_content_without_html(self, obj):
        # Remove HTML tags from content
        import re
        clean_content = re.sub('<[^<]+?>', '', obj.Content)
        return clean_content

    class Meta:
        model = BroadcastModel
        fields = ('id', 'Subject', 'Content','NewUser' ,'BroadCast_by', 'CreatedDate', 'User_mail_list', 'content_without_html')