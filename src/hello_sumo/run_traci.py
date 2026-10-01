import traci

sumo_binary = "sumo"

traci.start([sumo_binary, "-c", "simulation.sumocfg"])

step = 0

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    vehicle_ids = traci.vehicle.getIDList()

    for vehicle_id in vehicle_ids:
        speed = traci.vehicle.getSpeed(vehicle_id)
        position = traci.vehicle.getPosition(vehicle_id)

        print(
            f"Step {step}: "
            f"{vehicle_id} | "
            f"speed = {speed:.2f} m/s | "
            f"position = {position}"
        )

    step += 1

traci.close()

print("Simulation finished.")
