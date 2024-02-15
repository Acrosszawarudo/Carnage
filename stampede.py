def count_dead_ants(carnage):
    intac_ant = carnage.count("ant")
    heads = carnage.count("a")
    bodies = carnage.count("b")
    other_parts = len(carnage) - intac_ant - heads - bodies
    
    dead_ants_from_heads = max(heads - intac_ant, 0)
    
    dead_ants_from_body_parts = min(max(other_parts - dead_ants_from_heads, 0), bodies)
    
    return dead_ants_from_heads + dead_ants_from_body_parts
    
carnage = "...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t"
dead_ants = count_dead_ants(carnage)
    
print(f"Number of dead ants based on body pats: {dead_ants}")
    