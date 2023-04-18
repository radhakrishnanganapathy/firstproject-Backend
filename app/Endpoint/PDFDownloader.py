from fastapi import APIRouter
from app.models.Production import Production
from app.models.Salary import Salary
from app.models.Sales import Sales
from app.models.RawMaterial import RawMaterial
from app.models.TamilWords import TamilWords
from sqlalchemy.orm import Session
from app.DataBase.db import get_db
from fastapi import Depends, Body
from app.schemas import schemas

from fastapi import Response, HTTPException
import psycopg2
import psycopg2.extras
import io
import csv
import json
from prettytable import PrettyTable
import pdfkit
from jinja2 import Environment, FileSystemLoader
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

from sqlalchemy import Integer, String, Column, Boolean, Date, Time
from app.DataBase.db import Base
from app.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.get('/pdf-downloader')
def pdf_downlaod_dynamic(TableName:str,db:Session=Depends(get_db)):
     if TableName == 'salary':
          TableClass = Salary
     elif TableName == 'raw_material':
          TableClass = RawMaterial
     elif TableName == 'production':
          TableClass = Production
     elif TableName == 'sales':
          TableClass = Sales
     elif TableName == 'tamil_words':
          TableClass = TamilWords
     else:
          return {'DB':'Not Found'}
     item = db.query(TableClass).all()
     column_key = TableClass.__table__.columns.keys()
     pdf_buffer = io.BytesIO()
     pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
     print("column key ```````````", column_key)
     # Set up the table headers
     table_headers = column_key
     table_widths = [0.5*inch, 2*inch, 0.5*inch, 0.5*inch]
     x_offset = 0.25*inch
     y_offset = 10*inch
     for i in range(len(table_headers)):
          pdf.drawString(x_offset, y_offset, table_headers[i])
          x_offset += table_widths[i]
     # Set up the table data
     x_offset = 0.25*inch
     y_offset -= 0.5*inch
     for i in item:
          for column_len in range(len(column_key)):
               field = getattr(i,column_key[column_len],'')
               print("ssssssssssssssssssss",field)
               pdf.drawString(x_offset, y_offset, str(field))
               # for wid in range(len(table_widths)):
               x_offset += table_widths[column_len]
          x_offset = 0.25*inch
          y_offset -= 0.5*inch

     # Save the PDF document
     pdf.save()

     # Set the response headers to download the PDF file
     headers = {'Content-Disposition' : 'attachment; filename=students.pdf'}

     # Return the PDF document as a response
     pdf_buffer.seek(0)
     return Response(content=pdf_buffer.getvalue(), media_type='application/pdf', headers=headers)