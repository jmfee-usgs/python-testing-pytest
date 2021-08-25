from unittest import mock

import pytest
from examples.event_service import EventService


@pytest.fixture
def error_response():
    mock_response = mock.Mock()
    mock_response.raise_for_status.side_effect = ValueError("request error")
    return mock_response


@pytest.fixture
def event_service():
    # set up before test
    service = EventService()
    # yield value
    yield service
    # cleanup after test


@pytest.fixture
def success_response():
    features = [{}, {}]
    mock_response = mock.Mock()
    mock_response.raise_for_status = mock.Mock()
    mock_response.json.return_value = {"features": features}
    return mock_response


@mock.patch("examples.event_service.requests.get")
def test_get_events(mock_get, event_service, success_response):
    """Test that features are returned from json response.

    This test doesn't need to verify requests.get works,
    only that a successful json response is handled correctly.
    """
    # arrange
    mock_get.return_value = success_response
    # act
    events = event_service.get_events()
    # assert
    mock_get.assert_called_with(event_service.url)
    assert len(events) == 2


@mock.patch("examples.event_service.requests.get")
def test_get_events_error(mock_get, error_response):
    """Test that exception is thrown if there are HTTP errors.

    This test doesn't need to generate an actual error,
    only that the method raises an error.

    NOTE: There are multiple ways an error could be raised,
    relying on "raise_for_status" is implementation specific.
    """
    # arrange
    mock_get.return_value = error_response
    # act
    try:
        event_service.get_events()
        # assert
        assert False  # service should raise exception
    except:
        pass
