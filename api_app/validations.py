# from filters.schema import base_query_param_schema
# from filters.validations import (
#     CSVofIntegers,
#     IntegerLike,
#     DatetimeWithTZ, Alphanumeric
# )

# # make a validation schema for letter filter query params
# letter_query_schema = base_query_param_schema.extend(
#     {
#         "id": IntegerLike(),
#         "title": str,
#         "tag": CSVofIntegers(),
#         "date": DatetimeWithTZ(),
#     }
# )