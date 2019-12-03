def get_distinct(Model, fields):
    project = {
        "$project": {
            "_id": 0
        }
    }
    for field in fields:
        project["$project"][field] = f"${field}"

    result =  Model.objects.mongo_aggregate([
        project,
        {
            "$group": {
                "_id": None,
                "distinct": {
                    "$addToSet": "$$ROOT"
                }
            }
        },
        {
            "$unwind": {
                "path": "$distinct",
                "preserveNullAndEmptyArrays": False
            }
        },
        {
            "$replaceRoot": {
                "newRoot": "$distinct"
            }
        }
    ])
    return result
