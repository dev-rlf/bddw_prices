from price_records.models import PriceRecord
from products.models import CatSeriesItem

from .models import TearSheetDetail


def return_price_records_by_rule_type(pk: int):
    """
    lookup all pricerecords using tearsheet pk
    organize into dict by rule type
    """
    category_series_items = CatSeriesItem.objects.filter(tear_sheet=pk)

    if len(category_series_items) != 0:
        list_of_price_records = PriceRecord.objects.filter(
            cat_series_item__in=category_series_items
        )

        rule_types = []

        for x in list_of_price_records:
            if x.rule_type not in rule_types:
                rule_types.append(x.rule_type)

        price_records = []

        for p in rule_types:
            price_records.append(
                {f"{p}": [x for x in list_of_price_records if x.rule_type == p]}
            )
        return price_records

    else:
        return None


def return_details_by_title(pk: int):
    """
    lookup all detail records by tearsheek pk
    organize into dict by title
    """

    details = TearSheetDetail.objects.filter(tear_sheet__pk=pk)

    if len(details) != 0:
        names = []

        for x in details:
            if x.name not in names:
                names.append(x.name)
        detail_records = []
        for p in names:
            detail_records.append({f"{p}": [x for x in details if x.name == p]})

        return detail_records

    else:
        return None
