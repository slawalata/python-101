from lib_balloon import Balloon


def test_volume_should_be_zero_after_pinched():
    # before test
    red = Balloon("RED", 1000)

    # test
    red.pinched()

    # expected result
    assert 0 == red.current_volume


def test_should_not_reduce_current_volume_if_not_enough_air():
    # before test
    initial_volume = 1000
    deflated_volume = 2000

    expected_volume = initial_volume
    expected_deflated_state = False

    red = Balloon("RED", initial_volume)

    # System Under Test / SUT
    current_deflated_status = red.deflated(deflated_volume)

    # assertion
    assert expected_deflated_state == current_deflated_status, \
        f" Expected {expected_deflated_state} but get {current_deflated_status}"

    current_volume = red.current_volume
    assert expected_volume == current_volume, \
        f" Expected {expected_volume} but get {current_volume}"


def test_should_reduce_current_ballon_volume():
    # before test
    initial_volume = 1000
    deflated_volume = 500

    expected_volume = initial_volume - deflated_volume
    expected_deflated_state = True

    red = Balloon("RED", initial_volume)

    # System Under Test / SUT
    current_deflated_status = red.deflated(deflated_volume)

    # assertion
    current_volume = red.current_volume
    assert expected_volume == current_volume, \
        f" Expected {expected_volume} but get {current_volume}"


