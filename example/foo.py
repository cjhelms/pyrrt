import pyrrt.planner.rrt
import pyrrt.region.all_space_and_time
import pyrrt.space.distance
import pyrrt.space.euclidean_2
import pyrrt.steer.straight_path


def main() -> None:
    MAX_NODE_COUNT = 100
    rrt = pyrrt.planner.rrt.RRT(
        pyrrt.space.euclidean_2.Euclidean2,
        pyrrt.space.distance.euclidean_distance,
        pyrrt.steer.straight_path.straight_path,
        pyrrt.region.all_space_and_time.AllSpaceAndTime(),
        lambda node_count: node_count > MAX_NODE_COUNT,
    )
    rrt.explore(pyrrt.space.euclidean_2.Euclidean2(0.0, 0.0))


if __name__ == "__main__":
    main()
