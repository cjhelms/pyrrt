import pyrrt


def main() -> None:
    MAX_NODE_COUNT = 100
    rrt = pyrrt.planner.RRT(
        pyrrt.space.Euclidean2,
        pyrrt.space.euclidean_distance,
        pyrrt.steer.straight_path,
        pyrrt.region.AllSpaceAndTime(),
        lambda node_count: node_count > MAX_NODE_COUNT,
    )
    rrt.explore(pyrrt.space.Euclidean2(0.0, 0.0))


if __name__ == "__main__":
    main()
