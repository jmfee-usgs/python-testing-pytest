from unittest import mock

from examples.event_service import EventService


# patch the requests module used everywhere
@mock.patch("requests.get")
def test_get_events(mock_get):
    """Test that features are returned from json response.

    This test doesn't need to verify requests.get works,
    only that a successful json response is handled correctly.
    """
    # arrange
    features = [mock.sentinel.feature1, mock.sentinel.feature2]
    mock_response = mock.Mock()
    mock_response.raise_for_status = mock.Mock()
    mock_response.json.return_value = {"features": features}
    mock_get.return_value = mock_response
    service = EventService()
    # act
    events = service.get_events()
    # assert
    mock_get.assert_called_with(service.url)
    assert len(events) == 2
    assert events == features


# patch only the requests module imported into examples.event_service
@mock.patch("examples.event_service.requests.get")
def test_get_events_error(mock_get):
    """Test that exception is thrown if there are HTTP errors.

    This test doesn't need to generate an actual error,
    only that the method raises an error.

    NOTE: There are multiple ways an error could be raised,
    relying on "raise_for_status" is implementation specific.
    """
    # arrange
    mock_response = mock.Mock()
    mock_response.raise_for_status.side_effect = ValueError("request error")
    mock_get.return_value = mock_response
    service = EventService()
    # act
    try:
        service.get_events()
        # assert
        assert False  # service should raise exception
    except:
        pass
