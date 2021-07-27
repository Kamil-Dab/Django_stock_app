from .models import Stock, Companies, StockQuery


def get_records(data: StockQuery):
    '''
    Get records from database (Stock) which match the filter created by user
    Filter contains company name, start date and end date.
    :param data: StockQuery object which have company name, start date and end date chose by user
    :return: a collection of records that match the filter criteria
    '''
    company_id = Companies.objects \
        .filter(name=str(data.company_name))[0]
    records = Stock.objects \
        .filter(company_id=company_id.id) \
        .exclude(date__gte=data.end_date) \
        .filter(date__gte=data.start_date)
    return records
