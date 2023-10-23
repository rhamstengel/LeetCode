class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0  # Total gas available
        current_gas = 0  # Gas at the current station
        start_station = 0  # Starting station index
        
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]  # Calculate the total gas available
            
            # If the gas at the current station is negative, it means we can't reach the next station
            if current_gas < 0:
                current_gas = 0  # Reset the gas at the current station
                start_station = i  # Move to the next station
            
            current_gas += gas[i] - cost[i]  # Update the gas at the current station
        
        # If the total gas available is negative or zero, it means we can't complete the circuit
        if total_gas < 0:
            return -1
        
        return start_station % len(gas)  # Return the starting station index modulo the number of stations
