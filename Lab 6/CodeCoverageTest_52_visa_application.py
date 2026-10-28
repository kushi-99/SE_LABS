import pytest
from visa_application import (
    visa_fee,
    documents_complete,
    application_status,
)


def test_visa_fee_included_entries():
    assert visa_fee("tourist", 1, "normal", "B") == 0


def test_visa_fee_express():
    assert visa_fee("tourist", 3, "express", "B") == 200


def test_visa_fee_normal():
    assert visa_fee("tourist", 3, "normal", "B") == 80


def test_visa_fee_nationality_a():
    assert visa_fee("tourist", 3, "normal", "A") == 40


def test_visa_fee_student_nationality_a():
    assert visa_fee("student", 3, "normal", "A") == 40


def test_visa_fee_extra_entries_over_five():
    assert visa_fee("tourist", 7, "normal", "B") == 360


def test_visa_fee_express_over_five():
    assert visa_fee("tourist", 7, "express", "B") == 780


def test_visa_fee_unknown_type():
    with pytest.raises(ValueError, match="unknown visa type"):
        visa_fee("other", 2, "normal", "B")


def test_visa_fee_negative_entries():
    with pytest.raises(ValueError, match="invalid entries"):
        visa_fee("tourist", -1, "normal", "B")


def test_documents_renewal_complete():
    assert documents_complete(1, 0, True) is True


def test_documents_renewal_incomplete():
    assert documents_complete(0, 3, True) is False


def test_documents_too_few_photos():
    assert documents_complete(3, 1, False) is False


def test_documents_complete():
    assert documents_complete(3, 2, False) is True


def test_documents_insufficient_forms():
    assert documents_complete(2, 2, False) is False


def test_application_status_open():
    assert application_status(30, False, False) == "open"


def test_application_status_closing():
    assert application_status(20, False, False) == "closing"


def test_application_status_closed():
    assert application_status(10, False, False) == "closed"


def test_application_status_express_peak():
    assert application_status(25, True, True) == "open"