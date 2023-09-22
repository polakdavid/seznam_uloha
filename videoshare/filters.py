import re, operator
from django.forms.models import model_to_dict
from django.db.models.query import QuerySet

class Filters(object):
    """
    Object to make easier to filter and parse data
    """

    def __init__(self):
        self.context = []

    def convert_queryset_dictlist(self, query_set: QuerySet):
        for item in query_set:
            self.context.append(model_to_dict(item))

    def append_list_items(self, dictlist: list):
        counter=1
        for item in dictlist:
            item.update({"id": counter})
            self.context.append(item)
            counter += 1


    def filter_by_key(self, pattern: str, key: str):
        filtered_context = []

        for item in self.context:
            if re.search(pattern, item[key]) is not None:
                filtered_context.append(item)

        return filtered_context

    def to_list(self):
        return self.context

    def order_asc(self):
        self.context = sorted(self.context, key=operator.itemgetter('name'), reverse=False)


    def order_desc(self):
        self.context = sorted(self.context, key=operator.itemgetter('name'), reverse=True)

