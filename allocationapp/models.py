#from django.db import models
from djongo import models
from django import forms
from django.utils import timezone
from djongo import models as djongo_models

# from simple_history.models import HistoricalRecords


# Create your models here.
class AllocatedToModel(models.Model):
    """ Model to store Allocated user data inside the bench"""
    WWID = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=255,blank=True, null=True)
    Email = models.EmailField(blank=True)

    def __str__(self):
        return self.Name

class BenchAllocationDataModel(models.Model):
    """ Model to store bench allocation data"""
    id = models.IntegerField(default=1,primary_key=True)
    Program = models.CharField(max_length=10,blank=True)
    SKU = models.CharField(max_length=10,blank=True)
    Vendor = models.CharField(max_length=255,blank=True)
    Who = models.ArrayField(model_container=AllocatedToModel,blank=True)
    FromWW = models.CharField(max_length=20,blank=True)
    ToWW = models.CharField(max_length=20,blank=True)
    Duration = models.CharField(max_length=10,null=True,blank=True)
    Team = models.CharField(max_length=20,blank=True)
    Remarks = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return f"Allocated to {self.Who} from {self.FromWW} to {self.ToWW}"


class BenchesModel(models.Model):
    """ Model to store bench details"""
    key = models.CharField(max_length=10,blank=True,primary_key=True)
    status = models.CharField(max_length=100,blank=True,null=True)
    BenchName = models.CharField(max_length=10,null=True,blank=True)
    IsAllocated = models.BooleanField(default=False)
    IsRequested = models.BooleanField(default=False)
    seatNo = models.CharField(max_length=10,blank=True,null=True)
    seatLabel = models.CharField(max_length=10,null=True,blank=True)
    dir = models.CharField(max_length=5,null=True,blank=True) 
    labelNo = models.CharField(max_length=5,blank=True,null=True)
    team = models.CharField(max_length=10,null=True,blank=True)
    AllocationData = models.ArrayField(model_container=BenchAllocationDataModel,blank=True,null=True)
    #AllocatedDate = models.DateTimeField(blank=True,null=True,auto_now=True)
    objects = models.DjongoManager()
    def __str__(self):
        return str(self.BenchId)

class BenchesRowModel(models.Model):
    seatRowLabel = models.CharField(primary_key=True,unique=True,max_length=10)
    IsRowSpace = models.BooleanField(default=False)
    seats = models.ArrayField(model_container=BenchesModel,null=True,blank=True)
    objects = models.DjongoManager()
    def __str__(self):
        return str(self.SeatRowLabel)


class LabModel(models.Model):
    """ Model to store the lab layout"""
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200,blank=True,null=True,unique=True)
    NumberOfWorkbenches = models.IntegerField()
    AllocatedWorkbenches = models.IntegerField(default=0)
    #AddedDate = models.DateTimeField(auto_now_add=True,null=True)
    BenchDetails = models.ArrayField(model_container=BenchesRowModel,null=True,blank=True)
    objects = models.DjongoManager()
    
    def __str__(self):
        return self.Name


class AllocationDetailsModel(models.Model):
    """
     Model to store the Allocation requests
    """
    id = models.AutoField(primary_key=True,unique=True)
    Program = models.CharField(max_length=100,blank=True)
    Sku = models.CharField(max_length=100,blank=True)
    Vendor = models.CharField(max_length=100,blank=True)
    Team = models.CharField(max_length=100,blank=True,null=True)
    AllocatedTo = models.ArrayField(model_container=AllocatedToModel,blank=True,null=True)
    NotifyTo = models.JSONField(blank=True,null=True)
    FromWW = models.CharField(max_length=20,blank=True)
    ToWW = models.CharField(max_length=20,blank=True)
    Duration = models.CharField(max_length=10,blank=True,null=True)
    NumberOfbenches = models.IntegerField()
    Remarks = models.TextField(blank=True)
    Location = models.ForeignKey(LabModel,on_delete=models.SET_NULL,null=True,db_index=True)
    IsAllocated = models.BooleanField(default=False)
    IsRequested = models.BooleanField(default=False)
    BenchData = models.JSONField(blank=True,null=True)
    DeallocatedBenchData = models.JSONField(blank=True,null=True)
    AllocatedDate = models.DateTimeField(auto_now=True,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=100,blank=True,null=True)
    Reason = models.CharField(max_length=255,blank=True,null=True)
    approvedBy = models.CharField(max_length=255,blank=True,null=True)
    #changes
    RejectedBy = models.CharField(max_length=255,blank=True,null=True)
    RejectedDate = models.CharField(blank=True, max_length=255, null=True)
    DeallocatedBy = models.CharField(max_length=255,blank=True,null=True)
    deallocatedDate = models.DateTimeField(auto_now=True,blank=True,null=True)
    # changes
    RequestedBy = models.ArrayField(model_container=AllocatedToModel,blank=True,null=True)
    RequestedDate = models.DateTimeField(auto_now=True,blank=True,null=True)
    def __str__(self):
        return str(self.id)
    


class ProgramsModel(models.Model):
    """ Model for storing the programs data"""
    ProgramShortName = models.CharField(max_length=100,blank=True,null=True) 
    ProgramName = models.CharField(max_length=255,blank=True,null=True)
    CreatedBy = models.CharField(max_length=255,blank=True,null=True)
    CreatedDate = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.ProgramName
        
class SkuModel(models.Model): 
    """ Models for storing the SKU data"""
    ProgramName = models.ForeignKey(ProgramsModel,on_delete=models.CASCADE,null=True)
    SkuName = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.SkuName

class VendorsModel(models.Model):
    """ Model for storing the Vendor data"""
    id = models.AutoField(primary_key=True)
    VendorName = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.VendorName
    
class TeamsModel(models.Model):
    """ Model for storing Teams data"""
    id = models.AutoField(primary_key=True)
    TeamName = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.TeamName

class UserRolesModel(models.Model):
    """ Model for storing User Roles"""
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255,blank=True,unique=True)
    isactive = models.BooleanField(default=True)
    def __str__(self):
        return self.role_name

class UserModel(models.Model):
    """ Models for storing approved User data"""
    WWID = models.PositiveIntegerField(primary_key=True,default=0)
    Name = models.CharField(max_length=255,blank=True,null=True)
    Idsid = models.CharField(max_length=255,blank=True,null=True)
    DisplayName = models.CharField(max_length=255,blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    Role = models.ForeignKey(to=UserRolesModel,on_delete=models.SET_NULL,null=True)
    Badge = models.CharField(max_length=2,blank=True,null=True)
    LastLoggedOn = models.DateTimeField()
    CreatedOn = models.DateTimeField()
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.DisplayName


class UserRequestModel(models.Model):
    """ Model to store user add requests"""
    RequestId = models.AutoField(primary_key=True)
    WWID = models.PositiveIntegerField(default=0)
    Name = models.CharField(max_length=255,blank=True,null=True)
    Idsid = models.CharField(max_length=255,blank=True,null=True)
    DisplayName = models.CharField(max_length=255,blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    Role = models.ForeignKey(to=UserRolesModel,on_delete=models.SET_NULL,null=True)
    Badge = models.CharField(max_length=2,blank=True,null=True)
    ApprovedOn = models.DateTimeField()
    CreatedOn = models.DateTimeField()
    ApprovedBy = models.CharField(max_length=255,blank=True,null=True)
    IsActive = models.BooleanField(default=True)
    status = models.CharField(max_length=100,null=True,blank=True)
    Reason = models.TextField(blank=True,null=True)
    IsAdded = models.BooleanField(default=False)
    IsRequested = models.BooleanField(default=False)
    
    def __str__(self):
        return self.DisplayName


class SuggestionsModel(models.Model):
    """ Models for storing suggestions"""
    id = models.AutoField(primary_key=True)
    suggestion_by = models.ArrayField(model_container=AllocatedToModel,blank=True,null=True)
    suggestion = models.TextField()
    status = models.CharField(max_length=100,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    resolved_date = models.DateTimeField(null=True)
    closing_comments = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.suggestion


class ApproverUserModel(models.Model):
    """ Model for storing approvers data"""
    WWID = models.PositiveIntegerField(primary_key=True,default=0)
    Name = models.CharField(max_length=255,blank=True,null=True)
    Idsid = models.CharField(max_length=255,blank=True,null=True)
    DisplayName = models.CharField(max_length=255,blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    Badge = models.CharField(max_length=2,blank=True,null=True)
    LastLoggedOn = models.DateTimeField()
    CreatedOn = models.DateTimeField()
    IsActive = models.BooleanField(default=True)

    def __str__(self):
            return self.DisplayName

class BoardAllocationDataModel(models.Model):
    """ Model to store board allocation data"""
    id = models.AutoField(primary_key=True)
    Program = models.CharField(max_length=100,blank=True)
    Sku = models.CharField(max_length=100,blank=True)
    Team = models.CharField(max_length=255,blank=True)
    Vendor = models.CharField(max_length=255,blank=True)
    TotalBoard = models.IntegerField(default=0)
    createdBy = models.CharField(max_length=255,blank=True)
    createdDate = models.DateTimeField(auto_now_add=True,null=True)
    modifiedBy = models.CharField(max_length=255,null=True,blank=True)
    modifiedDate = models.DateTimeField(auto_now_add=True,null=True)
    deletedBy = models.CharField(max_length=255,blank=True)
    deletedDate = models.DateTimeField(auto_now_add=True,null=True)
    isdeleted = models.BooleanField(default=False)
    year = models.PositiveIntegerField()
    January = models.JSONField()
    February = models.JSONField()
    March = models.JSONField()
    April = models.JSONField()
    May = models.JSONField()
    June = models.JSONField()
    July = models.JSONField()
    August = models.JSONField()
    September = models.JSONField()
    October = models.JSONField()
    November = models.JSONField()
    December = models.JSONField()

    def save(self, *args, **kwargs):
        if not self.pk:
            action = 'insert'
        elif not getattr(self, 'isdeleted', False):
            # This is an update operation (excluding soft deletes)
            action = 'update'
        else:
            action = 'delete',
            self.isdeleted = True
        
        super(BoardAllocationDataModel, self).save(*args, **kwargs)
        # Create a historical record
        BoardAllocationDataModelTrackData.objects.create(
            instance_id=self.id,
            action=action,
            Program = self.Program,
            Sku = self.Sku,
            Team = self.Team,
            Vendor = self.Vendor,
            TotalBoard = self.TotalBoard,
            createdBy = self.createdBy,
            createdDate = self.createdDate,
            modifiedBy = self.modifiedBy,
            modifiedDate = self.modifiedDate,
            deletedBy = self.deletedBy,
            deletedDate = self.deletedDate,
            isdeleted = self.isdeleted,
            year = self.year,
            January=self.January or {},
            February=self.February or {},
            March = self.March or {},
            April = self.April or {},
            May = self.May or {},
            June = self.June or {},
            July = self.July or {},
            August = self.August or {},
            September = self.September or {},
            October = self.October or {},
            November = self.November or {},
            December = self.December or {}
        )

    def __str__(self):
        return str(self.Program)
    
class BoardAllocationDataModelTrackData(models.Model):
    ACTION_CHOICES = (
        ('insert', 'Insert'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    )

    id = models.AutoField(primary_key=True)
    instance_id = models.IntegerField()  # ID of the instance in BoardAllocationDataModel
    Program = models.CharField(max_length=100,blank=True)
    Sku = models.CharField(max_length=100,blank=True)
    Team = models.CharField(max_length=255,blank=True)
    Vendor = models.CharField(max_length=255,blank=True)
    TotalBoard = models.IntegerField(default=0)
    createdBy = models.CharField(max_length=255,blank=True)
    createdDate = models.DateTimeField(auto_now_add=True,null=True)
    modifiedBy = models.CharField(max_length=255,null=True,blank=True)
    modifiedDate = models.DateTimeField(auto_now_add=True,null=True)
    deletedBy = models.CharField(max_length=255,blank=True)
    deletedDate = models.DateTimeField(auto_now_add=True,null=True)
    isdeleted = models.BooleanField(default=False)
    year = models.PositiveIntegerField()
    January = models.JSONField()
    February = models.JSONField()
    March = models.JSONField()
    April = models.JSONField()
    May = models.JSONField()
    June = models.JSONField()
    July = models.JSONField()
    August = models.JSONField()
    September = models.JSONField()
    October = models.JSONField()
    November = models.JSONField()
    December = models.JSONField()
    action = models.CharField(max_length=250, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class UtilizationSummaryModel(models.Model):
    id = models.AutoField(primary_key=True)
    workweek = models.CharField(max_length=20,blank=True)
    Location = models.CharField(max_length=100,blank=True)
    BenchData = models.CharField(max_length=255)
    Program = models.CharField(max_length=100,blank=True)
    Sku = models.CharField(max_length=100,blank=True)
    Vendor = models.CharField(max_length=100,blank=True)
    FromWW = models.CharField(max_length=20,blank=True)
    ToWW = models.CharField(max_length=20,blank=True)
    Duration = models.CharField(max_length=10,blank=True)
    AllocatedTo = models.ArrayField(model_container=AllocatedToModel,blank=True)
    NumberOfbenches = models.IntegerField()
    Remarks = models.TextField(blank=True)
    Team = models.CharField(max_length=100,blank=True)
    approvedBy = models.CharField(max_length=255,blank=True)
    Planned_Utilization = models.FloatField(default=0)
    Actual_Utilization = models.FloatField(default=0)
    Actual_utilization_in_percentage = models.CharField(max_length=255,blank=True, null=True)
    Utilization_Percentage = models.CharField(max_length=255,blank=True,null=True)
    Allocated_POC = models.CharField(max_length=100)
    Remarks_Utilization = models.CharField(max_length=255,blank=True)
    Createdby = models.CharField(max_length=255,blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True,null=True)
    Modifiedby = models.CharField(max_length=255,blank=True)
    ModifiedDate = models.DateTimeField(auto_now_add=True,null=True)
    Deletedby = models.CharField(max_length=255,blank=True)
    DeletedDate = models.DateTimeField(auto_now_add=True,null=True)
    isDeleted = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            action = 'insert'
        elif not getattr(self, 'isdeleted', False):
            # This is an update operation (excluding soft deletes)
            action = 'update'
        else:
            action = 'delete',
            self.isdeleted = True
        
        super(UtilizationSummaryModel, self).save(*args, **kwargs)
        # Create a historical record
        UtilizationSummaryModelTrackData.objects.create(
            instance_id=self.id,
            action=action,
            workweek = self.workweek,
            Location = self.Location,
            BenchData = self.BenchData,
            Program = self.Program,
            Sku = self.Sku,
            Vendor = self.Vendor,
            FromWW = self.FromWW,
            ToWW = self.ToWW,
            Duration = self.Duration,
            AllocatedTo = self.AllocatedTo,
            NumberOfbenches = self.NumberOfbenches,
            Remarks = self.Remarks,
            Team = self.Team,
            approvedBy = self.approvedBy,
            Planned_Utilization = self.Planned_Utilization,
            Actual_Utilization = self.Actual_Utilization,
            Actual_utilization_in_percentage = self.Actual_utilization_in_percentage,
            Utilization_Percentage = self.Utilization_Percentage,
            Allocated_POC = self.Allocated_POC,
            Remarks_Utilization = self.Remarks_Utilization,
            Createdby = self.Createdby,
            CreatedDate = self.CreatedDate,
            Modifiedby = self.Modifiedby,
            ModifiedDate = self.ModifiedDate,
            Deletedby = self.Deletedby,
            DeletedDate = self.DeletedDate,
            isDeleted = self.isDeleted
        )

    def soft_delete(self):
        self.isDeleted = True
        self.save()

    def undelete(self):
        self.isDeleted = False
        self.save()

    objects = models.Manager()  # The default manager
    active_objects = models.Manager()  # A manager that includes only non-deleted records
    def __str__(self):
        return f"{self.workweek} - {self.Location}"
    
class UtilizationSummaryModelTrackData(models.Model):
    ACTION_CHOICES = (
        ('insert', 'Insert'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    )

    id = models.AutoField(primary_key=True)
    instance_id = models.IntegerField()  # ID of the instance in BoardAllocationDataModel
    workweek = models.CharField(max_length=20,blank=True)
    Location = models.CharField(max_length=100,blank=True)
    BenchData = models.CharField(max_length=255)
    Program = models.CharField(max_length=100,blank=True)
    Sku = models.CharField(max_length=100,blank=True)
    Vendor = models.CharField(max_length=100,blank=True)
    FromWW = models.CharField(max_length=20,blank=True)
    ToWW = models.CharField(max_length=20,blank=True)
    Duration = models.CharField(max_length=10,blank=True)
    AllocatedTo = models.ArrayField(model_container=AllocatedToModel,blank=True)
    NumberOfbenches = models.IntegerField()
    Remarks = models.TextField(blank=True)
    Team = models.CharField(max_length=100,blank=True)
    approvedBy = models.CharField(max_length=255,blank=True)
    Planned_Utilization = models.FloatField(default=0)
    Actual_Utilization = models.FloatField(default=0)
    Actual_utilization_in_percentage = models.CharField(max_length=255,blank=True, null=True)
    Utilization_Percentage = models.CharField(max_length=255,blank=True,null=True)
    Allocated_POC = models.CharField(max_length=100)
    Remarks_Utilization = models.CharField(max_length=255,blank=True)
    Createdby = models.CharField(max_length=255,blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True,null=True)
    Modifiedby = models.CharField(max_length=255,blank=True)
    ModifiedDate = models.DateTimeField(auto_now_add=True,null=True)
    Deletedby = models.CharField(max_length=255,blank=True)
    DeletedDate = models.DateTimeField(auto_now_add=True,null=True)
    isDeleted = models.BooleanField(default=False)
    action = models.CharField(max_length=250, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class BroadcastModel(models.Model):
    """ Models for Broadcast Page"""
    id = models.AutoField(primary_key=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Content = models.CharField(max_length=100,null=True,blank=True)
    BroadCast_by = models.ArrayField(model_container=AllocatedToModel,blank=True,null=True)
    NewUser = models.ArrayField(model_container=AllocatedToModel,blank=True,null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True,null=True)
    User_mail_list = djongo_models.JSONField(blank=True, null=True)
    def __str__(self):
        return self.id
    

    

    

