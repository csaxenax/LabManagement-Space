from django.urls import path,include
from . import views

urlpatterns = [
    # Home Page API's
    # path('OverallAvailability/',views.OverallAvailabilityView.as_view(),name="overallavailability"), 
    # path('OverallSummary/',views.SummaryAPIView.as_view(),name='summary'),
    path('LabProgramVendorSummary/<str:slug>',views.LPVSummaryView.as_view(),name='lpvsummary'),
    path('LabwiseSummary/',views.LabWiseSummaryView.as_view(),name='labwise_summary'),
    # Allocationpage API's
    path('ListAllLocations/',views.ListAllLocationsView.as_view(),name="locations"),
    path('LabDetails/',views.LabdetailsView.as_view(),name='labdetails'),
    path('BookBench/',views.BookBenchView.as_view(),name='booking'),
    path('ViewApprovalRequests/',views.ApproveViewPage.as_view(),name='viewapproverequests'),
    path('RejectApprovalRequests/',views.RejectAPIView.as_view(),name='rejectapproverequests'),
    path('AllocationReport/',views.AllocationReportView.as_view(),name='allocationreport'),
    path('GetProgramDetails/',views.GetProgramDetailsView.as_view(),name='programdetails'),
    path('GetSkuDetails/',views.GetSKUDetailsView.as_view(),name='skudetails'),
    path('GetVendorDetails/',views.GetVendorDetails.as_view(),name="vendordetails"),
    path('ReportView/',views.ReportPageView.as_view(),name='report'),
    path('GetTeamNames/',views.GetTeamNamesView.as_view(),name='teams'),
    path('AddProgram/',views.AddProgramView.as_view(),name='programskudata'),
    path('EditDeleteProgram/',views.EditDeleteProgramView.as_view(),name='editdeleteprogram'),
    path('AddSku/',views.AddSkuView.as_view(),name='addsku'),
    path('EditDeleteSku/',views.EditDeleteSkuView.as_view(),name='editdeletesku'),
    path('VendorData/',views.AddVendorView.as_view(),name='addvendor'),
    path('TeamData/',views.AddTeamView.as_view(),name='addteam'),
    path('DeleteVendor/',views.DeleteVendor.as_view(),name='deletevendor'),
    path('DeleteTeam/',views.DeleteTeam.as_view(),name='deleteteam'),
    path('AddUser/',views.AddUserView.as_view(),name='adduser'),
    path('DeleteUser/',views.DeleteUserView.as_view(),name='deleteuser'),
    path('GetAllRoles/',views.GetUserRoles.as_view(),name='getuserroles'),
    path('DeallocateBenches/',views.DeallocateBenchesView.as_view(),name='deallocatebenches'),
    path('GetCurrentUserData/',views.CurrentUserDataView.as_view(),name='getusername'),
    path('AddNewUser/',views.AddUserRequestView.as_view(),name='addnewuser'),
    path('ApproveUser/',views.ApproveUserView.as_view(),name='approveuser'),
    path('RejectUser/',views.RejectUserView.as_view(),name='rejectuser'),
    path('GetBuildingNames/',views.GetBuildingNamesView.as_view(),name='getbuildingnames'),
    path('GetProgramSkuVendorDropdownNames/',views.GetProgramSkuVendorDropdownNamesView.as_view(),name='getprogramskuvendordropdownnames'),
    path('GiveSuggestions/',views.SuggestionsView.as_view(),name='suggestions'),
    path('GetAllocation/',views.GetAllocationView.as_view(),name='getallocationdetails'),
    path('GetSuggestions/',views.GetSuggestionsView.as_view(),name='getsuggestion'),
    path('ExtendAllocation/',views.ExtendAllocation.as_view(),name='extendallocation'),
    path('GetDrillDownChartData/',views.GetDrillDownChartData.as_view(),name='getdrilldownchartdata'),
    path('TeamDrillDownData/',views.TeamDrillDownView.as_view(),name='teamsdrilldowndata'),
    path('ProgramDrillDownData/',views.ProgramDrillDownView.as_view(),name='programdrilldown'),
    path('ProgramVendorDrillDownData/',views.ProgramVendorView.as_view(),name='programvendordrilldown'),
    path('ValidateUserMail/',views.ValidateUserMail.as_view(),name='validateusermail'),
    path('AddApproverUser/',views.AddApproverUserView.as_view(),name='addapproveruser'),
    path('DeleteApproverUser/',views.DeleteApproverUserView.as_view(),name='deleteapproveruser'),
    path('EditApprovalRequests/',views.EditAPIView.as_view(),name='editapprovalrequests'),
    path('board-api/', views.BoardAPI.as_view(), name='board-api'),
    path('board-api/<int:id>/',views.BoardAPI.as_view(),name='board-api-id'),
    path('workWeek/', views.WorkWeekWiseData.as_view(),name='created'),
    path('allocated/', views.ForecastSummary.as_view(),name='created'),
    path('forecastRvp/', views.ForecastSummaryRVP.as_view(),name='created'),
    path('forecastTableSummary/', views.ForecastSummaryTable.as_view(),name='created'),
    path('quaterlyData/', views.ForecastQuaterWiseSummary.as_view(),name='created'),
    path('year-list/', views.YearListAPI.as_view(), name='year-list-api'),
    path('yearWiseData/', views.YearWiseData.as_view(), name='year-list-api'),
    path('excelUpload/', views.excelUpload.as_view(), name='excel'),
    path('freeBenchReport/',views.FreeBenchReport.as_view(),name='free-bench'),
]
