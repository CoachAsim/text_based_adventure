import time

# Global variables to track game state
inventory = []
ship_health = 100
has_quantum_shield = False

def print_slow(text):
    """Print text with a typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def start_game():
    """Welcome function that introduces the game and its objective"""
    print_slow("""
    🌟 Welcome to COSMIC EXPLORER! 🌟
    
    As a young astronaut aboard the research vessel 'Sagan', you've been tasked with 
    studying a mysterious phenomenon near a black hole in the Cygnus constellation.
    
    Your mission is to:
    1. Collect data about the black hole
    2. Study the effects of gravitational time dilation
    3. Return safely to Earth with your discoveries
    
    Remember: In space, careful observation and scientific thinking are your best tools!
    """)
    
    time.sleep(1)
    return observatory_deck()

def observatory_deck():
    """First scene: The observatory deck of the spacecraft"""
    while True:
        print_slow("""
        You're on the Observatory Deck of the Sagan. Through the reinforced windows, 
        you can see the massive black hole in the distance, its accretion disk glowing 
        with intense radiation.
        
        Available actions:
        1. Use the telescope to study the black hole
        2. Check the gravitational sensors
        3. Move to the Engineering Bay
        4. Review your inventory
        """)
        
        choice = input("What would you like to do? (1-4): ")
        
        if choice == "1":
            print_slow("""
            Through the telescope, you observe the incredible sight of light bending 
            around the black hole's event horizon. You record valuable data about the 
            accretion disk's temperature and composition.
            """)
            if "telescope data" not in inventory:
                inventory.append("telescope data")
                print_slow("📝 Added telescope data to your inventory!")
        
        elif choice == "2":
            print_slow("""
            The gravitational sensors show increasing spatial distortion. You notice 
            that time is passing slightly slower on the ship compared to Earth due to 
            the black hole's gravitational field - a perfect example of Einstein's 
            theory of relativity!
            """)
            if "gravitational readings" not in inventory:
                inventory.append("gravitational readings")
                print_slow("📝 Added gravitational readings to your inventory!")
        
        elif choice == "3":
            return engineering_bay()
        
        elif choice == "4":
            print_slow("\nCurrent inventory:")
            for item in inventory:
                print_slow(f"- {item}")
        
        else:
            print_slow("Please select a valid option (1-4)")

def engineering_bay():
    """Second scene: The Engineering Bay"""
    global ship_health, has_quantum_shield
    
    while True:
        print_slow(f"""
        You're in the Engineering Bay. Ship's health: {ship_health}%
        The closer you get to the black hole, the more strain it puts on the ship's systems.
        
        Available actions:
        1. Repair ship systems
        2. Install quantum shield (requires both telescope data and gravitational readings)
        3. Return to Observatory Deck
        4. Proceed to Navigation Chamber
        """)
        
        choice = input("What would you like to do? (1-4): ")
        
        if choice == "1":
            if ship_health < 100:
                ship_health += 20
                if ship_health > 100:
                    ship_health = 100
                print_slow(f"Repairs completed. Ship health now at {ship_health}%")
            else:
                print_slow("All systems are already at optimal condition!")
        
        elif choice == "2":
            if "telescope data" in inventory and "gravitational readings" in inventory and not has_quantum_shield:
                print_slow("""
                Using your collected data, you calibrate and install the quantum shield.
                This will protect the ship from intense gravitational forces!
                """)
                has_quantum_shield = True
                inventory.append("quantum shield")
            elif has_quantum_shield:
                print_slow("The quantum shield is already installed!")
            else:
                print_slow("You need both telescope data and gravitational readings to install the quantum shield!")
        
        elif choice == "3":
            return observatory_deck()
        
        elif choice == "4":
            return navigation_chamber()
        
        else:
            print_slow("Please select a valid option (1-4)")

def navigation_chamber():
    """Final scene: The Navigation Chamber"""
    while True:
        print_slow("""
        You're in the Navigation Chamber. From here, you can attempt to navigate 
        closer to the black hole for final readings, or return to Earth with your data.
        
        Available actions:
        1. Move closer to black hole
        2. Plot course back to Earth
        3. Return to Engineering Bay
        """)
        
        choice = input("What would you like to do? (1-3): ")
        
        if choice == "1":
            if has_quantum_shield:
                print_slow("""
                Protected by the quantum shield, you safely navigate closer to the black hole.
                You gather groundbreaking data about the nature of spacetime and gravity!
                
                Congratulations! You've completed your mission with spectacular results.
                Your discoveries will revolutionize our understanding of black holes!
                """)
                return True
            else:
                print_slow("""
                Without proper protection, the gravitational forces tear the ship apart.
                Remember: Never approach a black hole without proper shielding!
                
                d - Try again with better preparation!
                """)
                return False
        
        elif choice == "2":
            if "telescope data" in inventory and "gravitational readings" in inventory:
                print_slow("""
                You successfully return to Earth with valuable data about the black hole.
                While you played it safe, your discoveries will still advance our 
                understanding of the cosmos!
                
                Congratulations on completing your mission!
                """)
                return True
            else:
                print_slow("""
                You return to Earth, but without enough data to justify the mission.
                
                GAME OVER - Try again and collect more data!
                """)
                return False
        
        elif choice == "3":
            return engineering_bay()
        
        else:
            print_slow("Please select a valid option (1-3)")

# Start the game
if __name__ == "__main__":
    start_game()