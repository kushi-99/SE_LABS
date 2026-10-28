import pytest
from visa_application import (
    visa_fee,
    documents_complete,
    application_status,
)


# Visa fee: validation branches
def test_unknown_visa_type():
    with pytest.raises(ValueError):
        visa_fee("other", 1, "normal", "B")


def test_negative_entries():
    with pytest.raises(ValueError):
        visa_fee("tourist", -1, "normal", "B")


# Visa fee: included entries and nationality branches
def test_no_extra_entries():
    assert visa_fee("tourist", 1, "normal", "B") == 0


def test_nationality_a_non_student():
    assert visa_fee("tourist", 3, "normal", "A") == 40


def test_nationality_a_student():
    assert visa_fee("student", 3, "normal", "A") == 40


def test_nationality_b():
    assert visa_fee("business", 4, "normal", "B") == 40


# Visa fee: normal and express branches
def test_normal_rate():
    assert visa_fee("tourist", 3, "normal", "B") == 80


def test_express_rate():
    assert visa_fee("tourist", 3, "express", "B") == 200


# Visa fee: extra > 5 and nested express condition
def test_more_than_five_extra_entries_normal():
    assert visa_fee("tourist", 7, "normal", "B") == 360


def test_more_than_five_extra_entries_express():
    assert visa_fee("tourist", 7, "express", "B") == 780


def test_exactly_five_extra_entries():
    assert visa_fee("tourist", 6, "normal", "B") == 200


# Document completeness: renewal branches
def test_renewal_with_form():
    assert documents_complete(1, 0, True) is True


def test_renewal_without_form():
    assert documents_complete(0, 3, True) is False


# Document completeness: photos and forms branches
def test_nonrenewal_too_few_photos():
    assert documents_complete(3, 1, False) is False


def test_nonrenewal_enough_photos_and_forms():
    assert documents_complete(3, 2, False) is True


def test_nonrenewal_not_enough_forms():
    assert documents_complete(2, 2, False) is False


# Application status: express and normal processing
def test_normal_processing_open():
    assert application_status(30, False, False) == "open"


def test_express_processing_open():
    assert application_status(10, True, False) == "open"


# Application status: peak season
def test_peak_season_open():
    assert application_status(45, False, True) == "open"


# Application status: open, closing and closed
def test_status_at_open_boundary():
    assert application_status(30, False, False) == "open"


def test_status_at_closing_boundary():
    assert application_status(15, False, False) == "closing"


def test_status_below_closing_boundary():
    assert application_status(14, False, False) == "closed"
    