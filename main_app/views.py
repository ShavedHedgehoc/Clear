from django.shortcuts import render

# Create your views here.

def index():
    pass


def read_xl_file(r_file):
    xl = pd.ExcelFile(r_file)
    sh = xl.sheet_names[0]
    r_df = pd.read_excel(xl, sheet_name = sh, dtype = str)        
    return r_df


def upload_simple(request):
    df_to_append = read_xl_file('brief.xls')
    for index, row in df_to_append.iterrows():
        marking, _ = Marking.objects.get_or_create(r_name=row['marking'])            
        batch, _ = Batch.objects.get_or_create(r_name=row['batch'])
        apparatus, _ = Apparatus.objects.get_or_create(
            rd_name=row['apparatus'])
        container, _ = Container.objects.get_or_create(
            rd_name=row['container'])
        conveyor, _ = Conveyor.objects.get_or_create(
            rd_name=row['conveyor'])
        new_prod_obj = Production.objects.create(
            p_date=get_date(row['date']),
            p_marking=marking,
            p_batch=batch,
            p_apparatus=apparatus,
            p_container=container,
            p_conveyor=conveyor)
    return render(request, 'success-page.html')