"""Gatekeep, empirically"""

import gatekeep
from gatekeep.traffic_light import gatekeeper, simulation, world, specification
from gatekeep.controller.random import RandomController


def single_step_vid(spec):
    """

    Args:
      spec: an LTL `Proposition`

    Returns:
      proof_cert: a certificate
    """
    num_trajectories = 1
    video_path = "gatekept_traffic_light-single.mp4"
    tl_world = world.TrafficLightWorld(max_steps=int(1e1))
    tl_sim = simulation.TrafficLightSim(
        tl_world,
        spawn_rate=1.75e-1,
        max_vehicles=int(2**4),
        vehicle_steps_per_action=int(1e2),
        video_path=video_path,
    )
    controller = RandomController(tl_world)
    tl_gatekeeper = gatekeeper.Gatekeeper(
        tl_sim, spec, controller, num_trajectories=num_trajectories
    )
    next_state, reward, done, proof_cert, trajectories = tl_gatekeeper.run_step()
    tl_gatekeeper.render_and_save_video()
    return reward, proof_cert


def main() -> int:
    """Main entry point of the program."""
    reward, proof_cert = single_step_vid(specification.safety)
    print(f"reward: {reward} ==== proofcert: {proof_cert}")
    return 0
