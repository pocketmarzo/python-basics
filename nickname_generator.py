import random


list_one = [
    "volatile", "cryptic", "latent", "recursive", "subversive", 
    "synthetic", "augmented", "visceral", "chromed", "abrasive", 
    "dystopian", "obsolete", "grungy", "fluorescent", "encrypted", 
    "kinetic", "neural", "seamless", "corrupted", "glitched", 
    "high-fidelity", "low-life", "neon-drenched", "cybernetic", 
    "autonomous", "decentralized", "binary", "liquid", "radioactive", 
    "industrial", "urban", "metallic", "clandestine", "rogue", "virtual", 
    "hardwired", "carbon-based", "silicon-born", "ghosted", "paradoxical"
    ]
list_two = [
    "protocol", "glitch", "firewall", "grid", "mainframe", "uplink", 
    "cipher", "daemon", "nexus", "implant", "proxy", "circuit", "node", 
    "interface", "backdoor", "payload", "artifact", "static", "vector", 
    "terminal", "algorithm", "shards", "sprawl", "echo", "fragment", 
    "sequence", "void", "breach", "buffer", "latency", "synapse", "conduit", 
    "anomaly", "overflow", "syndrome", "outlier", "cipher-text", "black-hole", 
    "feedback", "entropy"
    ]
char_reserv = "kG9!zP#2vLuR5@mT8&bN1(dX4)sF7_yE0+aC3oI6^jQ9$hW2kZ5@pM8&rN1(tY4)uV7_xB0+nC3%mI6^qR9$lP2*vS5@kT8&bN1(d"
empty = []

def nickname():
    one = random.choice(list_one)
    two = random.choice(list_two)   
    return f"{one}_{two}"

def get_password(length=15):
    
    password = ""
    for _ in range(length):
        password += random.choice(char_reserv)
    return password
    
def main():
    user = input("Enter 'go' to generate: ").strip().lower()
    if user == "go":
        print(f"-----generation complete-----")

        print(f"Nickname: {nickname()}")
        print(f"Password: {get_password()}")

if __name__ == "__main__":
    main()