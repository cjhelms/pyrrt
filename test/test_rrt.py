from __future__ import annotations

import pyrrt


def test_rrt_should_construct_with_valid_arguments() -> None:
    pyrrt.planner.RRT(
        pyrrt.space.Euclidean2,
        pyrrt.steer.straight_path,
        pyrrt.region.AllSpaceAndTime(),
    )
