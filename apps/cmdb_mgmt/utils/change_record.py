from apps.cmdb_mgmt.models.change_record import ChangeRecord, CREATE_INST_ASST


def create_change_record(inst_id, model_id, label, _type, before_data=None, after_data=None, operator=""):
    """创建实例变更记录"""
    change_data = {"operator": operator}
    if before_data:
        change_data["before_data"] = before_data
    if after_data:
        change_data["after_data"] = after_data
    ChangeRecord.objects.create(
        inst_id=inst_id,
        model_id=model_id,
        label=label,
        type=_type,
        **change_data
    )


def batch_create_change_record(label, _type, change_records, operator=""):
    """创建实例变更记录"""
    batch_change_data = [
        ChangeRecord(
            label=label,
            type=_type,
            operator=operator,
            **change_record
        )
        for change_record in change_records
    ]
    ChangeRecord.objects.bulk_create(batch_change_data)


def create_change_record_by_asso(label, _type, data, operator=""):
    """创建关联关系变更记录"""

    change_data = {"operator": operator}

    if _type == CREATE_INST_ASST:
        change_data["after_data"] = data
    else:
        change_data["before_data"] = data

    batch_change_data = [
        ChangeRecord(
            inst_id=inst_info["_id"],
            model_id=inst_info["model_id"],
            label=label,
            type=_type,
            **change_data
        )
        for inst_info in [data["src"], data["dst"]]
    ]

    ChangeRecord.objects.bulk_create(batch_change_data)
