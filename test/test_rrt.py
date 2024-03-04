from __future__ import annotations

import dataclasses

import pyrrt


def test_rrt_should_construct_with_valid_arguments() -> None:
    pyrrt.planner.RRT(
        pyrrt.space.Euclidean2,
        pyrrt.space.euclidean_distance,
        pyrrt.steer.straight_path,
        pyrrt.region.AllSpaceAndTime(),
        lambda node_count: True,
    )


def test_euclidean_distance_should_compute_euclidean_distance() -> None:
    @dataclasses.dataclass
    class ArbitrarySpace:
        a: float
        b: float
        c: float

    FIRST_POINT = ArbitrarySpace(1.0, 2.0, 3.0)
    SECOND_POINT = ArbitrarySpace(5.0, 4.0, 6.0)
    distance = pyrrt.space.euclidean_distance(FIRST_POINT, SECOND_POINT)
    # || p1 - p2 ||2
    #   =
    # ( ( p1.a - p2.a  )^2 + ( p1.b - p2.b )^2 + ( p1.c - p2.c )^2 )^( 1/2 )
    #   =
    # ( ( 1.0 - 5.0 )^2 + ( 2.0 - 4.0 ) ^ 2 + ( 3.0 - 6.0 )^2 )^( 1/2 )
    #   =
    # ( -4.0^2 + -2.0^2 + -3.0^ )^( 1/2 )
    #   =
    # ( 16.0 + 4.0 + 9.0 )^( 1/2 )
    #   =
    # 29.0^( 1/2 )
    EXPECTED_DISTANCE = 29.0**0.5
    assert distance == EXPECTED_DISTANCE


def test_euclidean_distance_should_work_with_any_metric_space() -> None:
    @dataclasses.dataclass
    class FirstSpace:
        x: float
        y: float

    @dataclasses.dataclass
    class SecondSpace:
        a: float
        b: float
        c: float
        d: float

    def compute_distance_and_check(
        first_point: pyrrt.space.T, second_point: pyrrt.space.T
    ) -> None:
        distance = pyrrt.space.euclidean_distance(first_point, second_point)
        EXPECTED_DISTANCE = 1.0
        assert distance == EXPECTED_DISTANCE

    compute_distance_and_check(FirstSpace(1.0, 1.0), FirstSpace(2.0, 1.0))
    compute_distance_and_check(
        SecondSpace(1.0, 1.0, 1.0, 1.0), SecondSpace(1.0, 1.0, 2.0, 1.0)
    )
