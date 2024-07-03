from nada_dsl import *

# Function to determine the stage based on team size
def journey_to_hackerhouse(team_size):
    max_team_size = 4
    if team_size <= max_team_size:
        party = Party(name="Hackerhouse Goa")
        return [Output(SecretInteger(team_size), "team accepted", party)]
    else:
        party = Party(name="Search for New Team")
        return [Output(SecretInteger(team_size), "individual", party)]

# Main story flow
def main_story(team_size):
    print("In a land where code ruled and developers were heroes, a team of coders dreamed of glory at Hackerhouse Goa...")
    print("Our heroes gathered, ready to embark on their journey. They knew that only a team with the right size could proceed.")
    print("--------------------------------------------------------------------------")

    # Determine the current stage of the journey
    results = journey_to_hackerhouse(team_size)

    # Print the outcome of the journey using nada_dsl Outputs
    for result in results:
        print(f"Debug: result = {result}")  # Debugging line to inspect the Output object
        
        # Try to access the value inside the Output object
        try:
            members = result.value.value
        except AttributeError:
            members = "unknown"
        
        if result.name == "team accepted":
            print(f"Outcome: {result.party.name} - The team of {members} members was perfect. They were accepted and continued their quest!")
        else:
            print(f"Outcome: {result.party.name} - Alas, the team had {members} members, which was too many. They had to disband and search for new companions on their journey.")

# Example usage
team_size = 3  # Change this value to test with different team sizes
main_story(team_size)
