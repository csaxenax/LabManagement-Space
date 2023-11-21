import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "labmanager.settings")  # Replace 'your_project' with your actual project name
django.setup()

from allocationapp.models import LabModel,BenchesRowModel,BenchesModel

json_data = '''[
  {
    "seatRowLabel": "A",
    "seats": [
      {
        "key": "A_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "A_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "A_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "A_4",
        "BenchName": "A_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 1",
        "dir": "d",
        "seatNo": "1",
        "labelNo": "A1",
        "team": "SIV"
      },
      {
        "key": "A_5",
        "BenchName": "A_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 2",
        "dir": "d",
        "seatNo": "2",
        "labelNo": "A2",
        "team": "SIV"
      },
      {
        "key": "A_6",
        "BenchName": "A_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 3",
        "dir": "d",
        "seatNo": "3",
        "labelNo": "A3",
        "team": "SIV"
      },
      {
        "key": "A_7",
        "BenchName": "A_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 4",
        "dir": "d",
        "seatNo": "4",
        "labelNo": "A4",
        "team": "SIV"
      },
      {
        "key": "A_8",
        "BenchName": "A_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 5",
        "dir": "d",
        "seatNo": "5",
        "labelNo": "A5",
        "team": "SIV"
      },
      {
        "key": "A_9",
        "BenchName": "A_9",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 6",
        "dir": "d",
        "seatNo": "6",
        "labelNo": "A6",
        "team": "SIV"
      },
      {
        "key": "A_10",
        "BenchName": "A_10",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 7",
        "dir": "d",
        "seatNo": "7",
        "labelNo": "A7",
        "team": "SIV"
      },
      {
        "key": "A_11",
        "BenchName": "A_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "A 8",
        "dir": "d",
        "seatNo": "8",
        "labelNo": "A8",
        "team": "SIV"
      },
      {
        "key": "A_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "A_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "A_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": true
  },
  {
    "seatRowLabel": "B",
    "seats": [
      {
        "key": "B_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "B_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "B_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "B_4",
        "BenchName": "B_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "B 9",
        "dir": "d",
        "seatNo": "9",
        "labelNo": "B1",
        "team": "SIV"
      },
      {
        "key": "B_5",
        "BenchName": "B_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "B 10",
        "dir": "d",
        "seatNo": "10",
        "labelNo": "B2",
        "team": "SIV"
      },
      {
        "key": "B_6",
        "BenchName": "B_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "B 11",
        "dir": "d",
        "seatNo": "11",
        "labelNo": "B3",
        "team": "SIV"
      },
      {
        "key": "B_7",
        "BenchName": "B_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "B 12",
        "dir": "d",
        "seatNo": "12",
        "labelNo": "B4",
        "team": "SIV"
      },
      {
        "key": "B_8",
        "BenchName": "B_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "B 13",
        "dir": "d",
        "seatNo": "13",
        "labelNo": "B5",
        "team": "SIV"
      },
      {
        "key": "B_9",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "B_10",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "B_11",
        "BenchName": "B_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "B 14",
        "dir": "d",
        "seatNo": "14",
        "labelNo": "B6",
        "team": "SIV"
      },
      {
        "key": "B_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "B_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "B_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": false
  },
  {
    "seatRowLabel": "C",
    "seats": [
      {
        "key": "C_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "C_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "C_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "C_4",
        "BenchName": "C_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 15",
        "dir": "d",
        "seatNo": "15",
        "labelNo": "B14",
        "team": "SIV"
      },
      {
        "key": "C_5",
        "BenchName": "C_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 16",
        "dir": "d",
        "seatNo": "16",
        "labelNo": "B13",
        "team": "SIV"
      },
      {
        "key": "C_6",
        "BenchName": "C_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 17",
        "dir": "d",
        "seatNo": "17",
        "labelNo": "B12",
        "team": "SIV"
      },
      {
        "key": "C_7",
        "BenchName": "C_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 18",
        "dir": "d",
        "seatNo": "18",
        "labelNo": "B11",
        "team": "SIV"
      },
      {
        "key": "C_8",
        "BenchName": "C_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 19",
        "dir": "d",
        "seatNo": "19",
        "labelNo": "B10",
        "team": "SIV"
      },
      {
        "key": "C_9",
        "BenchName": "C_9",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 20",
        "dir": "d",
        "seatNo": "20",
        "labelNo": "B9",
        "team": "SIV"
      },
      {
        "key": "C_10",
        "BenchName": "C_10",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 21",
        "dir": "d",
        "seatNo": "21",
        "labelNo": "B8",
        "team": "SIV"
      },
      {
        "key": "C_11",
        "BenchName": "C_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "C 22",
        "dir": "d",
        "seatNo": "22",
        "labelNo": "B7",
        "team": "SIV"
      },
      {
        "key": "C_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "C_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "C_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": true
  },
  {
    "seatRowLabel": "D",
    "seats": [
      {
        "key": "D_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "D_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "D_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "D_4",
        "BenchName": "D_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 23",
        "dir": "d",
        "seatNo": "23",
        "labelNo": "C1",
        "team": "SIV"
      },
      {
        "key": "D_5",
        "BenchName": "D_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 24",
        "dir": "d",
        "seatNo": "24",
        "labelNo": "C2",
        "team": "SIV"
      },
      {
        "key": "D_6",
        "BenchName": "D_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 25",
        "dir": "d",
        "seatNo": "25",
        "labelNo": "C3",
        "team": "SIV"
      },
      {
        "key": "D_7",
        "BenchName": "D_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 26",
        "dir": "d",
        "seatNo": "26",
        "labelNo": "C4",
        "team": "SIV"
      },
      {
        "key": "D_8",
        "BenchName": "D_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 27",
        "dir": "d",
        "seatNo": "27",
        "labelNo": "C5",
        "team": "SIV"
      },
      {
        "key": "D_9",
        "BenchName": "D_9",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 28",
        "dir": "d",
        "seatNo": "28",
        "labelNo": "C6",
        "team": "SIV"
      },
      {
        "key": "D_10",
        "BenchName": "D_10",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 29",
        "dir": "d",
        "seatNo": "29",
        "labelNo": "C7",
        "team": "SIV"
      },
      {
        "key": "D_11",
        "BenchName": "D_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "D 30",
        "dir": "d",
        "seatNo": "30",
        "labelNo": "C8",
        "team": "SIV"
      },
      {
        "key": "D_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "D_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "D_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": false
  },
  {
    "seatRowLabel": "E",
    "seats": [
      {
        "key": "E_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "E_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "E_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "E_4",
        "BenchName": "E_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 31",
        "dir": "d",
        "seatNo": "31",
        "labelNo": "C16",
        "team": "SIV"
      },
      {
        "key": "E_5",
        "BenchName": "E_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 32",
        "dir": "d",
        "seatNo": "32",
        "labelNo": "C15",
        "team": "SIV"
      },
      {
        "key": "E_6",
        "BenchName": "E_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 33",
        "dir": "d",
        "seatNo": "33",
        "labelNo": "C14",
        "team": "SIV"
      },
      {
        "key": "E_7",
        "BenchName": "E_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 34",
        "dir": "d",
        "seatNo": "34",
        "labelNo": "C13",
        "team": "SIV"
      },
      {
        "key": "E_8",
        "BenchName": "E_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 35",
        "dir": "d",
        "seatNo": "35",
        "labelNo": "C12",
        "team": "SIV"
      },
      {
        "key": "E_9",
        "BenchName": "E_9",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 36",
        "dir": "d",
        "seatNo": "36",
        "labelNo": "C11",
        "team": "SIV"
      },
      {
        "key": "E_10",
        "BenchName": "E_10",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 37",
        "dir": "d",
        "seatNo": "37",
        "labelNo": "C10",
        "team": "SIV"
      },
      {
        "key": "E_11",
        "BenchName": "E_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "E 38",
        "dir": "d",
        "seatNo": "38",
        "labelNo": "C9",
        "team": "SIV"
      },
      {
        "key": "E_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "E_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "E_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": true
  },
  {
    "seatRowLabel": "F",
    "seats": [
      {
        "key": "F_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "F_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "F_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "F_4",
        "BenchName": "F_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 39",
        "dir": "d",
        "seatNo": "39",
        "labelNo": "D1",
        "team": "SIV"
      },
      {
        "key": "F_5",
        "BenchName": "F_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 40",
        "dir": "d",
        "seatNo": "40",
        "labelNo": "D2",
        "team": "SIV"
      },
      {
        "key": "F_6",
        "BenchName": "F_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 41",
        "dir": "d",
        "seatNo": "41",
        "labelNo": "D3",
        "team": "SIV"
      },
      {
        "key": "F_7",
        "BenchName": "F_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 42",
        "dir": "d",
        "seatNo": "42",
        "labelNo": "D4",
        "team": "SIV"
      },
      {
        "key": "F_8",
        "BenchName": "F_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 43",
        "dir": "d",
        "seatNo": "43",
        "labelNo": "D5",
        "team": "SIV"
      },
      {
        "key": "F_9",
        "BenchName": "F_9",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 44",
        "dir": "d",
        "seatNo": "44",
        "labelNo": "D6",
        "team": "SIV"
      },
      {
        "key": "F_10",
        "BenchName": "F_10",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 45",
        "dir": "d",
        "seatNo": "45",
        "labelNo": "D7",
        "team": "SIV"
      },
      {
        "key": "F_11",
        "BenchName": "F_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "F 46",
        "dir": "d",
        "seatNo": "46",
        "labelNo": "D8",
        "team": "SIV"
      },
      {
        "key": "F_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "F_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "F_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": false
  },
  {
    "seatRowLabel": "G",
    "seats": [
      {
        "key": "G_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "G_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "G_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "G_4",
        "BenchName": "G_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 47",
        "dir": "d",
        "seatNo": "47",
        "labelNo": "D16",
        "team": "SIV"
      },
      {
        "key": "G_5",
        "BenchName": "G_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 48",
        "dir": "d",
        "seatNo": "48",
        "labelNo": "D15",
        "team": "SIV"
      },
      {
        "key": "G_6",
        "BenchName": "G_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 49",
        "dir": "d",
        "seatNo": "49",
        "labelNo": "D14",
        "team": "SIV"
      },
      {
        "key": "G_7",
        "BenchName": "G_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 50",
        "dir": "d",
        "seatNo": "50",
        "labelNo": "D13",
        "team": "SIV"
      },
      {
        "key": "G_8",
        "BenchName": "G_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 51",
        "dir": "d",
        "seatNo": "51",
        "labelNo": "D12",
        "team": "SIV"
      },
      {
        "key": "G_9",
        "BenchName": "G_9",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 52",
        "dir": "d",
        "seatNo": "52",
        "labelNo": "D11",
        "team": "SIV"
      },
      {
        "key": "G_10",
        "BenchName": "G_10",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 53",
        "dir": "d",
        "seatNo": "53",
        "labelNo": "D10",
        "team": "SIV"
      },
      {
        "key": "G_11",
        "BenchName": "G_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "G 54",
        "dir": "d",
        "seatNo": "54",
        "labelNo": "D9",
        "team": "SIV"
      },
      {
        "key": "G_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "G_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "G_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": true
  },
  {
    "seatRowLabel": "H",
    "seats": [
      {
        "key": "H_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "H_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "H_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "H_4",
        "BenchName": "H_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 55",
        "dir": "d",
        "seatNo": "55",
        "labelNo": "E1",
        "team": "SIV"
      },
      {
        "key": "H_5",
        "BenchName": "H_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 56",
        "dir": "d",
        "seatNo": "56",
        "labelNo": "E2",
        "team": "SIV"
      },
      {
        "key": "H_6",
        "BenchName": "H_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 57",
        "dir": "d",
        "seatNo": "57",
        "labelNo": "E3",
        "team": "SIV"
      },
      {
        "key": "H_7",
        "BenchName": "H_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 58",
        "dir": "d",
        "seatNo": "58",
        "labelNo": "E4",
        "team": "SIV"
      },
      {
        "key": "H_8",
        "BenchName": "H_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 59",
        "dir": "d",
        "seatNo": "59",
        "labelNo": "E5",
        "team": "SIV"
      },
      {
        "key": "H_9",
        "BenchName": "H_9",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 60",
        "dir": "d",
        "seatNo": "60",
        "labelNo": "E6",
        "team": "SIV"
      },
      {
        "key": "H_10",
        "BenchName": "H_10",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 61",
        "dir": "d",
        "seatNo": "61",
        "labelNo": "E7",
        "team": "SIV"
      },
      {
        "key": "H_11",
        "BenchName": "H_11",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "H 62",
        "dir": "d",
        "seatNo": "62",
        "labelNo": "E8",
        "team": "SIV"
      },
      {
        "key": "H_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "H_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "H_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": false
  },
  {
    "seatRowLabel": "I",
    "seats": [
      {
        "key": "I_1",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_2",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_3",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_4",
        "BenchName": "I_4",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "I 63",
        "dir": "d",
        "seatNo": "63",
        "labelNo": "E13",
        "team": "Non-SIV"
      },
      {
        "key": "I_5",
        "BenchName": "I_5",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "I 64",
        "dir": "d",
        "seatNo": "64",
        "labelNo": "E12",
        "team": "Non-SIV"
      },
      {
        "key": "I_6",
        "BenchName": "I_6",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "I 65",
        "dir": "d",
        "seatNo": "65",
        "labelNo": "E11",
        "team": "Non-SIV"
      },
      {
        "key": "I_7",
        "BenchName": "I_7",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "I 66",
        "dir": "d",
        "seatNo": "66",
        "labelNo": "E10",
        "team": "Non-SIV"
      },
      {
        "key": "I_8",
        "BenchName": "I_8",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "I 67",
        "dir": "d",
        "seatNo": "67",
        "labelNo": "E9",
        "team": "Non-SIV"
      },
      {
        "key": "I_9",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_10",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_11",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_12",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_13",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      },
      {
        "key": "I_14",
        "BenchName": "",
        "status": "available",
        "IsAllocated": false,
        "IsRequested": false,
        "AllocationData": null,
        "seatLabel": "",
        "dir": "",
        "seatNo": "",
        "labelNo": "",
        "team": ""
      }
    ],
    "IsRowSpace": true
  }
]
'''


json_da = json.loads(json_data)


for row_data in json_da:
    seats = row_data.get("seats", [])
    bench_details = [{"BenchName": seat["BenchName"]} for seat in seats]

    lab_instance = LabModel(
        Name="SRR-ECO- EC04 2B",
        NumberOfWorkbenches=len(seats),
        AllocatedWorkbenches=0,
    )
    lab_instance.save()

    benches_row_instance = BenchesRowModel(
        seatRowLabel=row_data["seatRowLabel"],
        IsRowSpace=row_data["IsRowSpace"],
    )
    benches_row_instance.save()

    for bench in bench_details:
        bench_instance = BenchesModel(**bench)
        bench_instance.save()
        benches_row_instance.seats.add(bench_instance)

    lab_instance.BenchDetails.append(benches_row_instance)
    lab_instance.save()